"""
check_binder_urls.py
--------------------
Scans README.md for all Binder badge URLs and reports which ones are
reachable (HTTP 200) and which return errors.

Usage:
    python src/utils/check_binder_urls.py
    python src/utils/check_binder_urls.py --readme path/to/README.md
    python src/utils/check_binder_urls.py --timeout 15
"""

import argparse
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


BINDER_PATTERN = re.compile(
    r'https://mybinder\.org/v2/gh/[^\s"\')\]>]+'
)


def fetch_status(url: str, timeout: int) -> tuple[str, int | str]:
    """Return (url, status_code_or_error_string)."""
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return url, resp.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except Exception as e:
        return url, str(e)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Binder URLs in README.md")
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to README.md (default: README.md)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="HTTP timeout in seconds (default: 10)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=10,
        help="Number of parallel workers (default: 10)",
    )
    args = parser.parse_args()

    readme = Path(args.readme)
    if not readme.exists():
        print(f"ERROR: {readme} not found.", file=sys.stderr)
        sys.exit(1)

    content = readme.read_text(encoding="utf-8")
    urls = sorted(set(BINDER_PATTERN.findall(content)))

    if not urls:
        print("No Binder URLs found in README.")
        sys.exit(0)

    print(f"Found {len(urls)} unique Binder URLs — checking reachability...\n")

    ok, failed = [], []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch_status, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            url, status = future.result()
            if isinstance(status, int) and 200 <= status < 400:
                ok.append((url, status))
                print(f"  ✅  {status}  {url}")
            else:
                failed.append((url, status))
                print(f"  ❌  {status}  {url}")

    print(f"\n{'='*60}")
    print(f"  OK : {len(ok)}")
    print(f"  FAILED : {len(failed)}")

    if failed:
        print("\nFailed URLs:")
        for url, status in failed:
            print(f"  [{status}] {url}")
        sys.exit(1)


if __name__ == "__main__":
    main()

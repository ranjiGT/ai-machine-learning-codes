"""
generate_cheatsheet.py  (v2 — academic poster style)
-----------------------------------------------------
Generates a large-format A0-landscape PDF cheat sheet poster covering all 125
ML topics, styled as a professional academic conference poster.

Usage:
    python src/utils/generate_cheatsheet.py [--output PATH]

Output:
    cheatsheet_poster.pdf  (default, repo root)

Dependencies: matplotlib (already in requirements.txt).
"""

import argparse
import math
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42

# ---------------------------------------------------------------------------
# Colour palette — one accent colour per section (cycles over 20 sections)
# ---------------------------------------------------------------------------
PALETTE = [
    "#c0392b", "#2980b9", "#27ae60", "#7d3c98", "#d35400",
    "#16a085", "#1a5276", "#b7950b", "#76448a", "#1f618d",
    "#117a65", "#a04000", "#922b21", "#1a5276", "#145a32",
    "#6e2f8f", "#b9770e", "#0e6655", "#884ea0", "#1f618d",
]

# ---------------------------------------------------------------------------
# Topic catalogue: (section_title, [(num_str, label), ...])
# ---------------------------------------------------------------------------
SECTIONS = [
    ("Supervised Learning Basics", [
        ("01", "Linear Regression"),
        ("02", "Logistic Regression"),
        ("03", "Decision Trees"),
        ("04", "Random Forest"),
        ("05", "K-Nearest Neighbours"),
        ("06", "Principal Component Analysis"),
        ("07", "Naïve Bayes"),
        ("08", "Underfitting vs Overfitting"),
        ("09", "Reduced Error Pruning"),
    ]),
    ("Evaluation & Model Selection", [
        ("10", "Random Sampling"),
        ("11", "Cross-Validation"),
        ("12", "Nested Cross-Validation"),
        ("13", "Hold-Out Method"),
        ("14", "Hyperparameter Tuning"),
        ("15", "Bootstrap Evaluation"),
        ("108", "Regression Evaluation Metrics"),
    ]),
    ("Tree-Based & Rule-Based Methods", [
        ("16", "Ensemble Methods"),
        ("17", "Hunt's Algorithm"),
        ("18", "Impurity Measures"),
        ("19", "Rule-Based Classifier"),
        ("20", "Sequential Covering Algorithm"),
        ("65", "Laplace Correction"),
        ("79", "ID3 Algorithm"),
    ]),
    ("Probabilistic & Bayesian", [
        ("21", "Bayesian Belief Networks"),
        ("51", "Uncertainty Sampling"),
        ("52", "Query by Committee"),
        ("53", "Expected Model Change"),
        ("54", "Expected Error Reduction"),
        ("55", "Variance Reduction"),
        ("56", "Information Density"),
    ]),
    ("Neural Networks Fundamentals", [
        ("22", "Artificial Neural Networks"),
        ("23", "Feed Forward NNs"),
        ("91", "Intro to Deep NNs"),
        ("92", "Structure of a Neuron"),
        ("93", "Weight Matrix in NNs"),
        ("94", "Generalization of NNs"),
        ("95", "Learning Neural Networks"),
        ("96", "Vectorization of NNs"),
        ("97", "Decision Boundary of NNs"),
    ]),
    ("Training Deep Networks", [
        ("80", "Gradient Descent"),
        ("98", "The Chain Rule"),
        ("99", "Backpropagation"),
        ("100", "The Delta Rule"),
        ("101", "Vanishing/Exploding Gradients"),
        ("106", "Teacher Forcing"),
        ("107", "LSTM"),
    ]),
    ("Activation Functions", [
        ("102", "Step Activation"),
        ("103", "Sigmoid Activation"),
        ("104", "Hyperbolic (Tanh) Activation"),
        ("105", "ReLU Activation"),
        ("114", "Softmax Activation"),
    ]),
    ("Support Vector Machines", [
        ("24", "Support Vector Machine"),
        ("25", "Maximal Margin Classifier"),
        ("26", "Non-Linear SVM"),
        ("110", "Kernel Function & Matrix"),
        ("111", "Semi-Supervised Learning"),
        ("112", "Safe SSL"),
        ("113", "S3VM & TSVM"),
    ]),
    ("Imbalanced Data & Metrics", [
        ("27", "Class Imbalance Problem"),
        ("28", "SMOTE"),
        ("29", "ROC and AUC Curves"),
        ("30", "ISO Accuracy Lines"),
        ("63", "Multi-label Eval. Metrics"),
    ]),
    ("Clustering", [
        ("31", "Unsupervised Clustering"),
        ("32", "K-Means Clustering"),
        ("33", "Bisecting K-Means"),
        ("34", "Cluster Similarity Measures"),
        ("35", "Fuzzy C-Means"),
        ("36", "DBSCAN Technique"),
        ("37", "Mean-Shift Clustering"),
        ("38", "Hierarchical Clustering"),
        ("39", "Linkage Measures"),
    ]),
    ("Cluster Validation", [
        ("40", "Cluster Validation"),
        ("41", "Cohesion & Separation"),
        ("42", "Silhouette Coefficient"),
        ("43", "Cophenetic Correlation"),
        ("44", "Hopkins Statistic"),
        ("45", "Cluster Purity"),
        ("46", "Rand & Jaccard Index"),
    ]),
    ("Active Learning", [
        ("47", "Active Learning Intro"),
        ("48", "Membership Query Synthesis"),
        ("49", "Stream-Based Sampling"),
        ("50", "Pool-Based Sampling"),
    ]),
    ("Multi-class & Multi-label", [
        ("57", "Multi-class: OvR and OvO"),
        ("58", "Multi-label Classification"),
        ("59", "Problem Transformation"),
        ("60", "Binary Relevance"),
        ("61", "Label Powerset"),
        ("62", "RAkEL"),
        ("64", "Multi-Target Classification"),
    ]),
    ("Association Rules", [
        ("66", "Association Rules"),
        ("67", "Apriori Principle"),
        ("68", "Item-set Lattice"),
        ("69", "Lift Measure"),
        ("70", "ECLAT"),
        ("71", "FWER"),
        ("72", "False Discovery Rate"),
    ]),
    ("Dimensionality Reduction & Theory", [
        ("73", "SVD"),
        ("74", "VC Dimension"),
        ("75", "Concept Learning"),
        ("76", "Find-S Algorithm"),
        ("77", "Candidate Elimination"),
        ("78", "Inductive Bias"),
        ("86", "LDA"),
        ("87", "t-SNE"),
    ]),
    ("Regression Variants", [
        ("81", "Ridge Regression"),
        ("82", "Lasso Regression"),
        ("83", "Polynomial Regression"),
        ("84", "Isotonic Regression"),
        ("85", "Elastic Net"),
        ("109", "Linear Learning Machines"),
    ]),
    ("Lazy & Instance-Based Learning", [
        ("88", "Lazy Learning"),
        ("89", "Weighted K-NN"),
        ("90", "Case-Based Reasoning"),
    ]),
    ("Stream & Adaptive Learning", [
        ("117", "Stream-Based & Adaptive Learning"),
        ("118", "DenStream"),
        ("119", "ADWIN"),
        ("120", "VFDT & CVFDT"),
        ("121", "Concept Drift Detection"),
        ("122", "MONIC"),
        ("125", "CluStream"),
    ]),
    ("Time Series & Explainability", [
        ("116", "Advanced Time Series ML"),
        ("124", "ARIMA & SARIMA"),
        ("123", "SHAP Values"),
    ]),
    ("Capstone & Projects", [
        ("115", "End-to-End Real-World ML Project"),
    ]),
]

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------
FIG_W_IN = 46.8   # A0 landscape  (1189 mm)
FIG_H_IN = 33.1   # A0 landscape  ( 841 mm)
DPI = 120

NCOLS = 5
NROWS = math.ceil(len(SECTIONS) / NCOLS)   # 4

TITLE_BAR_H  = 0.090
FOOTER_BAR_H = 0.026
BODY_TOP     = 1.0 - TITLE_BAR_H
BODY_BOTTOM  = FOOTER_BAR_H

COL_GAP     = 0.010
ROW_GAP     = 0.010
OUTER_PAD   = 0.012

# Typography
TITLE_FS    = 38
SUBTITLE_FS = 13
SEC_FS      = 10.5
TOPIC_FS    = 8.5
NUM_FS      = 7.5
FOOTER_FS   = 9

# Colours
BG_COLOR    = "#f4f4f4"
TITLE_BG    = "#0d1b2a"
FOOTER_BG   = "#0d1b2a"
CARD_BG     = "white"
CARD_EDGE   = "#cccccc"
TOPIC_FG    = "#1c1c1c"
DIVIDER_CLR = "#e0e0e0"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _darken(hex_color: str, amount: float = 0.20) -> str:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(
        max(0, int(r * (1 - amount))),
        max(0, int(g * (1 - amount))),
        max(0, int(b * (1 - amount))),
    )


def _lighten(hex_color: str, amount: float = 0.82) -> str:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(
        min(255, int(r + (255 - r) * amount)),
        min(255, int(g + (255 - g) * amount)),
        min(255, int(b + (255 - b) * amount)),
    )


# ---------------------------------------------------------------------------
# Card drawing
# ---------------------------------------------------------------------------

def draw_card(ax, x0, y0, w, h, sec_idx, title, color, topics):
    """Draw one section card in axes-fraction space [0,1]."""

    # -- Drop shadow ---------------------------------------------------------
    S = 0.0016
    ax.add_patch(FancyBboxPatch(
        (x0 + S, y0 - S), w, h,
        boxstyle="round,pad=0.003",
        linewidth=0, facecolor="#999999", alpha=0.30,
        transform=ax.transAxes, zorder=1, clip_on=False,
    ))

    # -- White card body -----------------------------------------------------
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle="round,pad=0.003",
        linewidth=0.7, edgecolor=CARD_EDGE, facecolor=CARD_BG,
        transform=ax.transAxes, zorder=2, clip_on=False,
    ))

    # -- Coloured header strip -----------------------------------------------
    hdr_h = min(0.036, h * 0.20)
    ax.add_patch(FancyBboxPatch(
        (x0, y0 + h - hdr_h), w, hdr_h,
        boxstyle="round,pad=0.003",
        linewidth=0, facecolor=color,
        transform=ax.transAxes, zorder=3, clip_on=False,
    ))

    # Left-side accent bar on card
    bar_w = 0.0040
    ax.add_patch(FancyBboxPatch(
        (x0, y0), bar_w, h - hdr_h,
        boxstyle="square,pad=0",
        linewidth=0, facecolor=_lighten(color, 0.60),
        transform=ax.transAxes, zorder=3, clip_on=False,
    ))

    # Section number pill inside header
    pill_r = hdr_h * 0.36
    px = x0 + pill_r * 1.7
    py = y0 + h - hdr_h / 2
    ax.add_patch(plt.Circle(
        (px, py), pill_r,
        facecolor=_darken(color, 0.35), linewidth=0,
        transform=ax.transAxes, zorder=4, clip_on=False,
    ))
    ax.text(px, py, f"{sec_idx+1:02d}",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=NUM_FS - 0.5, fontweight="bold", color="white",
            zorder=5, clip_on=False)

    # Section title
    ax.text(x0 + pill_r * 3.8, y0 + h - hdr_h / 2,
            title,
            transform=ax.transAxes, ha="left", va="center",
            fontsize=SEC_FS, fontweight="bold", color="white",
            zorder=5, clip_on=False)

    # -- Topic list ----------------------------------------------------------
    n = len(topics)
    if n == 0:
        return

    list_top    = y0 + h - hdr_h - 0.003
    list_bottom = y0 + 0.003
    line_h      = (list_top - list_bottom) / max(n, 1)

    for i, (num, label) in enumerate(topics):
        ly = list_top - (i + 0.5) * line_h

        # Thin horizontal divider
        if i > 0:
            ax.plot([x0 + bar_w + 0.004, x0 + w - 0.004],
                    [ly + line_h / 2, ly + line_h / 2],
                    color=DIVIDER_CLR, linewidth=0.45,
                    transform=ax.transAxes, zorder=3, clip_on=False)

        # Number badge
        bw, bh = 0.026, min(line_h * 0.64, 0.018)
        bx = x0 + bar_w + 0.006
        by = ly - bh / 2
        ax.add_patch(FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="round,pad=0.001",
            linewidth=0.6, edgecolor=_lighten(color, 0.50),
            facecolor=_lighten(color, 0.80),
            transform=ax.transAxes, zorder=4, clip_on=False,
        ))
        ax.text(bx + bw / 2, ly, num,
                transform=ax.transAxes, ha="center", va="center",
                fontsize=NUM_FS, fontweight="bold", color=_darken(color, 0.10),
                zorder=5, clip_on=False)

        # Topic label
        ax.text(x0 + bar_w + 0.038, ly, label,
                transform=ax.transAxes, ha="left", va="center",
                fontsize=TOPIC_FS, color=TOPIC_FG,
                zorder=5, clip_on=False)


# ---------------------------------------------------------------------------
# Poster builder
# ---------------------------------------------------------------------------

def build_poster(output_path: Path):
    fig = plt.figure(figsize=(FIG_W_IN, FIG_H_IN), dpi=DPI, facecolor=BG_COLOR)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(BG_COLOR)

    # ── Title bar ─────────────────────────────────────────────────────────
    ax.add_patch(FancyBboxPatch(
        (0, BODY_TOP), 1.0, TITLE_BAR_H,
        boxstyle="square,pad=0", linewidth=0, facecolor=TITLE_BG,
        transform=ax.transAxes, zorder=10, clip_on=False,
    ))
    # Red accent stripe at very top
    ax.plot([0, 1], [1.0, 1.0], color="#e74c3c", linewidth=7,
            transform=ax.transAxes, zorder=11, clip_on=False)

    ax.text(0.5, BODY_TOP + TITLE_BAR_H * 0.64,
            "Machine Learning — Complete Topic Reference",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=TITLE_FS, fontweight="bold", color="white", zorder=11)

    ax.text(0.5, BODY_TOP + TITLE_BAR_H * 0.22,
            "125 topics  ·  20 themes  ·  github.com/ranjiGT/ai-machine-learning-codes",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=SUBTITLE_FS, color="#aab4cc", zorder=11)

    # ── Footer bar ────────────────────────────────────────────────────────
    ax.add_patch(FancyBboxPatch(
        (0, 0), 1.0, FOOTER_BAR_H,
        boxstyle="square,pad=0", linewidth=0, facecolor=FOOTER_BG,
        transform=ax.transAxes, zorder=10, clip_on=False,
    ))
    ax.text(0.5, FOOTER_BAR_H / 2,
            "Generated by generate_cheatsheet.py  ·  Ranjith Raj Valavanthara  ·  CC BY-NC 4.0  ·  2026",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=FOOTER_FS, color="#aab4cc", zorder=11)

    # ── Card grid ─────────────────────────────────────────────────────────
    body_h  = BODY_TOP - BODY_BOTTOM
    usable_w = 1.0 - 2 * OUTER_PAD
    usable_h = body_h - 2 * OUTER_PAD

    card_w = (usable_w - (NCOLS - 1) * COL_GAP) / NCOLS
    card_h = (usable_h - (NROWS - 1) * ROW_GAP) / NROWS

    for idx, (title, topics) in enumerate(SECTIONS):
        col   = idx % NCOLS
        row   = idx // NCOLS
        color = PALETTE[idx % len(PALETTE)]

        x0 = OUTER_PAD + col * (card_w + COL_GAP)
        y0 = BODY_BOTTOM + OUTER_PAD + (NROWS - 1 - row) * (card_h + ROW_GAP)

        draw_card(ax, x0, y0, card_w, card_h, idx, title, color, topics)

    # ── Save ──────────────────────────────────────────────────────────────
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=DPI, bbox_inches="tight",
                facecolor=BG_COLOR, format="pdf")
    plt.close(fig)
    print(f"Poster saved → {output_path.resolve()}")


def main():
    parser = argparse.ArgumentParser(description="Generate ML cheat sheet poster PDF")
    parser.add_argument(
        "--output", default="cheatsheet_poster.pdf",
        help="Output PDF path (default: cheatsheet_poster.pdf in repo root)",
    )
    args = parser.parse_args()
    build_poster(Path(args.output))


if __name__ == "__main__":
    main()


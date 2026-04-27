"""
generate_cheatsheet.py
----------------------
Generates a large-format A0-landscape PDF cheat sheet poster covering all 124
ML topics in the ai-machine-learning-codes repository.

Usage:
    python src/utils/generate_cheatsheet.py [--output PATH]

Output:
    cheatsheet_poster.pdf (default, placed in repo root)

Dependencies: matplotlib (already in requirements.txt) — no extra packages needed.
"""

import argparse
import math
from pathlib import Path

import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams["pdf.fonttype"] = 42  # embed TrueType fonts in PDF
matplotlib.rcParams["ps.fonttype"] = 42

# ---------------------------------------------------------------------------
# Topic catalogue: each section has (title, hex_color, [(num, label), ...])
# Difficulty legend: 🟢 Foundational  🟡 Intermediate  🔴 Advanced
# ---------------------------------------------------------------------------

SECTIONS = [
    (
        "1 · Supervised Learning Basics",
        "#4e79a7",
        [
            ("01", "Linear Regression"),
            ("02", "Logistic Regression"),
            ("03", "Decision Trees"),
            ("04", "Random Forest"),
            ("05", "K-Nearest Neighbours (KNN)"),
            ("06", "Principal Component Analysis (PCA)"),
            ("07", "Naïve Bayes"),
            ("08", "Underfitting vs Overfitting"),
            ("09", "Reduced Error Pruning"),
        ],
    ),
    (
        "2 · Evaluation & Model Selection",
        "#f28e2b",
        [
            ("10", "Random Sampling"),
            ("11", "Cross-Validation"),
            ("12", "Nested Cross-Validation"),
            ("13", "Hold-Out Method"),
            ("14", "Hyperparameter Tuning"),
            ("15", "Bootstrap Evaluation"),
            ("108", "Regression Evaluation Metrics"),
        ],
    ),
    (
        "3 · Tree-Based & Rule-Based Methods",
        "#e15759",
        [
            ("16", "Ensemble Methods"),
            ("17", "Hunt's Algorithm"),
            ("18", "Impurity Measures"),
            ("19", "Rule-Based Classifier"),
            ("20", "Sequential Covering Algorithm"),
            ("65", "Laplace Correction"),
            ("79", "ID3 Algorithm"),
        ],
    ),
    (
        "4 · Probabilistic & Bayesian Learning",
        "#76b7b2",
        [
            ("21", "Bayesian Belief Networks"),
            ("51", "Uncertainty Sampling"),
            ("52", "Query by Committee"),
            ("53", "Expected Model Change"),
            ("54", "Expected Error Reduction"),
            ("55", "Variance Reduction — Active Learning"),
            ("56", "Information Density — Active Learning"),
        ],
    ),
    (
        "5 · Neural Networks Fundamentals",
        "#59a14f",
        [
            ("22", "Artificial Neural Networks"),
            ("23", "Feed Forward Neural Networks"),
            ("91", "Intro to Deep Neural Networks"),
            ("92", "Structure of a Neuron"),
            ("93", "Weight Matrix in NNs"),
            ("94", "Generalization of NNs"),
            ("95", "Learning Neural Networks"),
            ("96", "Vectorization of NNs"),
            ("97", "Decision Boundary of NNs"),
        ],
    ),
    (
        "6 · Training Deep Networks",
        "#edc948",
        [
            ("98", "The Chain Rule"),
            ("99", "Backpropagation Algorithm"),
            ("100", "The Delta Rule"),
            ("101", "Vanishing & Exploding Gradients"),
            ("80", "Gradient Descent Algorithm"),
            ("106", "Teacher Forcing in Deep Learning"),
            ("107", "LSTM"),
        ],
    ),
    (
        "7 · Activation Functions",
        "#b07aa1",
        [
            ("102", "Step Activation Function"),
            ("103", "Sigmoid Activation Function"),
            ("104", "Hyperbolic (Tanh) Activation"),
            ("105", "ReLU Activation Function"),
            ("114", "Softmax Activation Function"),
        ],
    ),
    (
        "8 · Support Vector Machines",
        "#ff9da7",
        [
            ("24", "Support Vector Machine"),
            ("25", "Maximal Margin Classifier"),
            ("26", "Non-Linear SVM"),
            ("110", "Kernel Function & Kernel Matrix"),
            ("111", "Semi-Supervised Learning (SSL)"),
            ("112", "Safe Semi-Supervised Learning"),
            ("113", "Semi-Supervised SVM (S3VM & TSVM)"),
        ],
    ),
    (
        "9 · Imbalanced Data & Metrics",
        "#9c755f",
        [
            ("27", "Class Imbalance Problem"),
            ("28", "SMOTE"),
            ("29", "ROC and AUC Curves"),
            ("30", "ISO Accuracy Lines"),
            ("63", "Multi-label Evaluation Metrics"),
        ],
    ),
    (
        "10 · Clustering",
        "#bab0ac",
        [
            ("31", "Unsupervised Learning — Clustering"),
            ("32", "K-Means Clustering"),
            ("33", "Bisecting K-Means"),
            ("34", "Cluster Similarity Measures"),
            ("35", "Fuzzy C-Means"),
            ("36", "DBSCAN Technique"),
            ("37", "Mean-Shift Clustering"),
            ("38", "Hierarchical Clustering"),
            ("39", "Linkage Measures"),
        ],
    ),
    (
        "11 · Cluster Validation",
        "#4e79a7",
        [
            ("40", "Cluster Validation Techniques"),
            ("41", "Cohesion & Separation"),
            ("42", "Silhouette Coefficient"),
            ("43", "Cophenetic Correlation"),
            ("44", "Hopkins Statistic"),
            ("45", "Cluster Purity"),
            ("46", "Rand Statistic & Jaccard Index"),
        ],
    ),
    (
        "12 · Active Learning",
        "#f28e2b",
        [
            ("47", "Active Learning Intro"),
            ("48", "Membership Query Synthesis"),
            ("49", "Stream-Based Selective Sampling"),
            ("50", "Pool-Based Sampling"),
        ],
    ),
    (
        "13 · Multi-class & Multi-label",
        "#e15759",
        [
            ("57", "Multi-class: OvR and OvO"),
            ("58", "Multi-label Classification"),
            ("59", "Problem Transformation Methods"),
            ("60", "Binary Relevance"),
            ("61", "Label Powerset"),
            ("62", "Random K-Labelsets (RAkEL)"),
            ("64", "Multi-Target Classification"),
        ],
    ),
    (
        "14 · Association Rules",
        "#76b7b2",
        [
            ("66", "Association Rules"),
            ("67", "Apriori Principle"),
            ("68", "Item-set Lattice"),
            ("69", "Lift Measure"),
            ("70", "ECLAT"),
            ("71", "Family-Wise Error Rate (FWER)"),
            ("72", "False Discovery Rate (FDR)"),
        ],
    ),
    (
        "15 · Dimensionality Reduction & Theory",
        "#59a14f",
        [
            ("73", "Singular Value Decomposition (SVD)"),
            ("74", "VC Dimension"),
            ("75", "Concept Learning"),
            ("76", "Find-S Algorithm"),
            ("77", "Candidate Elimination Algorithm"),
            ("78", "Inductive Bias"),
            ("86", "Linear Discriminant Analysis (LDA)"),
            ("87", "t-SNE"),
        ],
    ),
    (
        "16 · Regression Variants",
        "#edc948",
        [
            ("81", "Ridge Regression"),
            ("82", "Lasso Regression"),
            ("83", "Polynomial Regression"),
            ("84", "Isotonic Regression"),
            ("85", "Elastic Net Regression"),
            ("109", "Linear Learning Machines (LLMs)"),
        ],
    ),
    (
        "17 · Lazy & Instance-Based Learning",
        "#b07aa1",
        [
            ("88", "Lazy Learning Algorithms"),
            ("89", "Weighted K-NN"),
            ("90", "Case-Based Reasoning"),
        ],
    ),
    (
        "18 · Stream & Adaptive Learning",
        "#ff9da7",
        [
            ("117", "Stream-Based & Adaptive Learning"),
            ("118", "DenStream"),
            ("119", "ADWIN"),
            ("120", "VFDT & CVFDT"),
            ("121", "Concept Drift Detection"),
            ("122", "MONIC"),
        ],
    ),
    (
        "19 · Time Series & Explainability",
        "#9c755f",
        [
            ("116", "Advanced Time Series Analysis in ML"),
            ("124", "ARIMA & SARIMA"),
            ("123", "SHAP Values"),
        ],
    ),
    (
        "20 · Capstone & Projects",
        "#bab0ac",
        [
            ("115", "End-to-End Real-World ML Project"),
        ],
    ),
]

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------

FIG_W_IN = 46.8  # A0 landscape width  (mm → inches: 1189/25.4)
FIG_H_IN = 33.1  # A0 landscape height (mm → inches:  841/25.4)
DPI = 100

NCOLS = 5
HEADER_H = 0.075  # fraction of figure height for the title strip
FOOTER_H = 0.030
BODY_H = 1.0 - HEADER_H - FOOTER_H
MARGIN = 0.010  # fractional margin around each card

SECTION_HEADER_FS = 11
TOPIC_FS = 8.5
TITLE_FS = 42
SUBTITLE_FS = 18
NUM_COLOR = "white"
BG_COLOR = "#1a1a2e"


def _wrap(text: str, max_chars: int = 34) -> str:
    """Very simple word-wrap for long topic labels."""
    if len(text) <= max_chars:
        return text
    words = text.split()
    lines, current = [], []
    for w in words:
        if sum(len(x) + 1 for x in current) + len(w) > max_chars:
            lines.append(" ".join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def draw_section(ax, x0, y0, w, h, title, color, topics):
    """Draw one section card inside axes-fraction coordinates [0,1]."""
    # Card background
    rect = FancyBboxPatch(
        (x0, y0),
        w,
        h,
        boxstyle="round,pad=0.003",
        linewidth=0,
        facecolor=color,
        transform=ax.transAxes,
        zorder=2,
        clip_on=False,
    )
    ax.add_patch(rect)

    # Section header strip (slightly darker)
    hdr_h = 0.048
    hdr_rect = FancyBboxPatch(
        (x0, y0 + h - hdr_h),
        w,
        hdr_h,
        boxstyle="round,pad=0.001",
        linewidth=0,
        facecolor=_darken(color, 0.28),
        transform=ax.transAxes,
        zorder=3,
        clip_on=False,
    )
    ax.add_patch(hdr_rect)

    ax.text(
        x0 + w / 2,
        y0 + h - hdr_h / 2,
        title,
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=SECTION_HEADER_FS,
        fontweight="bold",
        color="white",
        zorder=4,
        clip_on=False,
    )

    # Topic lines
    n = len(topics)
    if n == 0:
        return
    line_h = (h - hdr_h - 0.006) / n
    for i, (num, label) in enumerate(topics):
        line_y = y0 + h - hdr_h - (i + 0.5) * line_h - 0.003
        # Bullet number badge
        badge = FancyBboxPatch(
            (x0 + 0.005, line_y - 0.010),
            0.024,
            0.020,
            boxstyle="round,pad=0.002",
            linewidth=0,
            facecolor=_darken(color, 0.4),
            transform=ax.transAxes,
            zorder=4,
            clip_on=False,
        )
        ax.add_patch(badge)
        ax.text(
            x0 + 0.005 + 0.012,
            line_y,
            num,
            transform=ax.transAxes,
            ha="center",
            va="center",
            fontsize=6.5,
            fontweight="bold",
            color="white",
            zorder=5,
            clip_on=False,
        )
        ax.text(
            x0 + 0.034,
            line_y,
            _wrap(label),
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=TOPIC_FS,
            color="white",
            zorder=5,
            clip_on=False,
        )


def _darken(hex_color: str, amount: float) -> str:
    """Return a darkened version of a hex colour."""
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    r = max(0, int(r * (1 - amount)))
    g = max(0, int(g * (1 - amount)))
    b = max(0, int(b * (1 - amount)))
    return f"#{r:02x}{g:02x}{b:02x}"


def build_poster(output_path: Path):
    fig = plt.figure(figsize=(FIG_W_IN, FIG_H_IN), dpi=DPI, facecolor=BG_COLOR)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_facecolor(BG_COLOR)

    # ---- Title strip -------------------------------------------------------
    title_y = 1.0 - HEADER_H
    ax.text(
        0.5,
        title_y + HEADER_H * 0.62,
        "Machine Learning — Complete Topic Reference",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=TITLE_FS,
        fontweight="bold",
        color="white",
        zorder=10,
    )
    ax.text(
        0.5,
        title_y + HEADER_H * 0.22,
        "124 topics across 20 themes  ·  github.com/ranjiGT/ai-machine-learning-codes",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=SUBTITLE_FS,
        color="#aaaacc",
        zorder=10,
    )

    # Thin separator
    ax.plot(
        [0, 1],
        [title_y, title_y],
        color="#444466",
        linewidth=1.5,
        transform=ax.transAxes,
        zorder=5,
    )

    # ---- Body grid ---------------------------------------------------------
    body_top = title_y - MARGIN
    body_bottom = FOOTER_H + MARGIN
    body_h = body_top - body_bottom

    n_sections = len(SECTIONS)
    n_rows = math.ceil(n_sections / NCOLS)

    col_w = (1.0 - 2 * MARGIN) / NCOLS
    row_h = body_h / n_rows

    for idx, (sec_title, color, topics) in enumerate(SECTIONS):
        col = idx % NCOLS
        row = idx // NCOLS  # row 0 is top

        x0 = MARGIN + col * col_w + MARGIN * 0.5
        # rows drawn top-to-bottom
        y_top = body_top - row * row_h
        y0 = y_top - row_h + MARGIN * 0.5
        w = col_w - MARGIN
        h = row_h - MARGIN

        draw_section(ax, x0, y0, w, h, sec_title, color, topics)

    # ---- Footer ------------------------------------------------------------
    ax.text(
        0.5,
        FOOTER_H / 2,
        "Generated by generate_cheatsheet.py  ·  Ranjith Raj Valavanthara  ·  CC BY-NC 4.0",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=9,
        color="#666688",
        zorder=10,
    )

    # ---- Save --------------------------------------------------------------
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=DPI,
        bbox_inches="tight",
        facecolor=BG_COLOR,
        format="pdf",
    )
    plt.close(fig)
    print(f"Poster saved → {output_path.resolve()}")


def main():
    parser = argparse.ArgumentParser(description="Generate ML cheat sheet poster PDF")
    parser.add_argument(
        "--output",
        default="cheatsheet_poster.pdf",
        help="Output PDF path (default: cheatsheet_poster.pdf in repo root)",
    )
    args = parser.parse_args()
    build_poster(Path(args.output))


if __name__ == "__main__":
    main()

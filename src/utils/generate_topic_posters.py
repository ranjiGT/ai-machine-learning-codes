"""
generate_topic_posters.py
--------------------------
Generates a 20-page A3-landscape PDF — one page per ML theme/section —
covering all 125 topics with key bullet points, key formulas, and
programmatic matplotlib diagrams.

Usage:
    python src/utils/generate_topic_posters.py [--output PATH]

Output:
    topic_posters.pdf  (default, repo root)

Dependencies: matplotlib, numpy  (already in requirements.txt)
"""

import argparse
import math
from pathlib import Path

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages

matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42

RNG = np.random.default_rng(42)

# ============================================================
# Colours
# ============================================================
PALETTE = [
    "#c0392b", "#2980b9", "#27ae60", "#7d3c98", "#d35400",
    "#16a085", "#1a5276", "#b7950b", "#76448a", "#1f618d",
    "#117a65", "#a04000", "#922b21", "#1a5276", "#145a32",
    "#6e2f8f", "#b9770e", "#0e6655", "#884ea0", "#1f618d",
]

BG           = "#f5f5f5"
TITLE_BAR    = "#0d1b2a"
CARD_BG      = "white"
CARD_EDGE    = "#cccccc"
TOPIC_FG     = "#1c1c1c"
FORMULA_FG   = "#2c3e50"
BULLET_FG    = "#3d3d3d"
DIVIDER      = "#e8e8e8"

FIG_W, FIG_H = 16.54, 11.69   # A3 landscape (inches)
DPI          = 150

# Fractions of figure height
HDR_H  = 0.100
FOOT_H = 0.035
BODY_T = 1.0 - HDR_H
BODY_B = FOOT_H
PAD    = 0.013
GAP    = 0.009


# ============================================================
# DIAGRAM FUNCTIONS  — each receives a clean axes, draws on it
# ============================================================

def _clean(ax, bg_alpha=0.0):
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.patch.set_alpha(bg_alpha)


def diag_regression_line(ax):
    x = RNG.uniform(0, 10, 40)
    y = 0.8 * x + 1 + RNG.normal(0, 1.0, 40)
    ax.scatter(x, y, s=9, color="#2980b9", alpha=0.65, zorder=2)
    xs = np.linspace(0, 10, 100)
    ax.plot(xs, 0.8 * xs + 1, color="#c0392b", linewidth=1.8, zorder=3)
    _clean(ax)


def diag_sigmoid_curve(ax):
    x = np.linspace(-6, 6, 200)
    ax.plot(x, 1 / (1 + np.exp(-x)), color="#2980b9", linewidth=2)
    ax.axhline(0.5, color="#c0392b", linewidth=0.8, linestyle="--")
    ax.axvline(0,   color="#aaa",    linewidth=0.8, linestyle="--")
    _clean(ax)


def diag_decision_tree(ax):
    nodes  = {0:(0.50,0.87), 1:(0.25,0.60), 2:(0.75,0.60),
              3:(0.12,0.28), 4:(0.38,0.28), 5:(0.62,0.28), 6:(0.88,0.28)}
    edges  = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
    labels = {0:"x<5?", 1:"x<3?", 2:"x<7?", 3:"✓", 4:"✗", 5:"✓", 6:"✗"}
    cols   = {0:"#2980b9", 1:"#27ae60", 2:"#27ae60",
              3:"#c0392b", 4:"#3498db", 5:"#c0392b", 6:"#3498db"}
    for (a, b) in edges:
        ax.plot([nodes[a][0], nodes[b][0]], [nodes[a][1], nodes[b][1]],
                color="#aaa", linewidth=0.9, zorder=1)
    for n, (x, y) in nodes.items():
        ax.add_patch(plt.Circle((x, y), 0.085, color=cols[n], zorder=2))
        ax.text(x, y, labels[n], ha="center", va="center",
                fontsize=5.0, fontweight="bold", color="white", zorder=3)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    _clean(ax)


def diag_knn(ax):
    c1 = RNG.uniform(0, 4, (15, 2))
    c2 = RNG.uniform(3, 7, (15, 2))
    ax.scatter(c1[:,0], c1[:,1], s=10, color="#2980b9", alpha=0.7)
    ax.scatter(c2[:,0], c2[:,1], s=10, color="#c0392b", alpha=0.7)
    ax.scatter(3.5, 3.5, s=55, color="black", marker="*", zorder=5)
    ax.add_patch(plt.Circle((3.5, 3.5), 1.0, color="#27ae60",
                             fill=False, linewidth=1.4, linestyle="--", zorder=4))
    _clean(ax)


def diag_pca(ax):
    data = RNG.multivariate_normal([3, 3], [[2.0, 1.4], [1.4, 2.0]], 50)
    ax.scatter(data[:,0], data[:,1], s=9, color="#2980b9", alpha=0.55)
    for scale, col in [(1.8, "#c0392b"), (0.9, "#27ae60")]:
        a = np.pi / 4
        ax.annotate("", xy=(3 + scale*np.cos(a), 3 + scale*np.sin(a)),
                    xytext=(3, 3),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6))
    _clean(ax)


def diag_histogram(ax):
    data = np.concatenate([RNG.normal(3, 0.8, 80), RNG.normal(6.5, 0.6, 40)])
    ax.hist(data, bins=18, color="#2980b9", alpha=0.75, edgecolor="white", linewidth=0.3)
    _clean(ax)


def diag_bias_variance(ax):
    x = np.linspace(0.5, 10, 100)
    bias = 4 * np.exp(-0.35 * x) + 0.3
    var  = 0.28 * x**0.8 + 0.2
    ax.plot(x, bias,                    color="#2980b9",  linewidth=1.5, label="Bias²")
    ax.plot(x, var,                     color="#c0392b",  linewidth=1.5, label="Var")
    ax.plot(x, np.sqrt(bias**2+var**2), color="#27ae60",  linewidth=1.5, linestyle="--")
    ax.set_xlabel("Complexity", fontsize=5, color="#555")
    _clean(ax)


def diag_neural_net(ax):
    layers = [3, 4, 4, 2]
    cols   = ["#2980b9", "#27ae60", "#27ae60", "#c0392b"]
    pos    = []
    for l, n in enumerate(layers):
        ys = np.linspace(0.12, 0.88, n)
        xs = np.full(n, 0.10 + l * 0.27)
        pos.append(list(zip(xs, ys)))
    for l in range(len(layers) - 1):
        for x1, y1 in pos[l]:
            for x2, y2 in pos[l+1]:
                ax.plot([x1, x2], [y1, y2], color="#ccc", linewidth=0.35, zorder=1)
    for l, pts in enumerate(pos):
        for x, y in pts:
            ax.add_patch(plt.Circle((x, y), 0.040, color=cols[l], zorder=3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    _clean(ax)


def diag_gradient_descent(ax):
    x = np.linspace(-3, 3, 120)
    X, Y = np.meshgrid(x, x)
    ax.contourf(X, Y, X**2 + Y**2, levels=16, cmap="Blues", alpha=0.55)
    path = [(2.5, 2.5)]
    for _ in range(8):
        path.append((path[-1][0] * 0.68, path[-1][1] * 0.68))
    px, py = zip(*path)
    ax.plot(px, py, "o-", color="#c0392b", markersize=2.5, linewidth=1.2)
    _clean(ax)


def diag_activation_curves(ax):
    x = np.linspace(-3, 3, 200)
    ax.plot(x, 1/(1+np.exp(-x)),  color="#2980b9", linewidth=1.4, label="Sigmoid")
    ax.plot(x, np.tanh(x),        color="#c0392b", linewidth=1.4, label="Tanh")
    ax.plot(x, np.maximum(0, x),  color="#27ae60", linewidth=1.4, label="ReLU")
    ax.axhline(0, color="#ccc", linewidth=0.5)
    ax.legend(fontsize=4.5, loc="upper left")
    _clean(ax)


def diag_svm_hyperplane(ax):
    rng2 = np.random.RandomState(7)
    c1 = rng2.randn(20, 2) + [-1.2, -1.2]
    c2 = rng2.randn(20, 2) + [ 1.2,  1.2]
    ax.scatter(c1[:,0], c1[:,1], s=9, color="#2980b9", alpha=0.7)
    ax.scatter(c2[:,0], c2[:,1], s=9, color="#c0392b", alpha=0.7)
    x = np.linspace(-3.5, 3.5, 100)
    ax.plot(x, -x,       color="black", linewidth=1.6)
    ax.plot(x, -x + 1.3, color="#888",  linewidth=0.9, linestyle="--")
    ax.plot(x, -x - 1.3, color="#888",  linewidth=0.9, linestyle="--")
    ax.fill_between(x, -x-1.3, -x+1.3, alpha=0.08, color="black")
    ax.set_xlim(-3.5, 3.5); ax.set_ylim(-3.5, 3.5)
    _clean(ax)


def diag_roc_curve(ax):
    fpr = np.array([0, 0.05, 0.10, 0.20, 0.35, 0.55, 0.75, 1.0])
    tpr = np.array([0, 0.42, 0.64, 0.80, 0.88, 0.93, 0.97, 1.0])
    ax.fill_between(fpr, tpr, alpha=0.15, color="#c0392b")
    ax.plot(fpr, tpr, color="#c0392b", linewidth=2.0)
    ax.plot([0,1],[0,1], color="#aaa", linewidth=0.9, linestyle="--")
    ax.text(0.55, 0.28, "AUC≈0.88", fontsize=6.5, color="#c0392b")
    ax.set_xlabel("FPR", fontsize=5); ax.set_ylabel("TPR", fontsize=5)
    for sp in ["bottom","left"]:
        ax.spines[sp].set_visible(True); ax.spines[sp].set_linewidth(0.5)
    ax.tick_params(labelsize=4.5)
    ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
    ax.patch.set_alpha(0)


def diag_kmeans(ax):
    centres = [(2, 2), (6, 2), (4, 6)]
    colours = ["#2980b9", "#c0392b", "#27ae60"]
    for (cx, cy), col in zip(centres, colours):
        pts = RNG.normal([cx, cy], 0.8, (20, 2))
        ax.scatter(pts[:,0], pts[:,1], s=7, color=col, alpha=0.6)
        ax.scatter(cx, cy, s=70, color=col, marker="*",
                   edgecolors="black", linewidth=0.5, zorder=5)
    _clean(ax)


def diag_dbscan(ax):
    core   = RNG.uniform(1, 4, (30, 2))
    border = RNG.uniform(0, 5, (10, 2))
    noise  = np.array([[0.3, 4.8], [4.9, 0.3], [4.6, 4.6]])
    ax.scatter(core[:,0],   core[:,1],   s=12, color="#2980b9", label="Core")
    ax.scatter(border[:,0], border[:,1], s=12, color="#f39c12", label="Border")
    ax.scatter(noise[:,0],  noise[:,1],  s=20, color="#c0392b", marker="x",
               linewidths=1.2, label="Noise")
    ax.legend(fontsize=4.5, loc="upper right")
    _clean(ax)


def diag_dendrogram(ax):
    leaves  = [0.10, 0.26, 0.46, 0.62, 0.76, 0.90]
    level1  = [0.18, 0.54, 0.83]
    level2  = [0.36, 0.83]
    root_x  = 0.595
    col     = ["#2980b9", "#c0392b", "#27ae60"]
    for i, (la, lb, lc) in enumerate(zip(leaves[::2], leaves[1::2], level1)):
        for lf in [la, lb]:
            ax.plot([lf, lc], [0, 0.25], color=col[i], linewidth=1.0)
        ax.plot([lc, lc], [0.25, 0.52], color=col[i], linewidth=1.0)
    ax.plot([level1[0], level2[0]], [0.52, 0.52], color="#7f8c8d", linewidth=1.0)
    ax.plot([level1[1], level2[0]], [0.52, 0.52], color="#7f8c8d", linewidth=1.0)
    ax.plot([level2[0], level2[0]], [0.52, 0.78], color="#7f8c8d", linewidth=1.0)
    ax.plot([level1[2], level2[0]], [0.52, 0.78], color="#7f8c8d", linewidth=1.0)
    ax.plot([root_x,  root_x],  [0.78, 0.92], color="#333", linewidth=1.2)
    ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1)
    _clean(ax)


def diag_silhouette_bars(ax):
    vals   = np.sort(RNG.uniform(0.25, 0.95, 18))
    colors = ["#2980b9" if v > 0.5 else "#c0392b" for v in vals]
    ax.barh(range(len(vals)), vals, color=colors, height=0.85)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlim(-0.05, 1)
    _clean(ax)


def diag_active_learning_pool(ax):
    unlabeled = RNG.uniform(0, 8, (50, 2))
    labeled   = RNG.uniform(0, 8, (10, 2))
    query     = RNG.uniform(3.2, 4.8, (3, 2))
    ax.scatter(unlabeled[:,0], unlabeled[:,1], s=6,  color="#bdc3c7", alpha=0.75)
    ax.scatter(labeled[:,0],   labeled[:,1],   s=16, color="#2980b9")
    ax.scatter(query[:,0],     query[:,1],     s=36, color="#c0392b", marker="*",
               zorder=5, label="Query")
    ax.legend(fontsize=4.5)
    _clean(ax)


def diag_association_rules(ax):
    items = {"Milk":(0.20,0.80), "Bread":(0.50,0.95), "Butter":(0.80,0.80),
             "Beer":(0.20,0.30), "Diapers":(0.80,0.30)}
    rules = [("Bread","Butter"), ("Beer","Diapers"), ("Milk","Bread")]
    for src, tgt in rules:
        x0,y0 = items[src]; x1,y1 = items[tgt]
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color="#c0392b", lw=1.0))
    for name, (x, y) in items.items():
        ax.add_patch(plt.Circle((x, y), 0.07, color="#2980b9", zorder=3))
        ax.text(x, y - 0.10, name, ha="center", fontsize=4.5, color="#1a1a1a")
    ax.set_xlim(0, 1); ax.set_ylim(0.05, 1.10)
    _clean(ax)


def diag_svd(ax):
    sv = np.array([4.5, 2.8, 1.4, 0.8, 0.4, 0.18, 0.08])
    colors = ["#c0392b" if i < 3 else "#bdc3c7" for i in range(len(sv))]
    ax.bar(range(len(sv)), sv, color=colors, width=0.7)
    ax.axvline(2.5, color="#c0392b", linewidth=1.1, linestyle="--")
    ax.text(2.7, 4.0, "Keep k", fontsize=5.5, color="#c0392b")
    _clean(ax)


def diag_ridge_lasso(ax):
    alpha = np.linspace(0, 5, 100)
    for i, col in enumerate(["#2980b9", "#c0392b", "#27ae60"]):
        coef = (i + 1) * np.exp(-0.55 * alpha) + 0.05
        ax.plot(alpha, coef, color=col, linewidth=1.5)
    ax.axhline(0, color="#aaa", linewidth=0.5)
    ax.set_xlabel("λ", fontsize=5, color="#555")
    _clean(ax)


def diag_stream_drift(ax):
    t  = np.arange(200)
    s1 = np.sin(t * 0.10) + RNG.normal(0, 0.15, 200)
    s2 = np.sin(t * 0.10 + 2) + 1.8 + RNG.normal(0, 0.15, 200)
    ax.plot(t, np.where(t < 100, s1, s2), color="#2980b9", linewidth=0.9)
    ax.axvline(100, color="#c0392b", linewidth=1.5, linestyle="--")
    ax.text(102, 2.2, "Drift", fontsize=5.5, color="#c0392b")
    _clean(ax)


def diag_arima_forecast(ax):
    t = np.arange(80)
    y = 0.05*t + np.sin(t*np.pi/6) + RNG.normal(0, 0.18, 80)
    ax.plot(t[:61], y[:61], color="#2980b9", linewidth=1.3)
    ax.plot(t[60:], y[60:], color="#c0392b", linewidth=1.3, linestyle="--")
    ax.fill_between(t[60:], y[60:]-0.5, y[60:]+0.5, alpha=0.18, color="#c0392b")
    ax.axvline(60, color="#aaa", linewidth=0.8, linestyle=":")
    _clean(ax)


def diag_shap_bars(ax):
    features = ["f₁", "f₂", "f₃", "f₄", "f₅"]
    vals     = [0.43, -0.29, 0.20, -0.13, 0.09]
    colors   = ["#c0392b" if v > 0 else "#2980b9" for v in vals]
    ax.barh(features, vals, color=colors, height=0.6)
    ax.axvline(0, color="black", linewidth=0.7)
    _clean(ax)


def diag_multilabel(ax):
    data = np.array([[1,0,1,0],[1,1,0,1],[0,1,1,0],[1,0,0,1],[0,1,1,1]])
    ax.imshow(data, cmap="Blues", aspect="auto", vmin=0, vmax=1.2)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, str(data[i,j]), ha="center", va="center", fontsize=7,
                    color="white" if data[i,j] else "#999")
    ax.set_xticks(range(4)); ax.set_xticklabels(["L1","L2","L3","L4"], fontsize=5)
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)


def diag_ensemble(ax):
    tree_x = [0.18, 0.50, 0.82]
    for tx in tree_x:
        ax.add_patch(plt.Circle((tx, 0.68), 0.13, color="#2980b9", zorder=2))
        ax.text(tx, 0.68, "T", ha="center", va="center",
                fontsize=11, color="white", fontweight="bold")
        ax.annotate("", xy=(0.50, 0.26), xytext=(tx, 0.55),
                    arrowprops=dict(arrowstyle="-|>", color="#27ae60", lw=1.1))
    ax.add_patch(FancyBboxPatch((0.32,0.09), 0.36, 0.15,
                                boxstyle="round,pad=0.02", color="#27ae60", zorder=2))
    ax.text(0.50, 0.165, "Vote/Avg", ha="center", va="center",
            fontsize=7, color="white", fontweight="bold")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    _clean(ax)


def diag_impurity(ax):
    p = np.linspace(0.001, 0.999, 200)
    ax.plot(p, 1 - p**2 - (1-p)**2,
            color="#2980b9", linewidth=1.5, label="Gini")
    ax.plot(p, -(p*np.log2(p) + (1-p)*np.log2(1-p)) / 2,
            color="#c0392b", linewidth=1.5, label="Entropy/2")
    ax.set_xlabel("p", fontsize=5)
    ax.legend(fontsize=4.5)
    _clean(ax)


def diag_smote(ax):
    minority = RNG.normal([3, 3], 0.5, (15, 2))
    majority = RNG.normal([6, 6], 1.4, (50, 2))
    synth    = RNG.normal([3, 3], 0.9, (15, 2))
    ax.scatter(majority[:,0], majority[:,1], s=7,  color="#bdc3c7", alpha=0.7)
    ax.scatter(minority[:,0], minority[:,1], s=16, color="#c0392b",   label="Minority")
    ax.scatter(synth[:,0],    synth[:,1],    s=16, color="#c0392b",   marker="^",
               label="Synthetic")
    ax.legend(fontsize=4.5)
    _clean(ax)


def diag_cross_val(ax):
    k = 5
    for fold in range(k):
        for part in range(k):
            color = "#c0392b" if part == fold else "#2980b9"
            ax.add_patch(mpatches.Rectangle(
                (part / k + 0.005, (k - fold - 1) / k + 0.02),
                0.96/k, 0.92/k, color=color, linewidth=0))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.text(0.11, -0.06, "Val", fontsize=6, color="#c0392b", ha="center")
    ax.text(0.60, -0.06, "Train", fontsize=6, color="#2980b9", ha="center")
    _clean(ax)


def diag_bootstrap(ax):
    xs = np.linspace(0, 10, 100)
    for i in range(6):
        idx = RNG.integers(0, 100, 100)
        ax.plot(xs, np.sin(xs * 0.6 + i * 0.5) * (1 + 0.08*i),
                linewidth=0.7, alpha=0.55)
    _clean(ax)


def diag_bayesian_net(ax):
    nodes = {"Weather":(0.50,0.84), "Sprinkler":(0.25,0.52),
             "Rain":(0.75,0.52),    "Wet Grass":(0.50,0.18)}
    edges = [("Weather","Sprinkler"),("Weather","Rain"),
             ("Sprinkler","Wet Grass"),("Rain","Wet Grass")]
    for src, tgt in edges:
        x0,y0 = nodes[src]; x1,y1 = nodes[tgt]
        ax.annotate("", xy=(x1,y1), xytext=(x0,y0),
                    arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.0))
    for name, (x, y) in nodes.items():
        ax.add_patch(FancyBboxPatch((x-0.16, y-0.07), 0.32, 0.13,
                                   boxstyle="round,pad=0.01", color="#2980b9", zorder=3))
        ax.text(x, y, name, ha="center", va="center",
                fontsize=4.8, color="white", fontweight="bold", zorder=4)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    _clean(ax)


def diag_lazy_learning(ax):
    train = RNG.uniform(0, 8, (40, 2))
    query = np.array([4.0, 4.0])
    dists = np.linalg.norm(train - query, axis=1)
    near  = train[np.argsort(dists)[:3]]
    ax.scatter(train[:,0], train[:,1], s=9, color="#bdc3c7")
    ax.scatter(*query, s=60, color="#c0392b", marker="*", zorder=5)
    for p in near:
        ax.plot([query[0], p[0]], [query[1], p[1]],
                color="#2980b9", linewidth=1.0, linestyle="--")
    _clean(ax)


def diag_placeholder(ax):
    _clean(ax)
    ax.text(0.5, 0.5, "◆", ha="center", va="center",
            fontsize=26, color="#d0d0d0", transform=ax.transAxes)


DIAGRAM_FUNS = {
    "regression_line":     diag_regression_line,
    "sigmoid_curve":       diag_sigmoid_curve,
    "decision_tree":       diag_decision_tree,
    "knn":                 diag_knn,
    "pca":                 diag_pca,
    "histogram":           diag_histogram,
    "bias_variance":       diag_bias_variance,
    "neural_net":          diag_neural_net,
    "gradient_descent":    diag_gradient_descent,
    "activation_curves":   diag_activation_curves,
    "svm_hyperplane":      diag_svm_hyperplane,
    "roc_curve":           diag_roc_curve,
    "kmeans":              diag_kmeans,
    "dbscan":              diag_dbscan,
    "dendrogram":          diag_dendrogram,
    "silhouette_bars":     diag_silhouette_bars,
    "active_learning_pool":diag_active_learning_pool,
    "association_rules":   diag_association_rules,
    "svd":                 diag_svd,
    "ridge_lasso":         diag_ridge_lasso,
    "stream_drift":        diag_stream_drift,
    "arima_forecast":      diag_arima_forecast,
    "shap_bars":           diag_shap_bars,
    "multilabel":          diag_multilabel,
    "ensemble":            diag_ensemble,
    "impurity":            diag_impurity,
    "smote":               diag_smote,
    "cross_val":           diag_cross_val,
    "bootstrap":           diag_bootstrap,
    "bayesian_net":        diag_bayesian_net,
    "lazy_learning":       diag_lazy_learning,
    None:                  diag_placeholder,
}


# ============================================================
# SECTIONS DATA
# Each topic: num, title, points (≤3), formula, diagram key
# ============================================================

SECTIONS = [
    {
        "title": "Supervised Learning Basics",
        "desc":  "Core algorithms that learn a mapping from labelled inputs to outputs",
        "color": PALETTE[0],
        "topics": [
            {"num":"01","title":"Linear Regression",
             "points":["Model: ŷ = wᵀx + b","Loss: MSE = Σ(y−ŷ)²/n","Normal eq: w=(XᵀX)⁻¹Xᵀy"],
             "formula":r"$\hat{y}=\mathbf{w}^T\mathbf{x}+b$","diagram":"regression_line"},
            {"num":"02","title":"Logistic Regression",
             "points":["σ(z)=1/(1+e⁻ᶻ) squashes to [0,1]","Loss: binary cross-entropy","Decision boundary: wᵀx+b=0"],
             "formula":r"$P(y=1)=\sigma(\mathbf{w}^T\mathbf{x})$","diagram":"sigmoid_curve"},
            {"num":"03","title":"Decision Trees",
             "points":["Splits on best impurity gain","Greedy, top-down induction","Prone to overfitting"],
             "formula":r"$IG = H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v)$","diagram":"decision_tree"},
            {"num":"04","title":"Random Forest",
             "points":["Bagging of decision trees","Random feature subset per split","Reduces variance via averaging"],
             "formula":r"$\hat{f}=\frac{1}{B}\sum_{b=1}^{B}T_b(\mathbf{x})$","diagram":"ensemble"},
            {"num":"05","title":"K-Nearest Neighbours",
             "points":["Label = majority vote of k neighbours","No training — lazy learner","Sensitive to scale & k"],
             "formula":r"$d(\mathbf{x},\mathbf{x}')=\|\mathbf{x}-\mathbf{x}'\|_2$","diagram":"knn"},
            {"num":"06","title":"Principal Component Analysis",
             "points":["Projects to axes of max variance","Eigenvectors of cov matrix","Reduces dimensionality"],
             "formula":r"$\mathbf{z}=\mathbf{W}^T(\mathbf{x}-\mu)$","diagram":"pca"},
            {"num":"07","title":"Naïve Bayes",
             "points":["Assumes feature independence","P(y|x)∝P(y)·ΠP(xᵢ|y)","Fast & effective on text"],
             "formula":r"$\hat{y}=\arg\max_y P(y)\prod_i P(x_i|y)$","diagram":"histogram"},
            {"num":"08","title":"Underfitting vs Overfitting",
             "points":["Underfitting: high bias, low variance","Overfitting: low bias, high variance","Sweet spot minimises total error"],
             "formula":r"$E_{total}=\text{Bias}^2+\text{Var}+\sigma^2$","diagram":"bias_variance"},
            {"num":"09","title":"Reduced Error Pruning",
             "points":["Remove subtrees that don't hurt accuracy","Uses a held-out pruning set","Greedy bottom-up simplification"],
             "formula":r"$\text{Prune if } Acc_{pruned} \geq Acc_{full}$","diagram":"decision_tree"},
        ],
    },
    {
        "title": "Evaluation & Model Selection",
        "desc":  "Techniques for estimating generalisation performance and selecting models",
        "color": PALETTE[1],
        "topics": [
            {"num":"10","title":"Random Sampling",
             "points":["Random train/test split","Quick but high variance","Stratify to preserve class ratios"],
             "formula":r"$Acc=\frac{TP+TN}{N}$","diagram":"histogram"},
            {"num":"11","title":"Cross-Validation",
             "points":["Split data into k folds","Train on k−1, test on 1","Average over all k rotations"],
             "formula":r"$\widehat{Err}=\frac{1}{k}\sum_{i=1}^k Err_i$","diagram":"cross_val"},
            {"num":"12","title":"Nested Cross-Validation",
             "points":["Outer loop: estimate performance","Inner loop: hyperparameter tuning","Unbiased estimate of tuned model"],
             "formula":r"$\hat{E}=\frac{1}{k_o}\sum E_{\text{inner-best}}$","diagram":"cross_val"},
            {"num":"13","title":"Hold-Out Method",
             "points":["Typical split: 70/30 or 80/20","Fast but wastes data","Use only for large datasets"],
             "formula":r"$\text{Error}=\frac{1}{|D_{test}|}\sum\mathcal{L}(y,\hat{y})$","diagram":"cross_val"},
            {"num":"14","title":"Hyperparameter Tuning",
             "points":["Grid search / random search","Bayesian optimisation","Always tune on validation set"],
             "formula":r"$\theta^*=\arg\min_\theta E_{val}(\theta)$","diagram":"gradient_descent"},
            {"num":"15","title":"Bootstrap Evaluation",
             "points":["Sample n points with replacement","Estimate confidence intervals","0.632 bootstrap corrects optimism bias"],
             "formula":r"$\hat{E}_{.632}=0.368\cdot\hat{E}_{train}+0.632\cdot\hat{E}_{oob}$","diagram":"bootstrap"},
            {"num":"108","title":"Regression Evaluation Metrics",
             "points":["MAE: mean absolute error","RMSE: penalises large errors","R²: fraction of variance explained"],
             "formula":r"$R^2=1-\frac{SS_{res}}{SS_{tot}}$","diagram":"roc_curve"},
        ],
    },
    {
        "title": "Tree-Based & Rule-Based Methods",
        "desc":  "Algorithms that build interpretable rule sets from training data",
        "color": PALETTE[2],
        "topics": [
            {"num":"16","title":"Ensemble Methods",
             "points":["Bagging reduces variance (RF)","Boosting reduces bias (AdaBoost)","Stacking combines diverse models"],
             "formula":r"$H(\mathbf{x})=\text{sign}\!\left(\sum_m\alpha_m h_m(\mathbf{x})\right)$","diagram":"ensemble"},
            {"num":"17","title":"Hunt's Algorithm",
             "points":["Basis of most tree learners","Recursively split training set","Stop when node is pure / small"],
             "formula":r"$\text{Split}^*=\arg\max_S \Delta\text{Impurity}$","diagram":"decision_tree"},
            {"num":"18","title":"Impurity Measures",
             "points":["Gini: 1−Σpₖ²","Entropy: −Σpₖ log pₖ","Misclassification: 1−max pₖ"],
             "formula":r"$\text{Gini}=1-\sum_k p_k^2$","diagram":"impurity"},
            {"num":"19","title":"Rule-Based Classifier",
             "points":["IF-THEN rules, easy to interpret","Coverage: fraction rules apply to","Accuracy: fraction correctly classified"],
             "formula":r"$R: (A_1\wedge A_2)\Rightarrow y$","diagram":None},
            {"num":"20","title":"Sequential Covering",
             "points":["Learn one rule, remove covered","Repeat until set is covered","Order-sensitive rule list"],
             "formula":r"$\text{FOIL gain}=t\!\left(\log\frac{p_1}{p_1+n_1}-\log\frac{p_0}{p_0+n_0}\right)$","diagram":None},
            {"num":"65","title":"Laplace Correction",
             "points":["Avoids zero probabilities","Add 1 to each count (add-1 smoothing)","Posterior: (nₖ+1)/(n+|V|)"],
             "formula":r"$P(x_i|y)=\frac{n_{iy}+1}{n_y+|V|}$","diagram":"histogram"},
            {"num":"79","title":"ID3 Algorithm",
             "points":["Splits on maximum Information Gain","Uses entropy as impurity measure","Only handles discrete features"],
             "formula":r"$IG(S,A)=H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v)$","diagram":"decision_tree"},
        ],
    },
    {
        "title": "Probabilistic & Bayesian Learning",
        "desc":  "Principled probabilistic inference and uncertainty-aware models",
        "color": PALETTE[3],
        "topics": [
            {"num":"21","title":"Bayesian Belief Networks",
             "points":["DAG encoding conditional independences","Joint: P(x)=ΠP(xᵢ|parents(xᵢ))","Inference by variable elimination"],
             "formula":r"$P(\mathbf{x})=\prod_i P(x_i\mid pa(x_i))$","diagram":"bayesian_net"},
            {"num":"51","title":"Uncertainty Sampling",
             "points":["Query the sample model is least sure about","Margin: P(y₁|x)−P(y₂|x) small","Entropy: −Σ P(y|x)log P(y|x) large"],
             "formula":r"$x^*=\arg\min_x P(\hat{y}\mid x)$","diagram":"active_learning_pool"},
            {"num":"52","title":"Query by Committee",
             "points":["Maintain committee of hypotheses","Query where committee disagrees most","Vote entropy: −Σ(V/C)log(V/C)"],
             "formula":r"$x^*=\arg\max_x H_{\text{vote}}(x)$","diagram":"active_learning_pool"},
            {"num":"53","title":"Expected Model Change",
             "points":["Query that causes biggest gradient","Maximise ||∇L(θ)||","Computationally expensive"],
             "formula":r"$x^*=\arg\max_x \mathbb{E}[\|\nabla L\|]$","diagram":None},
            {"num":"54","title":"Expected Error Reduction",
             "points":["Query that most reduces future error","Average over possible labels","Expensive: retrains for each candidate"],
             "formula":r"$x^*=\arg\min_x \mathbb{E}[E_{gen}]$","diagram":None},
            {"num":"55","title":"Variance Reduction",
             "points":["Focus on output-space variance","Fisher information criterion","Related to experimental design"],
             "formula":r"$x^*=\arg\min_x \text{Var}[\hat{y}]$","diagram":None},
            {"num":"56","title":"Information Density",
             "points":["Weight uncertainty by representativeness","Dense regions get more queries","ID: US(x)·(avg sim)^β"],
             "formula":r"$x^*\propto\phi_U(x)\cdot\left(\frac{1}{U}\sum_u\text{sim}(x,x^u)\right)^\beta$","diagram":None},
        ],
    },
    {
        "title": "Neural Networks Fundamentals",
        "desc":  "Biologically inspired models built from layers of interconnected nodes",
        "color": PALETTE[4],
        "topics": [
            {"num":"22","title":"Artificial Neural Networks",
             "points":["Layers of weighted sums + activations","Universal approximator (1 hidden layer)","Trained by gradient-based optimisation"],
             "formula":r"$\mathbf{h}=\phi(\mathbf{W}\mathbf{x}+\mathbf{b})$","diagram":"neural_net"},
            {"num":"23","title":"Feed Forward NNs",
             "points":["Information flows input→output only","No cycles or recurrent connections","Multi-layer perceptron (MLP)"],
             "formula":r"$\mathbf{y}=f^{(L)}\circ\cdots\circ f^{(1)}(\mathbf{x})$","diagram":"neural_net"},
            {"num":"91","title":"Intro to Deep NNs",
             "points":["Many hidden layers → deep learning","Hierarchical feature learning","Needs large data & GPUs"],
             "formula":r"$f(\mathbf{x};\theta)=f_L(\ldots f_1(\mathbf{x}))$","diagram":"neural_net"},
            {"num":"92","title":"Structure of a Neuron",
             "points":["Receives weighted inputs: z=Σwᵢxᵢ+b","Non-linear activation: a=φ(z)","Biological analogy: dendrites→axon"],
             "formula":r"$a=\phi\!\left(\sum_i w_i x_i + b\right)$","diagram":"neural_net"},
            {"num":"93","title":"Weight Matrix in NNs",
             "points":["W[l] maps layer l−1 to l","Dims: (n_l, n_{l−1})","Shared weights → parameter efficiency"],
             "formula":r"$\mathbf{z}^{[l]}=\mathbf{W}^{[l]}\mathbf{a}^{[l-1]}+\mathbf{b}^{[l]}$","diagram":None},
            {"num":"94","title":"Generalisation of NNs",
             "points":["Dropout, weight decay, early stopping","Implicit regularisation by SGD noise","Bias–variance trade-off applies"],
             "formula":r"$\mathcal{L}_{reg}=\mathcal{L}+\lambda\|\mathbf{W}\|_F^2$","diagram":"bias_variance"},
            {"num":"95","title":"Learning Neural Networks",
             "points":["Backprop + SGD / Adam","Mini-batch gradient descent","Learning rate scheduling"],
             "formula":r"$\mathbf{W}\leftarrow\mathbf{W}-\eta\nabla_\mathbf{W}\mathcal{L}$","diagram":"gradient_descent"},
            {"num":"96","title":"Vectorization of NNs",
             "points":["Batch all examples: Z=WX+b","GPU parallelism over batch dim","Eliminates explicit Python loops"],
             "formula":r"$\mathbf{Z}=\mathbf{W}\mathbf{X}+\mathbf{b}\mathbf{1}^T$","diagram":None},
            {"num":"97","title":"Decision Boundary",
             "points":["Surface where P(y=1|x)=0.5","Highly non-linear for deep nets","Controlled by weights & activations"],
             "formula":r"$\{x: f(\mathbf{x})=0.5\}$","diagram":"svm_hyperplane"},
        ],
    },
    {
        "title": "Training Deep Networks",
        "desc":  "Optimisation algorithms and practical techniques for training deep models",
        "color": PALETTE[5],
        "topics": [
            {"num":"80","title":"Gradient Descent",
             "points":["Move in direction of negative gradient","Batch / SGD / mini-batch variants","Convergence rate depends on curvature"],
             "formula":r"$\theta_{t+1}=\theta_t-\eta\nabla_\theta\mathcal{L}$","diagram":"gradient_descent"},
            {"num":"98","title":"The Chain Rule",
             "points":["dL/dW = (dL/da)·(da/dz)·(dz/dW)","Enables computing all gradients","Foundation of automatic differentiation"],
             "formula":r"$\frac{dL}{dx}=\frac{dL}{dy}\cdot\frac{dy}{dx}$","diagram":None},
            {"num":"99","title":"Backpropagation",
             "points":["Forward pass: compute activations","Backward pass: propagate δ errors","O(n) per layer — efficient"],
             "formula":r"$\delta^{[l]}=(\mathbf{W}^{[l+1]T}\delta^{[l+1]})\odot\phi'(\mathbf{z}^{[l]})$","diagram":"neural_net"},
            {"num":"100","title":"The Delta Rule",
             "points":["Single-layer online learning rule","Δw = η(y−ŷ)x — Widrow–Hoff","Precursor to backpropagation"],
             "formula":r"$\Delta w_i=\eta(y-\hat{y})x_i$","diagram":None},
            {"num":"101","title":"Vanishing/Exploding Gradients",
             "points":["Gradients shrink/grow through layers","Sigmoid/tanh worsen vanishing","Fix: ReLU, BatchNorm, residuals"],
             "formula":r"$\|\nabla_1\|\approx\prod_l\|\mathbf{W}^{[l]}\|\cdot\phi'$","diagram":"ridge_lasso"},
            {"num":"106","title":"Teacher Forcing",
             "points":["Feed ground-truth as next RNN input","Speeds up training convergence","Can cause exposure bias"],
             "formula":r"$h_t=f(h_{t-1},\,y^*_{t-1})$","diagram":"stream_drift"},
            {"num":"107","title":"LSTM",
             "points":["Forget, input, output gates","Cell state acts as long-term memory","Solves vanishing gradient for sequences"],
             "formula":r"$\mathbf{c}_t=\mathbf{f}_t\odot\mathbf{c}_{t-1}+\mathbf{i}_t\odot\tilde{\mathbf{c}}_t$","diagram":"neural_net"},
        ],
    },
    {
        "title": "Activation Functions",
        "desc":  "Non-linearities that give neural networks their expressive power",
        "color": PALETTE[6],
        "topics": [
            {"num":"102","title":"Step Activation",
             "points":["Binary output: 0 or 1","Not differentiable at 0","Used in original perceptron"],
             "formula":r"$\phi(z)=\mathbf{1}[z\geq 0]$","diagram":"activation_curves"},
            {"num":"103","title":"Sigmoid Activation",
             "points":["Smooth, squashes to (0,1)","Saturates → vanishing gradient","Used in binary output layers"],
             "formula":r"$\sigma(z)=\frac{1}{1+e^{-z}}$","diagram":"sigmoid_curve"},
            {"num":"104","title":"Hyperbolic (Tanh)",
             "points":["Zero-centred output in (−1,1)","Better than sigmoid for hidden layers","Still saturates at extremes"],
             "formula":r"$\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$","diagram":"activation_curves"},
            {"num":"105","title":"ReLU Activation",
             "points":["max(0,z) — cheap to compute","No saturation for z>0","Dead ReLU: fix with Leaky ReLU"],
             "formula":r"$\text{ReLU}(z)=\max(0,z)$","diagram":"activation_curves"},
            {"num":"114","title":"Softmax Activation",
             "points":["Converts logits to probabilities","Outputs sum to 1","Used in multi-class output layer"],
             "formula":r"$\text{softmax}(z_k)=\frac{e^{z_k}}{\sum_j e^{z_j}}$","diagram":"histogram"},
        ],
    },
    {
        "title": "Support Vector Machines",
        "desc":  "Maximum-margin classifiers with kernel extensions for non-linear data",
        "color": PALETTE[7],
        "topics": [
            {"num":"24","title":"Support Vector Machine",
             "points":["Maximise margin between classes","C balances margin vs misclassification","Only support vectors matter"],
             "formula":r"$\min_{\mathbf{w},b}\frac{1}{2}\|\mathbf{w}\|^2+C\sum\xi_i$","diagram":"svm_hyperplane"},
            {"num":"25","title":"Maximal Margin Classifier",
             "points":["Hard-margin SVM (linearly separable)","Unique maximum-margin hyperplane","Geometric margin = 2/||w||"],
             "formula":r"$\text{margin}=\frac{2}{\|\mathbf{w}\|}$","diagram":"svm_hyperplane"},
            {"num":"26","title":"Non-Linear SVM",
             "points":["Map x→φ(x) to higher dimension","Kernel trick: K(x,x')=φ(x)·φ(x')","RBF, polynomial, sigmoid kernels"],
             "formula":r"$K(\mathbf{x},\mathbf{x}')=\exp\!\left(-\gamma\|\mathbf{x}-\mathbf{x}'\|^2\right)$","diagram":"svm_hyperplane"},
            {"num":"110","title":"Kernel Function & Matrix",
             "points":["K must be PSD (Mercer's theorem)","Gram matrix K_ij = K(xᵢ,xⱼ)","Enables SVM in infinite-dim spaces"],
             "formula":r"$K_{ij}=\phi(\mathbf{x}_i)^T\phi(\mathbf{x}_j)$","diagram":None},
            {"num":"111","title":"Semi-Supervised Learning",
             "points":["Uses few labelled + many unlabelled","Self-training, co-training, label prop","Low-density assumption for decision boundary"],
             "formula":r"$\min_{f}\frac{1}{l}\sum\mathcal{L}+\lambda R(f,\mathcal{U})$","diagram":"active_learning_pool"},
            {"num":"112","title":"Safe Semi-Supervised",
             "points":["SSL should not hurt vs supervised","Safety constraints on unlabelled usage","TSVM with safe wrapper"],
             "formula":r"$R_{SSL}\leq R_{SL}+\epsilon$","diagram":None},
            {"num":"113","title":"S3VM & TSVM",
             "points":["Place decision boundary in low-density region","Transductive: label unlabelled data","Non-convex optimisation"],
             "formula":r"$\min\frac{1}{2}\|\mathbf{w}\|^2+C\sum\xi+C^*\sum\xi^*$","diagram":"svm_hyperplane"},
        ],
    },
    {
        "title": "Imbalanced Data & Metrics",
        "desc":  "Strategies and metrics for learning under class imbalance",
        "color": PALETTE[8],
        "topics": [
            {"num":"27","title":"Class Imbalance Problem",
             "points":["Minority class often more important","Accuracy misleads on skewed data","Solutions: resampling, cost-sensitive learning"],
             "formula":r"$Acc_{majority\text{-}only}\approx\frac{N_{maj}}{N}$","diagram":"histogram"},
            {"num":"28","title":"SMOTE",
             "points":["Synthetic Minority Over-sampling Technique","Interpolate between minority neighbours","Avoids exact duplicates"],
             "formula":r"$x_{new}=x_i+\lambda(x_{nn}-x_i),\,\lambda\sim U[0,1]$","diagram":"smote"},
            {"num":"29","title":"ROC and AUC Curves",
             "points":["TPR vs FPR at each threshold","AUC = P(score_pos > score_neg)","AUC=1 perfect, 0.5 random"],
             "formula":r"$AUC=\int_0^1 TPR\,d(FPR)$","diagram":"roc_curve"},
            {"num":"30","title":"ISO Accuracy Lines",
             "points":["Contours of equal accuracy on ROC","Slope = (1−π)/π (prior ratio)","Visualise cost-sensitive trade-offs"],
             "formula":r"$TPR=(1+\frac{1-\pi}{\pi})FPR-\frac{(1-\pi)Acc}{\pi}$","diagram":"roc_curve"},
            {"num":"63","title":"Multi-label Eval. Metrics",
             "points":["Hamming loss: avg label error","Subset accuracy: exact match ratio","F1-micro/macro for label imbalance"],
             "formula":r"$HL=\frac{1}{n|L|}\sum_{i,j}y_{ij}\oplus\hat{y}_{ij}$","diagram":"multilabel"},
        ],
    },
    {
        "title": "Clustering",
        "desc":  "Unsupervised discovery of natural groupings in unlabelled data",
        "color": PALETTE[9],
        "topics": [
            {"num":"31","title":"Unsupervised Clustering",
             "points":["No labels — find intrinsic groups","Compactness (within) vs separation (between)","Many algorithms: K-means, DBSCAN, etc."],
             "formula":r"$J=\sum_k\sum_{\mathbf{x}\in C_k}\|\mathbf{x}-\mu_k\|^2$","diagram":"kmeans"},
            {"num":"32","title":"K-Means Clustering",
             "points":["Assign to nearest centroid; re-compute","Convergence guaranteed, not global opt","k chosen via elbow / silhouette"],
             "formula":r"$\mu_k=\frac{1}{|C_k|}\sum_{\mathbf{x}\in C_k}\mathbf{x}$","diagram":"kmeans"},
            {"num":"33","title":"Bisecting K-Means",
             "points":["Start with one cluster; bisect worst","Produces hierarchical structure","SSE guides split choice"],
             "formula":r"$\text{Bisect: pick }k\text{ with max SSE}$","diagram":"kmeans"},
            {"num":"34","title":"Cluster Similarity",
             "points":["Single, complete, average, Ward linkage","Proximity matrix between pairs","Cosine sim for high-dim text"],
             "formula":r"$\text{avg}=\frac{1}{|A||B|}\sum_{a\in A,b\in B}d(a,b)$","diagram":None},
            {"num":"35","title":"Fuzzy C-Means",
             "points":["Each point has membership degree ∈[0,1]","Minimise weighted SSE","Reduces to K-means for m→1"],
             "formula":r"$u_{ik}=\left(\sum_j\left(\frac{d_{ik}}{d_{jk}}\right)^{2/(m-1)}\right)^{-1}$","diagram":"kmeans"},
            {"num":"36","title":"DBSCAN",
             "points":["Core: ≥MinPts in ε-neighbourhood","Finds arbitrary-shape clusters","Marks outliers as noise"],
             "formula":r"$N_\varepsilon(p)=\{q:d(p,q)\leq\varepsilon\}$","diagram":"dbscan"},
            {"num":"37","title":"Mean-Shift Clustering",
             "points":["Shift each point to mean of neighbours","No k needed; finds modes of density","Bandwidth h controls granularity"],
             "formula":r"$m(x)=\frac{\sum_{x_i\in N(x)}K(x_i-x)x_i}{\sum_{x_i\in N(x)}K(x_i-x)}$","diagram":"kmeans"},
            {"num":"38","title":"Hierarchical Clustering",
             "points":["Agglomerative: bottom-up merging","Divisive: top-down splitting","Visualised as dendrogram"],
             "formula":r"$d(A\cup B,C)=\frac{|A|d(A,C)+|B|d(B,C)}{|A|+|B|}$","diagram":"dendrogram"},
            {"num":"39","title":"Linkage Measures",
             "points":["Single: nearest pair (chaining)","Complete: farthest pair (compact)","Ward: min variance increase"],
             "formula":r"$d_{ward}=\sqrt{\frac{2n_An_B}{n_A+n_B}}\|\mu_A-\mu_B\|$","diagram":"dendrogram"},
        ],
    },
    {
        "title": "Cluster Validation",
        "desc":  "Quantitative criteria for assessing cluster quality",
        "color": PALETTE[10],
        "topics": [
            {"num":"40","title":"Cluster Validation",
             "points":["Internal: cohesion + separation (no labels)","External: compare to ground truth","Relative: compare among clusterings"],
             "formula":r"$Q = f(\text{cohesion},\text{separation})$","diagram":"silhouette_bars"},
            {"num":"41","title":"Cohesion & Separation",
             "points":["Cohesion: avg within-cluster dist","Separation: avg between-cluster dist","High cohesion + high separation = good"],
             "formula":r"$SEP=\frac{1}{k}\sum_k\min_{j\neq k}d(\mu_k,\mu_j)$","diagram":"silhouette_bars"},
            {"num":"42","title":"Silhouette Coefficient",
             "points":["s(i)=(b(i)−a(i))/max(a,b)","a: avg within-cluster dist","b: avg nearest-cluster dist"],
             "formula":r"$s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}$","diagram":"silhouette_bars"},
            {"num":"43","title":"Cophenetic Correlation",
             "points":["Correlation: pairwise dists vs tree dists","Close to 1 = dendro faithful","Measures hierarchical quality"],
             "formula":r"$r=\frac{\sum(z-\bar{z})(d-\bar{d})}{\sqrt{\sum(z-\bar{z})^2\sum(d-\bar{d})^2}}$","diagram":"dendrogram"},
            {"num":"44","title":"Hopkins Statistic",
             "points":["Tests if data is uniformly distributed","H close to 0.5 → random","H close to 1 → clustered structure"],
             "formula":r"$H=\frac{\sum u_i^d}{\sum u_i^d+\sum w_i^d}$","diagram":"histogram"},
            {"num":"45","title":"Cluster Purity",
             "points":["Assign each cluster to majority class","Purity = fraction correctly assigned","Cannot capture over-segmentation"],
             "formula":r"$P=\frac{1}{N}\sum_k\max_j|C_k\cap T_j|$","diagram":"histogram"},
            {"num":"46","title":"Rand & Jaccard Index",
             "points":["Rand: (TP+TN)/all pairs","Jaccard: TP/(TP+FP+FN)","Adjusted Rand corrects for chance"],
             "formula":r"$RI=\frac{TP+TN}{TP+FP+FN+TN}$","diagram":"multilabel"},
        ],
    },
    {
        "title": "Active Learning",
        "desc":  "Interactive learning that queries the most informative unlabelled examples",
        "color": PALETTE[11],
        "topics": [
            {"num":"47","title":"Active Learning Intro",
             "points":["Label most informative examples first","Reduces annotation cost significantly","Query strategies: uncertainty, QBC, EER"],
             "formula":r"$x^*=\arg\max_{x\in\mathcal{U}}\phi(x)$","diagram":"active_learning_pool"},
            {"num":"48","title":"Membership Query Synthesis",
             "points":["Learner generates its own queries","Can query any point in input space","Risk: unnatural/unrealistic queries"],
             "formula":r"$x^*=\arg\max_{x}\phi(x),\;x\text{ generated}$","diagram":"active_learning_pool"},
            {"num":"49","title":"Stream-Based Sampling",
             "points":["Each instance arrives once, decide to label","Accept if informativeness > threshold","No pool needed; suits streaming data"],
             "formula":r"$\text{label if }\phi(x)\geq\tau$","diagram":"stream_drift"},
            {"num":"50","title":"Pool-Based Sampling",
             "points":["Select best query from an unlabelled pool","Most common paradigm","Rank pool, pick top-k each round"],
             "formula":r"$x^*=\arg\max_{x\in\mathcal{U}}\phi(x)$","diagram":"active_learning_pool"},
        ],
    },
    {
        "title": "Multi-class & Multi-label",
        "desc":  "Extending classification beyond binary to multiple classes and labels",
        "color": PALETTE[12],
        "topics": [
            {"num":"57","title":"Multi-class: OvR and OvO",
             "points":["OvR: one binary clf per class","OvO: one clf per pair (k(k−1)/2)","OvR faster; OvO more accurate on some tasks"],
             "formula":r"$\hat{y}=\arg\max_k f_k(\mathbf{x})$","diagram":"histogram"},
            {"num":"58","title":"Multi-label Classification",
             "points":["Each instance can have multiple labels","Label set y⊆L, |L|>>1","Hamming loss, F1, subset acc as metrics"],
             "formula":r"$h:\mathcal{X}\to 2^{\mathcal{L}}$","diagram":"multilabel"},
            {"num":"59","title":"Problem Transformation",
             "points":["Convert multi-label to binary problems","Binary Relevance, Label Powerset, RAkEL","No modification of base classifier needed"],
             "formula":r"$\mathcal{L}\to\{0,1\}^{|\mathcal{L}|}$","diagram":"multilabel"},
            {"num":"60","title":"Binary Relevance",
             "points":["One binary classifier per label","Ignores label correlations","Simple, parallelisable"],
             "formula":r"$H_j(x)=h_j(x),\;j=1\ldots|\mathcal{L}|$","diagram":"multilabel"},
            {"num":"61","title":"Label Powerset",
             "points":["Each unique label subset becomes a class","Captures full label correlations","Exponential classes if many labels"],
             "formula":r"$H(x)=\text{decode}(h(x))$","diagram":"multilabel"},
            {"num":"62","title":"RAkEL",
             "points":["Random k-label subsets + Label Powerset","Ensemble of LP classifiers","Balances correlation and scalability"],
             "formula":r"$H(x)=\text{vote}\{LP_{S_m}(x)\}_{m=1}^M$","diagram":"multilabel"},
            {"num":"64","title":"Multi-Target Classification",
             "points":["Multiple correlated discrete outputs","Exploit inter-output correlations","Chain classifiers, joint output models"],
             "formula":r"$h:\mathcal{X}\to\mathcal{Y}_1\times\cdots\times\mathcal{Y}_T$","diagram":"multilabel"},
        ],
    },
    {
        "title": "Association Rules",
        "desc":  "Mining frequent patterns and co-occurrence rules in transactional data",
        "color": PALETTE[13],
        "topics": [
            {"num":"66","title":"Association Rules",
             "points":["Rule: {A}→{B}","Support: P(A∪B)","Confidence: P(B|A)"],
             "formula":r"$\text{conf}(A\to B)=\frac{P(A\cup B)}{P(A)}$","diagram":"association_rules"},
            {"num":"67","title":"Apriori Principle",
             "points":["All subsets of a frequent itemset are frequent","Prune search space bottom-up","Generates candidates level by level"],
             "formula":r"$\text{sup}(X)\geq\text{minsup}\;\Rightarrow\;\text{sup}(Y)\geq\text{minsup}\;\forall Y\subseteq X$","diagram":"association_rules"},
            {"num":"68","title":"Item-set Lattice",
             "points":["Lattice of all 2^|I| item subsets","Frequent itemsets form an ideal","Monotonicity enables pruning"],
             "formula":r"$\mathcal{F}=\{X:\text{sup}(X)\geq\sigma\}$","diagram":"association_rules"},
            {"num":"69","title":"Lift Measure",
             "points":["Lift = conf/(P(B)) — independence baseline","Lift > 1: positive correlation","Lift < 1: negative correlation"],
             "formula":r"$\text{lift}=\frac{P(A\cup B)}{P(A)P(B)}$","diagram":"histogram"},
            {"num":"70","title":"ECLAT",
             "points":["Vertical representation: item→tid-list","Intersect tid-lists for support","Depth-first; efficient for dense data"],
             "formula":r"$\text{sup}(A\cup B)=|t(A)\cap t(B)|$","diagram":"association_rules"},
            {"num":"71","title":"FWER",
             "points":["Family-Wise Error Rate: P(≥1 false positive)","Bonferroni: α/m per test","Holm-Bonferroni: step-down correction"],
             "formula":r"$\text{FWER}=P\!\left(\bigcup_i H_{0i}\text{ rejected falsely}\right)$","diagram":"histogram"},
            {"num":"72","title":"False Discovery Rate",
             "points":["FDR = E[FP/R]: expected false discoveries","Benjamini–Hochberg procedure","Less stringent than FWER; more power"],
             "formula":r"$FDR=\mathbb{E}\!\left[\frac{V}{\max(R,1)}\right]$","diagram":"histogram"},
        ],
    },
    {
        "title": "Dimensionality Reduction & Theory",
        "desc":  "Formal ML theory and methods for compacting high-dimensional representations",
        "color": PALETTE[14],
        "topics": [
            {"num":"73","title":"SVD",
             "points":["M = UΣVᵀ — always exists","Optimal low-rank approximation (Eckart–Young)","Basis of LSA, PCA, recommender systems"],
             "formula":r"$\mathbf{M}=\mathbf{U}\Sigma\mathbf{V}^T$","diagram":"svd"},
            {"num":"74","title":"VC Dimension",
             "points":["Max points a hypothesis class can shatter","VC(hyperplanes in ℝⁿ) = n+1","PAC bound: E[err] ≤ O(√(d/n))"],
             "formula":r"$R\leq\hat{R}+O\!\left(\sqrt{\frac{d}{n}}\right)$","diagram":"bias_variance"},
            {"num":"75","title":"Concept Learning",
             "points":["Hypothesis: consistent with all examples","Version space: all consistent hypotheses","Candidate Elimination refines boundaries"],
             "formula":r"$h\in VS\Leftrightarrow h$ consistent with $D$","diagram":None},
            {"num":"76","title":"Find-S Algorithm",
             "points":["Start most specific; generalise for positives","Ignores negative examples","Returns most specific consistent hypothesis"],
             "formula":r"$h\leftarrow h\cup x^+\;(\mathrm{LGG})$","diagram":None},
            {"num":"77","title":"Candidate Elimination",
             "points":["Maintains S (specific) and G (general) bounds","Positive: remove inconsistent G hypotheses","Negative: remove inconsistent S hypotheses"],
             "formula":r"$VS=[S,G]\text{ over the lattice}$","diagram":None},
            {"num":"78","title":"Inductive Bias",
             "points":["Assumptions enabling generalisation","Stronger bias → fewer data needed","Accuracy depends on bias matching data"],
             "formula":r"$h\notin VS\Rightarrow\text{bias applied}$","diagram":None},
            {"num":"86","title":"LDA",
             "points":["Maximise between-class / within-class scatter","Fisher's criterion for projection","Both classification and dimensionality reduction"],
             "formula":r"$J(\mathbf{w})=\frac{\mathbf{w}^T\mathbf{S}_B\mathbf{w}}{\mathbf{w}^T\mathbf{S}_W\mathbf{w}}$","diagram":"pca"},
            {"num":"87","title":"t-SNE",
             "points":["Non-linear 2D/3D embedding","Preserves local neighbour structure","Perplexity controls neighbourhood size"],
             "formula":r"$KL(P\|Q)=\sum_{i\neq j}p_{ij}\log\frac{p_{ij}}{q_{ij}}$","diagram":"kmeans"},
        ],
    },
    {
        "title": "Regression Variants",
        "desc":  "Regularised and non-standard regression methods",
        "color": PALETTE[15],
        "topics": [
            {"num":"81","title":"Ridge Regression",
             "points":["L2 penalty: λΣwᵢ²","Shrinks all coefficients toward 0","Closed-form solution exists"],
             "formula":r"$\hat{\mathbf{w}}=(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$","diagram":"ridge_lasso"},
            {"num":"82","title":"Lasso Regression",
             "points":["L1 penalty: λΣ|wᵢ|","Exact zero coefficients → feature selection","No closed form — use coordinate descent"],
             "formula":r"$\min\|y-X\mathbf{w}\|^2+\lambda\|\mathbf{w}\|_1$","diagram":"ridge_lasso"},
            {"num":"83","title":"Polynomial Regression",
             "points":["Add x², x³, … as new features","Still linear in the parameters","High degree → overfitting"],
             "formula":r"$y=w_0+w_1 x+w_2 x^2+\cdots+w_d x^d$","diagram":"regression_line"},
            {"num":"84","title":"Isotonic Regression",
             "points":["Fits non-decreasing (monotone) function","Pool Adjacent Violators algorithm","Useful for calibration"],
             "formula":r"$\min\sum(y_i-\hat{y}_i)^2\;\text{s.t. }\hat{y}_i\leq\hat{y}_{i+1}$","diagram":"regression_line"},
            {"num":"85","title":"Elastic Net",
             "points":["Combines L1 and L2 penalties","Groups correlated features together","Two hyperparameters: α, ρ"],
             "formula":r"$\lambda\left[\rho\|\mathbf{w}\|_1+\frac{1-\rho}{2}\|\mathbf{w}\|_2^2\right]$","diagram":"ridge_lasso"},
            {"num":"109","title":"Linear Learning Machines",
             "points":["Perceptron, LMS, Widrow–Hoff","Convergence theorem for separable data","Foundation of deep learning"],
             "formula":r"$f(\mathbf{x})=\text{sign}(\mathbf{w}^T\mathbf{x}+b)$","diagram":"regression_line"},
        ],
    },
    {
        "title": "Lazy & Instance-Based Learning",
        "desc":  "Models that defer computation to query time and memorise training data",
        "color": PALETTE[16],
        "topics": [
            {"num":"88","title":"Lazy Learning",
             "points":["No explicit training phase","All computation at query time","High memory; flexible to local structure"],
             "formula":r"$\hat{y}=\arg\max_y \sum_{x_i\in N(x)}\mathbf{1}[y_i=y]$","diagram":"lazy_learning"},
            {"num":"89","title":"Weighted K-NN",
             "points":["Closer neighbours get more weight","wᵢ = 1/d(x,xᵢ)² common","Smoother decision boundaries"],
             "formula":r"$\hat{y}=\arg\max_y\sum_{i\in N(x)}\frac{y_i=y}{d(x,x_i)^2}$","diagram":"lazy_learning"},
            {"num":"90","title":"Case-Based Reasoning",
             "points":["Retrieve similar past cases","Adapt solution to current problem","4R cycle: Retrieve, Reuse, Revise, Retain"],
             "formula":r"$\text{sim}(c_1,c_2)=\sum_i w_i f(c_1^i,c_2^i)$","diagram":"lazy_learning"},
        ],
    },
    {
        "title": "Stream & Adaptive Learning",
        "desc":  "Algorithms that learn from infinite data streams with concept drift",
        "color": PALETTE[17],
        "topics": [
            {"num":"117","title":"Stream-Based & Adaptive Learning",
             "points":["One-pass over infinite data","Bounded memory O(1) or O(k)","Drift detectors trigger model update"],
             "formula":r"$\forall t:\;|\mathcal{M}_t|\leq M$","diagram":"stream_drift"},
            {"num":"118","title":"DenStream",
             "points":["Fading function f(t)=2^{−λt}","p-MC / o-MC micro-clusters","Offline DBSCAN on p-MC centroids"],
             "formula":r"$w=\sum_i 2^{-\lambda(t_c-t_i)}$","diagram":"dbscan"},
            {"num":"119","title":"ADWIN",
             "points":["Adaptive sliding window detector","Hoeffding-bound based cut test","Removes old data on drift detection"],
             "formula":r"$|\hat\mu_0-\hat\mu_1|>\varepsilon_{cut}$","diagram":"stream_drift"},
            {"num":"120","title":"VFDT & CVFDT",
             "points":["Hoeffding bound: use n samples to pick split","CVFDT adds sliding-window adaptation","Continuous monitoring of best split"],
             "formula":r"$\varepsilon=\sqrt{\frac{R^2\ln(1/\delta)}{2n}}$","diagram":"decision_tree"},
            {"num":"121","title":"Concept Drift Detection",
             "points":["DDM: error rate + std dev threshold","EDDM: inter-error distance grows","Page-Hinkley: cumulative sum test"],
             "formula":r"$p_t+s_t>p_{min}+k\cdot s_{min}$","diagram":"stream_drift"},
            {"num":"122","title":"MONIC",
             "points":["Tracks cluster transitions over time windows","Overlap: |Cᵢ∩Cⱼ|/|Cᵢ|","Survive/split/merge/appear/disappear events"],
             "formula":r"$o(C_i,C_j)=\frac{|C_i\cap C_j|}{|C_i|}$","diagram":"kmeans"},
            {"num":"125","title":"CluStream",
             "points":["CF sufficient stats: CF1x, CF2x, CF1t, CF2t, n","Online: RMSD boundary assignment","Offline: weighted k-means on micro-centroids"],
             "formula":r"$\text{RMSD}=\sqrt{\frac{CF2^x}{n}-\left(\frac{CF1^x}{n}\right)^2}$","diagram":"kmeans"},
        ],
    },
    {
        "title": "Time Series & Explainability",
        "desc":  "Classical forecasting and model-agnostic explanation methods",
        "color": PALETTE[18],
        "topics": [
            {"num":"116","title":"Advanced Time Series ML",
             "points":["Feature engineering: lag, rolling stats","Tree-based & NN models for TS","Cross-validation must respect time order"],
             "formula":r"$X_t=f(X_{t-1},\ldots,X_{t-p})$","diagram":"arima_forecast"},
            {"num":"124","title":"ARIMA & SARIMA",
             "points":["AR(p): past values; MA(q): past errors","I(d): differencing for stationarity","SARIMA adds seasonal (P,D,Q,s) terms"],
             "formula":r"$\phi(B)(1-B)^d X_t=\theta(B)\varepsilon_t$","diagram":"arima_forecast"},
            {"num":"123","title":"SHAP Values",
             "points":["Shapley value: fair credit attribution","Efficiency: Σφᵢ = f(x) − E[f]","TreeExplainer: exact O(TLD²)"],
             "formula":r"$\phi_i=\sum_{S\subseteq F\setminus i}\frac{|S|!(|F|-|S|-1)!}{|F|!}[v(S\cup i)-v(S)]$","diagram":"shap_bars"},
        ],
    },
    {
        "title": "Capstone & Projects",
        "desc":  "End-to-end ML system design, including data, modelling, and deployment",
        "color": PALETTE[19],
        "topics": [
            {"num":"115","title":"End-to-End Real-World ML Project",
             "points":["EDA → feature engineering → modelling","Baseline → tuning → ensembling","Evaluation on hold-out; deployment pipeline"],
             "formula":r"$\text{Pipeline: }\mathcal{D}\to f_\theta\to\hat{y}$","diagram":"roc_curve"},
        ],
    },
]


# ============================================================
# LAYOUT ENGINE
# ============================================================

def _darken(hex_color, amount=0.20):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(
        max(0, int(r*(1-amount))),
        max(0, int(g*(1-amount))),
        max(0, int(b*(1-amount))),
    )


def _lighten(hex_color, amount=0.80):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(
        min(255, int(r + (255-r)*amount)),
        min(255, int(g + (255-g)*amount)),
        min(255, int(b + (255-b)*amount)),
    )


def draw_topic_card(fig, ax, x0, y0, w, h, topic, color):
    """Draw one topic card at (x0,y0,w,h) in axes-fraction space."""
    S = 0.0012
    # Shadow
    ax.add_patch(FancyBboxPatch(
        (x0+S, y0-S), w, h,
        boxstyle="round,pad=0.003",
        linewidth=0, facecolor="#aaaaaa", alpha=0.25,
        transform=ax.transAxes, zorder=1, clip_on=False))

    # Card body
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle="round,pad=0.003",
        linewidth=0.6, edgecolor="#cccccc", facecolor=CARD_BG,
        transform=ax.transAxes, zorder=2, clip_on=False))

    # Coloured header strip (top 18% of card)
    hdr_h = h * 0.195
    ax.add_patch(FancyBboxPatch(
        (x0, y0+h-hdr_h), w, hdr_h,
        boxstyle="round,pad=0.003",
        linewidth=0, facecolor=color,
        transform=ax.transAxes, zorder=3, clip_on=False))

    # Topic number pill
    pill_r = hdr_h * 0.34
    px = x0 + pill_r * 1.7
    py = y0 + h - hdr_h / 2
    ax.add_patch(plt.Circle(
        (px, py), pill_r,
        facecolor=_darken(color, 0.35), linewidth=0,
        transform=ax.transAxes, zorder=4, clip_on=False))
    ax.text(px, py, topic["num"],
            transform=ax.transAxes, ha="center", va="center",
            fontsize=6.5, fontweight="bold", color="white",
            zorder=5, clip_on=False)

    # Topic title in header
    ax.text(x0 + pill_r*3.5, y0 + h - hdr_h/2,
            topic["title"],
            transform=ax.transAxes, ha="left", va="center",
            fontsize=8.8, fontweight="bold", color="white",
            zorder=5, clip_on=False)

    # Left accent bar
    bar_w = 0.003
    ax.add_patch(FancyBboxPatch(
        (x0, y0), bar_w, h - hdr_h,
        boxstyle="square,pad=0",
        linewidth=0, facecolor=_lighten(color, 0.55),
        transform=ax.transAxes, zorder=3, clip_on=False))

    # --- Formula (below header) ---
    content_top = y0 + h - hdr_h - 0.005
    formula_y   = content_top - 0.013
    ax.text(x0 + bar_w + 0.010, formula_y,
            topic.get("formula", ""),
            transform=ax.transAxes, ha="left", va="top",
            fontsize=7.2, color=FORMULA_FG,
            zorder=4, clip_on=False)

    # --- Bullet points ---
    bullets = topic.get("points", [])
    left_w  = w * 0.52   # fraction given to text
    bul_top = formula_y - 0.016
    for i, pt in enumerate(bullets):
        by = bul_top - i * 0.016
        ax.text(x0 + bar_w + 0.012, by, "▸",
                transform=ax.transAxes, ha="left", va="top",
                fontsize=5.5, color=color, zorder=4, clip_on=False)
        ax.text(x0 + bar_w + 0.022, by, pt,
                transform=ax.transAxes, ha="left", va="top",
                fontsize=6.5, color=BULLET_FG, zorder=4, clip_on=False)

    # --- Diagram (right panel, inset axes) ---
    diagram_key = topic.get("diagram")
    # Convert card axes-fraction coords → figure-fraction coords
    # The main ax fills the full figure, so they're the same.
    diag_x = x0 + w * 0.535
    diag_y = y0 + h * 0.075
    diag_w = w * 0.440
    diag_h = h * 0.700
    ax_diag = fig.add_axes([diag_x, diag_y, diag_w, diag_h])
    ax_diag.patch.set_facecolor(_lighten(color, 0.93))
    for sp in ax_diag.spines.values():
        sp.set_color(_lighten(color, 0.60))
        sp.set_linewidth(0.5)
    draw_fn = DIAGRAM_FUNS.get(diagram_key, diag_placeholder)
    draw_fn(ax_diag)
    ax_diag.set_zorder(5)


def build_section_poster(section_idx, section, pdf):
    topics = section["topics"]
    color  = section["color"]
    n      = len(topics)

    # Grid layout: 3 columns, auto rows
    ncols = 3
    nrows = math.ceil(n / ncols)

    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI, facecolor=BG)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off"); ax.set_facecolor(BG)

    # ── Header bar ──────────────────────────────────────────────────────
    ax.add_patch(FancyBboxPatch(
        (0, BODY_T), 1.0, HDR_H,
        boxstyle="square,pad=0",
        linewidth=0, facecolor=TITLE_BAR,
        transform=ax.transAxes, zorder=10, clip_on=False))

    # Accent stripe in section colour
    ax.plot([0, 1], [1.0, 1.0], color=color, linewidth=9,
            transform=ax.transAxes, zorder=11, clip_on=False)

    # Section number badge
    badge_r = HDR_H * 0.38
    bx = PAD + badge_r
    by = BODY_T + HDR_H / 2
    ax.add_patch(plt.Circle(
        (bx, by), badge_r, facecolor=color, linewidth=0,
        transform=ax.transAxes, zorder=11, clip_on=False))
    ax.text(bx, by, f"{section_idx+1:02d}",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=14, fontweight="bold", color="white", zorder=12)

    ax.text(bx + badge_r * 2.1, BODY_T + HDR_H * 0.64,
            section["title"],
            transform=ax.transAxes, ha="left", va="center",
            fontsize=24, fontweight="bold", color="white", zorder=11)

    ax.text(bx + badge_r * 2.1, BODY_T + HDR_H * 0.22,
            section["desc"],
            transform=ax.transAxes, ha="left", va="center",
            fontsize=10, color="#aab4cc", zorder=11)

    ax.text(0.98, BODY_T + HDR_H * 0.43,
            "github.com/ranjiGT/ai-machine-learning-codes",
            transform=ax.transAxes, ha="right", va="center",
            fontsize=8, color="#6677aa", zorder=11)

    # ── Footer bar ──────────────────────────────────────────────────────
    ax.add_patch(FancyBboxPatch(
        (0, 0), 1.0, FOOT_H,
        boxstyle="square,pad=0",
        linewidth=0, facecolor=TITLE_BAR,
        transform=ax.transAxes, zorder=10, clip_on=False))
    ax.text(0.5, FOOT_H/2,
            "Ranjith Raj Valavanthara  ·  CC BY-NC 4.0  ·  2026",
            transform=ax.transAxes, ha="center", va="center",
            fontsize=8, color="#8899bb", zorder=11)

    # ── Card grid ───────────────────────────────────────────────────────
    body_h  = BODY_T - BODY_B
    usable_w = 1.0 - 2*PAD
    usable_h = body_h - 2*PAD

    card_w = (usable_w - (ncols-1)*GAP) / ncols
    card_h = (usable_h - (nrows-1)*GAP) / nrows

    for idx, topic in enumerate(topics):
        col  = idx % ncols
        row  = idx // ncols
        x0   = PAD + col * (card_w + GAP)
        y0   = BODY_B + PAD + (nrows-1-row) * (card_h + GAP)
        draw_topic_card(fig, ax, x0, y0, card_w, card_h, topic, color)

    pdf.savefig(fig, dpi=DPI, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"  Page {section_idx+1:02d}: {section['title']}  ({n} topics)")


# ============================================================
# ENTRY POINT
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate per-topic ML poster PDF (one page per theme)")
    parser.add_argument(
        "--output", default="topic_posters.pdf",
        help="Output PDF path (default: topic_posters.pdf in repo root)")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating {len(SECTIONS)}-page topic poster PDF → {output.resolve()}")
    with PdfPages(output) as pdf:
        for i, section in enumerate(SECTIONS):
            build_section_poster(i, section, pdf)
    print(f"\nDone! Saved → {output.resolve()}")


if __name__ == "__main__":
    main()

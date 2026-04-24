# AI & Machine Learning Practical Codes

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD)
[![Open Linear Regression Notebook](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/01_linear_regression/linear_regression_starter.ipynb)

Practical Python examples for Machine Learning and Data Science topics from my YouTube channel.

- Channel: [RanjiRaj18](https://www.youtube.com/@RanjiRaj18)
- Playlist: [Machine Learning and Data Science Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR)

This repository is designed for learners who want:
- topic-wise practical code
- Jupyter notebooks that can run locally
- one-click cloud execution using Binder

## Repository Goals

- Keep each topic short, practical, and beginner-friendly.
- Map every video to runnable Python code.
- Make it easy for subscribers to fork, run, and learn.

## Project Structure

```text
.
├── notebooks/
│   └── 01_linear_regression/
│       └── linear_regression_starter.ipynb
├── src/
│   ├── data/
│   ├── ml_basics/
│   └── utils/
├── requirements.txt
├── runtime.txt
├── environment.yml
├── CONTRIBUTING.md
└── README.md
```

## Run Locally (Jupyter)

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Start Jupyter Lab.

```bash
git clone https://github.com/ranjiGT/ai-machine-learning-codes.git
cd ai-machine-learning-codes

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

jupyter lab
```

## Run in the Cloud (Binder)

Once the repo is pushed to GitHub, anyone can open notebooks without local setup.

Use this URL format:

```text
https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD
```

### Binder Troubleshooting

- First build can take several minutes. If it times out, retry once.
- If `HEAD` fails, verify your default branch contains `requirements.txt`, `runtime.txt`, and `environment.yml`.
- Avoid pinning conflicting Jupyter packages. This repo uses `jupyterlab>=4.3,<5` and does not pin `notebook`.
- If Binder reports dependency resolution errors, simplify version pins in `requirements.txt` and rebuild.

## Topic-to-Video Mapping

> 113 topics across 11 themes — click a section to expand. Each tile opens the interactive Binder notebook.

<details open>
<summary><b>🟦 Supervised Learning — Core Classifiers (01–17)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>01. Linear Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/01_linear_regression/linear_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=e9VYOWWP6zM">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>02. Logistic Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/02_logistic_regression/logistic_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=S4IG2wv9Lnk">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>03. Decision Trees</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/03_decision_trees/decision_tree_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=k3SYtpv5y6Y">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>04. Random Forest</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/04_random_forest/random_forest_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=p2arCEdJ8Fk">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>05. KNN</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/05_knn/knn_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=Pqo9o0286Qs">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>06. PCA</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/06_pca/pca_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=7bpjiA2VDZE">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>07. Naive Bayes</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/07_naive_bayes/naive_bayes_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=AkPSgAh3q4g">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>08. Underfitting vs Overfitting</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/08_underfitting_overfitting/underfitting_overfitting_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=WxINg-eof2M">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>09. Reduced Error Pruning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/09_reduced_error_pruning/reduced_error_pruning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=4VAOjWCHzXk">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>10. Random Sampling</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/10_random_sampling/random_sampling_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=zWvGgThvZ7g">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>11. Cross Validation</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/11_cross_validation/cross_validation_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=bPqliS8U3XE">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>12. Nested Cross Validation</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/12_nested_cross_validation/nested_cross_validation_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=X6HeBURppHc">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>13. Hold-Out Method</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/13_holdout_method/holdout_method_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=4NnI3SBuww4">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>14. Hyperparameter Tuning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/14_hyperparameter_tuning/hyperparameter_tuning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=cyIINCqyi5g">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>15. Bootstrap Evaluation</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/15_bootstrap_evaluation/bootstrap_evaluation_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=CAGIcnxB-PU">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>16. Ensemble Methods</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/16_ensemble_methods/ensemble_methods_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=SZbEZcdyOWU">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>17. Hunt's Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/17_hunts_algorithm/hunts_algorithm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=-kfOyPwGxww">▶ Watch</a>
</td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🟨 Probabilistic & Rule-Based Methods (18–26)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>18. Impurity Measures</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/18_impurity_measures/impurity_measures_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=kgCLE2FOQGU">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>19. Rule-Based Classifier</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/19_rule_based_classifier/rule_based_classifier_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=fmZaVTpRO-Q">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>20. Sequential Covering Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/20_sequential_covering_algorithm/sequential_covering_algorithm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=wgyvJCGOSj8">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>21. Bayesian Belief Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/21_bayesian_belief_networks/bayesian_belief_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=ibKIrRGUxG4">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>22. Artificial Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/22_artificial_neural_networks/artificial_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=1BZm5RAljn0">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>23. Feed Forward Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/23_feed_forward_neural_networks/feed_forward_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=6AK7qC2XGHY">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>24. Support Vector Machine</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/24_support_vector_machine/support_vector_machine_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=nyFFTge142U">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>25. Maximal Margin Classifier</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/25_maximal_margin_classifier/maximal_margin_classifier_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=2b2YuHwm_hw">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>26. Non-Linear SVM</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/26_non_linear_svm/non_linear_svm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=qjErFs0tepw">▶ Watch</a>
</td>
</tr>
</table>

</details>

<details>
<summary><b>🟧 Class Imbalance & Evaluation Curves (27–30)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>27. Class Imbalance Problem and Solutions</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/27_class_imbalance_problem/class_imbalance_problem_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>28. SMOTE</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/28_smote/smote_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>29. ROC and AUC Curves</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/29_roc_auc_curves/roc_auc_curves_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>30. ISO Accuracy Lines</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/30_iso_accuracy_lines/iso_accuracy_lines_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🟩 Clustering (31–46)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>31. Unsupervised Learning - Clustering</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/31_unsupervised_learning_clustering/unsupervised_learning_clustering_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>32. K-means Clustering</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/32_kmeans_clustering/kmeans_clustering_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>33. Bisecting K-means</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/33_bisecting_kmeans/bisecting_kmeans_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>34. Cluster Similarity Measures</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/34_cluster_similarity_measures/cluster_similarity_measures_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>35. Fuzzy C-Means</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/35_fuzzy_cmeans/fuzzy_cmeans_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>36. DBSCAN Technique</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/36_dbscan_technique/dbscan_technique_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>37. Mean-Shift Clustering</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/37_mean_shift_clustering/mean_shift_clustering_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>38. Hierarchical Clustering</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/38_hierarchical_clustering/hierarchical_clustering_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>39. Linkage Measures</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/39_linkage_measures/linkage_measures_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>40. Cluster Validation Techniques</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/40_cluster_validation_techniques/cluster_validation_techniques_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>41. Cohesion and Separation in Cluster</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/41_cohesion_separation_clusters/cohesion_separation_clusters_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>42. Silhouette Coefficient</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/42_silhouette_coefficient/silhouette_coefficient_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>43. Cophenetic Correlation Coefficient</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/43_cophenetic_correlation_coefficient/cophenetic_correlation_coefficient_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>44. Hopkins Statistic</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/44_hopkins_statistic/hopkins_statistic_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>45. Cluster Purity</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/45_cluster_purity/cluster_purity_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>46. Rand Statistic and Jaccard Index</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/46_rand_jaccard_index/rand_jaccard_index_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🟪 Active Learning (47–56)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>47. Active Learning in Machine Learning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/47_active_learning_intro/active_learning_intro_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>48. Membership Query Synthesis</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/48_membership_query_synthesis/membership_query_synthesis_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>49. Stream-Based Selective Sampling</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/49_stream_based_selective_sampling/stream_based_selective_sampling_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>50. Pool-Based Sampling</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/50_pool_based_sampling/pool_based_sampling_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>51. Uncertainty Sampling</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/51_uncertainty_sampling/uncertainty_sampling_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>52. Query by Committee</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/52_query_by_committee/query_by_committee_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>53. Expected Model Change</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/53_expected_model_change/expected_model_change_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>54. Expected Error Reduction</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/54_expected_error_reduction/expected_error_reduction_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>55. Variance Reduction in Active Learning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/55_variance_reduction_active_learning/variance_reduction_active_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>56. Information Density in Active Learning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/56_information_density_active_learning/information_density_active_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🔵 Multi-label & Multi-class Classification (57–64)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>57. Multi-class Classification (OvR and OvO)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/57_multiclass_ovr_ovo/multiclass_ovr_ovo_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>58. Multi-label Classification</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/58_multilabel_classification/multilabel_classification_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>59. Problem Transformation Methods</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/59_problem_transformation_methods/problem_transformation_methods_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>60. Binary Relevance</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/60_binary_relevance/binary_relevance_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>61. Label Powerset</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/61_label_powerset/label_powerset_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>62. Random K Labelsets (RAkEL)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/62_rakel/rakel_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>63. Multi-label Evaluation Metrics</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/63_multilabel_evaluation_metrics/multilabel_evaluation_metrics_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>64. Multi-Target Classification</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/64_multitarget_classification/multitarget_classification_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🟫 Pattern Mining & Statistical Theory (65–74)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>65. Laplace Correction</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/65_laplace_correction/laplace_correction_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>66. Association Rules</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/66_association_rules/association_rules_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>67. Apriori Principle</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/67_apriori_principle/apriori_principle_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>68. Item-set Lattice</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/68_itemset_lattice/itemset_lattice_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>69. Lift Measure</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/69_lift_measure/lift_measure_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>70. ECLAT</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/70_eclat/eclat_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>71. Family-Wise Error Rate (FWER)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/71_fwer/fwer_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>72. False Discovery Rate (FDR)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/72_fdr/fdr_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>73. Singular Value Decomposition (SVD)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/73_svd/svd_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>74. Vapnik–Chervonenkis (VC) Dimension</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/74_vc_dimension/vc_dimension_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>⬛ Concept Learning, Algorithms & Regression (75–85)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>75. Concept Learning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/75_concept_learning/concept_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>76. Find-S Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/76_find_s_algorithm/find_s_algorithm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>77. Candidate Elimination Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/77_candidate_elimination/candidate_elimination_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>78. Inductive Bias</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/78_inductive_bias/inductive_bias_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>79. ID3 Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/79_id3_algorithm/id3_algorithm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>80. Gradient Descent Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/80_gradient_descent/gradient_descent_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>81. Ridge Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/81_ridge_regression/ridge_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>82. Lasso Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/82_lasso_regression/lasso_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>83. Polynomial Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/83_polynomial_regression/polynomial_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>84. Isotonic Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/84_isotonic_regression/isotonic_regression_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>85. Elastic Net Regression</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/85_elastic_net/elastic_net_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🔶 Dimensionality Reduction & Lazy Learning (86–90)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>86. Linear Discriminant Analysis (LDA)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/86_linear_discriminant_analysis/linear_discriminant_analysis_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>87. t-SNE</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/87_t_sne/t_sne_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>88. Lazy Learning Algorithms</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/88_lazy_learning_algorithms/lazy_learning_algorithms_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>89. Weighted K-NN</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/89_weighted_knn/weighted_knn_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>90. Case-Based Reasoning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/90_case_based_reasoning/case_based_reasoning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>🔴 Deep Learning (91–107)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>91. Introduction to Deep Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/91_intro_deep_neural_networks/intro_deep_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>92. Structure of a Neuron</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/92_structure_of_a_neuron/structure_of_a_neuron_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>93. Weight Matrix in Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/93_weight_matrix_neural_networks/weight_matrix_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>94. Generalization of Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/94_generalization_neural_networks/generalization_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>95. Learning Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/95_learning_neural_networks/learning_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>96. Vectorization of Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/96_vectorization_neural_networks/vectorization_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>97. Decision Boundary of Neural Networks</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/97_decision_boundary_neural_networks/decision_boundary_neural_networks_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>98. The Chain Rule</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/98_chain_rule/chain_rule_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>99. Backpropagation Algorithm</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/99_backpropagation_algorithm/backpropagation_algorithm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>100. The Delta Rule</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/100_delta_rule/delta_rule_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>101. Vanishing and Exploding Gradients</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/101_vanishing_exploding_gradients/vanishing_exploding_gradients_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>102. Step Activation Function</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/102_step_activation_function/step_activation_function_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>103. Sigmoid Activation Function</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/103_sigmoid_activation_function/sigmoid_activation_function_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>104. Hyperbolic Activation Function</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/104_hyperbolic_activation_function/hyperbolic_activation_function_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>105. ReLU Activation Function</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/105_relu_activation_function/relu_activation_function_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>106. Teacher Forcing in Deep Learning</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/106_teacher_forcing_deep_learning/teacher_forcing_deep_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>107. LSTM</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/107_lstm/lstm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td></td>
</tr>
</table>

</details>

<details>
<summary><b>⚫ Advanced & Semi-Supervised Methods (108–113)</b></summary>
<br/>

<table>
<tr>
<td align="center" width="33%">
<b>108. Regression Evaluation Metrics</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/108_regression_evaluation_metrics/regression_evaluation_metrics_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>109. Linear Learning Machines (LLMs)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/109_linear_learning_machines/linear_learning_machines_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>110. Kernel Function and Kernel Matrix</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/110_kernel_function_matrix/kernel_function_matrix_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
<tr>
<td align="center" width="33%">
<b>111. Semi-Supervised Learning (SSL)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/111_semi_supervised_learning/semi_supervised_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>112. Safe Semi-Supervised Learning (SSL)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/112_safe_semi_supervised_learning/safe_semi_supervised_learning_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
<td align="center" width="33%">
<b>113. Semi-Supervised SVM (S3VM & TSVM)</b><br/>
<a href="https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/113_s3vm_tsvm/s3vm_tsvm_starter.ipynb">📓 Open</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR">▶ Watch</a>
</td>
</tr>
</table>

</details>

## Co-Author Setup

If you want to co-author with [yatchmaster](https://github.com/yatchmaster):

1. Add `yatchmaster` as a collaborator in GitHub repository settings.
2. Use feature branches and pull requests.
3. Add co-author trailers in commit messages when both contribute:

```text
Co-authored-by: yatchmaster <their-email@users.noreply.github.com>
```

See `CONTRIBUTING.md` for a full workflow.

## Contributing

Contributions are welcome from subscribers and learners.
Please read `CONTRIBUTING.md` before opening pull requests.

## License

This project is open for educational use. Add your preferred license file (MIT recommended).

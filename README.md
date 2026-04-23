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

Create one folder per topic and map it to your YouTube video:

| Topic | Notebook | Run on Binder | YouTube |
| --- | --- | --- | --- |
| Linear Regression | `notebooks/01_linear_regression/linear_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/01_linear_regression/linear_regression_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=e9VYOWWP6zM) |
| Logistic Regression | `notebooks/02_logistic_regression/logistic_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/02_logistic_regression/logistic_regression_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=S4IG2wv9Lnk) |
| Decision Trees | `notebooks/03_decision_trees/decision_tree_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/03_decision_trees/decision_tree_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=k3SYtpv5y6Y) |
| Random Forest | `notebooks/04_random_forest/random_forest_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/04_random_forest/random_forest_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=p2arCEdJ8Fk) |
| KNN | `notebooks/05_knn/knn_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/05_knn/knn_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=Pqo9o0286Qs) |
| PCA | `notebooks/06_pca/pca_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/06_pca/pca_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=7bpjiA2VDZE) |
| Naive Bayes | `notebooks/07_naive_bayes/naive_bayes_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/07_naive_bayes/naive_bayes_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=AkPSgAh3q4g) |
| Underfitting vs Overfitting | `notebooks/08_underfitting_overfitting/underfitting_overfitting_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/08_underfitting_overfitting/underfitting_overfitting_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=WxINg-eof2M) |
| Reduced Error Pruning | `notebooks/09_reduced_error_pruning/reduced_error_pruning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/09_reduced_error_pruning/reduced_error_pruning_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=4VAOjWCHzXk) |
| Random Sampling | `notebooks/10_random_sampling/random_sampling_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/10_random_sampling/random_sampling_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=zWvGgThvZ7g) |
| Cross Validation | `notebooks/11_cross_validation/cross_validation_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/11_cross_validation/cross_validation_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=bPqliS8U3XE) |
| Nested Cross Validation | `notebooks/12_nested_cross_validation/nested_cross_validation_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/12_nested_cross_validation/nested_cross_validation_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=X6HeBURppHc) |
| Hold-Out Method | `notebooks/13_holdout_method/holdout_method_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/13_holdout_method/holdout_method_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=4NnI3SBuww4) |
| Hyperparameter Tuning | `notebooks/14_hyperparameter_tuning/hyperparameter_tuning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/14_hyperparameter_tuning/hyperparameter_tuning_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=cyIINCqyi5g) |
| Bootstrap Evaluation | `notebooks/15_bootstrap_evaluation/bootstrap_evaluation_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/15_bootstrap_evaluation/bootstrap_evaluation_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=CAGIcnxB-PU) |
| Ensemble Methods | `notebooks/16_ensemble_methods/ensemble_methods_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/16_ensemble_methods/ensemble_methods_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=SZbEZcdyOWU) |
| Hunt's Algorithm | `notebooks/17_hunts_algorithm/hunts_algorithm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/17_hunts_algorithm/hunts_algorithm_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=-kfOyPwGxww) |
| Impurity Measures | `notebooks/18_impurity_measures/impurity_measures_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/18_impurity_measures/impurity_measures_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=kgCLE2FOQGU) |
| Rule-Based Classifier | `notebooks/19_rule_based_classifier/rule_based_classifier_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/19_rule_based_classifier/rule_based_classifier_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=fmZaVTpRO-Q) |
| Sequential Covering Algorithm | `notebooks/20_sequential_covering_algorithm/sequential_covering_algorithm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/20_sequential_covering_algorithm/sequential_covering_algorithm_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=wgyvJCGOSj8) |
| Bayesian Belief Networks | `notebooks/21_bayesian_belief_networks/bayesian_belief_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/21_bayesian_belief_networks/bayesian_belief_networks_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=ibKIrRGUxG4) |
| Artificial Neural Networks | `notebooks/22_artificial_neural_networks/artificial_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/22_artificial_neural_networks/artificial_neural_networks_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=1BZm5RAljn0) |
| Feed Forward Neural Networks | `notebooks/23_feed_forward_neural_networks/feed_forward_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/23_feed_forward_neural_networks/feed_forward_neural_networks_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=6AK7qC2XGHY) |
| Support Vector Machine | `notebooks/24_support_vector_machine/support_vector_machine_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/24_support_vector_machine/support_vector_machine_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=nyFFTge142U) |
| Maximal Margin Classifier | `notebooks/25_maximal_margin_classifier/maximal_margin_classifier_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/25_maximal_margin_classifier/maximal_margin_classifier_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=2b2YuHwm_hw) |
| Non-Linear SVM | `notebooks/26_non_linear_svm/non_linear_svm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/26_non_linear_svm/non_linear_svm_starter.ipynb) | [Watch](https://www.youtube.com/watch?v=qjErFs0tepw) |
| Class Imbalance Problem and Solutions | `notebooks/27_class_imbalance_problem/class_imbalance_problem_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/27_class_imbalance_problem/class_imbalance_problem_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| SMOTE | `notebooks/28_smote/smote_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/28_smote/smote_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| ROC and AUC Curves | `notebooks/29_roc_auc_curves/roc_auc_curves_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/29_roc_auc_curves/roc_auc_curves_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| ISO Accuracy Lines | `notebooks/30_iso_accuracy_lines/iso_accuracy_lines_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/30_iso_accuracy_lines/iso_accuracy_lines_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Unsupervised Learning - Clustering | `notebooks/31_unsupervised_learning_clustering/unsupervised_learning_clustering_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/31_unsupervised_learning_clustering/unsupervised_learning_clustering_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| K-means Clustering | `notebooks/32_kmeans_clustering/kmeans_clustering_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/32_kmeans_clustering/kmeans_clustering_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Bisecting K-means | `notebooks/33_bisecting_kmeans/bisecting_kmeans_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/33_bisecting_kmeans/bisecting_kmeans_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cluster Similarity Measures | `notebooks/34_cluster_similarity_measures/cluster_similarity_measures_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/34_cluster_similarity_measures/cluster_similarity_measures_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Fuzzy C-Means | `notebooks/35_fuzzy_cmeans/fuzzy_cmeans_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/35_fuzzy_cmeans/fuzzy_cmeans_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| DBSCAN Technique | `notebooks/36_dbscan_technique/dbscan_technique_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/36_dbscan_technique/dbscan_technique_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Mean-Shift Clustering | `notebooks/37_mean_shift_clustering/mean_shift_clustering_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/37_mean_shift_clustering/mean_shift_clustering_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Hierarchical Clustering | `notebooks/38_hierarchical_clustering/hierarchical_clustering_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/38_hierarchical_clustering/hierarchical_clustering_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Linkage Measures | `notebooks/39_linkage_measures/linkage_measures_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/39_linkage_measures/linkage_measures_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cluster Validation Techniques | `notebooks/40_cluster_validation_techniques/cluster_validation_techniques_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/40_cluster_validation_techniques/cluster_validation_techniques_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cohesion and Separation in Cluster | `notebooks/41_cohesion_separation_clusters/cohesion_separation_clusters_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/41_cohesion_separation_clusters/cohesion_separation_clusters_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Silhouette Coefficient | `notebooks/42_silhouette_coefficient/silhouette_coefficient_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/42_silhouette_coefficient/silhouette_coefficient_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cophenetic Correlation Coefficient | `notebooks/43_cophenetic_correlation_coefficient/cophenetic_correlation_coefficient_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/43_cophenetic_correlation_coefficient/cophenetic_correlation_coefficient_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Hopkins Statistic | `notebooks/44_hopkins_statistic/hopkins_statistic_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/44_hopkins_statistic/hopkins_statistic_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Cluster Purity | `notebooks/45_cluster_purity/cluster_purity_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/45_cluster_purity/cluster_purity_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Rand Statistic and Jaccard Index | `notebooks/46_rand_jaccard_index/rand_jaccard_index_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/46_rand_jaccard_index/rand_jaccard_index_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Active Learning in Machine Learning | `notebooks/47_active_learning_intro/active_learning_intro_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/47_active_learning_intro/active_learning_intro_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Membership Query Synthesis | `notebooks/48_membership_query_synthesis/membership_query_synthesis_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/48_membership_query_synthesis/membership_query_synthesis_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Stream-Based Selective Sampling | `notebooks/49_stream_based_selective_sampling/stream_based_selective_sampling_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/49_stream_based_selective_sampling/stream_based_selective_sampling_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Pool-Based Sampling | `notebooks/50_pool_based_sampling/pool_based_sampling_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/50_pool_based_sampling/pool_based_sampling_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Uncertainty Sampling | `notebooks/51_uncertainty_sampling/uncertainty_sampling_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/51_uncertainty_sampling/uncertainty_sampling_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Query by Committee | `notebooks/52_query_by_committee/query_by_committee_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/52_query_by_committee/query_by_committee_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Expected Model Change | `notebooks/53_expected_model_change/expected_model_change_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/53_expected_model_change/expected_model_change_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Expected Error Reduction | `notebooks/54_expected_error_reduction/expected_error_reduction_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/54_expected_error_reduction/expected_error_reduction_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Variance Reduction in Active Learning | `notebooks/55_variance_reduction_active_learning/variance_reduction_active_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/55_variance_reduction_active_learning/variance_reduction_active_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Information Density in Active Learning | `notebooks/56_information_density_active_learning/information_density_active_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/56_information_density_active_learning/information_density_active_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Multi-class Classification (OvR and OvO) | `notebooks/57_multiclass_ovr_ovo/multiclass_ovr_ovo_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/57_multiclass_ovr_ovo/multiclass_ovr_ovo_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Multi-label Classification | `notebooks/58_multilabel_classification/multilabel_classification_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/58_multilabel_classification/multilabel_classification_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Problem Transformation Methods | `notebooks/59_problem_transformation_methods/problem_transformation_methods_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/59_problem_transformation_methods/problem_transformation_methods_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Binary Relevance | `notebooks/60_binary_relevance/binary_relevance_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/60_binary_relevance/binary_relevance_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Label Powerset | `notebooks/61_label_powerset/label_powerset_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/61_label_powerset/label_powerset_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Random K Labelsets (RAkEL) | `notebooks/62_rakel/rakel_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/62_rakel/rakel_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Multi-label Evaluation Metrics | `notebooks/63_multilabel_evaluation_metrics/multilabel_evaluation_metrics_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/63_multilabel_evaluation_metrics/multilabel_evaluation_metrics_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Multi-Target Classification | `notebooks/64_multitarget_classification/multitarget_classification_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/64_multitarget_classification/multitarget_classification_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Laplace Correction | `notebooks/65_laplace_correction/laplace_correction_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/65_laplace_correction/laplace_correction_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Association Rules | `notebooks/66_association_rules/association_rules_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/66_association_rules/association_rules_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Apriori Principle | `notebooks/67_apriori_principle/apriori_principle_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/67_apriori_principle/apriori_principle_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Item-set Lattice | `notebooks/68_itemset_lattice/itemset_lattice_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/68_itemset_lattice/itemset_lattice_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Lift Measure | `notebooks/69_lift_measure/lift_measure_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/69_lift_measure/lift_measure_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| ECLAT | `notebooks/70_eclat/eclat_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/70_eclat/eclat_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Family-Wise Error Rate (FWER) | `notebooks/71_fwer/fwer_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/71_fwer/fwer_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| False Discovery Rate (FDR) | `notebooks/72_fdr/fdr_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/72_fdr/fdr_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Singular Value Decomposition (SVD) | `notebooks/73_svd/svd_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/73_svd/svd_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Vapnik–Chervonenkis (VC) Dimension | `notebooks/74_vc_dimension/vc_dimension_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/74_vc_dimension/vc_dimension_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Concept Learning | `notebooks/75_concept_learning/concept_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/75_concept_learning/concept_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Find-S Algorithm | `notebooks/76_find_s_algorithm/find_s_algorithm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/76_find_s_algorithm/find_s_algorithm_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Candidate Elimination Algorithm | `notebooks/77_candidate_elimination/candidate_elimination_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/77_candidate_elimination/candidate_elimination_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Inductive Bias | `notebooks/78_inductive_bias/inductive_bias_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/78_inductive_bias/inductive_bias_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| ID3 Algorithm | `notebooks/79_id3_algorithm/id3_algorithm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/79_id3_algorithm/id3_algorithm_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Gradient Descent Algorithm | `notebooks/80_gradient_descent/gradient_descent_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/80_gradient_descent/gradient_descent_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Ridge Regression | `notebooks/81_ridge_regression/ridge_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/81_ridge_regression/ridge_regression_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Lasso Regression | `notebooks/82_lasso_regression/lasso_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/82_lasso_regression/lasso_regression_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Polynomial Regression | `notebooks/83_polynomial_regression/polynomial_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/83_polynomial_regression/polynomial_regression_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Isotonic Regression | `notebooks/84_isotonic_regression/isotonic_regression_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/84_isotonic_regression/isotonic_regression_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Elastic Net Regression | `notebooks/85_elastic_net/elastic_net_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/85_elastic_net/elastic_net_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Linear Discriminant Analysis (LDA) | `notebooks/86_linear_discriminant_analysis/linear_discriminant_analysis_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/86_linear_discriminant_analysis/linear_discriminant_analysis_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| t-SNE | `notebooks/87_t_sne/t_sne_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/87_t_sne/t_sne_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Lazy Learning Algorithms | `notebooks/88_lazy_learning_algorithms/lazy_learning_algorithms_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/88_lazy_learning_algorithms/lazy_learning_algorithms_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Weighted K-NN | `notebooks/89_weighted_knn/weighted_knn_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/89_weighted_knn/weighted_knn_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Case-Based Reasoning | `notebooks/90_case_based_reasoning/case_based_reasoning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/90_case_based_reasoning/case_based_reasoning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Introduction to Deep Neural Networks | `notebooks/Deep Learning/91_intro_deep_neural_networks/intro_deep_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/91_intro_deep_neural_networks/intro_deep_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Structure of a Neuron | `notebooks/Deep Learning/92_structure_of_a_neuron/structure_of_a_neuron_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/92_structure_of_a_neuron/structure_of_a_neuron_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Weight Matrix in Neural Networks | `notebooks/Deep Learning/93_weight_matrix_neural_networks/weight_matrix_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/93_weight_matrix_neural_networks/weight_matrix_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Generalization of Neural Networks | `notebooks/Deep Learning/94_generalization_neural_networks/generalization_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/94_generalization_neural_networks/generalization_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Learning Neural Networks | `notebooks/Deep Learning/95_learning_neural_networks/learning_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/95_learning_neural_networks/learning_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Vectorization of Neural Networks | `notebooks/Deep Learning/96_vectorization_neural_networks/vectorization_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/96_vectorization_neural_networks/vectorization_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Decision Boundary of Neural Networks | `notebooks/Deep Learning/97_decision_boundary_neural_networks/decision_boundary_neural_networks_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/97_decision_boundary_neural_networks/decision_boundary_neural_networks_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| The Chain Rule | `notebooks/Deep Learning/98_chain_rule/chain_rule_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/98_chain_rule/chain_rule_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Backpropagation Algorithm | `notebooks/Deep Learning/99_backpropagation_algorithm/backpropagation_algorithm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/99_backpropagation_algorithm/backpropagation_algorithm_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| The Delta Rule | `notebooks/Deep Learning/100_delta_rule/delta_rule_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/100_delta_rule/delta_rule_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Vanishing and Exploding Gradients | `notebooks/Deep Learning/101_vanishing_exploding_gradients/vanishing_exploding_gradients_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/101_vanishing_exploding_gradients/vanishing_exploding_gradients_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Step Activation Function | `notebooks/Deep Learning/102_step_activation_function/step_activation_function_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/102_step_activation_function/step_activation_function_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Sigmoid Activation Function | `notebooks/Deep Learning/103_sigmoid_activation_function/sigmoid_activation_function_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/103_sigmoid_activation_function/sigmoid_activation_function_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Hyperbolic Activation Function | `notebooks/Deep Learning/104_hyperbolic_activation_function/hyperbolic_activation_function_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/104_hyperbolic_activation_function/hyperbolic_activation_function_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| ReLU Activation Function | `notebooks/Deep Learning/105_relu_activation_function/relu_activation_function_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/105_relu_activation_function/relu_activation_function_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Teacher Forcing in Deep Learning | `notebooks/Deep Learning/106_teacher_forcing_deep_learning/teacher_forcing_deep_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/106_teacher_forcing_deep_learning/teacher_forcing_deep_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| LSTM | `notebooks/Deep Learning/107_lstm/lstm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/Deep%20Learning/107_lstm/lstm_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Regression Evaluation Metrics | `notebooks/108_regression_evaluation_metrics/regression_evaluation_metrics_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/108_regression_evaluation_metrics/regression_evaluation_metrics_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Linear Learning Machines (LLMs) | `notebooks/109_linear_learning_machines/linear_learning_machines_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/109_linear_learning_machines/linear_learning_machines_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Kernel Function and Kernel Matrix | `notebooks/110_kernel_function_matrix/kernel_function_matrix_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/110_kernel_function_matrix/kernel_function_matrix_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Semi-Supervised Learning (SSL) | `notebooks/111_semi_supervised_learning/semi_supervised_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/111_semi_supervised_learning/semi_supervised_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Safe Semi-Supervised Learning (SSL) | `notebooks/112_safe_semi_supervised_learning/safe_semi_supervised_learning_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/112_safe_semi_supervised_learning/safe_semi_supervised_learning_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |
| Semi-Supervised SVM (S3VM & TSVM) | `notebooks/113_s3vm_tsvm/s3vm_tsvm_starter.ipynb` | [Open](https://mybinder.org/v2/gh/ranjiGT/ai-machine-learning-codes/HEAD?urlpath=lab/tree/notebooks/113_s3vm_tsvm/s3vm_tsvm_starter.ipynb) | [Watch Playlist](https://www.youtube.com/watch?v=N7sx9_nX8Ng&list=PLPN-43XehstOjGY6vM6nBpSggHoAv9hkR) |

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

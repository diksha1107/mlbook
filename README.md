# mlbook

This repository contains a collection of Python notebooks focused on machine learning concepts and examples.

## What is in this repository?

- Notebook-based lessons and experiments in [src](src)
- Helper code for plotting and visualization in [utils](utils)
- A small testing or scratch notebook in [tests](tests)
- Local data and environment folders that are kept out of version control

## Repository structure

```text
mlbook/
├── data/         # local data files
├── ml-env/       # local Python environment
├── src/          # main notebooks
├── tests/        # extra or experimental notebooks
├── utils/        # helper modules
└── README.md     # repository summary
```

## Notebook contents

| Notebook | Focus |
|----------|-------|
| [src/CH2_Perceptron.ipynb](src/CH2_Perceptron.ipynb) | Perceptron |
| [src/CH2_Adaline_GD.ipynb](src/CH2_Adaline_GD.ipynb) | Adaline with batch gradient descent |
| [src/CH2_Adaline_SGD.ipynb](src/CH2_Adaline_SGD.ipynb) | Adaline with stochastic gradient descent |
| [src/CH3_LogisticRegression.ipynb](src/CH3_LogisticRegression.ipynb) | Logistic regression |
| [src/CH3_SKlearn_basics.ipynb](src/CH3_SKlearn_basics.ipynb) | Scikit-learn basics and preprocessing |
| [src/CH3_SVM.ipynb](src/CH3_SVM.ipynb) | Support Vector Machines |
| [src/CH3_DecisionTrees.ipynb](src/CH3_DecisionTrees.ipynb) | Decision trees |
| [src/CH4_DataPreprocessing.ipynb](src/CH4_DataPreprocessing.ipynb) | Data preprocessing |
| [src/CH5_DimensionalityReduction.ipynb](src/CH5_DimensionalityReduction.ipynb) | Dimensionality reduction including PCA & LDA |

## Additional files

- [utils/plot_utils.py](utils/plot_utils.py) contains helper functions used by several notebooks.
- [tests/test.ipynb](tests/test.ipynb) is a scratch or experimental notebook.

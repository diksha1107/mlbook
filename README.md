# mlbook

Python notebooks for classic linear models from scratch and introductory scikit-learn examples.

## Notebooks

| File | Topic |
|------|--------|
| [`src/CH2_Perceptron.ipynb`](src/CH2_Perceptron.ipynb) | Perceptron |
| [`src/CH2_Adaline_GD.ipynb`](src/CH2_Adaline_GD.ipynb) | Adaline (batch GD) |
| [`src/CH2_Adaline_SGD.ipynb`](src/CH2_Adaline_SGD.ipynb) | Adaline (SGD) |
| [`src/CH3_LogisticRegression.ipynb`](src/CH3_LogisticRegression.ipynb) | Logistic regression (GD) |
| [`src/CH3_SKlearn_basics.ipynb`](src/CH3_SKlearn_basics.ipynb) | sklearn basics: data loading, preprocessing, pipelines |
| [`src/CH3_SVM.ipynb`](src/CH3_SVM.ipynb) | Support Vector Machine |
| [`src/CH3_DecisionTrees.ipynb`](src/CH3_DecisionTrees.ipynb) | Decision trees |

[`utils/plot_utils.py`](utils/plot_utils.py) — helper functions like `plot_decision_regions` and `plot_loss`.

## Usage

- Open the notebook files from `src/`.
- If you use the provided `ml-env/` virtual environment, activate it with `source ml-env/bin/activate`.
- Notebooks import `utils.plot_utils` from the repository root, so run them with the repo root as the working directory.

## Setup

```bash
python -m venv ml-env && source ml-env/bin/activate  # Windows: ml-env\Scripts\activate
pip install numpy scipy scikit-learn matplotlib pandas jupyter ipykernel
jupyter lab  # or notebook
```

## Data

- Put the UCI Iris CSV at `data/iris.data` (no header) for notebooks that read it with `pd.read_csv`.
- `CH3_SKlearn_basics.ipynb` and other sklearn examples can also use `sklearn.datasets.load_iris()`.

## Notes

- `tests/test.ipynb` is available as an experimental or scratch notebook.
- The `ml-env/` virtual environment and `data/` directory are excluded by `.gitignore`.

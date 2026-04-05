# mlbook

Python notebooks for classic linear models from scratch (Perceptron, Adaline, logistic regression) plus introductory scikit-learn.

## Notebooks

| File | Topic |
|------|--------|
| [`src/CH2_Perceptron.ipynb`](src/CH2_Perceptron.ipynb) | Perceptron |
| [`src/CH2_Adaline_GD.ipynb`](src/CH2_Adaline_GD.ipynb) | Adaline (batch GD) |
| [`src/CH2_Adaline_SGD.ipynb`](src/CH2_Adaline_SGD.ipynb) | Adaline (SGD) |
| [`src/CH3_LogisticRegression.ipynb`](src/CH3_LogisticRegression.ipynb) | Logistic regression (GD) |
| [`src/CH3_SKlearn_basics.ipynb`](src/CH3_SKlearn_basics.ipynb) | sklearn: data, split, scaling, pipelines |

[`src/utils.py`](src/utils.py) — `plot_decision_regions`, `plot_loss`. Run notebooks with working directory `src/` so `import utils` resolves.

## Setup

```bash
python -m venv ml-env && source ml-env/bin/activate  # Windows: ml-env\Scripts\activate
pip install numpy scipy scikit-learn matplotlib pandas jupyter ipykernel
jupyter lab  # or notebook; open files under src/
```

## Data

Put the UCI Iris CSV at `data/iris.data` (no header) for notebooks that use `pd.read_csv`. `CH3_SKlearn_basics` uses `sklearn.datasets.load_iris()` only.

`data/` and `ml-env/` are gitignored.

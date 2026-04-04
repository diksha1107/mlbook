# plotting decision regions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, model, X_test=None, y_test=None, resolution=0.01):
    
    # color map
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    markers = ('o', 's', '^', 'v', '<')
    colmap = ListedColormap(colors[:len(np.unique(y))])

    # creating grid
    h_min, h_max = X[:,0].min()-1, X[:,0].max()+1
    v_min, v_max = X[:,1].min()-1, X[:,1].max()+1

    hh, vv = np.meshgrid(np.arange(h_min, h_max, resolution), 
                         np.arange(v_min, v_max, resolution))
    grid = np.c_[hh.ravel(), vv.ravel()] #transpose the data into required format

    # predicting class for each grid point
    grid_col = model.predict(grid)
    grid_col = grid_col.reshape(hh.shape)

    # plot decision regions
    plt.contourf(hh, vv, grid_col, alpha=0.3, cmap=colmap)
    plt.xlim(h_min, h_max)
    plt.ylim(v_min, v_max)

    # plotting training data points over the decision regions
    for i, val in enumerate(np.unique(y)):
        plt.scatter(X[y==val, 0], X[y==val, 1], c=colors[i], marker=markers[i],
        edgecolors='black', label=f"Class {val}")

    # plotting testing data points over the decision regions
    if X_test is not None:
        plt.scatter(X_test[:, 0], X_test[:, 1],c='none', edgecolor='black', alpha=1.0,
        linewidth=1, marker='o',s=100, label='Test set')

    
    plt.legend()
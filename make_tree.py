# PYTHON STANDARD LIBRARY
import csv

# EXTERNAL LIBRARIES
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform


def make_tree(matrix, labels):
    """Return dendrogram of sequences."""

    labels = labels

    sf = squareform(matrix, force='tovector')
    sf2 = hierarchy.linkage(sf, 'single')

    hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
    fig, ax = plt.subplots(figsize=(12, 10))
    hierarchy.dendrogram(sf2, ax=ax, labels=labels, orientation='left')

    matplotlib.rc('xtick', labelsize=8)
    matplotlib.rc('ytick', labelsize=8)

    hierarchy.set_link_color_palette(None)  # reset to default after use
    fig.tight_layout()
    fig.savefig("dendrogram.png", bbox_inches='tight', dpi=400)


def get_labels(file):
    with open(file, 'r') as fh:
        labels = fh.readline().rstrip().split(',')
        labels = [label.replace("Mycobacterium", "M.") for label in labels]
        return np.array(labels)


if __name__ == "__main__":
    # YOU SET THESE:
    labels_file = "sp_names.csv"
    distance_file = "Difference_matrix.csv"

    labels = get_labels(labels_file)
    print(labels)
    matrix = np.genfromtxt(distance_file, delimiter=',')
    make_tree(matrix, labels)


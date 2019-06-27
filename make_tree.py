# PYTHON STANDARD LIBRARY
import csv

# EXTERNAL LIBRARIES
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform


def make_tree(matrix, labels):
    """Return dendrogram of sequences."""

    labels = labels

    sf = squareform(matrix, force='tovector')
    sf2 = hierarchy.linkage(sf, 'single')

    hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
    fig, ax = plt.subplots(figsize=(8, 3))
    hierarchy.dendrogram(sf2, ax=ax, labels=labels, orientation='left')

    hierarchy.set_link_color_palette(None)  # reset to default after use

    plt.show()


if __name__ == "__main__":
    # YOU SET THESE:
    labels_file = ""
    distance_file = ""

    labels = np.genfromtxt(labels_file, delimiter=',')
    matrix = np.genfromtxt(distance_file, delimiter=',')
    make_tree(matrix, labels)

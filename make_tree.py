import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform


def make_tree(matrix, labels, threshold=None, filename="dendrogram.png", figsize=(15, 10)):
    """Return dendrogram from distance matrix and labels."""
    print("Making dendrogram...")

    # FORMAT MATRIX AS VECTOR
    sf = squareform(matrix, force='tovector')
    sf2 = hierarchy.linkage(sf, 'single')

    # CREATE FIGURE
    fig, ax = plt.subplots(figsize=figsize)
    fig.tight_layout()

    # ADD DENDROGRAM TO FIGURE
    with plt.rc_context({'lines.linewidth': 0.5}):
        hierarchy.set_link_color_palette(['m', 'c', 'y', 'k'])
        hierarchy.dendrogram(sf2, ax=ax, labels=labels, orientation='left', color_threshold=threshold)

    # SAVE FIGURE
    fig.savefig(filename, bbox_inches='tight', dpi=600)

    print(f"...Saved dendrogram as: {filename}")


def get_labels(file, delimiter=','):
    """Get labels from delimited file"""
    return np.array([label for label in open(file, 'r').readline().rstrip().split(delimiter)])


if __name__ == "__main__":
    labels_csv = "sp_names.csv"
    matrix_csv = "Difference_matrix.csv"

    labels = get_labels(labels_csv)
    matrix = np.genfromtxt(matrix_csv, delimiter=',')
    make_tree(matrix=matrix, labels=labels, threshold=3, figsize=(15, 10))

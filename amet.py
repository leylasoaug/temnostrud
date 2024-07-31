import numpy as np
from sklearn.metrics import pairwise_distances

def label_placement(X, y, num_clusters):
    """
    Generate label placement function.

    Parameters:
    X (numpy array): Feature matrix.
    y (numpy array): Label vector.
    num_clusters (int): Number of clusters.

    Returns:
    labels (numpy array): Label placement vector.
    """
    # Compute the pairwise distances between samples
    distances = pairwise_distances(X)

    # Initialize the label placement vector
    labels = np.zeros_like(y)

    # Initialize the cluster centers
    cluster_centers = np.random.rand(num_clusters, X.shape[1])

    # Iterate over the samples
    for i, x in enumerate(X):
        # Compute the distance between the sample and each cluster center
        distances_to_centers = np.linalg.norm(x - cluster_centers, axis=1)

        # Assign the sample to the cluster with the closest center
        labels[i] = np.argmin(distances_to_centers)

    return labels

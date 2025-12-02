

# 1. Using one of the this dataset to demonstrate k-means clustering using the scikit learn package (50 points).
# Be sure to review the readings before you start on this assignment.
# 2. Calculate the sum of least square error for each different values of 'k'.
# Using Matplotlib determine the optimal number of clusters (k) using the elbow method along with a brief explanation (50 points).
# 3. Plot the optimal clusters with their centroids along with a brief explanation (50 points). Comment your code as needed.

# https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008 Links to an external site.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches  # For custom legend handles

# --- Declaring variables ---
file_name = "dmdata/diabetic_data.csv"
optimal_k = 3  # Optimal K chosen based on prior Elbow Method analysis
random_state = 42

# --- 1. Data Loading and Preprocessing ---
print("1. Loading and Preprocessing Data...")
df = pd.read_csv(file_name)

# Handle missing values and drop columns
df['max_glu_serum'] = df['max_glu_serum'].fillna('None').replace('?', 'None')
df['A1Cresult'] = df['A1Cresult'].fillna('None').replace('?', 'None')
df['race'] = df['race'].replace('?', 'Unknown').fillna('Unknown')

# Drop columns with mnumerous unique values, irrelevant information, or large amount of missing data for clustering
cols_to_drop = [
    'patient_nbr', 'encounter_id', 'weight', 'payer_code', 'medical_specialty',
    'diag_1', 'diag_2', 'diag_3',  # Dropping diagnosis codes for simplicity
]
df = df.drop(columns=cols_to_drop, errors='ignore')

# Identify original categorical and continuous columns before encoding
original_categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Convert categorical variables to numerical using one-hot encoding
df_dummies = pd.get_dummies(df, columns=original_categorical_cols, drop_first=False)

# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df_dummies)

# Reduce dimensionality with PCA, using 3 components for consistency with optimal_k
pca = PCA(n_components=optimal_k)
pca_data = pca.fit_transform(standardized_data)

# --- 2. Calculate SSE for Elbow Method (Justification for optimal_k) ---

# Calculate the Sum of Squared Errors (SSE, or Inertia) for k from 1 to 10
sse = []
k_range = range(1, 11)
print(f"2. Calculating SSE for K={min(k_range)} to K={max(k_range)}...")
for k in k_range:
    # Use the PCA-reduced data for the elbow calculation
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    kmeans.fit(pca_data)
    sse.append(kmeans.inertia_)

# Plot the elbow curve to determine optimal k
plt.figure(figsize=(8, 5))
plt.plot(k_range, sse, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Sum of Squared Errors (SSE/Inertia)')
plt.xticks(k_range)
plt.grid(True)
plt.legend()
plt.show()

# I selected optimal_k to be 3 due to the fact that he curve shows a sharp drop from K=1 to K=2,
# and another significant bend or "elbow" at K=3. Beyond K=3, the WCSS continues to decrease, but
# the reduction is marginal, indicating that adding more clusters primarily adds complexity without
# providing substantial new structure. Therefore, K=3 is selected as the optimal trade-off.

# --- 3. Optimal K-Means Clustering (K=3) ---
print(f"3. Performing Optimal K-Means Clustering (K={optimal_k})...")
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=random_state)
cluster_labels = kmeans.fit_predict(pca_data)
centroids = kmeans.cluster_centers_

# --- 4. Visualization of Principle Component 1 and Principle Component 2 ---
print("4. Visualizing Cluster Separation (PC1 vs PC2)...")
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
custom_cmap = ListedColormap(colors)

fig, ax = plt.subplots(figsize=(10, 7))

# Plot data points using the cluster labels (using only the first two PCs for 2D plot)
scatter = ax.scatter(
    pca_data[:, 0],  # PC1 values
    pca_data[:, 1],  # PC2 values
    c=cluster_labels,
    cmap=custom_cmap,
    s=10,
    alpha=0.6
)

# Plot the centroids
centroid_scatter = ax.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='X',
    s=300,
    c='red',
    edgecolor='black',
    label='Centroids'
)

# Manual legend creation
all_handles = []
for i in range(optimal_k):
    cluster_handle = mpatches.Patch(color=colors[i], label=f'Cluster {i}')
all_handles.append(cluster_handle)
all_handles.append(centroid_scatter)

ax.legend(handles=all_handles, loc="upper left", title="Cluster")
plt.title(f'K-Means Clustering: Optimal Clusters (K={optimal_k}) - PC1 vs PC2')
plt.xlabel(f'Principal Component 1')
plt.ylabel(f'Principal Component 2')
plt.grid(True)
plt.show()
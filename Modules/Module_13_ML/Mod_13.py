import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
import time
from tqdm import tqdm
import sys

diabetes_data = pd.read_csv('dmdata/diabetic_data.csv')

diabetes_data.info() #what columns are what

# remove categorical columns likely contributing more noise than value, and identifier columns which play no role.
diabetes_data = diabetes_data.drop(['encounter_id',
                                    'patient_nbr',
                                    'payer_code',
                                    'readmitted',
                                    'diag_1',
                                    'diag_2',
                                    'diag_3',
                                    'max_glu_serum',
                                    'change',
                                    'diabetesMed',
                                    ],
                                   axis=1,
                                   errors='ignore')

# find numeric/categorical columns

numeric_cols = diabetes_data.select_dtypes(include=['number']).columns.tolist()
categorical_cols = diabetes_data.select_dtypes(include=['object']).columns.tolist()

# now convert categorical columns to numerical ones using "OneHotEncoder" method
# which is a type of dummy encoding for the categorial features.
# normalize numerical columns be the same size with the standard scaler transform to
# a unit variance.

preprocesser = ColumnTransformer(transformers=
                            [
                            ('num', StandardScaler(), numeric_cols),
                            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_cols)
                            ],
                            remainder='drop')

# apply to df
processed_data = preprocesser.fit_transform(diabetes_data)


#now to 2d flatten it with PCA
pca_2d = PCA(n_components=2)
processed_data_2d = pca_2d.fit_transform(processed_data)

# ----- Figure out elbow ----- #
#try 15 encodings to find best fit.
k_len = range(1,15)

print("Starting elbow calculation.")
inertia = []
start = time.perf_counter()
for k in tqdm(k_len):
    k_means = KMeans(n_clusters=k, n_init=10, random_state=42)
    k_means.fit(processed_data_2d)
    inertia.append(k_means.inertia_)
end = time.perf_counter()

print(f"Elapsed: {end - start:.6f} seconds")
print("inertia",inertia)



# plot the elbow
#combined plot
"""
Here we generate the plot of the sum of least square error, or "intertia." There isn't a clear
elbow anywhere in the chart, though after about 3 it seems to taper off quite a bit. I chose to run the data after
running PCA to flatten it, so that we're looking only at the 2d plot data to determine the optimal k value. The overall
graph when I generated the elbow plot before was similar to after. 
"""
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(k_len, inertia,'bo-')


k_opt = 3 #approximate optimun

kmeans_fin = KMeans(n_clusters=k_opt, n_init=100,random_state=42)
cluster_labels = kmeans_fin.fit_predict(processed_data_2d)
centroids = kmeans_fin.cluster_centers_

# Plotting it all

plt.subplot(1,2,2)
plt.scatter(processed_data_2d[:, 0], processed_data_2d[:, 1], c=cluster_labels, cmap='viridis', alpha=0.6, s=50)

plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=300, label='Centroids')
plt.title(f'K-Means Clustering (k = {k_opt}) - Diabetes Patients')
plt.xlabel(f'First Principal Component ({pca_2d.explained_variance_ratio_[0]:.1%} variance)')
plt.ylabel(f'Second Principal Component ({pca_2d.explained_variance_ratio_[1]:.1%} variance)')
plt.legend()
plt.grid(True, alpha=0.3)

"""
The centroids split the data into three section, a top, a right, and a left section. There are a significant 
number of outliers along the second principle component, which is likely skewing the centroid locations somewhat. 
Despite that the centroids are very close to each other with this analysis likely related to the large number
of categorical columns.  
"""

# Here is some post analysis of the clusters to try and see which categories and values were associated
# with each cluster.
diabetes_data["cluster"] = cluster_labels
print("Number of patients in each cluster: \n",diabetes_data['cluster'].value_counts())
print("Averages for each numeric column by cluster: \n",diabetes_data.groupby('cluster')[numeric_cols].mean())
for col in ['age', 'race', 'gender', 'admission_type_id', 'discharge_disposition_id']:
    print("\n---", col, "---")
    print(diabetes_data.groupby('cluster')[col].value_counts(normalize=True))

plt.show()



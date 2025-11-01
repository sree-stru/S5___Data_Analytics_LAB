import pandas as pd
import numpy as np

data = {'category': ['a', 'b', 'c', 'a'],
        'value': [45, 22, 64, 28]}
df = pd.DataFrame(data)

nominal_cols = ['category']
numeric_cols = ['value']

for col in numeric_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col] = (df[col] - min_val) / (max_val - min_val)

dt = df[numeric_cols[0]].to_numpy().reshape(-1, 1)

n = len(df)

nom_sim = np.zeros((n, n))
nom_dissim = np.zeros((n, n))

num_sim = np.zeros((n, n))
num_dissim = np.zeros((n, n))

mixed_sim = np.zeros((n, n))
mixed_dissim = np.zeros((n, n))

for i in range(n):
    for j in range(n):

        nominal_match = 0
        
        if df.loc[i, nominal_cols[0]] == df.loc[j, nominal_cols[0]]:
            nominal_match = 1
        
        nom_sim[i, j] = nominal_match / len(nominal_cols)
        nom_dissim[i, j] = 1 - nom_sim[i, j]

        num_diff = np.abs(dt[i] - dt[j])[0]
        
        num_dissim[i, j] = num_diff 
        num_sim[i, j] = 1 - num_dissim[i, j]

        mixed_sim[i, j] = (nom_sim[i, j] + num_sim[i, j]) / 2
        mixed_dissim[i, j] = 1 - mixed_sim[i, j]

def print_pyramid(matrix, name):
    n = len(matrix)
    print(f"\n{name} Pyramid:")
    print("-" * (len(name) + 9))
    
    for i in range(n):
        row_vals = []
        for j in range(i + 1):
            row_vals.append(matrix[i, j])
        
        row_str = " ".join(f"{v:.3f}" for v in row_vals)
        print(row_str)

print_pyramid(nom_sim, "Nominal Similarity")
print_pyramid(nom_dissim, "Nominal Dissimilarity")

print_pyramid(num_sim, "Numeric Similarity")
print_pyramid(num_dissim, "Numeric Dissimilarity")

print_pyramid(mixed_sim, "Mixed Similarity")
print_pyramid(mixed_dissim, "Mixed Dissimilarity")

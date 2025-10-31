
---------------------CODE---------------------
from multiprocessing.sharedctypes import Value
import pandas as pd

file_path = input("Enter CSV file path: ")
df = pd.read_csv(file_path)
print("\nDataset Loaded Successfully!\n")

target_col = df.columns[-1]
X = df.drop(columns=[target_col])
y = df[target_col]
classes = y.unique()
N = len(df)

priors = (y.value_counts() / N).to_dict()

conditional_probs = {
    c: {
        col: (df [df[target_col] == c] [col].value_counts()  / len(df [df[target_col] == c] )).to_dict()
        for col in X.columns
    }
    for c in classes
}
print("\nEnter test data values:")
test_data = {col: input(f"Enter {col}: ") for col in X.columns}

def calculate_likelihood_product(c, test_data, conditional_probs, X_cols):
    likelihood = 1.0
    for col in X_cols:
        value = test_data[col]
        prob = conditional_probs.get(c, {}).get(col, {}).get(value, 1e-6)
        likelihood *= prob
    return likelihood

posteriors = {
    c: priors[c] * calculate_likelihood_product(c, test_data, conditional_probs, X.columns)
    for c in classes
}

predicted_class = max(posteriors, key=posteriors.get)

print("\nPosterior Probabilities:")
for c in posteriors:
    print(f"{c}: {posteriors[c]:.6f}")

print(f"\nPredicted Class: {predicted_class}")















---------------CSV FILE---------------
Outlook,Temp,Humidity,Windy,Play
Sunny,Hot,High,False,No
Sunny,Hot,High,True,No
Overcast,Hot,High,False,Yes
Rainy,Mild,High,False,Yes
Rainy,Cool,Normal,False,Yes
Rainy,Cool,Normal,True,No
Overcast,Cool,Normal,True,Yes
Sunny,Mild,High,False,No
Sunny,Cool,Normal,False,Yes
Rainy,Mild,Normal,False,Yes
Sunny,Mild,Normal,True,Yes
Overcast,Mild,High,True,Yes
Overcast,Hot,Normal,False,Yes
Rainy,Mild,High,True,No


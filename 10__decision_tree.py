
------------------------CODE-----------------------
import pandas as pd
import math

file_path = input("Enter CSV file path: ").strip()
df = pd.read_csv(file_path)

target_col = df.columns[-1]

# ---------------- Entropy Function ----------------
def entropy(data, target):
    values = data[target].value_counts(normalize=True)
    return -sum(v * math.log2(v) for v in values if v > 0)

# ---------------- Information Gain ----------------
def info_gain(data, attr, target):
    total_entropy = entropy(data, target)
    
    weighted_entropy = 0
    for v in data[attr].unique():
        subset = data[data[attr] == v]
        
        weight = len(subset) / len(data)
        
        weighted_entropy += weight * entropy(subset, target)
        
    return total_entropy - weighted_entropy

# ---------------- ID3 Algorithm ----------------
def id3(data, target, attributes):
    # --- BASE CASE 1: Homogeneous Node ---
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]
        
    # --- BASE CASE 2: No Attributes Left ---
    if len(attributes) == 0:
        return data[target].mode()[0]
        
    # --- RECURSIVE STEP: Find Best Split ---
    gains = {attr: info_gain(data, attr, target) for attr in attributes}
    
    best_attr = max(gains, key=gains.get)
    
    tree = {best_attr: {}}

    # --- Build Subtrees for Each Value ---
    for val in data[best_attr].unique():
        subset = data[data[best_attr] == val].drop(columns=[best_attr])
        
        remaining_attributes = [a for a in attributes if a != best_attr]
        
        subtree = id3(subset, target, remaining_attributes)
        
        tree[best_attr][val] = subtree  

    return tree

# ---------------- Pretty Print Function ----------------
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→ " + str(tree))
        return
        
    for attr, branches in tree.items():
        print(indent + f"[{attr}]")
        
        for value, subtree in branches.items():
            print(indent + f" ├── {value}:")
            
            print_tree(subtree, indent + " │   ")

# ---------------- Prediction Function ----------------
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
        
    root = next(iter(tree))
    
    if root not in sample:
        return "Unknown"
        
    value = sample[root]
    
    if value not in tree[root]:
        return "Unknown"
        
    return predict(tree[root][value], sample)

# ---------------- Build Tree ----------------
attributes = list(df.columns[:-1])
decision_tree = id3(df, target_col, attributes)

print("\nDecision Tree Structure (Dictionary):\n")
print(decision_tree)

print("\nDecision Tree (Text Format):\n")
print_tree(decision_tree)

# ---------------- Test Data from User ----------------
print("\nEnter test data values:")
test_sample = {}
for attr in attributes:
    val = input(f"  {attr}: ").strip()
    test_sample[attr] = val

# ---------------- Predict ----------------
result = predict(decision_tree, test_sample)
print("\nPredicted Class:", result)
print("---------------------------------------")






















-----------------CSV FILE--------------------
Outlook,Temperature,Humidity,Wind,Play
Sunny,Hot,High,Weak,No
Sunny,Hot,High,Strong,No
Overcast,Hot,High,Weak,Yes
Rain,Mild,High,Weak,Yes
Rain,Cool,Normal,Weak,Yes
Rain,Cool,Normal,Strong,No
Overcast,Cool,Normal,Strong,Yes
Sunny,Mild,High,Weak,No
Sunny,Cool,Normal,Weak,Yes
Rain,Mild,Normal,Weak,Yes
Sunny,Mild,Normal,Strong,Yes
Overcast,Mild,High,Strong,Yes
Overcast,Hot,Normal,Weak,Yes
Rain,Mild,High,Strong,No







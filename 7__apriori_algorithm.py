----------------------------CODE------------------------------
import pandas as pd
from itertools import combinations
from collections import defaultdict

def get_transactions():
    df = pd.read_csv('filename')
    transactions = []
    for _, row in df.iterrows():
        transactions.append([str(item) for item in row if pd.notnull(item)])
    return transactions

def get_frequent_itemsets(transactions, min_support):
    itemsets = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            itemsets[frozenset([item])] += 1
    itemsets = {itemset: count for itemset, count in itemsets.items() if count >= min_support}
    return itemsets

def generate_and_display_rules(frequent_itemsets, min_confidence, min_lift):
    rules = []
    n_transactions = sum(frequent_itemsets.values())  
    for itemset, support in frequent_itemsets.items():
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    if antecedent in frequent_itemsets and consequent in frequent_itemsets:
                        support_A = frequent_itemsets[antecedent]
                        support_C = frequent_itemsets[consequent]
                        confidence = support / support_A
                        if confidence >= min_confidence:
                            relative_support_C = support_C / n_transactions
                            lift = confidence / relative_support_C
                            if lift >= min_lift:
                                rules.append((set(antecedent), set(consequent), confidence, lift))

    print("\n--- Association Rules ---")
    for antecedent, consequent, confidence, lift in rules:
        print(f"{antecedent} => {consequent}, confidence: {confidence:.2f}, lift: {lift:.2f}")

    print("\n--- Top 10 Rules by Lift ---")
    top_rules = sorted(rules, key=lambda x: x[3], reverse=True)[:10]
    for antecedent, consequent, confidence, lift in top_rules:
        print(f"{antecedent} => {consequent}, confidence: {confidence:.2f}, lift: {lift:.2f}")

def generate_candidates(itemsets, k):
    candidates = set()
    itemsets_list = list(itemsets.keys())
    for i in range(len(itemsets_list)):
        for j in range(i + 1, len(itemsets_list)):
            union_set = itemsets_list[i] | itemsets_list[j]
            if len(union_set) == k:
                candidates.add(union_set)
    return candidates

def apriori(transactions, min_support):
    transactions = list(map(set, transactions))
    itemsets = get_frequent_itemsets(transactions, min_support)
    all_frequent_itemsets = dict(itemsets)
    k = 2
    while itemsets:
        candidates = generate_candidates(itemsets, k)
        itemsets = defaultdict(int)
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    itemsets[candidate] += 1
        itemsets = {itemset: count for itemset, count in itemsets.items() if count >= min_support}
        all_frequent_itemsets.update(itemsets)
        k += 1

    print("Frequent Itemsets:")
    for itemset, count in all_frequent_itemsets.items():
        print(f"{set(itemset)}: {count} (Support Count)")
    return all_frequent_itemsets

# --- Main program ---
min_support = float(input("\nEnter minimum support (e.g., 0.5 for 50%): "))
min_confidence = float(input("Enter minimum confidence (e.g., 0.7 for 70%): "))
min_lift = float(input("Enter minimum lift (e.g., 1.0 for positive correlation): "))

transactions = get_transactions()
frequent_itemsets = apriori(transactions, min_support)
generate_and_display_rules(frequent_itemsets, min_confidence, min_lift)











-----------------CSV FILE-----------------

Bread,Milk,Diapers,Beer
Bread,Diapers,Eggs,Cola
Milk,Diapers,Beer,Cola
Bread,Milk,Diapers,Eggs
Bread,Beer,Cola,Cereal
Milk,Diapers,Beer,Eggs
Bread,Milk,Eggs,Cereal
Diapers,Beer,Cola,Cereal
Bread,Milk,Diapers,Beer
Bread,Eggs,Cola,Cereal




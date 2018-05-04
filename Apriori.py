# Authors:      Lyubov Sidlinskaya, Caleb Sutton, Nawaf Alsudairy
# Assignment:   Final Project: Apriori Algorithm
# Course:       CSC 535 Data Mining
# Date:         04-02-2018
#
# Description:      
#               Apriori Algorithm implementation which determines the association
#               rules of a given dataset. Algorithm follows the psuedocode found 
#               in "Data Mining: Inroductory and Advanced Topics" on page 172.

# Import packages
import numpy as np
import pandas as pd
import scipy as sci
import sys


# Function which determines and returns the final large itemsets
# based on the Apriori algorithm. 
def apriori(transactions, dataset, min_support):
    k_value = 1 # Scan number, which determines the length of each large itemset.
    L = []      # Empty set for holding large itemsets.
    # Initial candidates to begin apriori.       
    candidates = get_initial_candidates(dataset)
    # Termination condition, while candidates are not an empty set.
    while checkIfEmpty(candidates) == False:
       # Finds support and removes items which do not meet the min support.
        large_itemsets = get_support(transactions, candidates, min_support)
        L.append(large_itemsets)
        
        k_value +=1     # Increment K value,
        candidates = apriori_gen(transactions, large_itemsets, k_value)
    # Returns array of large itemsets
    return L



# Does not work. need a better way of getting support for items
#
def build_rules(large_itemsets, transactions, min_support, min_confidence):
    rules = []
    
    for k_value in large_itemsets:
        for itemset in large_itemsets:
            for x in itemset:
                confidence = get_support(transactions, itemset, min_support)/get_support(transactions, x, min_support) 
                if  confidence > min_confidence:
                    right = itemset
                    right.remove(x)
                    rules.append({'left': x, 'right': right})

    return rules



# Function which calculates the support for each item
# and returns an array of items which meet the min support.
def get_support(transactions, itemset, min_support):
    new_itemset = []  # New array to hold items.

    for item in itemset:
        count = 0
        # Checks if item is in transaction,
        # if found count is incremented.
        for transaction in transactions:
            if item.issubset(transaction):
                count +=1
        # Calculate support, based on the length of transactions.
        support = count / (len(transactions))
        # If support meets criteria, add to set and return.
        if support > min_support:
            new_itemset.append(item)


# Function which returns the transactions of the dataset.
def get_transactions(dataset):
    transactions = []

    for row in dataset.itertuples(index = False):
        row_transaction = []
        # For each value, if not null, then add value to 
        # transaction array.
        for value in row:
            if (pd.isnull(value)):
                continue
            else:
                row_transaction.append(value)
        transactions.append(row_transaction)

    return transactions

# Function which determines the large itemsets based on the K Value.
def apriori_gen(transactions, itemset, k):

    candidate_set = []   
    empty_set = []

    for I in itemset:
        for J in itemset:
            if J != I:
                match_value_len = (k-2)

                # We join any set with every set that has 
                # the value of (match-value_len) items in common. 
                if match_value_len >= 1:
                    inter_set = set(I).intersection(J)
                    if match_value_len == (len(inter_set)):
                        joined = set(I).union(J)

                        # Check if item already in set.
                        if joined not in candidate_set:
                            candidate_set.append(joined)

                # When match_value_len == 0, we combine each item with
                # all other items to create new candidates. 
                else:
                    if match_value_len == 0:
                        joined = set(I).union(J)
                        if joined not in candidate_set:
                            candidate_set.append(joined)
    # Return new candidates.
    return candidate_set

# Function which returns the initial candidates as an array of sets.
def get_initial_candidates(dataset):

    df = dataset
    # Counts the nuber of times items appear.
    count_table = df.apply(pd.value_counts)
    count_table.reset_index(level=0, inplace=True)
    
    # count_table["support"] = count_table.sum(axis = 1) / (len(df))
    # Create list from the individual items in table.
    df_list = count_table["index"].tolist()

    # For item in array, place in set, append to array & return.
    initial_candidates = []
    for i in df_list:
        k = set()
        k.add(i)
        initial_candidates.append(k)

    return initial_candidates


# Function to check if dataset container is an empty set.
# Returns False when not empty , True when empty.
def checkIfEmpty(container):
    if container:
        return False
    else:
        return True

def main():
    if len(sys.argv) > 2:
        file_name = sys.argv[1]                               # Accepts filename as cmd line argument.
        support_value = float(sys.argv[2])
        dataset = pd.read_csv(file_name, header = None)
    
        transactions = get_transactions(dataset)
        final_iteset = apriori(transactions, dataset, support_value)
        for item in final_iteset:
            print ("\n",item)

    else:
        print ("Please enter the correct cmd line arguments in the format:")
        print ("python Apriori.py  data.csv  support_decimal")
    
main()
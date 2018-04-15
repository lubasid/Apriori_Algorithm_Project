# Authors: Lyubov Sidlinskaya, Caleb Sutton 
# Assignment: Final Project: Apriori Algorithm
# Description:
# Course: CSC 535 Data Mining
# Date: 04-02-2018

# Import packages
import numpy as np
import pandas as pd
import scipy as sci


def apriori(transactions, dataset, min_support):

    k_value = 1  # Is the scan number
    L = []      # Empty set.
    print (dataset)
    support_data = get_initial_support(dataset)
    initial_itemsets = get_initial_itemset(support_data, min_support)

    L.append(initial_itemsets)

    while True:
        k_value +=1
        L_subset = apriori_gen(transactions, initial_itemsets, k_value)
        # print (L_subset)
        L.append(L_subset)

        initial_itemsets = get_support(transactions, L_subset, min_support)
        print ("the next itemset is : \n", initial_itemsets)

        if len(initial_itemsets) == 1:
            L_subset = initial_itemsets
            L.append(L_subset)
            break
        

    print ("\n\n\nEND WHILE LOOP: ", "     Final list is : ")
    for k in L:
        print ()
        print (k)


def build_rules():
    print ()

def get_support(transactions, itemset, min_support):
    new_itemset = []

    for item in itemset:
        count = 0
        for transaction in transactions:
            if item.issubset(transaction):
                count +=1
        support = count / (len(transactions))
        if support > min_support:
            new_itemset.append(item)

    return (new_itemset)


def get_transactions(dataset):
    transactions = []

    for row in dataset.itertuples(index = False):
        row_transaction = []
        for value in row:
            if (pd.isnull(value)):
                continue
            else:
                row_transaction.append(value)
        transactions.append(row_transaction)

    return transactions


def apriori_gen(transactions, itemset, k):
    print ("\nRunning APRIORI_GEN on : \n",  itemset)
    print ("\nMust match on ", ((k-2)), " values\n")
    candidate_set = []   
    empty_set = []

    for I in itemset:
        for J in itemset:
            if J != I:
                match_value_len = (k-2)
                if match_value_len >= 1:
                    inter_set = set(I).intersection(J)
                    if match_value_len == (len(inter_set)):
                        joined = set(I).union(J)
                        if joined not in candidate_set:
                            print (I, " + ", J, " === ", joined)
                            candidate_set.append(joined)
                else:
                    if match_value_len == 0:
                        joined = set(I).union(J)
                        if joined not in candidate_set:
                            print (I, " + ", J, " === ", joined)
                            candidate_set.append(joined)


    print ("\nNew candidates are :   " , candidate_set)
    return candidate_set

# Function which returns the support for the dataset as a dictionary
# in the form:    {'BISCUIT': 0.3125.....}
def get_initial_support(dataset):
    df = dataset
    count_table = df.apply(pd.value_counts)
    # count_table.reset_index(level=0, inplace=True)
    count_table["support"] = count_table.sum(axis = 1) / (len(df))
    support_dict = count_table["support"].to_dict()
    support_df = count_table[['support']]

    return support_df


# Function to eliminate itemsets that do not reach minimum support
# in the first itemsets.
def get_initial_itemset(itemset, min_support):

    itemset.drop(itemset[itemset.support <= min_support].index, inplace=True)
    itemset.reset_index(level=0, inplace=True)
    item_list = itemset["index"].tolist()
    large_itemset  = [[i]for i in item_list]

    return large_itemset

# Function to check if dataset container is an empty set.
def checkIfEmpty(container):
    if container:
        return False
    else:
        return True

def main():
    dataset = pd.read_csv("data.csv", header = None)
    support_int = 0.05
    transactions = get_transactions(dataset)
    apriori(transactions, dataset, support_int)

main()
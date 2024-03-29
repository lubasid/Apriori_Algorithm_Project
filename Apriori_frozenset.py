#!/bin/env python3.6

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
import sys
import time


# Function which determines and returns the final large itemsets
# based on the Apriori algorithm. 
def apriori(transactions, initial_candidates_list, min_support):
    k_value = 1 # Scan number, which determines the length of each large itemset.
    L = []      # Empty set for holding large itemsets.
    # Initial candidates to begin apriori.   
    candidates = initial_candidates_list
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

def build_rules(large_itemsets, min_confidence):
    rules = []
    
    individual_items = []
    for item in large_itemsets[0]:
        individual_items.append(item)

    large_itemsets.pop(0)

    for k_value in large_itemsets:
        for itemset in k_value:
            list_of_frozen_sets = []
            for individual_item in individual_items:
              
                if individual_item[0].issubset(itemset[0]):
                    list_of_frozen_sets.append(individual_item)

            for item_ in list_of_frozen_sets:
                confidence = itemset[1] / item_[1]
                if confidence > min_confidence:
                    rules.append({'left': item_[0], 'right': itemset[0].difference(item_[0]), 'confidence': confidence})

    return rules

def print_rules(rules, input_file):
    products = []

    with open(input_file, 'r', encoding = 'utf8') as f:
        for line in f:
            products.append(line.strip().rstrip(',').split(','))
    
    for product in products:
        product[0] = frozenset([product[0]])

        for rule in rules:
            if product[0].issubset(rule['left']):
                rule['left'] = product[1]
            elif product[0].issubset(rule['right']):
                rule['right'] = product[1]
    
    for rule in rules:
        print(rule['left'], '=>', rule['right'], 'with', str(round(rule['confidence'] * 100, 2)) + '%', 'confidence.')


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
        support = count
        # If support meets criteria, add to set and return.
        if support / len(transactions) >= min_support:
            new_itemset.append([(item), support])      
    return (new_itemset)


# Function which determines the large itemsets based on the K Value.
def apriori_gen(transactions, itemset, k):

    candidate_set = []
    for I in itemset:
        for J in itemset:
            
            if J[0] != I[0]:
                match_value_len = (k-2)

                # We join any set with every set that has 
                # the value of (match-value_len) items in common. 
                if match_value_len >= 1:
                    inter_set = set(I[0]).intersection(J[0])

                    if match_value_len == (len(inter_set)):
                        joined = set(I[0]).union(J[0])
                 
                        # Check if item already in set.
                        if joined not in candidate_set:
                            candidate_set.append(frozenset(joined))

                # When match_value_len == 0, we combine each item with
                # all other items to create new candidates. 
                else:
                    if match_value_len == 0:
                        joined = set(I[0]).union(J[0])
                        if joined not in candidate_set:
                            candidate_set.append(frozenset(joined))
    # Return new candidates.
    return candidate_set

# Function which returns the initial candidates as an array of sets.
def initial_candidates_set(transactions):

    print ()
    initial_candidates = []
    for items in transactions:
        frozen_items = frozenset(items)

    return initial_candidates


# Function to check if dataset container is an empty set.
# Returns False when not empty , True when empty.
def checkIfEmpty(container):
    if container:
        return False
    else:
        return True

def read_data(input_file):
    transactions = []
    initial_candidates = set()

    file = open(input_file, "r")
    for line in file:
        cur_line = frozenset(line.strip().rstrip(',').split(','))
        transactions.append(cur_line)
        for item in cur_line:
            initial_candidates.add(frozenset([item]))
    return transactions , initial_candidates



def main():
    if len(sys.argv) > 2:
        start_time = time.time()

        file_name = sys.argv[1]                               # Accepts filename as cmd line argument.
        support_value = float(sys.argv[2])
        confidence_value = float(sys.argv[3])
        transactions, initial_candidates = read_data(file_name)

        L_set = apriori(transactions, initial_candidates, support_value)


        print_rules(build_rules(L_set, confidence_value), 'products.csv')

        finish_time = time.time()
        print ("\n-------------------------------------")
        print('Execution Time: ' + str(finish_time - start_time))

    else:
        print ("Please enter the correct cmd line arguments in the format:")
        print ("python Apriori.py  data.csv  support_decimal confidence_decimal")
    
main()
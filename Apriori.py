# Authors: Lyubov Sidlinskaya, Caleb Sutton
# Assignment: Final Project: Apriori Algorithm
# Description:
# Course: CSC 535 Data Mining
# Date: 04-02-2018

# Import packages
import numpy as np
import pandas as pd
import scipy as sci

def apriori(datasetFrame):
    k_value = 0  # Is the scan number
    L = []      # Empty set.
    # Get support values for initial items{}
    itemset_s = getSupport(datasetFrame)
    print (itemset_s)
    counter_var = 1
    candidates = datasetFrame
    while counter_var != 2:
        largeItemset = getLargeItemset(itemset_s)
        counter_var +=1
#     for (k = 1; L_)
    
#     C_1 = dataset
#     for item in dataset:
#         k_value +=1
#         L_k = []    # Empty subset
    
# Function which returns the support for the dataset as a dictionary
# in the form:    {'BISCUIT': 0.3125.....}
def getSupport(dataset):
    df = dataset
    count_table = df.apply(pd.value_counts)
    count_table["support"] = count_table.sum(axis = 1) / (len(df)-1)
    support_dict = count_table["support"].to_dict()
    return support_dict
def getLargeItemset(itemset):
        for item in itemset:
            support = itemset[item]
            if support >= 0.15 * 16:
                #Add to large Itemsets
                print (support)

def main():
    dataset = pd.read_csv("GroceryStoreDataSet.csv", header = None)
    support_int = 0.15
    datasetFrame = pd.DataFrame(dataset)
    apriori(datasetFrame)
    
    #print (datasetFrame)
    
main()
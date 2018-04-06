 ## Final Project : Apriori_Algorithm_Project
 
###### Course: CSC 535 Data Mining
###### Missouri State University
###### Authors: Sidlinskaya, Sutton

Datasets:
http://fimi.ua.ac.be/data/
https://www.cse.buffalo.edu//faculty/azhang/Teaching/index.html
https://www.kaggle.com/c/instacart-market-basket-analysis/data


 
 #### Apriori Algorithm for Association Rules (page 173)
 ```
 Input:
    I     // Itemsets
    D     // Database of transactions
    s     // Support
 Output:
    L     // Large Itemset
    
 Apriori algorithm:
    k = 0;  // k is used as the scan number
    L = {empty set};
    C_1 = I; // Initial canidates are set to be the items.
    
    repeat:
        k = k+1;
        L_k = {empty set};
        for each I_i (in set ) C_k   do:
            c_i = 0;    // Initial counts for each itemset are 0.
        for each t_j (in set) D     do:
            for each I_i (in set) C_k   do:
                if I_i (in set) t_j then
                    c_i = c_i +1;
        for each I_i (in set) C_k do
            if c_i >= (s * |D|)   do
                L_k = L_k U I_i;
        L = L U L_k;
        C_k+1 = Apriori-Gen(l_k)
    until C_k+1 = {empty set}
 
 ```

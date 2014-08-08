MapReduce Algorithm Design
===================================================
These scripts are designed to work with the code provided to simulate a MapReduce frame work, titled MapReduce.py in this repo.  

These scripts included here perfom the following tasks:

- wordcount.py -> impliments a count of words in a document by mapping words as keys and 1 as a value, and reducing the 1 counts to a total count
- invertedindex.py -> uses the same documents, generates a list of words and emits the word, doc as the key,val pair.  Then reduces the list down to words and which documents contain them
- friend_count.py -> This looks at a list of users and friends to produce a count for each friend an individual user has, then reduces the user, total friend count.
- asymmetric_friends.py -> Here we look at which connections in the list are not reciprocated 
- unique_trims.py -> This script looks at DNA sequencer samples and trims off the tailing 10 nucleotide reads, and eliminates any duplicates in the reduce phase
- relational_join -> This set of code takes a 5x5 matrix in sparse matrix notation: (matrix, i,j, value) for non zero cells, and performs a matrix multiplication procedure, appropriately mapping the necessary values, shuffling these values into the destinaiton cell, then multiplying and adding them for the final value. 
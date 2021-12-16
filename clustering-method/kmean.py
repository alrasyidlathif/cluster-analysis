'''
kmean:
1. set number of centroid (cluster center)
2. generate random centroid (number of feature same with data)
3. set number of max iteration (optional)
4. while true OR iteration < max
4a. calculate similarity between each centroid and each data
4b. assign data to the most similar centroid to construct cluster (smallest value)
4c. update centroid value
4d. break if cluster iter(i) = iter(i-1) OR centroid value iter(i) = iter(i-1)
5. result: cluster
'''

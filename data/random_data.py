import numpy as np

def int_data(min_max, num_feature):
    min_feature_value = min_max[0]
    max_feature_value = min_max[1]
    return np.random.randint(min_feature_value,max_feature_value,(1,num_feature))

def multi_int_data(min_max, num_data, num_feature):
    min_feature_value = min_max[0]
    max_feature_value = min_max[1]
    return np.random.randint(min_feature_value,max_feature_value,(num_data,num_feature))

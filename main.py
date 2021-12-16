from data.random_data import int_data
from similarity_measure.numeric_data import euclidean, manhattan

A = int_data([1,20], 2)
B = int_data([1,20], 2)

print(f'A: {A}, B: {B}')
print(f'A-B euc dist: {euclidean(A, B)}')
print(f'A-B manh dist: {manhattan(A, B)}')

import os
from itertools import combinations

allNums = []
with open('input.txt', 'r') as f:
	for line in f:
		allNums.append(int(line))

for c in combinations(allNums,3):
	if c[0] + c[1] + c[2] == 2020:
		print(c[0], c[1], c[2])

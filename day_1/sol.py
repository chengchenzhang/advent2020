prob_input = []

with open("input.txt", 'r') as f:
	for line in f:
		prob_input.append(int(line))

print(prob_input)

#Problem Solving
h_table = set() 
for x in prob_input:
	h_table.add(x)

out = 0
for x in h_table:
	if 2020 - x in h_table:
		out = x * (2020 - x)

print(out)

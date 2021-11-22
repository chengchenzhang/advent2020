#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(int(line))

	return prob_input

#Problem Solving
def solve(p_input):
	h_table = set() 
	for x in p_input:
		h_table.add(x)

	out = 0
	for x in h_table:
		if 2020 - x in h_table:
			out = x * (2020 - x)

	return out

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)

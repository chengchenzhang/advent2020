#Processing input
import argparse
from functools import reduce
parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(line[:-1])
	return prob_input

#Problem Solving
def solve(p_input):
	def different_slope(right,down):
		trees_hit = 0
		pos = 0
		row_l = len(p_input[0])

		for i, row in enumerate(p_input):
			if i % down != 0:
				continue
			if row[pos] == '#':
				trees_hit = trees_hit + 1
			pos = (pos + right) % row_l
		return trees_hit
	
	diff_slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
	diff_out = [different_slope(x[0],x[1]) for x in diff_slopes]

	return reduce(lambda a,b: a*b,diff_out)

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)

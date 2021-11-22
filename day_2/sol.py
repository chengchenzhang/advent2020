#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			line = line[:-1]
			colon_split = line.split(": ")

			space_split = colon_split[0].split(" ")
			
			q_range = space_split[0].split("-")
			low_range = q_range[0]
			high_range = q_range[1]

			letter = space_split[1]
			str_seq = colon_split[1]

			prob_input.append([int(low_range), int(high_range), letter, str_seq])

	return prob_input

#Problem Solving
def solve(p_input):
	out = 0
	def check_pass(pass_p):
		c = 0
		for char in pass_p[3]:
			if char == pass_p[2]:
				c = c + 1

		if c >= pass_p[0] and c <= pass_p[1]:
			return True
		else:
			return False
	
	out = [check_pass(p) for p in p_input]
	return out.count(True)

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)

import time
import numpy as np

UP = 1
LF = 2
DG = 3

def get_dir_str(i):
	global UP,LF,DG

	if i == DG:
		# return "diagonal up"
		return u"\u2196"
	if i == UP:
		# return "up"
		return u"\u2191"
	if i == LF:
		#return "left"
		return u"\u2190"

def print_actions(x, y, table):
	print ("     " + " ".join(y))
	for i in range(0,table.shape[0]):
		if i > 0:
			res = x[i-1] + " "
		else :
			res = "  "
		for j in range(0,table.shape[1]):
			res += " " + get_dir_str(table[i][j])
		print (res)



def ED_BottomUp(x, y):
	global UP, LF, DG

	x_len = len(x)
	y_len = len(y)
	# Initialize the data structure to hold resulst already computed
	table_cost = np.zeros([x_len + 1, y_len + 1], dtype=int)
	table_action = np.zeros([x_len + 1, y_len + 1], dtype=int)

	table_cost[0, 1:] = range(1, y_len + 1)
	table_cost[1:, 0] = range(1, x_len + 1)
	table_action[0,:] = LF
	table_action[:, 0] = UP

	for i in range(1, x_len + 1):
		for j in range(1, y_len + 1):

			if x[i - 1] == y[j - 1]:
				diff = 0
			else:
				diff = 1

			c_dg = table_cost[i - 1][j - 1] + diff
			c_up = table_cost[i - 1][j] + 1
			c_lf = table_cost[i][j - 1] + 1

			min_cost = c_dg
			action = DG

			if c_up < min_cost:
				min_cost = c_up
				action = UP
			elif c_lf < min_cost:
				min_cost = c_lf
				action = LF

			table_cost[i][j] = min_cost
			table_action[i][j] = action

	# Return the result
	res = table_cost[x_len, y_len]
	return  res, table_action


def run_bottomup_ed(x, y):
	t0 = time.time()
	res, table_action = ED_BottomUp(x, y)
	t1 = time.time()
	exec_time = (t1 - t0)
	return res , exec_time , table_action


def test( x = None , y = None):
	if x is None or y is None:
		# x = "GCTATGCCACGC"
		# y = "GCTATGCCACGC"
		x = "exponential"
		y = "polynomial"

	print('Input strings are :')
	print(x)
	print(y)
	res, exec_time, table_action = run_bottomup_ed(x, y)
	print('Edit distance between the strings', res)
	print('Time taken {0:.10f} seconds'.format(exec_time))
	# print_actions(x, y, table_action)

def test_with_disp( x = None , y = None):
	if x is None or y is None:
		# x = "GCTATGCCACGC"
		# y = "GCTATGCCACGC"
		x = "exponential"
		y = "polynomial"
	print('Input strings are :')
	print(x)
	print(y)
	res, exec_time, table_action = run_bottomup_ed(x, y)
	print('Edit distance between the strings', res)
	print('Time taken {0:.10f} seconds'.format(exec_time))
	print_actions(x, y, table_action)

# test()

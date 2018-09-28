import time

def ED_Recursive(x, y):
	# Empty x
	if len(x) == 0:
		return len(y)
	# Empty y
	if len(y) == 0:
		return len(x)

	# check the last character
	if x[-1] != y[-1]:
		diff = 1
	else:
		diff = 0

	dg = ED_Recursive(x[:-1], y[:-1]) + diff
	up = ED_Recursive(x[:-1], y) + 1
	lf = ED_Recursive(x, y[:-1]) + 1
	return min(dg, up, lf)


def run_recursive_ed(x,y):
	t0 = time.time()
	res = ED_Recursive(x, y)
	t1 = time.time()
	exec_time = t1 - t0
	return res, exec_time



def test( x = None , y = None):
	if x is None or y is None:
		# x = "GCTATGCCACGC"
		# y = "GCTATGCCACGC"
		x = "Shakespeare"
		y = "shake spear"
	print('Input strings are :')
	print(x)
	print(y)
	res, exec_time = run_recursive_ed(x, y)
	print('Edit distance between the strings', res)
	print('Time taken {0:.10f} seconds'.format(exec_time))

# test()
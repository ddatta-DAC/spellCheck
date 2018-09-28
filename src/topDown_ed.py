import time

def ED_TopDown(x, y, memoized_val = None):
	# Initialize the data structure to hold resulstalready computed
	if memoized_val is None:
		memoized_val = { }

	# Handle empty strings
	if len(x) == 0:
		return len(y)
	if len(y) == 0:
		return len(x)

	# if the value has been previosuly calculated - use that
	if (len(x), len(y)) in memoized_val:
		return memoized_val[(len(x), len(y))]

	if x[-1] == y[-1]:
		diff = 0
	else :
		diff = 1

	# Check the 3 cases
	dg = ED_TopDown(x[:-1], y[:-1], memoized_val) + diff
	up = ED_TopDown(x[:-1], y, memoized_val) + 1
	lf = ED_TopDown(x, y[:-1], memoized_val) + 1

	# select minimum of the 3 cases
	res = min(dg, up, lf)

	# Store the calculated value
	memoized_val[(len(x), len(y))] = res
	# Returnthe result
	return res


def run_topdown_ed(x,y):
	t0 = time.time()
	res = ED_TopDown(x, y)
	t1 = time.time()
	exec_time = t1 - t0
	return res , exec_time

def test( x = None , y = None):
	if x is None or y is None:
		# x = "GCTATGCCACGC"
		# y = "GCTATGCCACGC"
		x = "exponential"
		y = "polynomial"
	print('Input strings are :')
	print(x)
	print(y)
	res, exec_time = run_topdown_ed(x, y)
	print('Edit distance between the strings', res)
	print('Time taken {0:.10f} seconds'.format(exec_time))

test()
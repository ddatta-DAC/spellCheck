import time


def ED_TopDown(x, y, memoized_val=None):
    # Initialize the data structure to hold resulst already computed
    if memoized_val is None:
        memoized_val = {}

    # Handle empty strings
    if len(x) == 0:
        return len(y),''
    if len(y) == 0:
        return len(x),''

    # if the value has been previosuly calculated - use that
    if (len(x), len(y)) in memoized_val:
        return memoized_val[(len(x), len(y))]

    if x[-1] == y[-1]:
        diff = 0
    else:
        diff = 1

    # Check the 3 cases
    dg,a1 = ED_TopDown(x[:-1], y[:-1], memoized_val)
    dg += diff
    up,a2 = ED_TopDown(x[:-1], y, memoized_val)
    up += 1
    lf,a3 = ED_TopDown(x, y[:-1], memoized_val)
    lf += 1


    _min = dg

    if diff == 0:
        a = a1 + 'M'
    else:
        a = a1 +'S'

    if up < _min:
        a = a2 + 'D'
        _min = up
    if lf < _min:
        a = a3 + 'I'
        _min = lf

    # Store the calculated value
    memoized_val[(len(x), len(y))] = (_min, a)
    # Return the result
    return _min, a


def run_topdown_ed(x, y):
    t0 = time.time()
    res, action = ED_TopDown(x, y)
    t1 = time.time()
    exec_time = t1 - t0
    # print(list(x))
    # print(list(y))
    print(list(action))
    return res, exec_time


def test(x=None, y=None):
    if x is None or y is None:
        x = "GCGTATGCGGC"
        y = "GCTATGCGGCT"
        # x = "exponential"
        # y = "polynomial"
    print('Input strings are :')
    print(list(x))
    print(list(y))
    res, exec_time = run_topdown_ed(x, y)
    print('Edit distance between the strings', res)
    print('Time taken {0:.10f} seconds'.format(exec_time))


# test()

import argparse
parser = argparse.ArgumentParser(description='Edit Distance')
parser.add_argument('-x', type=str, help="First string")
parser.add_argument('-y', type=str, help="Second string")
parser.add_argument('--test', type=int, help='to run test, enter --test 1')
args = vars(parser.parse_args())

if args['test'] == 1:
    test();
elif args['x'] != None and args['y'] != None:
    x = args['x']
    y = args['y']
    test(x,y)
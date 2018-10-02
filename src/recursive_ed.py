import time


def ED_Recursive(x, y):
    if len(x) == 0 and len(y) == 0 :
        return 0, ''
    # Empty x

    if len(x) == 0:
        return len(y), ''
    # Empty y
    if len(y) == 0:
        return len(x), ''

    # check the last character
    if x[-1] != y[-1]:
        diff = 1
    else:
        diff = 0

    dg, a1 = ED_Recursive(x[:-1], y[:-1])
    dg += diff
    up, a2 = ED_Recursive(x[:-1], y)
    up = up + 1
    lf, a3 = ED_Recursive(x, y[:-1])
    lf = lf + 1

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

    return _min, a



def run_recursive_ed(x, y):
    t0 = time.time()
    res, action = ED_Recursive(x, y)
    t1 = time.time()
    exec_time = t1 - t0

    print(list(action))
    return res, exec_time


def test(x=None, y=None):
    if x is None or y is None:
        # x = "GCGTATGCGGCTAACGC"
        # y = "GCTATGCGGCTATACGC"
        x = list("GCGTATGCGGC")
        y = list("GCTATGCGGCT")
        # x = "Shakespeare"
        # y = "shake spear"
    print('Input strings are :')
    print(x)
    print(y)
    res, exec_time = run_recursive_ed(x, y)
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

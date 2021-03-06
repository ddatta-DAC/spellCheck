import time
import numpy as np

UP = 1
LF = 2
DG = 3


def get_dir_str(i):
    global UP, LF, DG

    if i == DG:
        # return "diagonal up"
        return u"\u2196"
    if i == UP:
        # return "up"
        return u"\u2191"
    if i == LF:
        # return "left"
        return u"\u2190"


def print_actions(x, y, table):
    line = "       " + "  ".join(y)
    print(line)
    tmp = '-'
    for k in range(len(line)):
        tmp += '-'
    # print (tmp)

    for i in range(0, table.shape[0]):
        if i > 0:
            res = x[i - 1] + " "
        else:
            res = "  "
        for j in range(0, table.shape[1]):
            res += "  " + get_dir_str(table[i][j])
        print(res)
    steps = get_action(x,y,table)
    print(steps)



def get_action(x,y,table):
    i = len(x)
    j = len(y)

    steps = ''
    while i > 0 and j > 0:
        if table[i][j] == LF:
            steps += 'I'
            j -= 1
        elif table[i][j] == UP:
            steps += 'D'
            i -= 1
        elif table[i][j] == DG:
            if x[i - 1] != y[j - 1]:
                steps += 'S'
            else:
                steps += 'M'
            i -= 1
            j -= 1

    steps = steps[::-1]
    return list(steps)

def print_cost(x, y, table_cost):
    line = "       " + "  ".join(y)
    print(line)
    tmp = '-'
    for k in range(len(line)):
        tmp += '-'

    for i in range(0, table_cost.shape[0]):
        if i > 0:
            res = x[i - 1] + " "
        else:
            res = "  "
        for j in range(0, table_cost.shape[1]):
            res += "  " + str(int(table_cost[i][j]))
        print(res)


def ED_BottomUp(x, y):
    global UP, LF, DG

    x_len = len(x)
    y_len = len(y)
    # Initialize the data structure to hold resulst already computed
    table_cost = np.zeros([x_len + 1, y_len + 1], dtype=int)
    table_action = np.zeros([x_len + 1, y_len + 1], dtype=int)

    table_cost[0, 1:] = range(1, y_len + 1)
    table_cost[1:, 0] = range(1, x_len + 1)
    table_action[0, :] = LF
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
    return res, table_action, table_cost


def run_bottomup_ed(x, y):
    t0 = time.time()
    res, table_action, table_cost = ED_BottomUp(x, y)
    t1 = time.time()
    exec_time = (t1 - t0)
    steps = get_action(x,y,table_action)
    print (steps)
    return res, exec_time, table_action, table_cost


def test(x=None, y=None):
    if x is None or y is None:
        # x = "GCTATGCCACGC"
        # y = "GCTATGCCACGC"
        x = "exponential"
        y = "polynomial"

    print('Input strings are :')
    print(x)
    print(y)
    res, exec_time, table_action, table_cost = run_bottomup_ed(x, y)
    print('Edit distance between the strings', res)
    print('Time taken {0:.10f} seconds'.format(exec_time))


# print_actions(x, y, table_action)

def test_with_disp(x=None, y=None):
    if x is None or y is None:
        x = "ACGTATGCGGC"
        y = "GCTATGCGGCT"
    # x = "exponential"
    # y = "polynomial"
    print('Input strings are :')
    print(x)
    print(y)
    res, exec_time, table_action, table_cost = run_bottomup_ed(x, y)
    print('Edit distance between the strings', res)
    print('Time taken {0:.10f} seconds'.format(exec_time))
    print_actions(x, y, table_action)
    print_cost(x, y, table_cost)


# test_with_disp()

import argparse
parser = argparse.ArgumentParser(description='Edit Distance')
parser.add_argument('-x', type=str, help="First string")
parser.add_argument('-y', type=str, help="Second string")
parser.add_argument('--test', type=int, help='to run test, enter --test 1')
args = vars(parser.parse_args())

if args['test'] == 1:
    test_with_disp()
elif args['x'] != None and args['y'] != None:
    x = args['x']
    y = args['y']
    test_with_disp(x,y)


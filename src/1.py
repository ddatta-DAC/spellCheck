import argparse

parser = argparse.ArgumentParser(description='Edit Distance')
parser.add_argument('-x', type=str, help="First string")
parser.add_argument('-y', type=str, help="Second string")
parser.add_argument('--test', type=int, help='to run test, enter --test 1')
args = vars(parser.parse_args())

if args['test'] == 1:
    pass;
elif args['x']!= None and args['y']!= None:

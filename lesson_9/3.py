import argparse
import os
import sys
parser = argparse.ArgumentParser(
    description='cat-костыль для файла'
)
parser.add_argument(
    'files',
    metavar='FILES',
    nargs='+',
    help='два файла'
)

args = parser.parse_args()
for i in args.files:
    print(os.system('cat ' + i))
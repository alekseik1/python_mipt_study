import argparse
import os
parser = argparse.ArgumentParser(
    description='tree-костыль для директории'
)
parser.add_argument(
    'files',
    metavar='FILES',
    nargs='+',
    help='папка'
)
parser.add_argument(
    '--folders-only',
    action='store_true',
    help="dont't show folders"
)
parser.add_argument(
    '--include',
    metavar='include',
    help='include'
)
parser.add_argument(
    '--exclude',
    metavar='exclude',
    help='exclude'
)
parser.add_argument(
    '--all',
    action='store_true',
    help='all'
)
parser.add_argument(
    '--full-name',
    action='store_true',
    help='show dir full name'
)

args = parser.parse_args()
'''
s = '74:72:65:65:20:2d:6e'
l = ''
for i in s.split(":"):
    l += chr(int(i, 16))
s = l + ' '
if args.all:
    s += '-a '
if args.full_name:
    s += '-f '
if args.folders_only:
    s += '-d '
s += args.files[0]
if args.include:
    res = os.system(s + ' | grep ' + ' ' + str(args.include))
    exit(0)
if args.exclude:
    res = os.system(s + ' | grep -v ' + str(args.exclude[0]))
    exit(0)
print(os.system(s))
'''
def list_files(startpath):
    s = ''
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            s += ('{}{}'.format(subindent, f)) + '\n'
    return s
s = list_files(args.files[0])
print(s)

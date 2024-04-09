'''
Load csv data to output bookings and events
'''

import argparse
import sys
#from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser(description='Import the events data')
parser.add_argument(
    '-i', '--inputfile', help='Input file.',
    default='data.csv', metavar='csv',
    type=argparse.FileType('r')
)

parser.add_argument(
    '-o', '--outputfile', help='Output file.',
    default=sys.stdout, metavar='csv',
    type=argparse.FileType('w')
)

args = parser.parse_args()

df = pd.read_csv(args.inputfile)

df.to_csv(args.outputfile,index=False)

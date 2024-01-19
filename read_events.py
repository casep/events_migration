import pandas as pd
import argparse
import sys
from pathlib import Path  

parser = argparse.ArgumentParser(description='Import the events data')
parser.add_argument(
    '-ia', '--inputfilea', help='Input file A.',
    default='dataA.csv', metavar='csv',
    type=argparse.FileType('r')
)

parser.add_argument(
    '-ib', '--inputfileb', help='Input file B.',
    default='dataB.csv', metavar='csv',
    type=argparse.FileType('r')
)

parser.add_argument(
    '-o', '--outputfile', help='Output file.',
    default=sys.stdout, metavar='csv',
    type=argparse.FileType('w')
)

args = parser.parse_args()

dfa = pd.read_csv(args.inputfilea)
dfb = pd.read_csv(args.inputfileb)

frames = [dfa, dfb]
result = pd.concat(frames)

result.to_csv(args.outputfile,index=False)  


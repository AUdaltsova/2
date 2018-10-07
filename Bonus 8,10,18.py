import csv
import json
import argparse
import os

parser = argparse.ArgumentParser(description='Input the text')
parser.add_argument('input', type=str, help='input text')
parser.add_argument('output', type=str, help='output text')
args = parser.parse_args()
fin = open(args.input, 'r')
fout = open(args.output, 'w')
reader = csv.reader(fin)
s = str(next(reader))
s = s.split(",")
n = 1
for row in reader:
    n += 1
st = os.stat(args.input)
json.dump(os.path.abspath(st), fout)
json.dump(os.path.getctime(st), fout)
json.dump(os.path.getmtime(st), fout)
a = os.path.getsize(st)
a = a // 1024
json.dump(a, fout)
json.dump(n, fout)
json.dump(len(s), fout)
json.dump(s, fout)
fin.close()
fout.close()

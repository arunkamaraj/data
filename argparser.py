import argparse
p= argparse.ArgumentParser(description="trying")
p.add_argument("-i","--input",help="input file name ")
p.add_argument("-o","--output",help="output file name ")
args=p.parse_args()

print args.input
print args.output




import argparse
p=argparse.ArgumentParser()
p.add_argument('-i','--inp')
p.add_argument('-o','--out')
value=p.parse_args()
print value.inp
print value.out

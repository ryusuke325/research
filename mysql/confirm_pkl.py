"""いらないかも！"""
import pickle

with open('{}.pkl'.format(argv[1]) , "rb") as f:
    print(type(pkl.load(f)))

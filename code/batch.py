
import glob
from concurrent import futures
import os
import main
import sys
import itertools
import helper


if __name__ == '__main__':
    FNs = glob.glob('../data/trajectories/synthetic/*')
    MaxOrder=int(sys.argv[0])
    MinSupport=int(sys.argv[1])
    for fn in FNs:
        print(fn.split('/')[:2])
        helper.helper(fn,MaxOrder,MinSupport)


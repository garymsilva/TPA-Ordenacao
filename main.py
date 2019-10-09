import sys
from model import *
from utils.csv import readFile, writeFile

# Pseudo-codigo
# procedure main(args)
#     sort ← selectAlgorithm(args)
#     inputName ← parseInputFileName(args)
#     outputName ← parseOutputFileName(args)
#     A ← readCsv(inputName)
#     initTime ← getCpuTime
#     sort(A)
#     finishTime ← getCpuTime
#     writeCsv(A, outputName)
#     reportTime(A, initTime, finishTime)
# end procedure

def main(args):    
    raise NotImplementedError
#

if __name__ == "__main__":
    main(sys.argv[1:])
#

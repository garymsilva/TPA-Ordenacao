import sys
from model.sort import *
from utils.csv import readFile, writeFile
from model.register import *

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

algs = {
    "selectsort": selectionSort,
    "insertsort": insertionSort,
    "mergesort": mergeSort,
    "quicksort": quickSort,
    "heapsort": heapSort
}

def getTime():
    # TODO
    return 0
#

""" 
Ler o .csv e devolver uma lista com o Registros
"""
def getRegisters(path):
    listCSV = readFile(path, True)
    resgisters = []
    for line in listCSV: 
        newRegister = Register(line[0], line[1], line[2], line[3], line[4], line[5])
        resgisters.append(newRegister)
    #
    return resgisters
#

"""
Função de comparação que vamos passar nos métodos de ordenação
"""
def compareByUid(a, b):
    # TODO
    if a.uid > b.uid:           # se a > b retorna 1
        return 1
    elif a.uid == b.uid:        # se for igual, retorna 0
        return 0
    else:                       # se a < b, retorna -1
        return -1
    #
#

def main(args):
    if args["algIdentifier"] not in algs.keys():  # checar se o algoritmo chamado funciona
        return
    #

    registersList = getRegisters("caminho/do/arquivo.csv") # Lê o arquivo

    sort = algs[args["algIdentifier"]]  # sort recebe a função que o usuário escolheu no terminal
    
    initTime = getTime()
    result = sort(registersList, compareByUid)   # chama sort(), passando a lista de registros e o método de comparação
    endTime = getTime()
    
    # TODO: print do resultado
    return
#

if __name__ == "__main__":
    args = {
        "algIdentifier": sys.argv[1] # pega o primeiro parâmetro passado no terminal. Ex: python main.py insertsort
    }
    main(args)
#

import sys, os, time
from multiprocessing import Process
from datetime import datetime
from pathlib import Path
from model.sort import sortMethodsSet
from utils.csv import readFile, writeFile
from utils.timeout import timeout
from model.register import Register

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

algorithms = sortMethodsSet # conjunto de funções, importado do módulo "sort.py"

def getTime():
    return time.time() * 1000
#

"""
Ler o .csv e devolver uma lista com os Registros
"""
def getRegisters(path):
    listCSV = readFile(path, True)
    registers = []
    for line in listCSV: 
        newRegister = Register(line[0], line[1], line[2], line[3], line[4], line[5])
        registers.append(newRegister)
    #
    return registers
#

def getFiles(path):
    p = Path(path)
    files = os.listdir(p)
    return files
#

"""
Registra um resultado nos logs
"""
def updateLog(algorithm, n, time):
    writeFile("results.csv", [str(datetime.now()), algorithm, str(n), str(time)])
    # print(algorithm, str(n)+" registros", str(time)+"ms")
#

"""
Função de comparação que vamos passar nos métodos de ordenação
"""
def compareByUid(a, b):
    if a.uid > b.uid:           # se a > b retorna 1
        return 1
    elif a.uid == b.uid:        # se for igual, retorna 0
        return 0
    else:                       # se a < b, retorna -1
        return -1
    #
#

""" Executa UM teste, para UM algoritmo, com UM conjunto de arquivos """
@timeout(15*60)
def runTest(sort, file):
    registers = getRegisters(file)
    start = getTime()
    sort(registers, compareByUid)
    end = getTime()
    return registers, start, end
#

def main(args):
    # registers = getRegisters("data/data_10e0.csv")
    # registers = [10, 56, 2, 34, 12, 9, 3, 43, 11, 6]
    # registers = [10, 56, 2, 34, 12, 9, 3, 43, 11, 6]
    


    # if args["algIdentifier"] in algorithms.keys():
    #     print("Running", args["algIdentifier"])
    #     sort = algorithms[args["algIdentifier"]]
    #     registers, startTime, endTime = runTest(sort, args["inputFile"])
    #     updateLog(args["algIdentifier"], len(registers), endTime-startTime)
        
    #     for reg in registers:
    #         print(str(reg.uid))
    #     #
    # #

    if args["algIdentifier"] in algorithms.keys():
        sort = algorithms[args["algIdentifier"]]
        for fileName in getFiles(args["directory"]):
            for i in range(0, 5):
                print("Running", args["algIdentifier"], fileName)
                try:
                    registers, startTime, endTime = runTest(sort, args["directory"]+"/"+fileName)
                    updateLog(args["algIdentifier"], len(registers), endTime-startTime)
                except Exception as e:
                    print("Timeout:", args["algIdentifier"], len(registers))
                    updateLog(args["algIdentifier"], len(registers), -1)
                #
            #
        #
    #

    if args["algIdentifier"] == "all":
        for alg in algorithms.keys():
            sort = algorithms[alg]
            for fileName in getFiles(args["directory"]):
                for i in range(0, 5):
                    print("Running", alg, fileName)
                    try:
                        registers, startTime, endTime = runTest(sort, args["directory"]+"/"+fileName)
                        updateLog(alg, len(registers), endTime-startTime)
                    except Exception as e:
                        print("Timeout:", alg, len(registers))
                        updateLog(alg, len(registers), -1)
                    #
                #
            #
        #
    #
    
    return
#

if __name__ == "__main__":
    # Default values
    args = {}

    # Update args with user input
    lenArgs = len(sys.argv)
    
    if lenArgs >= 2:
        args["algIdentifier"] = str(sys.argv[1]) # pega o primeiro parâmetro passado no terminal. Ex: python main.py insertsort
    #

    if "-d" in sys.argv:
        dirIndex = sys.argv.index("-d") + 1
        args["directory"] = str(sys.argv[dirIndex])
    else:
        args["directory"] = "data"
    #

    if "-i" in sys.argv:
        fileIndex = sys.argv.index("-i") + 1
        args["inputFile"] = str(sys.argv[fileIndex])
    #
    
    main(args)
#

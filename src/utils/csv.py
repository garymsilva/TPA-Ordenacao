import csv

def readFile(fileName, skipHeader):
    with open(fileName, 'r') as csvfile:
        #Skip Header
        if skipHeader:
            next(csvfile)
        list = []
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            list.append(row)
        #
    #
    return list
#

def writeFile(fileName, rowData):
    with open(fileName, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        writer.writerow(rowData)
    #
#

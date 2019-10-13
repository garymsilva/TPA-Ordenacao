"""
registers: list
compare: function(a, b)
    Retorna: 
        -1 (ou algo menor que zero) se a < b
         0 se a=b
         1 (ou algo maior que zero) se a > b
"""

""" 1. Funções acessórias """

# Comparador padrão para inteiros
def _defaultCompare(a, b):
    return a-b
#

# Diz se left é MAIOR QUE right, baseado em uma função de comparação fornecida. Usa _defaultCompare se não for passada outra função.
def _greater(left, right, compare=_defaultCompare):
    if (compare(left, right) > 0):
        return True
    else:
        return False
    #
#

""" 2. Funções de ordenação """
# Todas as funções irão usar o _defaultCompare se não for passada outra função.

""" 2.1. Selection Sort """
def selectionSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

""" 2.2. Insertion Sort """
def insertionSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

""" 2.3. Merge Sort """
def _merge(registers, compare, start, middle, end):
    leftArray = []
    rightArray = []

    i = start
    while i <= middle:
        leftArray.append(registers[i])
        i += 1
    #

    j = middle + 1
    while j <= end:
        rightArray.append(registers[j])
        j += 1
    #

    i = j = 0
    k = start
    while k < end:
        if _greater(leftArray[i], rightArray[j], compare):
            registers[k] = rightArray[j]
            j += 1
        else:
            registers[k] = leftArray[i]
            i += 1
        #
        k += 1
    #
#

def _mergeSort(registers, compare, start, end):
    if start < end:
        middle = (start+end)//2
        _mergeSort(registers, compare, start, middle)
        _mergeSort(registers, compare, middle+1, end)
        _merge(registers, compare, start, middle, end)
    #
#

def mergeSort(registers, compare=_defaultCompare):
    _mergeSort(registers, compare, 0, len(registers)-1)
    return registers
#

""" 2.4. Quick Sort """
def quickSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

""" 2.5. Heap Sort """
def heapSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

def introSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

def timSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

def smoothSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

def patienceSort(registers, compare=_defaultCompare):
    raise NotImplementedError
#

sortMethodsSet = {
    "selectsort": selectionSort,
    "insertsort": insertionSort,
    "mergesort": mergeSort,
    "quicksort": quickSort,
    "heapsort": heapSort
}

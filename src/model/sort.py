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

# Diz se left é MENOR QUE right, baseado em uma função de comparação fornecida. Usa _defaultCompare se não for passada outra função.
def _less(left, right, compare=_defaultCompare):
    if (compare(left, right) < 0):
        return True
    else:
        return False
    #
#

# Permuta os elementos i e j de um array
def _exchange(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux
#

""" 2. Funções de ordenação """
# Todas as funções irão usar o _defaultCompare se não for passada outra função.

""" 2.1. Selection Sort """
def selectionSort(registers, compare=_defaultCompare):
    start = 0
    n = len(registers)
    end = n - 1

    print(str(start), str(n), str(end))

    for i in range(start, end):
        smallestIndex = i
        for j in range(i+1, n):
            if _less(registers[j], registers[smallestIndex], compare):
                smallestIndex = j
            #
        #
        _exchange(registers, i, smallestIndex)
    #
#

""" 2.2. Insertion Sort """
def insertionSort(registers, compare=_defaultCompare):
    for j in range(1, len(registers)):
        key = registers[j]
        i = j - 1
        while i >= 0 and _greater(registers[i], key, compare):
            registers[i+1] = registers[i]
            i -= 1
        #
        registers[i+1] = key
    #
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

    i = 0
    j = 0
    k = start
    while k < end and i < len(leftArray) and j < len(rightArray):
        if _greater(leftArray[i], rightArray[j], compare):
            registers[k] = rightArray[j]
            j += 1
        else:
            registers[k] = leftArray[i]
            i += 1
        #
        k += 1
    #

    if i == len(leftArray):
        while j < len(rightArray):
            registers[k] = rightArray[j]
            j += 1
            k += 1
        #
    #

    if j == len(rightArray):
        while i < len(leftArray):
            registers[k] = leftArray[i]
            i += 1
            k += 1
        #
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
#

""" 2.4. Quick Sort """
def _partition(registers, compare, start, end):
    pivot = registers[end]
    i = start - 1

    for j in range(start, end):
        if not _greater(registers[j], pivot, compare):
            i += 1
            _exchange(registers, i, j)
        #
    #
    _exchange(registers, i+1, end)

    return i + 1
#

def _quickSort(registers, compare, start, end):
    if start < end:
        middle = _partition(registers, compare, start, end)
        _quickSort(registers, compare, start, middle - 1)
        _quickSort(registers, compare, middle + 1, end)
    #
#

def quickSort(registers, compare=_defaultCompare):
    _quickSort(registers, compare, 0, len(registers)-1)
#

""" 2.5. Heap Sort """
def _parent(i):
    return (i-1)//2
#

def _left(i):
    return 2*(i+1)-1
#

def _right(i):
    return 2*(i+1)
#

def _maxHeapify(registers, compare, i=0, heapSize=None):
    left = _left(i)
    right = _right(i)
    largest = 0

    if heapSize == None:
        heapSize = len(registers)
    #

    if left < heapSize and _greater(registers[left], registers[i], compare):
        largest = left
    else:
        largest = i
    #

    if right < heapSize and _greater(registers[right], registers[largest], compare):
        largest = right
    #

    if largest != i:
        _exchange(registers, i, largest)
        _maxHeapify(registers, compare, largest, heapSize)
    #
#

def _buildMaxHeap(registers, compare):
    for i in range((len(registers)-1)//2, -1, -1):
        _maxHeapify(registers, compare, i)
    #
#

def heapSort(registers, compare=_defaultCompare):
    _buildMaxHeap(registers, compare)
    heapSize = len(registers)

    for i in range(len(registers)-1, 0, -1):
        _exchange(registers, 0, i)
        heapSize -= 1
        _maxHeapify(registers, compare, 0, heapSize)
    #
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

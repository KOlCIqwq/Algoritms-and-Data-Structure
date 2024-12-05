class MinHeap:
    def __init__(self):
        self.heap = []

    # Build an heap from an array
    # @param: arr, an array not null, if null return None
    # @return: None
    # Time: O(n), n as length of arr
    def build(self, arr):
        self.heap = []
        self.heap = arr
        n = len(arr)
        if n == 0:
            print("Can't be null")
            return
        for i in range(n // 2 - 1, -1, -1):
            self.heapifyDown(i)
    
    # Get the length of the heap
    # @param: None
    # @return: an integer
    # Time: O(1)
    def length(self):
        if self.heap == None:
            return 0
        return len(self.heap)

    # Peek the root
    # @param: None
    # @return: first element, but doesn't remove it from heap
    # Time: O(1)
    def getmin(self):
        if not self.heap:
            return None
        return self.heap[0]

    # Pop the root
    # @param: None
    # @return: first element and remove it from heap
    # Time: O(n), for heapify
    def extract(self):
        if not self.heap:
            return None
        minVal = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()  # Replace root with the last element
            self.heapifyDown(0)
        else:
            self.heap.pop()  # Remove the last element directly
        return minVal

    # Insert an element to the heap
    # @param: x
    # @return: None
    # Time: O(n), for heapify
    def insert(self, x):
        self.heap.append(x)
        self.heapifyUp(len(self.heap) - 1)

    # Change the value at i to x, heapify up and down
    # @param: i, x
    # @return: None
    # Time: O(n)
    def change(self, i, x):
        if i < 0 or i >= len(self.heap):
            print(f"Invalid index: {i}")
            return
        self.heap[i] = x
        self.heapifyUp(i)
        self.heapifyDown(i)
    
    # From a given index, heapify up 
    # @param: i
    # @return: None
    # Time: O(n)
    def heapifyUp(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    # Given an index, heapify down
    # @param: i
    # @return: None
    # Time: O(n)
    def heapifyDown(self, i):
        arr = self.heap
        n = len(arr)
        small = i
        left = i * 2 + 1
        right = left + 1

        if left < n and arr[left] < arr[small]:
            small = left
        if right < n and arr[right] < arr[small]:
            small = right

        if small != i:
            arr[i], arr[small] = arr[small], arr[i]
            self.heapifyDown(small)
    def getHeap(self):
        return self.heap

def processCommands():
    heap = MinHeap()
    exit = False
    while exit != True:
        a = input()
        rawInput = a.split()
        operation = rawInput[0]
        if operation == "build":
            arr = list(map(int, rawInput[1:]))
            heap.build(arr)
            print(heap.getHeap())
            continue
        elif operation == "length":
            print(heap.length())
            continue
        elif operation == "getmin":
            print(heap.getmin())
            continue
        elif operation == "insert":
            x = int(rawInput[1])
            heap.insert(x)
            print(heap.getHeap())
            continue
        elif operation == "extract":
            print(heap.extract())
            print(heap.getHeap())
            continue
        elif operation == "change":
            i = int(rawInput[1])
            x = int(rawInput[2])
            heap.change(i, x)
            print(*heap.getHeap())
            continue
        elif operation == "exit":
            exit = True
            break

processCommands()

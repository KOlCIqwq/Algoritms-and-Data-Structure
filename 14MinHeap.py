class minHeap:
    def __init__(self,top,heap):
        self.heap = heap
        self.top = top
    def build(self,values):
        values.sort()
        self.heap = values
        self.top = values[0]
    def length(self):
        return len(self.heap)
    def getmin(self):
        return self.top
    def extract(self,x):

    def find(self,x):
        
    def heapify(self,x):
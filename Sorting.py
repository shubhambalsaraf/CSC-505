#import numpy as np
#import math as m
class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0



    def merge(self, p, q, r):
        #import math as m
        n1 = q - p + 1  #length of left half of array
        n2 = r - q      #length of right half of array
        L = [None] * (n1 + 1) #initalize left array with all none value
        R = [None] * (n2 + 1) #initalize right array with all none value
        for i in range(0, n1): #for loop to copy left half in array
            L[i] = self.sorting_array[p + i]
        for j in range(0, n2): #for loop to copy right half in array
            R[j] = self.sorting_array[q + 1 + j]
        #L[n1] = m.inf
        L[n1] = 1000000                 #Infinite sentinel value is taken as 100000 since I was not able to import numpy or math
        #R[n2] = m.inf
        R[n2] = 1000000
        i = 0
        j = 0
        for k in range(p, r + 1):       #
            if L[i] <= R[j]:
                self.comparison_count +=1
                self.sorting_array[k] = L[i]
                i += 1
            else:
                self.comparison_count +=1
                self.sorting_array[k] = R[j]
                j += 1

    def merge_sort(self, p, r):             #original merge_sort function
        if p < r:
            q = (p+r) // 2
            self.merge_sort(p,q)
            self.merge_sort(q+1, r)         #calls itself recursively
            self.merge(p, q, r)             #calls merge function and gives the midpoint as additional input
        return self.sorting_array, self.comparison_count


    def heap_sort(self):
        self.build_max_heap()
        a_heapsize = len(self.sorting_array)
        for i in range(a_heapsize-1, 0, -1):
            self.sorting_array[0], self.sorting_array[i] = self.sorting_array[i], self.sorting_array[0]
            self.comparison_count += 1
            self.heapify(i,0)
        self.comparison_count -=1
        return self.sorting_array, self.comparison_count


    def build_max_heap(self):
        a_heapsize = len(self.sorting_array)
        for i in range(a_heapsize // 2 -1, -1, -1):
            self.heapify(a_heapsize, i)

    def left(self,i):       #function calculates for the left node
        return 2*i+1

    def right(self, i):     #function calculates for the right node
        return 2*i+2

    def heapify(self, a_heapsize, i):
        l = self.left(i)
        r = self.right(i)

        if l < a_heapsize and self.sorting_array[l] > self.sorting_array[i]:
            largest = l
        else:
            largest = i

        if r < a_heapsize and self.sorting_array[r] > self.sorting_array[largest]:
            largest = r

        if largest != i:
            self.comparison_count += 1
            self.sorting_array[i], self.sorting_array[largest] = self.sorting_array[largest], self.sorting_array[i]
            self.heapify(a_heapsize, largest)



    def insertion_sort(self):
        for j in range(1, len(self.sorting_array)):
            key = self.sorting_array[j]
            i = j - 1
            if self.sorting_array[i] > key:
                self.comparison_count += j
            else:
                self.comparison_count += 1
            while i >= 0 and  self.sorting_array[i] > key:
                self.sorting_array[i + 1] = self.sorting_array[i]
                i -= 1
            self.sorting_array[i + 1] = key
        return self.sorting_array, self.comparison_count


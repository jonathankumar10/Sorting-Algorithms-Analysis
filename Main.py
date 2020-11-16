import sys
import random
import time
import matplotlib.pyplot as pyplot


class Insertion:
    def insertionSort(self, input_array):
        for i in range(1,(len(input_array))):
            j = i
            while j>0 and input_array[j] < input_array[j-1]:
                # comparing and sorting of list is done here.
                print("Sorting via Insertion Sort: ", input_array)
                input_array[j], input_array[j-1] = input_array[j-1], input_array[j]
                j -= 1
        return input_array


class Bubble:
    def bubbleSort(self, input_array):
        isSorted = False
        # numberOfIterations is used as a counter to count number of times the sorting algo iterates through the list.
        numberOfIterations = 0
        while not isSorted:
            isSorted = True
            for i in range(len(input_array)-1):
                # comparing and sorting of list is done here.
                if input_array[i]>input_array[i+1]:
                    print("Sorting via Bubble Sort: ", input_array)
                    input_array[i], input_array[i+1] = input_array[i+1], input_array[i]
                    isSorted = False
            numberOfIterations += 1
        return input_array


class Selection:
    def selectionSort(self, input_array):
        currentIndex = 0
        while currentIndex < len(input_array):
            smallestIndex = currentIndex
            for i in range(currentIndex + 1,(len(input_array))):
                # comparing and sorting of list is done here.
                if input_array[smallestIndex] > input_array[i]:
                    smallestIndex = i
            print("Sorting via Selection Sort: ",input_array)
            input_array[currentIndex], input_array[smallestIndex] = input_array[smallestIndex], input_array[currentIndex]
            currentIndex += 1
        return input_array


class Merge:
    def mergeSort(self, input_array):
        if len(input_array) == 1:
            return input_array
        middleIndex = len(input_array)//2
        leftHalf = input_array[:middleIndex]
        rightHalf = input_array[middleIndex:]
        return self.mergingSortedArrays(self.mergeSort(leftHalf),self.mergeSort(rightHalf))

    def mergingSortedArrays(self, leftHalf, rightHalf):
        input_array = [None] *(len(leftHalf)+len(rightHalf))
        k=i=j=0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                input_array[k] = leftHalf[i]
                i += 1
            else:
                input_array[k] = rightHalf[j]
                j +=1
            k +=1

        while i<len(leftHalf):
            input_array[k] = leftHalf[i]
            i += 1
            k += 1

        while j<len(rightHalf):
            input_array[k] = rightHalf[j]
            j+=1
            k+=1

        print("Sorting via Merge Sort ", input_array)
        return input_array


class Heap:
    def heapify(self,input_array, n, i):
        largest = i  
        left = 2 * i + 1     
        right = 2 * i + 2
        # if left child exists
        if left < n and input_array[left] > input_array[largest]:
            largest = left
        # if right child exists
        if right < n and input_array[right] > input_array[largest]:
            largest = right
        # Swap and continue heapifying if root is not largest
        if largest != i: 
            input_array[i], input_array[largest] = input_array[largest], input_array[i]
            # Heapify root
            self.heapify(input_array, n, largest)
        print("Sorting via Heap Sort: ", input_array)

    def heapSort(self, input_array):
        n = len(input_array) 
        # Build a maxheap
        for i in range(n, -1, -1):
            self.heapify(input_array, n, i) 
        for i in range(n-1, 0, -1): 
            input_array[i], input_array[0] = input_array[0], input_array[i] 
            self.heapify(input_array, i, 0) 


class Quick:
    def partition(self, input_array, start, end):
        # This function takes last element as pivot
        pivot = input_array[end]
        pI = start

        for i in range(start, end):

            if input_array[i] <= pivot:
                input_array[i], input_array[pI] = input_array[pI], input_array[i]
                pI = pI + 1

        print("Sorting via Quick Sort: ", input_array)
        input_array[pI], input_array[end] = input_array[end], input_array[pI]
        return pI


    def quick_sort(self, input_array, start, end):
        if (start >= end):
            return

        part = self.partition(input_array, start, end)

        self.quick_sort(input_array, start, part - 1)
        self.quick_sort(input_array, part + 1, end)


class Median:
    def quick_median_sort(self, input_array):
        self.quick_sort_helper(input_array, 0, len(input_array)-1)


    def median(self, a, i, j, k):
        if a[i] < a[j]:
            if a[k] < a[i]:
                return i
            elif a[k] < a[j]:
                return k
            else:
                return j
        else:
            if a[k] < a[j]:
                return j
            elif a[k] < a[i]:
                return k
            else:
                return i


    def quick_sort_helper(self, input_array, first, last):
        if first < last:
            splitpoint = self.partition_median(input_array, first, last)
            self.quick_sort_helper(input_array, first, splitpoint-1)
            self.quick_sort_helper(input_array, splitpoint+1, last)


    # Make Partition
    def partition_median(self, input_array, first, last):
        pivotindex = self.median(input_array, first, last, (first + last) // 2)
        input_array[first], input_array[pivotindex] = input_array[pivotindex], input_array[first]
        pivotvalue = input_array[first]
        leftmark = first+1
        rightmark = last
        done = False
        # Compare and Swap based on both part
        while not done:
            while leftmark <= rightmark and input_array[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while input_array[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = input_array[leftmark]
                input_array[leftmark] = input_array[rightmark]
                input_array[rightmark] = temp

        print("Sorting via Quick Median Sort: ", input_array)
        temp = input_array[first]
        input_array[first] = input_array[rightmark]
        input_array[rightmark] = temp

        return rightmark




def random_Number_Generator(n):
    # generating a list of numbers ranging from 1 to 10,000.
    generated_list = []
    for i in range(0, n):
        j = random.randint(1,100000)  
        generated_list.append(j)
    return generated_list


def input_From_User(n):
    print("Enter the elements to be entered to the list: ")
    #enter elements.
    input_list = []
    for i in range (0,n):
        elements = int(input())
        input_list.append(elements)
    return input_list

def algorithms_comparison():
    element1 = list()
    time1 = list()
    element2 = list()
    time2 = list()
    element3 = list()
    time3 = list()
    element4 = list()
    time4 = list()
    element5 = list()
    time5 = list()
    element6 = list()
    time6 = list()

    for p in range(1,100):
        
        a1 = [random.randint(1, 1000) for _ in range(p)]
        start_point1 = time.time()
        isort.insertionSort(a1)
        end_point1 = time.time()
        element1.append(len(a1))
        time_difference1 = (end_point1-start_point1)
        time1.append(time_difference1)

        a2 = [random.randint(1, 1000) for _ in range(p)]
        start_point2 = time.time()
        hsort.heapSort(a2)
        end_point2 = time.time()
        element2.append(len(a2))
        time_difference2 = (end_point2-start_point2)
        time2.append(time_difference2)

        a3 = [random.randint(1, 1000) for _ in range(p)]
        start_point3 = time.time()
        msort.mergeSort(a3)
        end_point3 = time.time()
        element3.append(len(a3))
        time_difference3 = (end_point3-start_point3)
        time3.append(time_difference3)

    
        a4 = [random.randint(1, 1000) for _ in range(p)]
        start_point4 = time.time()
        qsort.quick_sort(a4, 0, len(a4)-1)
        end_point4 = time.time()
        element4.append(len(a4))
        time_difference4 = (end_point4-start_point4)
        time4.append(time_difference4)

    
        a5 = [random.randint(1, 1000) for _ in range(p)]
        start_point5 = time.time()
        ssort.selectionSort(a5)
        end_point5 = time.time()
        element5.append(len(a5))
        time_difference5 = (end_point5-start_point5)
        time5.append(time_difference5)

   
        a6 = [random.randint(1, 1000) for _ in range(p)]
        start_point6 = time.time()
        bsort.bubbleSort(a6)
        end_point6 = time.time()
        element6.append(len(a6))
        time_difference6 = (end_point6-start_point6)
        time6.append(time_difference6)

    pyplot.xlabel('List Length Size') 
    pyplot.ylabel('Time [s]') 
    pyplot.plot(element1, time1, label ='Insertion Sort')
    pyplot.plot(element2, time2, label ='Heap Sort')
    pyplot.plot(element3, time3, label ='Merge Sort')
    pyplot.plot(element4, time4, label ='Quick Sort')
    pyplot.plot(element5, time5,  label ='Selection Sort') 
    pyplot.plot(element6, time6,  label ='Bubble Sort')
    pyplot.grid() 
    pyplot.legend() 
    pyplot.show()


if __name__ == "__main__":
    msort = Merge()
    qsort = Quick()
    mqsort = Median()
    hsort = Heap()
    isort = Insertion()
    ssort = Selection()
    bsort = Bubble()

    input_list =[]

    print("Please enter the type of sorting algorithm you would like to use to sort the array.")
    options = input("The choices are 'Merge','Insertion','Quick','Selection','Heap','Bubble','All': ")
    options.lower()

    if options == "merge":
        #enter the size of the array/list.
        n = int(input("Enter the Array list size that needs to be sorted: "))
        choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
        choice_2.lower()

        if choice_2 == 'y':
            input_list = random_Number_Generator(n)
            print("The input array/list to be sorted is: " +str(input_list))
            sorted_merge = msort.mergeSort(input_list)
            print("The sorted array/list post Merge Sort is: " +str(sorted_merge))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            print("Would you like to see it's time vs number of Inputs Graph?")
            graph_option = input("Enter either (Y/N): ")
            graph_option.lower()
            if graph_option == 'y':
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    a = [random.randint(1, 1000) for j in range(i)]
                    start_point1 = time.time() 
                    msort.mergeSort(a)
                    end_point1 = time.time() 
                    elements.append(len(a)) 
                    times.append(end_point1-start_point1) 
  
                pyplot.xlabel('List/Array Length Size') 
                pyplot.ylabel('Time in seconds [s]') 
                pyplot.plot(elements, times, label ='Merge Sort') 
                pyplot.grid() 
                pyplot.legend() 
                pyplot.show()
            else:
                sys.exit()

        elif choice_2 == 'n':
            input_list = input_From_User(n)
            print("The input list from the user is: " +str(input_list))
            sorted_merge = msort.mergeSort(input_list)
            print("The sorted array/list post Merge Sort is: " +str(sorted_merge))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)

    if options == "insertion":
        #enter the size of the array/list.
        n = int(input("Enter the Array list size that needs to be sorted: "))
        choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
        choice_2.lower()

        if choice_2 == 'y':
            input_list = random_Number_Generator(n)
            print("The input array/list to be sorted is: " +str(input_list))
            isort.insertionSort(input_list)
            print("The sorted array/list post Insertion Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            print("Would you like to see it's time vs number of Inputs Graph?")
            graph_option = input("Enter either (Y/N): ")
            graph_option.lower()
            if graph_option == 'y':
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    a = [random.randint(1, 1000) for j in range(i)]
                    start_point1 = time.time() 
                    isort.insertionSort(a)
                    end_point1 = time.time() 
                    elements.append(len(a)) 
                    times.append(end_point1-start_point1) 
  
                pyplot.xlabel('List/Array Length Size') 
                pyplot.ylabel('Time in seconds [s]') 
                pyplot.plot(elements, times, label ='Insertion Sort') 
                pyplot.grid() 
                pyplot.legend() 
                pyplot.show()
            else:
                sys.exit()

        elif choice_2 == 'n':
            input_list = input_From_User(n)
            print("The input list from the user is: " +str(input_list))
            isort.insertionSort(input_list)
            print("The sorted array/list post Insertion Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)

    if options == "quick":

        print("Please enter the type of Quick sort algorithm you would like to use.")
        quick_option = input("The choices are 'Regular','Median': ")
        quick_option.lower()

        if quick_option == "regular":
            #enter the size of the array/list.
            n = int(input("Enter the Array list size that needs to be sorted: "))
            start = 0
            end = n-1
            choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
            choice_2.lower()

            if choice_2 == 'y':
                input_list = random_Number_Generator(n)
                print("The input array/list to be sorted is: " +str(input_list))
                qsort.quick_sort(input_list, start, end)
                print("The sorted array/list post Quick Sort is: " +str(input_list))
                total_execution_time = time.process_time()
                print("The total execution time is: " ,total_execution_time)
                print("Would you like to see it's time vs number of Inputs Graph?")
                graph_option = input("Enter either (Y/N): ")
                graph_option.lower()
                if graph_option == 'y':
                    elements = list() 
                    times = list() 
                    for i in range(1, n):  
                        a = [random.randint(1, 1000) for j in range(i)]
                        start_point1 = time.time() 
                        qsort.quick_sort(a, 0, len(a)-1)
                        end_point1 = time.time() 
                        elements.append(len(a)) 
                        times.append(end_point1-start_point1) 
    
                    pyplot.xlabel('List/Array Length Size') 
                    pyplot.ylabel('Time in seconds [s]') 
                    pyplot.plot(elements, times, label ='Quick Sort') 
                    pyplot.grid() 
                    pyplot.legend() 
                    pyplot.show()
                else:
                    sys.exit()

            elif choice_2 == 'n':
                input_list = input_From_User(n)
                print("The input list from the user is: " +str(input_list))
                qsort.quick_sort(input_list, start, end)
                print("The sorted array/list post Quick Sort is: " +str(input_list))
                total_execution_time = time.process_time()
                print("The total execution time is: " ,total_execution_time)
        
        if quick_option == "median":
            #enter the size of the array/list.
            n = int(input("Enter the Array list size that needs to be sorted: "))
            start = 0
            end = n-1
            choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
            choice_2.lower()

            if choice_2 == 'y':
                input_list = random_Number_Generator(n)
                print("The input array/list to be sorted is: " +str(input_list))
                mqsort.quick_median_sort(input_list)
                print("The sorted array/list post Quick Sort is: " +str(input_list))
                total_execution_time = time.process_time()
                print("The total execution time is: " ,total_execution_time)
                print("Would you like to see it's time vs number of Inputs Graph?")
                graph_option = input("Enter either (Y/N): ")
                graph_option.lower()
                if graph_option == 'y':
                    elements = list() 
                    times = list() 
                    for i in range(1, n):  
                        a = [random.randint(1, 1000) for j in range(i)]
                        start_point1 = time.time() 
                        mqsort.quick_median_sort(a)
                        end_point1 = time.time() 
                        elements.append(len(a)) 
                        times.append(end_point1-start_point1) 
    
                    pyplot.xlabel('List/Array Length Size') 
                    pyplot.ylabel('Time in seconds [s]') 
                    pyplot.plot(elements, times, label ='Quick Sort') 
                    pyplot.grid() 
                    pyplot.legend() 
                    pyplot.show()
                else:
                    sys.exit()

            elif choice_2 == 'n':
                input_list = input_From_User(n)
                print("The input list from the user is: " +str(input_list))
                mqsort.quick_median_sort(input_list)
                print("The sorted array/list post Quick Sort is: " +str(input_list))
                total_execution_time = time.process_time()
                print("The total execution time is: " ,total_execution_time)

    if options == "selection":
        #enter the size of the array/list.
        n = int(input("Enter the Array list size that needs to be sorted: "))
        choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
        choice_2.lower()

        if choice_2 == 'y':
            input_list = random_Number_Generator(n)
            print("The input array/list to be sorted is: " +str(input_list))
            ssort.selectionSort(input_list)
            print("The sorted array/list post Selection Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            print("Would you like to see it's time vs number of Inputs Graph?")
            graph_option = input("Enter either (Y/N): ")
            graph_option.lower()
            if graph_option == 'y':
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    a = [random.randint(1, 1000) for j in range(i)]
                    start_point1 = time.time() 
                    ssort.selectionSort(a)
                    end_point1 = time.time() 
                    elements.append(len(a)) 
                    times.append(end_point1-start_point1) 
  
                pyplot.xlabel('List/Array Length Size') 
                pyplot.ylabel('Time in seconds [s]') 
                pyplot.plot(elements, times, label ='Selection Sort') 
                pyplot.grid() 
                pyplot.legend() 
                pyplot.show()
            else:
                sys.exit()

        elif choice_2 == 'n':
            input_list = input_From_User(n)
            print("The input list from the user is: " +str(input_list))
            ssort.selectionSort(input_list)
            print("The sorted array/list post Selection Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)

    if options == "heap":
        #enter the size of the array/list.
        n = int(input("Enter the Array list size that needs to be sorted: "))
        choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
        choice_2.lower()

        if choice_2 == 'y':
            input_list = random_Number_Generator(n)
            print("The input array/list to be sorted is: " +str(input_list))
            hsort.heapSort(input_list)
            print("The sorted array/list post Heap Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            print("Would you like to see it's time vs number of Inputs Graph?")
            graph_option = input("Enter either (Y/N): ")
            graph_option.lower()
            elements = list()
            times = list()
            if graph_option == 'y':
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    a = [random.randint(1, 1000) for j in range(i)]
                    start_point1 = time.time() 
                    hsort.heapSort(a)
                    end_point1 = time.time() 
                    elements.append(len(a)) 
                    times.append(end_point1-start_point1) 
  
                pyplot.xlabel('List/Array Length Size') 
                pyplot.ylabel('Time in seconds [s]') 
                pyplot.plot(elements, times, label ='Heap Sort') 
                pyplot.grid() 
                pyplot.legend() 
                pyplot.show()
            else:
                sys.exit()

        elif choice_2 == 'n':
            input_list = input_From_User(n)
            print("The input list from the user is: " +str(input_list))
            hsort.heapSort(input_list)
            print("The sorted array/list post Heap Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)

    if options == "bubble":
        #enter the size of the array/list.
        n = int(input("Enter the Array list size that needs to be sorted: "))
        choice_2 = input("Would you like the random generator to generate inputs for the array to be sorted? Please type (Y/N): ")
        choice_2.lower()

        if choice_2 == 'y':
            input_list = random_Number_Generator(n)
            print("The input array/list to be sorted is: " +str(input_list))
            bsort.bubbleSort(input_list)
            print("The sorted array/list post Bubble Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            print("Would you like to see it's time vs number of Inputs Graph?")
            graph_option = input("Enter either (Y/N): ")
            graph_option.lower()
            if graph_option == 'y':
                elements = list() 
                times = list() 
                for i in range(1, n):  
                    a = [random.randint(1, 1000) for j in range(i)]
                    start_point1 = time.time() 
                    bsort.bubbleSort(a)
                    end_point1 = time.time() 
                    elements.append(len(a)) 
                    times.append(end_point1-start_point1) 
  
                pyplot.xlabel('List/Array Length Size') 
                pyplot.ylabel('Time in seconds [s]') 
                pyplot.plot(elements, times, label ='Bubble Sort') 
                pyplot.grid() 
                pyplot.legend() 
                pyplot.show()
            else:
                sys.exit()

        elif choice_2 == 'n':
            input_list = input_From_User(n)
            print("The input list from the user is: " +str(input_list))
            bsort.bubbleSort(input_list)
            print("The sorted array/list post Bubble Sort is: " +str(input_list))
            total_execution_time = time.process_time()
            print("The total execution time is: " ,total_execution_time)
            
    if options == 'all':
        all_choice = input("Would you like to compare all algorithms? Enter(Y/N): ")
        all_choice.lower()

        if all_choice == 'y':
            print("Comparing all the algorithms with their time and input!")
            algorithms_comparison()
        else:
            sys.exit()
            
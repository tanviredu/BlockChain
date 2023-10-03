from sorting_techniques import pysort
sortobj = pysort.Sorting();
my_list = [9,8,7,6,5,4,3,2,1]
sort1 =  sortobj.insertionSort(my_list)
# sort2 =  sortobj.quickSort(my_list)
sort3 =  sortobj.bubbleSort(my_list)
sort4 =  sortobj.mergeSort(my_list)
sort5 =  sortobj.selectionSort(my_list)
print(sort1)
# print(sort2)
print(sort3)
print(sort4)
print(sort5)
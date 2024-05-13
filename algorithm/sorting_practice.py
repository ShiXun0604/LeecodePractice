from lib.sorting import *

sorting = ArraySorting()


data1 = [5,4,3,2,1]
data2 = [1,2,3,4,5]
data3 = [3,1,2,5,4]
rand_data = rand_list(0, 100, 20)
# BUBBLE SORT
#sorting.bubble_sort(data2,'-')
# SELECTION SORT
#sorting.selection_sort(data2, '-')
# INSERTION SORT
#sorting.insertion_sort(data2, '-')
# MERGE SORT
#sorting.merge_sort(data2, '-')
# QUICK SORT
sorting.quick_sort(rand_data, '+')
print(rand_data)

#print(rand_data)
#sorting.show_details()

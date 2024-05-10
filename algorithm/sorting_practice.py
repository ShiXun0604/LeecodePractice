from lib.sorting import ArraySorting

sorting = ArraySorting()


data1 = [5,4,3,2,1]
data2 = [1,2,3,4,5]
data3 = [3,1,2,5,4]
# BUBBLE SORT
#sorting.bubble_sort(data2,'-')
# SELECTION SORT
#sorting.selection_sort(data2, '-')
# INSERTION SORT
#sorting.insertion_sort(data2, '-')
# MERGE SORT
sorting.merge_sort(data2, '-')


print(data2)
sorting.show_details()

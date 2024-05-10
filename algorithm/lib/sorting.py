# ----------- 遊戲規則 -----------
# 不使用任何library、min()、max()等語法，只能用if判斷大小
# swap時不使用data[i], data[j] = data[j], data[i]
# 為了程式碼的易讀性，只有在decrease中統計迴圈次數、資料交換次數與if次數

class ArraySorting():
    def __init__(self) -> None:
        self.swap_times = 0
        self.loop_times = 0
        self.if_times = 0
        pass
    
    def __reset(self) -> None:
        self.swap_times = 0
        self.loop_times = 0
    
    def show_details(self) -> str:
        print('Dedails only allowed in decrease mode(\'-\').')
        print('Swappin times:{}'.format(self.swap_times))
        print('Looping times:{}'.format(self.loop_times))
        print('If times:{}'.format(self.if_times))

    def bubble_sort(self, data:list[int], type:str='+') -> None:
        # brute and force method
        # Time complexity:BC=O(n)、WC=O(n^2)、AC=O(n^2)
        # Space complexity:O(1)
        self.__reset()

        if type == '+':
            for i in range(len(data)-1):
                flag = True
                for j in range(len(data)-i-1):
                    if data[j] > data[j+1]:
                        flag = False
                        # swap
                        temp = data[j]
                        data[j] = data[j+1]
                        data[j+1] = temp
                if flag:
                    break
        elif type == '-':
            for i in range(len(data)-1):
                flag = True
                for j in range(len(data)-i-1):
                    self.loop_times += 1
                    self.if_times +=1
                    if data[j] < data[j+1]:
                        flag = False
                        # swap
                        temp = data[j]
                        data[j] = data[j+1]
                        data[j+1] = temp

                        self.swap_times += 1
                self.if_times +=1
                if flag:
                    break
        else:
            raise TypeError('Incorrect type input:{}'.format(type))
    
    def selection_sort(self, data:list[int], type:str='+') -> None:
        # kind of two pointers
        # Time complexity:BC=O(n)、WC=O(n^2)、AC=O(n^2)
        # Space complexity:O(1)
        self.__reset()

        if type == '+':
            for i in range(len(data)-1):
                # min_num = data[i]
                for j in range(i+1, len(data)):
                    if data[j] < data[i]:
                        temp = data[j]
                        data[j] = data[i]
                        data[i] = temp
        elif type == '-':
            for i in range(len(data)-1):
                # min_num = data[i]
                for j in range(i+1, len(data)):
                    self.loop_times += 1
                    self.if_times +=1
                    if data[j] > data[i]:
                        self.swap_times += 1
                        temp = data[j]
                        data[j] = data[i]
                        data[i] = temp
        else:
            raise TypeError('Incorrect type input:{}'.format(type))
    
    def insertion_sort(self, data:list[int], type:str='+') -> None:
        # kind of two pointers
        # Time complexity:BC=O(n)、WC=O(n^2)、AC=O(n^2)
        # Space complexity:O(1)
        self.__reset()

        if type == '+':
            for i in range(1, len(data)):
                temp = data[i]
                # check insert place
                index = i
                for j in range(0, i):
                    if data[j] > temp:
                        index = j
                        break
                # shift data
                for j in range(i, index, -1):
                    data[j] = data[j-1]
                data[index] = temp
        elif type == '-':
            for i in range(1, len(data)):
                self.loop_times += 1
                temp = data[i]
                # check insert place
                index = i
                for j in range(0, i):
                    self.loop_times += 1
                    self.if_times += 1
                    if data[j] < temp:
                        index = j
                        break
                # shift data
                for j in range(i, index, -1):
                    self.loop_times += 1
                    self.swap_times += 1
                    data[j] = data[j-1]
                data[index] = temp
        else:
            raise TypeError('Incorrect type input:{}'.format(type))
    
    def merge_sort(self, data:list[int], type:str='+') -> None:
        # divide and conquer、recursive
        # Time complexity:BC=O(n)、WC=O(n^2)、AC=O(n^2)
        # Space complexity:O(1)
        self.__reset()

        if type == '+':
            ans = self.__merge_sort_increase(data)
        elif type == '-':
            ans = self.__merge_sort_decrease(data)
        else:
            raise TypeError('Incorrect type input:{}'.format(type))

        data[:len(data)] = ans[:len(data)]
        
    def __merge_sort_increase(self, data:list[int]) -> list[int]:
        # divide
        if len(data) == 1:
            return data
        else:
            data1 = self.__merge_sort_increase(data[:int(len(data)/2)])
            data2 = self.__merge_sort_increase(data[int(len(data)/2):len(data)])
        #merge
        i, j = 0, 0
        ans = []
        while len(ans)<len(data):
            if i<len(data1) and j<len(data2):
                if data1[i]<data2[j]:
                    ans.append(data1[i])
                    i += 1
                else:
                    ans.append(data2[j])
                    j += 1
            elif i<len(data1):
                for a in range(i, len(data1)):
                    ans.append(data1[a])
            elif j<len(data2):
                for a in range(j, len(data2)):
                    ans.append(data2[a])
        return ans
    
    def __merge_sort_decrease(self, data:list[int]) -> list[int]:
        # divide
        if len(data) == 1:
            return data
        else:
            data1 = self.__merge_sort_decrease(data[:int(len(data)/2)])
            data2 = self.__merge_sort_decrease(data[int(len(data)/2):len(data)])
        #merge
        i, j = 0, 0
        ans = []
        while len(ans)<len(data):
            self.if_times += 1
            self.loop_times += 1
            if i<len(data1) and j<len(data2):
                self.if_times += 1
                if data1[i]>data2[j]:
                    ans.append(data1[i])
                    i += 1
                else:
                    ans.append(data2[j])
                    j += 1
            elif i<len(data1):
                for a in range(i, len(data1)):
                    self.loop_times += 1
                    ans.append(data1[a])
            elif j<len(data2):
                for a in range(j, len(data2)):
                    self.loop_times += 1
                    ans.append(data2[a])
        return ans

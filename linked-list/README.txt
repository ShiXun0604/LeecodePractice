Development version: Python 3.9.1


心得筆記：
1. 操作linked list時
    (1)最好先創建head
    (2)新資料串上node時做兩件事
        a. 把node.next指向新的ListNode(data)
        b. 將指標node移到node.next，好進行下一次串接
    (3)不要將node.next放在判斷式，因為node會None，所以直接將node放在判斷式即可。
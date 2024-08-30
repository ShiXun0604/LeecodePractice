#include <iostream>
#include <string>
#include <list>
using namespace std;



class practice {
public:
  void list_practice(){
        

  // 新增刪出元素
  if (true){
    list<int> myList = {2, 4, 6};

    // 新增
    myList.push_back(8);
    myList.push_front(0);
    cout << myList << endl;

    }
    // 迭代
    if (false){
      list<int> myList = {1, 2, 3, 4, 5, 6};
      
      /* foreach遍歷 */
      for (int i : myList){
          cout << i << " ";
      }
      cout << endl;

      /* 正向迭代器 */
      for (list<int>::iterator it = myList.begin(); it != myList.end(); it++){
          cout << *it << " ";
      }
      cout << endl;

      /* 反向迭代器 */
      for (list<int>::reverse_iterator it = myList.rbegin(); it != myList.rend(); ){
          cout << *it << " ";
          advance(it, 2);
      }
      cout << endl;
    }
  }
};


int main() {



    return 0;
}
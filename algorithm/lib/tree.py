class TreeNode():
    def __init__(self, val:int=0, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self, root:TreeNode=None) -> None:
        self.root = root

    # Preorder traversal
    def preorder_traversal(self) -> list:
        ans_list = []
        self.__preorder_traversal(self.root, ans_list)
        return ans_list
        
    def __preorder_traversal(self, root:TreeNode, ans_list:list):
        ans_list.append(root.val)
        # print('{} '.format(root.val), end='')
        if root.left:
            self.__preorder_traversal(root.left, ans_list)
        if root.right:
            self.__preorder_traversal(root.right, ans_list)

    # inorder traversal
    def inorder_traversal(self) -> list:
        ans_list = []
        self.__inorder_traversal(self.root, ans_list)
        return ans_list
        
    def __inorder_traversal(self, root:TreeNode, ans_list:list):
        if root.left:
            self.__inorder_traversal(root.left, ans_list)
        ans_list.append(root.val)
        if root.right:
            self.__inorder_traversal(root.right, ans_list)

    # postorder traversal
    def postorder_traversal(self) -> list:
        ans_list = []
        self.__postorder_traversal(self.root, ans_list)
        return ans_list
        
    def __postorder_traversal(self, root:TreeNode, ans_list:list):
        if root.left:
            self.__postorder_traversal(root.left, ans_list)
        if root.right:
            self.__postorder_traversal(root.right, ans_list)
        ans_list.append(root.val)

    # tree building
    def build_tree(self, list1:list[int], list2:list[int], type:str) -> None:
        if type == 'pre&in':
            self.root = self.__build_tree_PreIn(list1, list2)

    def __build_tree_PreIn(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if preorder == []:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        BST = TreeNode(preorder[0])
        # divide and conquer
        index = inorder.index(preorder[0])
        inorder_L = inorder[0:index]
        inorder_R = inorder[index+1:len(inorder)]
        preorder_L = preorder[1:1+len(inorder_L)]
        preorder_R = preorder[1+len(inorder_L):len(preorder)]
        
        BST.left = self.__build_tree_PreIn(preorder_L, inorder_L)
        BST.right = self.__build_tree_PreIn(preorder_R, inorder_R)
        return BST
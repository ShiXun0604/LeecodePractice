from lib.tree import TreeNode

BST_0 = TreeNode(4 ,TreeNode(2 ,TreeNode(1), TreeNode(3)), TreeNode(6))

BST_1 = TreeNode(10,
    left=TreeNode(5,
        left=TreeNode(3,
            left=TreeNode(1)
        ),
        right=TreeNode(7)
    ),
    right=TreeNode(15,
        left=TreeNode(12,
            right=TreeNode(13)
        ),
        right=TreeNode(20)
    )
)

BST_2 = TreeNode(20,
    left=TreeNode(10,
        left=TreeNode(5,
            left=TreeNode(3,
                left=TreeNode(1)
            ),
            right=TreeNode(7)
        ),
        right=TreeNode(15,
            left=TreeNode(12)
        )
    ),
    right=TreeNode(30,
        left=TreeNode(25),
        right=TreeNode(35,
            left=TreeNode(32,
                left=TreeNode(31)
            ),
            right=TreeNode(40)
        )
    )
)
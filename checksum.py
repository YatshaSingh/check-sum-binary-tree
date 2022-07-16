def checksum(root):
    def dfs(root):
        child=0
        if not root:
            return None
        if root.left:
            child+=root.left
        if root.right:
            child+=root.right
        if child<=root.data:
            root.left=root.data
            root.right=root.data
        else:
            root.data=child
        dfs(root.left)
        dfs(root.right)
        total=0
        if root.left:
            tot+=root.left
        if root.right:
            tot+=root.right
        if root.left or root.right:
            root.data=tot

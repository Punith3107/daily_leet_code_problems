class Solution:
    def findSubtreeSizes(self, parent, s):
        n=len(parent)
        children=[[] for _ in range(n)]
        for i in range(1,n):
            children[parent[i]].append(i)
        last=[-1]*26
        new_parent=parent[:]
        stack=[(0,0,-1)]
        while stack:
            node,state,prev=stack.pop()
            c=ord(s[node])-97
            if state==0:
                prev=last[c]
                if node and prev!=-1:
                    new_parent[node]=prev
                last[c]=node
                stack.append((node,1,prev))
                for child in reversed(children[node]):
                    stack.append((child,0,-1))
            else:
                last[c]=prev
        tree=[[] for _ in range(n)]
        for i in range(1,n):
            tree[new_parent[i]].append(i)
        order=[0]
        for node in order:
            order.extend(tree[node])
        ans=[1]*n
        for node in reversed(order[1:]):
            ans[new_parent[node]]+=ans[node]
        return ans

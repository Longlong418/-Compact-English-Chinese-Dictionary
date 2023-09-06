class tree_node:
    def __init__(self,english="",chinese="") -> None:
        self.english=english
        self.chinese=chinese
        self.lchild=None
        self.rchild=None
        self.height=0
        
class Avl_tree:
    def __init__(self) -> None:
        self.root=None
        self.num=0

    def get_height(self,root:tree_node):#计算当前节点的高度值
        if root==None:
            return 0
        return  root.height
        
    def tleft(self,node:tree_node):
        """
        树结构示意图：
                node
               / \
              O   y
                 / \
                O   O
        """
        y=node.rchild
        yl=y.lchild
        y.lchild=node
        node.rchild=yl
        node.height=1+max(self.get_height(node.lchild),self.get_height(node.rchild))
        y.height=1+max(self.get_height(y.lchild),self.get_height(y.rchild))

        return y
        
    
    def tright(self,node:tree_node):
        """
        树结构示意图：
                node
               / \
              y   O
             / \
            O   O
        """
        y=node.lchild
        yr=y.rchild
        y.rchild=node
        node.lchild=yr 
        node.height=1+max(self.get_height(node.lchild),self.get_height(node.rchild))
        y.height=1+max(self.get_height(y.lchild),self.get_height(y.rchild))
        return y   



    #def _print_tree(self,root:tree_node):
        # if root==None:
        #     return 
        # print("{}:{}".format(root.english,root.chinese))
        # self._print_tree(root.lchild)
        # self._print_tree(root.rchild)

    def _insert(self,p:tree_node,english,chinese):
        
        if p==None:
            return tree_node(english,chinese)
        elif p.english==english:
            return p
        elif p.english>english:
            p.lchild=self._insert(p.lchild,english,chinese)
            #判断是否平衡
            bf=self.get_height(p.lchild)-self.get_height(p.rchild)
            if bf>=2:
                if english<p.lchild.english:#ll型不平衡
                    p=self.tright(p)
                else:###LR型
                    p.lchild=self.tleft(p.lchild)
                    p=self.tright(p)
        else:
            p.rchild=self._insert(p.rchild,english,chinese)
            bf=self.get_height(p.rchild)-self.get_height(p.lchild)
            if bf>=2:
                if english>p.rchild.english:##RR型
                    p=self.tleft(p)
                else:##RL型
                    p.rchild=self.tright(p.rchild)
                    p=self.tleft(p)
        p.height=1+max(self.get_height(p.lchild),self.get_height(p.rchild))
        return p

    def _delete(self,word,p:tree_node):
        if p==None:
            #print("{}单词不存在".format(word))
            return p
        elif p.english==word:
            if p.lchild==None:##如果只有右子树，将其右子树赋值到此节点
                return p.rchild
            elif p.rchild==None:##如果只有左子树，将其左子树赋值到此节点
                return p.lchild
            else:#同时拥有左右子树
                if self.get_height(p.lchild)>self.get_height(p.rchild):#左子树大于右子树
                    tnode=p.lchild
                    #找到左子树的最右节点 将最右节点的值赋予原节点并删除
                    while tnode.rchild:
                        tnode=tnode.rchild
                    p=self._delete(tnode.english,p)
                    p.english=tnode.english
                    p.chinese=tnode.chinese
                    return p
                else:#右子树大于左子树
                    tnode=p.rchild
                    #找到右子树的最左节点 将最左节点的值赋予原节点并删除
                    while tnode.lchild:
                        tnode=tnode.lchild
                    p=self._delete(tnode.english,p)
                    p.english=tnode.english
                    p.chinese=tnode.chinese
                    return p
        elif p.english>word:
            p.lchild=self._delete(word,p.lchild)#在左子树中删除
            bf=self.get_height(p.rchild)-self.get_height(p.lchild)
            if bf>=2:
                if self.get_height(p.rchild.lchild)>self.get_height(p.rchild.rchild):#Rl型不平衡
                    p.rchild=self.tright(p.rchild)
                    p=self.tleft(p)
                else:###RR型
                    p=self.tleft(p)
        elif p.english<word:
            p.rchild=self._delete(word,p.rchild)#在右子树中删除
            bf=self.get_height(p.lchild)-self.get_height(p.rchild)
            if bf>=2:
                if self.get_height(p.lchild.rchild)>self.get_height(p.lchild.lchild):#lR型不平衡
                    p.lchild=self.tleft(p.lchild)
                    p=self.tright(p)
                else:###ll型
                    p=self.tright(p)
        p.height=1+max(self.get_height(p.lchild),self.get_height(p.rchild))
        return p
                
    def insert(self,english,chinses):
        if self.search_word(english)!=False:
            return False
        self.num+=1
        self.root=self._insert(self.root,english,chinses)
        

    def delete(self,word):

        if self.search_word(word)==False:
            return False
        self.num-=1
        self.root=self._delete(word,self.root)
        
        
    # def print_tree(self):
    #   self._print_tree(self.root)

    def search_word(self,word):
        p=self.root
        while p:
            if p.english==word:
                return p.chinese
            elif p.english>word:
                p=p.lchild
            else:
                p=p.rchild
        return False









        
# t=avl_tree()
# s={'dog':'狗','big':'大','pig':'猪','your':'你的'}
# for i in s:
#     t.insert(i,s[i])
# ans=t.search_word('your')
# print(ans)
# t.delete('dog')
# ans=t.search_word('dog')
# print(ans)
# t.print_tree()


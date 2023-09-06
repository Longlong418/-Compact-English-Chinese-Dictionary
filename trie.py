class trie_node:
    def __init__(self) -> None:
        self.chines=""
        self.child={}
        self.val=False#该节点是否构成单词
class Trie:
    def __init__(self) -> None:
        self.root=trie_node()
        self.num=0#贮存的单词数量

    def insert(self,word,chines) -> None:
        temp=self._search(word)
        if temp!=False:
            return False
        tempnode=self.root
        for i in word:
            if i not in tempnode.child:
                tempnode.child[i]=trie_node()
            tempnode=tempnode.child[i]
        tempnode.val=True
        tempnode.chines=chines
        self.num+=1
        

    def search_word(self,word):
        temp=self.search(word)
        if temp==False:
            #print("未查询到该单词")##这里明天得改一下，把这个写在外边，没必要写到这里，这里做测试用
            return False
        else:
            return temp
    
    def search(self,word):
        t=''
        possible_word=[]
        tempnode=self.root
        for i in word:
            #print(tempnode.child.keys())
            if tempnode.val==True:
                possible_word.append("你可能在找:{}:{}".format(t,tempnode.chines))#模糊查找
            if i not in tempnode.child:
                return possible_word
            tempnode=tempnode.child[i]
            t+=i
            #print(possible)
        if tempnode.val==True:
            return tempnode.chines
        elif len(possible_word)!=0:
            return possible_word
        else:
            return False
    def _search(self,word):
        tempnode=self.root
        for i in word:
            #print(tempnode.child.keys())
            if i not in tempnode.child:
                return False
            tempnode=tempnode.child[i]
        if tempnode.val==True:
            return tempnode
        else:
            return False
            
    def delete(self,words):
        temp=self._search(words)
        if temp==False:
        # print("未查询到该单词")
            return False
        else:
            self.num-=1
            temp.val=False
            #print("{} 已被成功删除".format(words+":"+temp.chines))
        

# t=Trie()
# s={'dog':'狗','big':'大','yours':'你的的','your':'你的',"doggge":"nishi"}
# for i in s:
#     t.insert(i,s[i])
# ans=t.search_word('doggg')
# print(ans)




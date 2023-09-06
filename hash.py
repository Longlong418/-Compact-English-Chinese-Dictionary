class hashnode:
    def __init__(self,next=None) -> None:
        self.english=""
        self.chinese=""
        self.next=next
class Hashtable:
    def __init__(self) -> None:
        self.num=0
        self.mod=1022
        self.head=[hashnode() for i in range(self.mod)]

    def hashcode(self,word):#哈希函数：将单词的每个字母的Unicode编码值乘以该该字母位于该单词的次序之后相加
        index=0
        x=1 
        for i in word:
            index+=ord(i)*x
            x+=1
        return index%self.mod

    def mainsearch(self,word):
        key=self.hashcode(word)
        tnode=self.head[key]
        while tnode:
            if tnode.english==word:
                return tnode
            tnode=tnode.next
        return False
    #开散列表
    def insert(self,english,chinese):
        key=self.hashcode(english)
        res=self.mainsearch(english)
        if res==False:
            newnode=hashnode()
            newnode.chinese=chinese
            newnode.english=english
            newnode.next=self.head[key].next
            self.head[key].next=newnode
            self.num+=1
        else:
            return False##已存在
    def search_word(self,word):
        key=self.mainsearch(word)
        if key==False:
            return False
        else:
            return key.chinese

    def delete(self,word):
        key=self.hashcode(word)
        res=self.mainsearch(word)
        if res!=False:
            pre=self.head[key]
            p=self.head[key].next
            while p:
                if p.english!=word:
                    pre=p
                    p=p.next
                else:
                    pre.next=p.next
                    del p
                    break
            self.num-=1
        else:
            return False##不存在











            
# t=hashtable()
# s={'dog':'狗','big':'大','pig':'猪','your':'你的'}
# for i in s:
#     t.insert(i,s[i])
# print(t.num)
# ans=t.search_word('pig')
# print(ans)
# t.delet('pig')
# a=t.search_word('pig')
# print(a)




        


        

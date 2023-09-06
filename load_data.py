#wordindex=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words={}
cnt=1
with open("word_source\AllTestWord.txt",mode='r',encoding='utf-8') as f:
    a=f.readlines()
    newdata= [x.replace('\n','') for x in a]
    cnt=0
    for i in a:
        if cnt%2==0:
            key=newdata[cnt]
            data=newdata[cnt+1]
            words[key]=data
        cnt+=1


        


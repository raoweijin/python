class solution:
    def kfrequent(self, words,num):
        length = len(words)
        wordnum = {}
        for word in words:
            if word not in wordnum:
                wordnum[word] = 1
            else:
                wordnum[word]+=1
        print("wordnum", wordnum)
        d = []
        for k in wordnum.items():
            d.append([k[1],k[0]])
        print("d: ",d)
        d.sort()
        print("sorted d ",d)
        length = len(d)
        res=[]
        start = length-1
        print("num is ",num, type(num))
        end = length-1-num
        for i in range(start,end,-1):
            res.append(d[i][1])
        print("res is ",res)

mysolution = solution()
words= [     "yes", "lint", "code",    "yes", "code", "baby",    "you", "baby", "chrome",    "safari", "lint", "code",    "body", "lint", "code"]
k =3
print("words:")
print(words)
num = 3
mysolution.kfrequent(words,num)
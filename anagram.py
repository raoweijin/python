res = []
def fullSet(input, strList,res):
    print("input is ", input, "strlist is ",strList)
    length = len(input)
    if 0== length:
        #global res
        res.append(strList)
        return res
    for i in range(length):
        #temp = strList
        if (i > 0):
            if input[i] != input[i-1]:                
                temp  = strList + [input[i]]
                fullSet(input[:i]+input[i+1:],temp,res)
        else:
                temp  = strList + [input[i]]
                fullSet(input[:i]+input[i+1:],temp,res)
    return res
data=[1,2,2]

res = fullSet(data,[],[])

print(res)


'''
    
    Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
Tags 
'''
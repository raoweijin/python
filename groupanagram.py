strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
'''
Return 
[
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
'''
data = {}
for ie in strs:
    key  = ''.join(sorted(ie))
    if key not in data:
        data[key] =[ie]
    else:
        data[key].append(ie)
result = []
print(data)
for ie in data:
    result.append(data[ie])
print(result)
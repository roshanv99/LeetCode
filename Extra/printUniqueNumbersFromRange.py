'''
1. Store in dictionary and add the number of times rhe character appears
2. Print of more than 1
'''

n= [100 , 105] 
l = dict()
uc = list()
for i in range(n[0], n[1]+1):
    for j in str(i):
        if j not in l.keys():
            l[j] = 1
        else:
            l[j] +=1 
        

for key,value in l.items() :
    if value == 1:
       uc.append(int(key)) 

print(uc)

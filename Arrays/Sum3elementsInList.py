#Calculate highest possible sum of very 3 elements
#If size if less than 4 print INVALID

'''
onsider 1 element and from there take the next 2 elements and add all 3 like this do for all elements and give the max sum

for example
[5,0,1,2,3] is the array

take 5 then 2 elements 5+0+1 = 6
now with 5 itself take the next 2 elements 5+1+2=8
now with 5 itself take the next 2 elements 5+2+3=10

now 5 is over, we have added all 2 consecutive numbers with 5,

next take 0 and 2 elements 0+1+2 = 3
now with 0 itself take the next 2 elements 0+2+3=5

now 0 is over, we have added all 2 consecutive numbers with 0,

now take 1 and add two two elements 1+2+3=6

now 1 also over,

now take 2 ..here we don't have next 2 elements isn't it so we stop here

now from all obtained sums give the highest
'''




#######################################################

inp = list(map(int,list(input())))
s = 0
greatest = 0

for i in range(0,len(inp)-2):
    s = inp[i]
    #print(str(inp[i]))
    for j in range(i+1,len(inp)-1):
        s += sum(inp[j:j+2])
        #print(str(s) + ' | ', end=" " )
        if s>greatest:
            greatest = s
        s = inp[i]
        
    s=0

print(greatest)
    

#Remove the numbers 8 and 53 from the sequence and also convert to lower case

n = list(str(input("enter string: ")))
if not "".join(n).isalnum():
    print("INVALID")
    
count = 0
i = -1

while(i<len(n)-1):
    i+=1
    n[i-count] = n[i].lower()
    if n[i]=="8":
        count+=1

    if (i<len(n)-2) and n[i] == "5" and n[i+1] == "3":
        #print('!!! ' + str(n[i]) + str(n[i+1]))
        i  +=1
        count+=2
    
    #Also add 2 for last element
    
    #print(str(i) + ': ' + ''.join(n) + ' : ' + str(count))
print(''.join(n[:i-count+1]))

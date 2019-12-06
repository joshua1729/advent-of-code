# Solution for part 1

start_range = 246540
end_range = 787419

valid_password = 0

for i in range(start_range,end_range):
    if((i//100000 == (i%100000)//10000) or ((i%100000)//10000 == (i%10000)//1000) or (i%10000//1000 == (i%1000)//100) or ((i%1000)//100 == (i%100)//10) or ((i%100)//10 == (i%10)//1)):
        if((i//100000 <= (i%100000)//10000) and ((i%100000)//10000 <= (i%10000)//1000) and (i%10000//1000 <= (i%1000)//100) and ((i%1000)//100 <= (i%100)//10) and ((i%100)//10 <= (i%10)//1)):
            valid_password = valid_password+1 

print(valid_password)


# Solution for part 2
for i in range(start_range,end_range):
    k=str(i)
    if((k[0]==k[1]) or (k[1]==k[2]) or (k[2]==k[3]) or (k[3]==k[4]) or (k[4]==k[5])):
        if((k[0]<=k[1]) and (k[1]<=k[2]) and (k[2]<=k[3]) and (k[3]<=k[4]) and (k[4]<=k[5])):
            flag=0
            for char in k:
                if (k.count(char)==2):
                    flag=1
            if(flag==1):
                valid_password = valid_password+1
            
print(valid_password)

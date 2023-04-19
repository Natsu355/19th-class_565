num=int(input())
rev=0
new_num=num
while(num>0):
    rem=num%10
    rev=rev+(rem**3)
    num=num//10
if(rev==new_num):
    print("armstrong")
else:
    print("Not a armstrong")
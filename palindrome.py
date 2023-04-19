#######
#Palindrome 
#################
num=int(input())
rev=0
new_num=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==new_num):
    print("Palindrome")
else:
    print("Not a palindrome")
    
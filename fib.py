range_r=int(input("Enter the range of series : "))
if(range_r>2):
    first=0
    second=1
    temp=0
    print(first,second,end=" ")
    for i in range(range_r-2):
        temp=first+second
        first=second
        second=temp
        print(temp,end=" ")
else:
    print("The range should be greater than 2!!")        
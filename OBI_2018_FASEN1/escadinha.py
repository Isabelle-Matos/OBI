n = int(input())

num = [int(x) for x in input().split()]

count = 0

if len(num) == 1:
    print("1")
elif len(num) == 2:   
    print("1")
else:
    diff = abs(num[1] - num[0])
    count = 1

    for i in range(2, len(num)):

        if (num[i] - num[i-1]) == diff:
            pass
        else:
            diff = abs(num[i] - num[i-1])
            count += 1

     

    print(count)
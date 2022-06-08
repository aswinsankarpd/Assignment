def the_length(num):
    count = 0
    while(num>0):
        num = int(num/10)
        count=count+1
    print(count)

num = 100
the_length(num)
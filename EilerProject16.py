def Sum():
    number = str(2<<1000)
    sum = 0
    for num in list(number):
        sum+=int(num)
    print(sum)
Sum()
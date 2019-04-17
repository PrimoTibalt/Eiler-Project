def numberOfVaries():
    field = 400
    steps = 20
    number = 1
    factField = list(range(field - steps, field + 1))
    factSecond = list(range(1, steps+1))
    for num in range(20):
        number *= int(factField[num]) / int(factSecond[num])
    print(int(number))
numberOfVaries()

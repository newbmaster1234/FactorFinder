while True:
    a = int(input("\nWhat number\n>"))
    c = 0
    for b in range(1, a+1):
        if a % b == 0:
            print(b, 'is a factor')
            c = c + 1
    print("\nIt has", c, 'factors\n')


h = 9
i = 1

while i <= h:
    j = 1
    while j <= (h-i):
        print(" ", end="")
        j += 1
    
    k = 1
    while k <= 2 * i - 1:
        print("*", end="")
        k += 1
    
    print()
    i += 1

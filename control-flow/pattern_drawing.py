size = int(input("Enter the size of the pattern: "))
count = size
while size != 0:
    for i in range(count):
        print("*", end="")
    print(" ")
    size -= 1
    

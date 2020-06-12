#multiplication tables
print("======================================")
print("INTEGER MULTIPLICATION TABLE GENERATOR")
print("======================================")
while True:
        x = int(input("ENTER THE TABLE NUMBER:"))
        a = int(input("MINIMUM LIMIT OF THE TABLE:"))
        be = int(input("MAXIMUM LIMIT OF THE TABLE:"))
        b=be+1
        print(x, "TABLE")
        print("--------")
        for i in range(a, b):
            r = i*x
            print(i, "x", x, "=", r)

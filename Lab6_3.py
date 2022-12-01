"""def funkcja(*args):
    print(*args)

funkcja()
funkcja(1,2,3,"123",1.23)

def funkcja(*args):
    print(*args)
    for i in args:
        print(i)

funkcja(1,2,3,"123",1.23)"""

def funkcja(*args):
    print(*args)
    maks=args[0]
    for i in args[1::]:
        if i>maks:
            maks=i
    return maks

print(f"Max = {funkcja(1,2,3,1.23)}")
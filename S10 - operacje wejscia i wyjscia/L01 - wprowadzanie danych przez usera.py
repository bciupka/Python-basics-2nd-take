def check_int(s):
    if s[0] in ("-", "+"):
        return s[1:].isdigit()
    return s.isdigit()


a = input("a")
b = input("b")
c = input("c")

if not check_int(a) or not check_int(b) or not check_int(c):
    print("Not decimal")
else:
    a = int(a)
    b = int(b)
    c = int(c)
    if a == 0:
        print("Not quadratic")
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print("No solutions")
        elif delta == 0:
            x1 = -b / (2 * a)
            print(x1)
        else:
            x1 = (-b - (delta ** (1 / 2))) / (2 * a)
            x2 = (-b + (delta ** (1 / 2))) / (2 * a)
            print(x1, x2)

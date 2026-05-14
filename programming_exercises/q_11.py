s1 = float(input("Side 1: "))
s2 = float(input("Side 2: "))
s3 = float(input("Side 3: "))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("Valid Triangle")
else:
    print("Invalid Triangle")
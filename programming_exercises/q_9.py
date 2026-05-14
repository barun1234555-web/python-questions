o1 = int(input("Enter first octet: "))
o2 = int(input("Enter second octet: "))
o3 = int(input("Enter third octet: "))
o4 = int(input("Enter fourth octet: "))

if 0 <= o1 <= 255 and 0 <= o2 <= 255 and 0 <= o3 <= 255 and 0 <= o4 <= 255:
    
    if 1 <= o1 <= 126:
        print("Class A")
    elif 128 <= o1 <= 191:
        print("Class B")
    elif 192 <= o1 <= 223:
        print("Class C")
    elif 224 <= o1 <= 239:
        print("Class D (Multicast)")
    elif 240 <= o1 <= 255:
        print("Class E (Experimental)")
    elif o1 == 127:
        print("Loopback Address (127.x.x.x)")
    else:
        print("Reserved or Special Address")
        
else:
    print("Invalid IP components. Cannot determine Class.")
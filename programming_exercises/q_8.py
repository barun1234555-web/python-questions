# Reading four octets
o1 = int(input("Enter first octet: "))
o2 = int(input("Enter second octet: "))
o3 = int(input("Enter third octet: "))
o4 = int(input("Enter fourth octet: "))

# Checking if all octets are in range 0-255
if 0 <= o1 <= 255 and 0 <= o2 <= 255 and 0 <= o3 <= 255 and 0 <= o4 <= 255:
    print("All numbers are in the valid range.")
else:
    print("Invalid range! Octets must be between 0 and 255.")
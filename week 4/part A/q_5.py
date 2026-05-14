main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to find: ")

n = len(main_str)
m = len(sub_str)
found = False

for i in range(n - m + 1):
    if main_str[i : i + m] == sub_str:
        found = True
        break

if found:
    print("Substring is present.")
else:
    print("Substring is not present.")
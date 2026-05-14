import random
import string

def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + "@#$!%&"
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

print(f"Generated Password: {generate_password()}")
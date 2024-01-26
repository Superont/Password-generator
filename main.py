import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = 12  # You can change this to your desired length
password = generate_password(password_length)
print("Generated Password:", password)
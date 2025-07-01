import random
import string

def generate_random_password(length):
    
    characters = string.ascii_letters + string.digits 
    password_list = []

    for _ in range(length):
        random_char = random.choice(characters)
        password_list.append(random_char)

    
    random.shuffle(password_list)

    return "".join(password_list)


password_length = 10
new_password = generate_random_password(password_length)
print(f"Generated Password: {new_password}")
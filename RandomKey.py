import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_chars = letters + digits + special  
      
    if not all_chars:  
        return "Error: there isn't any symbols for generate"  
          
    password = ''.join(random.choice(all_chars) for _ in range(length))  
    return password  
      
# Answer

if __name__ == "__main__":
    length = int(input("Length of the password: "))
    password = generate_password(length)
    print("Password generated:", password)
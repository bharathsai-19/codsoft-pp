import random
import string

def password(length=12):
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    special=string.punctuation
    character =uppercase + lowercase + special +digits
    p= ''.join(random.choice(character)for _ in range(length))
    return p
print('generated password:',password())
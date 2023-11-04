import random
import string
def get_random_string():
    letters = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for item in range(4))
    return result_str
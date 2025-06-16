
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from login import login


def pay(fees):
    print(fees)
    login("mhamil")

pay(100)


from random import randint
  
print(randint(1,10))


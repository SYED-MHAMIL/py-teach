from fees.payment import pay
from login import login
def greet(username):
    login(username)
    print("hello")
    pay(3000)

greet("admin")
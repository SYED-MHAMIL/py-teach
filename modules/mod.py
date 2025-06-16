from login import login

from fees.payment import pay

def greet(username):
    login(username)
    print("hello")
    pay(3000)

greet("admin")
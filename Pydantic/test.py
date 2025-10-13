from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int

user = User("Ali", "ali@gmail.com", 1234)
print(user)

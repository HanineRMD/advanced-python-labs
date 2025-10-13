from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value
# Exemple valide
try:
    user = User(name="Ali", email="ali@gmail.com", account_id=-12)
except Exception as e:
    print("Erreur de validation :", e)

user = User(name="Ali", email="ali@gmail.com", account_id=1234)
user_json = user.model_dump_json()
print("JSON :", user_json)

# Retour en objet Python
user_dict = user.model_dump()
print("Dictionnaire :", user_dict)

from pydantic import BaseModel, field_validator, model_validator, computed_field


class User(BaseModel):
    username: str
    email: str
    password: str
    age: int

    @field_validator("username")
    def username_must_be_valid(cls, v: str):
        if len(v) < 3:
            raise ValueError("Username must be at least 3 characters")
        return v

    @field_validator("email")
    def email_must_be_valid(cls, v: str):
        if "@" not in v:
            raise ValueError("Email must contain @")
        return v

    @model_validator(mode="after")
    def password_must_contain_number(cls, values):
        if "password" in values and not any(i.isdigit() for i in values["password"]):
            raise ValueError("Password must contain a number")
        return values

    @computed_field
    def is_adult(self) -> bool:
        return self.age >= 18


user_data = {
    "username": "XXXXXXX",
    "email": "johndoe@example.com",
    "password": "XXXXXXXXXXX",
    "age": 20
}

user = User(**user_data)
print(user)
print(user.is_adult)

from pydantic import BaseModel, field_validator, model_validator, computed_field


class User(BaseModel):
    name: str

    @field_validator("name")
    def name_length(cls, v):
        if len(v) < 3:
            raise ValueError("Name should be at least 3 characters")
        return v

    @model_validator(mode="after")
    def check_name(cls, values):
        if values.name == "John":
            raise ValueError("John is not allowed")
        return values


user = User(name="Pratap")
print(user)


class SignUp(BaseModel):
    name: str
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def check_passwords_match(cls, values):
        if values.password != values.password_confirm:
            raise ValueError("Passwords do not match")
        return values


signup = SignUp(name="John", password="123", password_confirm="123")
print(signup)


class Product(BaseModel):
    name: str
    price: float

    @computed_field
    @property
    def discounted_price(self) -> float:
        return self.price * 0.9


product = Product(name="Product 1", price=10.0)
print(product.discounted_price)

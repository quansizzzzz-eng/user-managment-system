from fastapi import FastAPI, HTTPException

class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email

users = [
    User(1, "1admin", "1admin@exmple.com"),
    User(2, "2admin", "2admin@exmple.com"),
    User(3, "3admin", "3dmin@exmple.com"),
]

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return user
    else:
        raise HTTPException(404, "User not found")
    
@app.get("/users")
def get_users():
    return users

@app.post("/create_user")
def create_user(username: str, email: str):
    user = User(user[-1].user_id + 1, username, email)
    users.append(user)
    return user
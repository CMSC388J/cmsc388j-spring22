from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def root():
    return {'status': 'failed'}


users = {
    1: {
        "name": "nikolay",
        "age": 22,
    },
    2: {
        "name": "vyoma",
        "age": 21,
    }
}


@app.get('/users')
def get_all_users():
    user_list = []
    for key, value in users.items():
        user_list.append({
            "user_id": key,
            "user_data": value
        })
    return user_list


@app.get('/user/{user_id}')
def get_user(user_id: int):
    return users[user_id]


# {
#     "name": "vyoma",
#     "age": 21,
# }
class User(BaseModel):
    name: str
    age: int


@app.post('/user')
def make_user(user: User):
    users[len(users) + 1] = {
        "name": user.name,
        "age": user.age
    }
    return {"status": "User successfully created"}

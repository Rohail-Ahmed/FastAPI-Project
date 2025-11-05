from fastapi import FastAPI , HTTPException
from model import User
from database import add_user,get_user,get_all_users,update_user,delete_user


app = FastAPI()

@app.get("/")
def home():
    return {"message" : "API Running"}

@app.post("/register")
def register(user : User):
    try:
        add_user(user.username,user.password)
        return{"message":"User registered sucessfully"}
    except:
        raise HTTPException(status_code=400,detail="User already exists")

@app.post("/login")
def login(user : User):
    user_data = get_user(user.username,user.password)
    if user_data:
        return {"message":"Login Sucessfully"}
    else:
        raise HTTPException(status_code=401,detail="Invalid Credentials")

@app.get("/users")
def show_users():
    return get_all_users() 

@app.put("/update/{user_id}") 
def update(user_id:int,username:str):
    update_user(user_id,username) 
    return {"message":"User updated"}

@app.delete("/delete/{user_id}")
def delete(user_id:int):
    delete_user(user_id)
    return {"message":"User deleted"} 



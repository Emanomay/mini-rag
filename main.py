from fastapi import FastAPI
#from routes import base

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Welcome aty FAst API!"}


#app.include_router(base.base_router)

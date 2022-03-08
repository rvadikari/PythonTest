from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def root():
    print("Welcome to python test project")
    return {"message":"Welcome to python"}
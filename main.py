from fastapi import FastAPI
from routes.student_route import router


app = FastAPI(
    title="University Student CRUD API",
    description="FastAPI Student CRUD Application using in-memory storage",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {"message": "Student CRUD API is running"}

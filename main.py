import uvicorn
from fastapi import FastAPI
from app.api.v1 import group, student
app = FastAPI(
    docs_url='/api/docs'
)

app.include_router(group.router, prefix="/api/v1/group")
app.include_router(student.router, prefix="/api/v1/student")

@app.get("/")
async def root():
    return {"messege": "Hello world"}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8005
    )
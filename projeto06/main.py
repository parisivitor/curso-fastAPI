from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)


    """
    Toke: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc2MTIyNjU2LCJpYXQiOjE2NzU1MTc4NTYsInN1YiI6IjE0In0.0WG2SlsvStjVK7tHwXc8eS1hEQ6H0C5GnEcY8Nld70E
    TIpo: bearer
    """
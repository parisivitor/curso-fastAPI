from fastapi import APIRouter

router = APIRouter()

cursos = {
    1: {
        "titulo": "Ruby on Rails 5.0",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Python",
        "aulas": 50,
        "horas": 20
    }
}

@router.get('/api/v1/cursos')
async def get_cursos():
    return cursos
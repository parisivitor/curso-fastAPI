from fastapi import APIRouter

router = APIRouter()

usuarios = {
    1: {
        "Nome": "Ruby on Rails 5.0",
        "idade": 112
    },
    2: {
        "titulo": "Python",
        "aulas": 50,
    }
}

@router.get('/api/v1/usuarios')
async def get_usuarios():
    return usuarios
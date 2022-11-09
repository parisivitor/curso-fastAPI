from time import sleep
from typing import Dict, List, Optional, Any
from models import Curso
from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends
from fastapi.responses import JSONResponse
from routes import curso_router
from routes import usuario_router

app = FastAPI(
    title="API Curso FastAPI",
    version="0.0.1",
    description="Uma API para estudo do FastAPI"
)
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])

def fake_db():
    try:
        print('Abrindo conexão com o banco...')
        sleep(1)
    finally:
        print('Fechando conexão com o banco...')
        sleep(1)


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

sub_curso = {
    1: {
        "Vai caralho": "Python na veia",
        "Gostando ou nao?": True
    },
    2: {
        "Ruby é o caralho": True,
        "Tempo perdido em ruby": 100
    }
}

@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia.', summary='Retorna todos os cursos.', response_model=Dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos



@app.get('/curso/{curso_id}')
async def get_cursos(curso_id: int = Path(default=None, title="ID do curso", description="Deve ser entre 1 e 2", gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        # if curso['titulo'] == "Python":
        #     curso.update({"sub_curso": sub_curso})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado.")



@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso


@app.put('/curso/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe um curso com id {curso_id}")


@app.delete('/curso/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não existe um curso com id {curso_id}")


@app.get('/calculadora')
async def calculadora(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), c: Optional[int] = None, x_geek: str = Header(default=None)):
    soma: int = a + b
    if c:
        soma = soma + c
    print(f'X-GEEK: {x_geek}')
    return {"Resultado": soma}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, log_level="info", reload=True, debug=True)

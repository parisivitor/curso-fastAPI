from lib2to3.pgen2.token import OP
from typing import Optional
from pydantic import BaseModel






class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

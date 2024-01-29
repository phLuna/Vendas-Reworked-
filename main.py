from fastapi import FastAPI, HTTPException, status
import uvicorn

from tables.people import create_person, read_people

app = FastAPI()

@app.post("/people/add")
def criar_pessoa(name, phone_number, cpf):
    create_person(name, phone_number, cpf)
    return {"message": f'{name} foi criado(a) com sucesso!'}

@app.get("/people/read")
def ver_todos():
    try:
        people = read_people()
        return people
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Não encontrado!')
    

if __name__ == '__main__':
    uvicorn.run(app)
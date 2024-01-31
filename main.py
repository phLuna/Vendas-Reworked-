from fastapi import FastAPI, HTTPException, status
import uvicorn

from tables.people import create_person, read_people, update_person, delete_person

app = FastAPI()

@app.post("/people/add")
def criar_pessoa(name: str, phone_number: str, cpf: str):
    create_person(name, phone_number, cpf)
    return {"message": f'{name} foi criado(a) com sucesso!'}

@app.put("/people/update")
def atualizar_pessoa(id: int, item: str, update: str):
    response = update_person(id, item, update)
    return response

@app.get("/people/read")
def ver_todos():
    try:
        people = read_people()
        return people
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Não encontrado!')
    
@app.delete("/people/delete")
def deletar_pessoa(id:int):
    response = delete_person(id)
    return response
    

if __name__ == '__main__':
    uvicorn.run(app)
from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel
import uvicorn

from routes import clients_router

app = FastAPI(
    title='Gerenciamento de uma loja.',
    version='0.1',
    description='Uma API para gerenciar as vendas de uma loja.')
app.include_router(clients_router.router)

if __name__ == '__main__':
    uvicorn.run(app)
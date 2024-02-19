from fastapi import FastAPI
import uvicorn

from routes import clients_router, products_router, sells_router

app = FastAPI(
    title='Gerenciamento de uma loja.',
    version='0.1',
    description='Uma API para gerenciar as vendas de uma loja.')
app.include_router(clients_router.router, tags=['Clients'])
app.include_router(products_router.router, tags=['Products'])
app.include_router(sells_router.router, tags=['Sells'])

if __name__ == '__main__':
    uvicorn.run(app)

#banana
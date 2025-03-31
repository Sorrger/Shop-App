from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products 
from database import init_db

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], #here http://localhost:PORT adres of frontend later
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(products.router)

@app.on_event("startup")
def startup_event():
    init_db()



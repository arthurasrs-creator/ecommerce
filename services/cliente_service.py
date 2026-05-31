from database.db import db
from models.Cliente import Cliente

def criar_cliente(nome:str):
    try:
        novo_cliente = Cliente(nome=nome)

        db.session.add(novo_cliente)
        db.session.commit()

        return novo_cliente
    except Exception as e:
        db.session.rollback()
        print(e)
        return
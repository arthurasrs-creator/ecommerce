from database.db import db
from models.Categoria import Categoria

def criar_categoria(nome:str):
    try:
        categoria = Categoria.query.filter(Categoria.nome == nome).first()
        if categoria:
            return False
        
        nova_categoria = Categoria(nome=nome)

        db.session.add(nova_categoria)
        db.session.commit()

        return nova_categoria
    except Exception as e:
        db.session.rollback()
        print(e)
        return

def deletar_categoria(id:int):
    try:
        categoria = Categoria.query.get(id)
        if categoria is None:
            return None
        
        db.session.delete(categoria)
        db.session.commit()

        return categoria
    except Exception as e:
        db.session.rollback()
        print(e)
        return
from database.db import db
from models.Produto import Produto
from models.Categoria import Categoria

def criar_produto(nome:str, descricao:str, preco:float, estoque:int, id_categoria:int):
    try:
        categoria = Categoria.query.get(id_categoria)
        if not categoria:
            return False
        
        novo_produto = Produto(
            nome=nome,
            descrição=descricao,
            preço=preco,
            estoque=estoque,
            id_categoria=id_categoria
        )

        db.session.add(novo_produto)
        db.session.commit()

        return novo_produto
    except Exception as e:
        db.session.rollback()
        print(e)
        return
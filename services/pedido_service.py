from database.db import db
from models.Pedido import Pedido
from models.ItemPedido import ItemPedido
from models.Produto import Produto
from models.Cliente import Cliente

import traceback

def criar_pedido(id_cliente:int, status, id_produto:int, quantidade:int):
    try:
        cliente = Cliente.query.get(id_cliente)
        if not cliente:
            return None
        
        produto = Produto.query.get(id_produto)
        if not produto:
            return None
        
        if produto.estoque < quantidade:
            return False
        
        produto.estoque -= quantidade
        
        novo_pedido = Pedido(
            id_cliente=id_cliente,
            status=status
        )
        db.session.add(novo_pedido)
        db.session.flush()

        pedidos = ItemPedido(
            id_pedido=novo_pedido.id,
            id_produto=produto.id,
            quantidade=quantidade,
            preco_unidade=produto.preço
        )

        db.session.add(pedidos)
        db.session.commit()

        return novo_pedido
    except Exception:
        db.session.rollback()
        traceback.print_exc()
        raise


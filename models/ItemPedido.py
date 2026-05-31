from database.db import db

class ItemPedido(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    id_pedido = db.Column(
        db.Integer,
        db.ForeignKey("pedido.id"),
        nullable=False
    )
    id_produto = db.Column(
        db.Integer,
        db.ForeignKey("produto.id"),
        nullable=False
    )
    quantidade = db.Column(
        db.Integer,
        nullable=False
    )
    preco_unidade = db.Column(
        db.Float,
        nullable=False
    )
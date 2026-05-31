from database.db import db

class Cliente(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    nome = db.Column(
        db.String(200),
        nullable=False
    )
    pedidos = db.relationship(
        "Pedido",
        backref="cliente",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "nome":self.nome
        }
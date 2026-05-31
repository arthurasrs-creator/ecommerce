from database.db import db
from enums.tipo_status import TipoStatusPedido

class Pedido(db.Model):
     id = db.Column(
        db.Integer,
        primary_key=True
    )
     id_cliente = db.Column(
          db.Integer,
          db.ForeignKey("cliente.id"),
          nullable=False
     )
     status = db.Column(
          db.Enum(TipoStatusPedido),
          default=TipoStatusPedido.PENDENTE,
          nullable=False
     )
     itens = db.relationship(
        "ItemPedido",
        backref="pedido",
        lazy=True
    )
     
     def to_dict(self):
          return {
               "cliente": self.id_cliente,
               "status": self.status.value
          }
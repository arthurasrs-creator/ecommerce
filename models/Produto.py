from database.db import db

class Produto(db.Model):
     id = db.Column(
        db.Integer,
        primary_key=True
    )
     nome = db.Column(
        db.String(200),
        nullable=False
    )
     descrição = db.Column(
          db.String(255),
          nullable=False
     )
     preço = db.Column(
          db.Float,
          nullable=False
     )
     estoque = db.Column(
          db.Integer,
          nullable=False
     )
     id_categoria = db.Column(
          db.ForeignKey("categoria.id"),
          nullable=False
     )
     itens = db.relationship(
          "ItemPedido",
          backref="produto",
          lazy=True
     )
     def to_dict(self):
          return {
               "id": self.id,
               "nome": self.nome,
               "descricao": self.descrição,
               "preco": self.preco,
               "estoque": self.estoque,
               "categoria": self.id_categoria,
          }
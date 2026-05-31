from database.db import db

class Categoria(db.Model):
     id = db.Column(
        db.Integer,
        primary_key=True
    )
     nome = db.Column(
        db.String(200),
        nullable=False
    )
     produtos = db.relationship(
        "Produto",
        backref="categoria",
        lazy=True
    )
     def to_dict(self):
          return {
              "id": self.id, 
              "nome": self.nome 
          }
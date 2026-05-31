from flask import Flask
from database.db import db
from routes.cliente_route import cliente_bp
from routes.categoria_route import categoria_bp
from routes.produto_route import produto_bp
from routes.pedido_route import pedido_bp
import models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(cliente_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(produto_bp)
app.register_blueprint(pedido_bp)

if __name__ == "__main__":
    app.run(debug=True)
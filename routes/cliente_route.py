from flask import Blueprint, request, jsonify
from utils.response import response
from services.cliente_service import criar_cliente

cliente_bp = Blueprint("cliente", __name__, url_prefix="/cliente")

@cliente_bp.route("/", methods=["POST"])
def create_cliente():
    data = request.get_json()
    nome = data.get("nome")
    if nome is None:
        return response("Error", "Nome obrigatório!", 400)
    
    if not isinstance(nome, str):
        return response("error", "Nome deve ser texto!", 400)
    
    cliente = criar_cliente(nome)

    return jsonify(cliente.to_dict())
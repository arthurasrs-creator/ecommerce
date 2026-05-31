from flask import Blueprint, request, jsonify
from services.categoria_service import criar_categoria, deletar_categoria
from utils.response import response

categoria_bp = Blueprint("categoria", __name__, url_prefix="/categoria")

@categoria_bp.route("/", methods=["POST"])
def create_categoria():
    data = request.get_json()
    nome = data.get("nome")
    if nome is None:
        return response("Error", "Nome obrigatório!", 400)
    
    if not isinstance(nome, str):
        return response("error", "Nome deve ser texto!", 400)
    
    categoria = criar_categoria(nome)
    if categoria is False:
        return response("error", "essa categoria já existe!", 400)

    return jsonify(categoria.to_dict()), 201

@categoria_bp.route("/<int:id>", methods=["DELETE"])
def delete_categoria(id:int):
    categoria = deletar_categoria(id)
    if categoria is None:
        return response("error", "Categoria não encontrada!", 400)
    
    return jsonify(categoria.to_dict()), 200
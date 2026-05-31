from flask import Blueprint, request, jsonify
from services.produto_service import criar_produto
from utils.response import response

produto_bp = Blueprint("produto", __name__, url_prefix="/produto")

@produto_bp.route("/", methods=["POST"])
def create_produto():
    data = request.get_json()
    nome = data.get("nome")
    descricao = data.get("descricao")
    preco = data.get("preco")
    estoque = data.get("estoque")
    categoria = data.get("categoria")

    if nome is None:
        return response("error", "nome obrigatorio!", 400)
    elif descricao is None:
        return response("error", "descricao obrigatorio!", 400)
    elif preco is None:
        return response("error", "preco obrigatorio!", 400)
    elif estoque is None:
        return response("error", "estoque obrigatorio!", 400)
    elif categoria is None:
        return response("error", "categoria obrigatorio!", 400)

    try:
        preco = float(preco)
    except (ValueError, TypeError):
        return response("error", "valor invalido!", 400)
    
    if preco <= 0:
        return response("error", "preco nao pode ser negativo!", 400)
    
    try:
        estoque = int(estoque)
    except (ValueError, TypeError):
        return response("error", "valor invalido!", 400)
    
    if estoque <= 0:
        return response("error", "estoque nao pode ser negativo!", 400)
    
    produto = criar_produto(
        nome=nome,
        descricao=descricao,
        preco=preco,
        estoque=estoque,
        id_categoria=categoria
    )
    if produto is False:
        return response("error", "categoria nao encontrada!", 400)

    return jsonify(produto.to_dict())
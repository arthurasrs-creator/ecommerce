from flask import Blueprint, request, jsonify
from utils.response import response
from services.pedido_service import criar_pedido
from enums.tipo_status import TipoStatusPedido


pedido_bp = Blueprint("pedido", __name__, url_prefix="/pedido")

@pedido_bp.route("/", methods=["POST"])
def create_pedido():
    data = request.get_json()
    cliente = data.get("cliente")
    status = data.get("status")
    produto = data.get("produto")
    quantidade = data.get("quantidade")
    if cliente is None:
        return response("error", "cliente obrigatorio!", 400)
    if status is None:
        status = TipoStatusPedido.PENDENTE
    if produto is None:
        return response("error", "produto obrigatorio!", 400)
    if quantidade is None:
        return response("error", "quantidade obrigatorio!", 400)
    pedido = criar_pedido(
        id_cliente=cliente,
        id_produto=produto,
        status=status,
        quantidade=quantidade
    )
    if pedido is None:
        return response("error", "Falha ao criar pedido", 400)
    if pedido is False:
        return response("error", "Falha ao criar pedido, estoque insuficiente", 400)

    return jsonify(pedido.to_dict())

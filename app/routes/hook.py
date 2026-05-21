from flask import Blueprint, render_template, flash
from flask import request, redirect, url_for, session, jsonify
from uuid import uuid4
# from App.routes.jwt_session import auth_require


payment_bp = Blueprint('payment', __name__, url_prefix="/payment")

@payment_bp.get('/abacatepay')
def check_abacatepay():
    # 1. Validação do Secret (recomendado)
    print(request.args)

    secret_param = request.args.get('webhookSecret')
    if secret_param != "WEBHOOK_SECRET":
        return jsonify({"error": "Unauthorized"}), 401

    return 'ok'
    # 2. Pega o corpo raw para validação HMAC (mais seguro)
    raw_body = request.get_data()
    signature = request.headers.get('X-Webhook-Signature')

    # Validação HMAC (opcional mas altamente recomendado)
    if signature and not verify_signature(raw_body, signature):
        return jsonify({"error": "Invalid signature"}), 401


@payment_bp.get('/success')
def success():
    produto = {
        "nome": "Curso Técnico em Segurança Cibernética",
        "descricao": "Curso completo com foco em segurança da informação, redes e defesa cibernética.",
        "preco": 249.90,
        "imagem": "https://via.placeholder.com/400x300.png?text=Produto",
        "codigo_pedido": "PED-2026-0001",
        "forma_pagamento": "Cartão de Crédito",
        "data_pagamento": "19/05/2026"
    }
    return render_template("payments/success.html", produto=produto)

@payment_bp.post('/cancel')
def cancel():
    return "Pagamento não efetuado!!"

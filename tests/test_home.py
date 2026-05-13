def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Site com pagamento do abacatepay" in response.data


def test_success_route_accepts_post(client):
    response = client.post("/success")

    assert response.status_code == 200
    assert b"Pagamento realizado com sucesso" in response.data


def test_cancel_route_accepts_post(client):
    response = client.post("/cancel")

    assert response.status_code == 200
    assert "Pagamento".encode() in response.data


def test_success_route_does_not_accept_get(client):
    response = client.get("/success")

    assert response.status_code == 405
    assert b"voltar" in response.data


def test_cancel_route_does_not_accept_get(client):
    response = client.get("/cancel")

    assert response.status_code == 405
    assert b"voltar" in response.data


def test_not_found_uses_global_error_handler(client):
    response = client.get("/rota-que-nao-existe")

    assert response.status_code == 404
    assert b"voltar" in response.data


def test_unhandled_exception_uses_global_error_handler(client):
    app = client.application

    @app.get("/rota-com-erro")
    def rota_com_erro():
        raise RuntimeError("erro proposital para teste")

    response = client.get("/rota-com-erro")

    assert response.status_code == 500
    assert b"voltar" in response.data

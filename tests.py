from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_notas_vazia():
    response = client.get("/todas-as-notas")
    assert response.json() == {}


def test_main_nota_nao_localizada_na_atualizacao():
    response = client.get("/nota/1")
    assert response.status_code == 404


def test_main_nota_nao_localizada_na_exclusao():
    response = client.get("/excluir-nota/1")
    assert response.status_code == 404


def test_main_inserir_nota():
    response = client.post("/nova-nota/{anotacao: Text}?anotacao=Nota%2001")
    assert response.json()["anotacao"] == "Nota 01"


def test_main_obter_uma_nota():
    response = client.post("/nova-nota/{anotacao: Text}?anotacao=Nota%2002")
    id_da_nota = response.json()["id"]
    response = client.get("obter-nota/{id: UUID}?id="+id_da_nota)
    assert response.json()["anotacao"] == "Nota 02"


def test_mains_obter_todas_as_notas():
    response = client.get("/todas-as-notas")
    assert len(response.json()) == 2


def test_atualizar_uma_nota():
    response = client.post("/nova-nota/{anotacao: Text}?anotacao=Nota%2002")
    id_da_nota = response.json()["id"]
    response = client.put("atualizar-nota/{id: UUID}?id="+id_da_nota+"&nova_anotacao=Nota%20Atualizada")
    assert response.json()["anotacao"] == "Nota Atualizada"


def test_main_excluir_uma_nota():
    response = client.post("/nova-nota/{anotacao: Text}?anotacao=Nota%2004")
    id_da_nota = response.json()["id"]
    client.delete("/excluir-nota/{id: UUID}?id="+id_da_nota)
    response = client.get("todas-as-notas")
    assert len(response.json()) == 3


def test_main_excluir_todas_as_notas():
    client.delete("/exluir-todas-as-notas")
    response = client.get("/todas-as-notas")
    assert response.json() == {}

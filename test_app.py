import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_status(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['status'] == 'online'
    assert dados['sistema'] == 'Sistema CPM'

def test_registrar_chamada_lote(client):
    payload = {
        "presencas": [
            {"aluno_id": 1, "presente": True},
            {"aluno_id": 2, "presente": True}
        ]
    }
    resposta = client.post('/chamada/lote', json=payload)
    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados['total'] == 2
    assert 'Presencas registradas' in dados['mensagem']

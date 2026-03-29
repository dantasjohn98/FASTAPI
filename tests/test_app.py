from http import HTTPStatus
from fastapi.testclient import TestClient

from fastapi_zero.app import app



def test_root_deve_retornar_ola_mundo():
    
    #esse teste tem 3 etapas (AAA):
    #Arrange: preparar o ambiente para o teste
    #Act: executar a ação que queremos testar
    #Assert: verificar se o resultado é o esperado

    #Arrange
    client = TestClient(app)
    #Act
    response = client.get('/')
    #Assert
    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK
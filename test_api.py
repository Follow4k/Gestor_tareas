import pytest
from fastapi.testclient import TestClient

import api


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    base_de_prueba = tmp_path / "test.db"
    monkeypatch.setattr(api, "DB", str(base_de_prueba))
    api.crear_tabla()
    return TestClient(api.app)


def test_inicio_responde_200(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"mensaje": "Hola, mi gestor de tareas esta funcionando"}


def test_ruta_inexistente_responde_404(cliente):
    respuesta = cliente.get("/una-ruta-que-no-existe")

    assert respuesta.status_code == 404


def test_lista_vacia_al_principio(cliente):
    respuesta = cliente.get("/tareas")

    assert respuesta.status_code == 200
    assert respuesta.json() == []


def test_crear_tarea_responde_201(cliente):
    respuesta = cliente.post("/tareas", json={"descripcion": "comprar pan"})

    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["descripcion"] == "comprar pan"
    assert datos["hecha"] == 0


def test_crear_tarea_vacia_es_rechazada(cliente):
    respuesta = cliente.post("/tareas", json={"descripcion": ""})

    assert respuesta.status_code == 422 


def test_crear_tarea_muy_larga_es_rechazada(cliente):
    respuesta = cliente.post("/tareas", json={"descripcion": "a" * 101})

    assert respuesta.status_code == 422


def test_crear_tarea_solo_espacios_es_rechazada(cliente):
    respuesta = cliente.post("/tareas", json={"descripcion": "   "})

    assert respuesta.status_code == 422


def test_crear_tarea_sin_espacios_responde_201(cliente):
    respuesta = cliente.post("/tareas", json={"descripcion": "        comprar pan       "})

    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["descripcion"] == "comprar pan"
    assert datos["hecha"] == 0

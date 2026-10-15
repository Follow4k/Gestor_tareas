import sqlite3

from fastapi import FastAPI, HTTPException #HTTP devuelve errores (404, 500,etc)
from pydantic import BaseModel

app = FastAPI()

DB = "tareas.db"


#Modelo: que datos tiene que mandar quien crea una tarea
class TareaNueva(BaseModel):
    descripcion: str


#Funciones auxiliares (para no repetir codigo)
def conectar():
    return sqlite3.connect(DB)


def fila_a_dict(fila):
    #Convierte una tupla como (1, "Comprar pan", 0) en un diccionario con claves
    return {"id": fila[0], "descripcion": fila[1], "hecha": fila[2]}


#Endpoints
@app.get("/")
def inicio():
    return {"mensaje": "Hola, mi gestor de tareas esta funcionando"}


@app.get("/tareas")
def listar_tareas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    filas = cursor.fetchall()
    conexion.close()

    tareas = []
    for fila in filas:
        tareas.append(fila_a_dict(fila))
    return tareas


@app.post("/tareas", status_code=201)
def agregar_tarea(tarea: TareaNueva):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO tareas (descripcion, hecha) VALUES (?, ?)",
        (tarea.descripcion, 0),
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid  #id que SQLite le asigno a la fila nueva
    conexion.close()
    return {"id": nuevo_id, "descripcion": tarea.descripcion, "hecha": 0}


@app.put("/tareas/{id}/hecha")
def marcar_hecha(id: int):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE tareas SET hecha = 1 WHERE id = ?", (id,))
    conexion.commit()
    modificadas = cursor.rowcount  #filas que cambio el UPDATE
    conexion.close()

    if modificadas == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea marcada como hecha"}


@app.delete("/tareas/{id}")
def borrar_tarea(id: int):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conexion.commit()
    borradas = cursor.rowcount  #filas  que borro el DELETE
    conexion.close()

    if borradas == 0:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea borrada"}
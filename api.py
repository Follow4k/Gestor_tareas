import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get("/tareas")
def listar_tareas():
    conexion = sqlite3.connect("tareas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    resultados = cursor.fetchall()

    tareas = []
    for fila in resultados:
        tarea = {"id": fila[0], "descripcion": fila[1], "hecha": fila[2]}
        tareas.append(tarea)
    return tareas


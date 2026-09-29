import sqlite3

conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas(
id INTEGER PRIMARY KEY,
descripcion TEXT,
hecha INTEGER
)
""")
conexion.commit()

# cursor.execute(
#     "INSERT INTO tareas (descripcion, hecha) VALUES (?, ?)", ("Tomar 2 litros de agua", 0))

# conexion.commit()

cursor.execute("SELECT * FROM tareas")
resultados = cursor.fetchall()
print(resultados)

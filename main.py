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

# cursor.execute("SELECT * FROM tareas")
# resultados = cursor.fetchall()
# print(resultados)


def agregar_tarea(tarea):
    cursor.execute(
        "INSERT INTO tareas (descripcion, hecha) VALUES (?, ?)", (tarea, 0))
    conexion.commit()

#Actualizado x2
# agregar_tarea("Comprar pan")

def ver_tareas():
    cursor.execute(
        "SELECT * FROM tareas")
    resultados = cursor.fetchall()
    print(resultados)
#Hacer mas prolijo el print de ver_tareas

# ver_tareas()


def marcar_hecha(id):
    cursor.execute("UPDATE tareas SET hecha = 1 WHERE id = ?", (id,))
    conexion.commit()


# marcar_hecha(2)


def borrar_tarea(id):
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conexion.commit()


# borrar_tarea(1)

x = ""
while x != "salir":
    print("1. Agregar tareas", "2. Ver tareas",
          "3. Marcar como hecha", "4. Borrar tarea", "5. Salir")
    x = input("Que necesita hacer? ")

    if x.lower() == "salir":
        break
    elif x == "1":
        y = input("Que tarea le gustaria agregar: ")
        agregar_tarea(y)
    elif x == "2":
        ver_tareas()
    elif x == "3":
        l = int(input("Que tarea quiere marcar como hecha: "))
        marcar_hecha(l)
    elif x == "4":
        d = int(input("Que tarea borramos? "))
        borrar_tarea(d)
    else:
        print("Esa no es una tarea")

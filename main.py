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

def agregar_tarea(tarea):
    cursor.execute(
        "INSERT INTO tareas (descripcion, hecha) VALUES (?, ?)", (tarea, 0))
    conexion.commit()


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
    return cursor.rowcount


# marcar_hecha(2)

def borrar_tarea(id):
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conexion.commit()
    return cursor.rowcount

# borrar_tarea(1)

while True:
    print("1. Agregar tareas", "2. Ver tareas",
          "3. Marcar como hecha", "4. Borrar tarea", "5. Salir")
    x = input("Que necesita hacer? ")

    if x == "5" or x.lower() == "salir":
        break
    elif x == "1":
        y = input("Que tarea le gustaria agregar: ").strip()
        if y == "":
            print("La tarea no puede estar vacia")
        else:            
            agregar_tarea(y)
            print("Se agrego la tarea")
    elif x == "2":
        ver_tareas()
    elif x == "3":
        try:
            id_tareas = int(input("Que tarea quiere marcar como hecha: "))
            modificadas = marcar_hecha(id_tareas)
            if modificadas == 0:
                print("La tarea no existe")
            else:
                print("Se marco bien")
        except ValueError:
            print("Eso no es un numero")        
    elif x == "4":
        try:
            d = int(input("Que tarea borramos? "))
            modificadas = borrar_tarea(d)
            if modificadas == 0:
                print("La tarea no existe")
            else:
                print("Se borro bien")
        except ValueError:
            print("Eso no es un numero")
    else:
        print("Esa no es una tarea")

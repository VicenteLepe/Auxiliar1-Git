class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
<<<<<<< HEAD
    
    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
                print(f"[ ] {tarea.obtenerNombre()}" )
=======
>>>>>>> 07dcd9bac5e97ebc30c747d4b337950bab12db34

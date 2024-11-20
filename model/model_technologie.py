from alchemyClasses.technologie import Technologie
from alchemyClasses import db



# Crear una tecnología
def crear_technologie(nombre, sector, descripcion, estadoAdopcion):
    nueva_technologie = Technologie(
        nombre=nombre,
        sector=sector,
        descripcion=descripcion,
        estadoAdopcion=estadoAdopcion
    )
    try:
        db.session.add(nueva_technologie)
        db.session.commit()
        return 0
    except Exception as e:
        print(f"Error al crear la tecnología: {e}")
        return -1


# Leer todas las tecnologías
def leer_technologies():
    try:
        return Technologie.query.all()
    except Exception as e:
        print(f"Error al leer las tecnologías: {e}")
        return []

# Buscar tecnologías por nombre
def buscar_por_nombre_technologie(nombre):
    try:
        return Technologie.query.filter(Technologie.nombre.ilike(f"%{nombre}%")).all()
    except Exception as e:
        print(f"Error al buscar por nombre: {e}")
        return []

# Buscar tecnologías por sector
def buscar_por_sector(sector):
    try:
        return Technologie.query.filter(Technologie.sector.ilike(f"%{sector}%")).all()
    except Exception as e:
        print(f"Error al buscar por sector: {e}")
        return []

# Buscar tecnologías por descripción
def buscar_por_descripcion(descripcion):
    try:
        return Technologie.query.filter(Technologie.descripcion.ilike(f"%{descripcion}%")).all()
    except Exception as e:
        print(f"Error al buscar por descripción: {e}")
        return []

# Buscar tecnologías por estado de adopción
def buscar_por_estado_adopcion(estadoAdopcion):
    try:
        return Technologie.query.filter(Technologie.estadoAdopcion.ilike(f"%{estadoAdopcion}%")).all()
    except Exception as e:
        print(f"Error al buscar por estado de adopción: {e}")
        return []


# Leer una tecnología por su ID
def leer_technologie_por_id(id_technologie):
    try:
        return Technologie.query.get(id_technologie)
    except Exception as e:
        print(f"Error al leer la tecnología con ID {id_technologie}: {e}")
        return None


# Actualizar una tecnología por su ID
def actualizar_technologie(id_technologie, descripcion=None, estadoAdopcion=None):
    technologie = Technologie.query.get(id_technologie)
    if technologie is None:
        return -1
    else:
        if descripcion:
            technologie.descripcion = descripcion
        if estadoAdopcion:
            technologie.estadoAdopcion = estadoAdopcion
        try:
            db.session.commit()
            return 0
        except Exception as e:
            print(f"Error al actualizar la tecnología: {e}")
            return -1


# Eliminar una tecnología por su ID
def eliminar_technologie(id_technologie=None):
    if id_technologie is None:
        # Elimina todas las tecnologías
        try:
            Technologie.query.delete()
            db.session.commit()
            return 0
        except Exception as e:
            print(f"Error al eliminar todas las tecnologías: {e}")
            return -1
    else:
        technologie = leer_technologie_por_id(id_technologie)
        if technologie is not None:
            try:
                db.session.delete(technologie)
                db.session.commit()
                return 0
            except Exception as e:
                print(f"Error al eliminar la tecnología: {e}")
                return -1
        else:
            return -1


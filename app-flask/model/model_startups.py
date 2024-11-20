from alchemyClasses.startup import Startup
from alchemyClasses import db

# Crear una startup
def crear_startup(nombre, fechaFundacion, ubicacion, categoria, inversionRecibida):
    nueva_startup = Startup(
        nombre=nombre,
        fechaFundacion=fechaFundacion,
        ubicacion=ubicacion,
        categoria=categoria,
        inversionRecibida=inversionRecibida
    )
    try:
        db.session.add(nueva_startup)
        db.session.commit()
        return 0
    except Exception as e:
        print(f"Error al crear la startup: {e}")
        return -1

# Leer todas las startups
def leer_startups():
    return Startup.query.all()

# Leer una startup por su ID
def leer_startup_por_id(id_startup):
    return Startup.query.get(id_startup)
    
# Buscar startups por nombre
def buscar_por_nombre(nombre):
    try:
        return Startup.query.filter(Startup.nombre.ilike(f"%{nombre}%")).all()
    except Exception as e:
        print(f"Error al buscar por nombre: {e}")
        return []

# Buscar startups por ubicación
def buscar_por_ubicacion(ubicacion):
    try:
        return Startup.query.filter(Startup.ubicacion.ilike(f"%{ubicacion}%")).all()
    except Exception as e:
        print(f"Error al buscar por ubicación: {e}")
        return []

# Buscar startups por categoría
def buscar_por_categoria(categoria):
    try:
        return Startup.query.filter(Startup.categoria.ilike(f"%{categoria}%")).all()
    except Exception as e:
        print(f"Error al buscar por categoría: {e}")
        return []


# Actualizar una startup por su ID
def actualizar_startup(id_startup, ubicacion=None,inversionRecibida=None):
    startup = Startup.query.get(id_startup)
    if startup is None:
        return -1
    else:
        if ubicacion:
            startup.ubicacion = ubicacion
        if inversionRecibida is not None and float(inversionRecibida) > float(startup.inversionRecibida):
            startup.inversionRecibida = inversionRecibida
        try:
            db.session.commit()
            return 0
        except Exception as e:
            print(f"Error al actualizar la startup: {e}")
            return -1

# Eliminar una startup por su ID
def eliminar_startup(id_startup=None):
    if id_startup is None:
        # Elimina todas las startups
        try:
            Startup.query.delete()
            db.session.commit()
            return 0
        except Exception as e:
            print(f"Error al eliminar todas las startups: {e}")
            return -1
    else:
        startup = leer_startup_por_id(id_startup)
        if startup is not None:
            try:
                db.session.delete(startup)
                db.session.commit()
                return 0
            except Exception as e:
                print(f"Error al eliminar la startup: {e}")
                return -1
        else:
            return -1
            
 


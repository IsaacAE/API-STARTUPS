from flask import Blueprint, request, jsonify
from model import model_technologie as mt


technologie_blueprint = Blueprint('technologies', __name__, url_prefix='/api/technologies')

# Obtener todas las tecnologías
@technologie_blueprint.route('/read', methods=['GET'])
def ReadTechnologyService():
    technologies = mt.leer_technologies()
    technologies_json = [
        {
            "idTechnologie": technology.idTechnologie,
            "nombre": technology.nombre,
            "sector": technology.sector,
            "descripcion": technology.descripcion,
            "estadoAdopcion": technology.estadoAdopcion
        }
        for technology in technologies
    ]
    return jsonify(technologies_json), 200

# Obtener una tecnología por ID
@technologie_blueprint.route('/read/<int:idTechnologie>', methods=['GET'])
def ReadTechnologyByIdService(idTechnologie):
    technology = mt.leer_technologie_por_id(idTechnologie)
    if technology is None:
        return jsonify({"error": "Tecnología no encontrada"}), 404
    technology_json = {
        "idTechnologie": technology.idTechnologie,
        "nombre": technology.nombre,
        "sector": technology.sector,
        "descripcion": technology.descripcion,
        "estadoAdopcion": technology.estadoAdopcion
    }
    return jsonify(technology_json), 200

 #Búsqueda por nombre
@technologie_blueprint.route('/read/name/<string:nombre>', methods=['GET'])
def buscar_por_nombre_technologie(nombre):
    resultados = mt.buscar_por_nombre_technologie(nombre)
    tech_json = [{"idTechnologie": t.idTechnologie, "nombre": t.nombre} for t in resultados]
    return jsonify(tech_json), 200

# Búsqueda por sector
@technologie_blueprint.route('/read/sector/<string:sector>', methods=['GET'])
def buscar_por_sector(sector):
    resultados = mt.buscar_por_sector(sector)
    tech_json = [{"idTechnologie": t.idTechnologie, "sector": t.sector} for t in resultados]
    return jsonify(tech_json), 200

# Búsqueda por descripción
@technologie_blueprint.route('/read/description/<string:descripcion>', methods=['GET'])
def buscar_por_descripcion(descripcion):
    resultados = mt.buscar_por_descripcion(descripcion)
    tech_json = [{"idTechnologie": t.idTechnologie, "descripcion": t.descripcion} for t in resultados]
    return jsonify(tech_json), 200

# Búsqueda por estado de adopción
@technologie_blueprint.route('/read/adoption-state/<string:estadoAdopcion>', methods=['GET'])
def buscar_por_estado_adopcion(estadoAdopcion):
    resultados = mt.buscar_por_estado_adopcion(estadoAdopcion)
    tech_json = [{"idTechnologie": t.idTechnologie, "estadoAdopcion": t.estadoAdopcion} for t in resultados]
    return jsonify(tech_json), 200

# Crear una nueva tecnología
@technologie_blueprint.route('/create', methods=['POST'])
def CreateTechnologyService():
    data = request.get_json()
    nombre = data.get("nombre")
    sector = data.get("sector")
    descripcion = data.get("descripcion")
    estadoAdopcion = data.get("estadoAdopcion")

    if not nombre or not sector or not descripcion or not estadoAdopcion:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    retorno = mt.crear_technologie(nombre, sector, descripcion, estadoAdopcion)

    if retorno == -1:
        return jsonify({"error": "Error al crear la tecnología"}), 500
    return jsonify({"message": "Tecnología creada con éxito"}), 201

# Actualizar una tecnología por ID
@technologie_blueprint.route('/update/<int:idTechnologie>', methods=['PUT'])
def UpdateTechnologyService(idTechnologie):
    data = request.get_json()
    descripcion = data.get("descripcion")
    estadoAdopcion = data.get("estadoAdopcion")

    retorno = mt.actualizar_technologie(idTechnologie, descripcion, estadoAdopcion)

    if retorno == -1:
        return jsonify({"error": "Tecnología no encontrada o error al actualizar"}), 404
    return jsonify({"message": "Tecnología actualizada con éxito"}), 200

# Eliminar una tecnología por ID
@technologie_blueprint.route('/delete/<int:idTechnologie>', methods=['DELETE'])
def DeleteTechnologyService(idTechnologie):
    retorno = mt.eliminar_technologie(idTechnologie)

    if retorno == -1:
        return jsonify({"error": "Tecnología no encontrada o error al eliminar"}), 404
    return jsonify({"message": "Tecnología eliminada con éxito"}), 200



from flask import Blueprint, request, jsonify
from model import model_startups as ms

startup_blueprint = Blueprint('startup', __name__, url_prefix='/api/startups')

# Obtener todas las startups
@startup_blueprint.route('/read', methods=['GET'])
def ReadStartupService():
    startups = ms.leer_startups()
    startups_json = [
        {
            "idStartup": startup.idStartup,
            "nombre": startup.nombre,
            "fechaFundacion": str(startup.fechaFundacion),
            "ubicacion": startup.ubicacion,
            "categoria": startup.categoria,
            "inversionRecibida": startup.inversionRecibida
        }
        for startup in startups
    ]
    return jsonify(startups_json), 200

# Obtener una startup por ID
@startup_blueprint.route('/read/<int:idStartup>', methods=['GET'])
def obtener_startup_por_id(idStartup):
    startup = ms.leer_startup_por_id(idStartup)
    if startup is None:
        return jsonify({"error": "Startup no encontrada"}), 404
    startup_json = {
        "idStartup": startup.idStartup,
        "nombre": startup.nombre,
        "fechaFundacion": str(startup.fechaFundacion),
        "ubicacion": startup.ubicacion,
        "categoria": startup.categoria,
        "inversionRecibida": startup.inversionRecibida
    }
    return jsonify(startup_json), 200

# Crear una nueva startup
@startup_blueprint.route('/create', methods=['POST'])
def CreateStartupService():
    data = request.get_json()
    nombre = data.get("nombre")
    fechaFundacion = data.get("fechaFundacion")
    ubicacion = data.get("ubicacion")
    categoria = data.get("categoria")
    inversionRecibida = data.get("inversionRecibida", 0.0)

    if not nombre or not fechaFundacion or not ubicacion or not categoria:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    retorno = ms.crear_startup(nombre, fechaFundacion, ubicacion, categoria, inversionRecibida)

    if retorno == -1:
        return jsonify({"error": "Error al crear la startup"}), 500
    return jsonify({"message": "Startup creada con éxito"}), 201

# Actualizar una startup por ID
@startup_blueprint.route('/update/<int:idStartup>', methods=['PUT'])
def UpdateStartupService(idStartup):
    data = request.get_json()
    ubicacion = data.get("ubicacion")
    inversionRecibida = data.get("inversionRecibida")

    retorno = ms.actualizar_startup(idStartup, ubicacion, inversionRecibida)

    if retorno == -1:
        return jsonify({"error": "Startup no encontrada o error al actualizar"}), 404
    return jsonify({"message": "Startup actualizada con éxito"}), 200

# Eliminar una startup por ID
@startup_blueprint.route('/delete/<int:idStartup>', methods=['DELETE'])
def DeleteStartupService(idStartup):
    retorno = ms.eliminar_startup(idStartup)

    if retorno == -1:
        return jsonify({"error": "Startup no encontrada o error al eliminar"}), 404
    return jsonify({"message": "Startup eliminada con éxito"}), 200



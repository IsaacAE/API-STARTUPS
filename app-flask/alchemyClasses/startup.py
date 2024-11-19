from sqlalchemy import Column, Integer, String, Date, Float
from alchemyClasses import db

class Startup(db.Model):
    __tablename__ ='Startups'
    idStartup = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(50),nullable = False)
    fechaFundacion = Column(Date,nullable = False)
    ubicacion = Column(String(50),nullable = False)
    categoria = Column(String(50),nullable = False)
    inversionRecibida = Column(Float,nullable = False)
    
    
    def __init__(self, nombre, fechaFundacion, ubicacion, categoria, inversionRecibida):
        self.nombre = nombre
        self.fechaFundacion = fechaFundacion
        self.ubicacion = ubicacion
        self.categoria = categoria
        self.inversionRecibida = inversionRecibida

    def __str__(self):
        return (
            f"<Startup(id_startup={self.id_startup}, nombre='{self.nombre}', "
            f"fechaFundacion={self.fechaFundacion}, ubicacion='{self.ubicacion}', "
            f"categoria='{self.categoria}', inversionRecibida={self.inversionRecibida})>"
        )

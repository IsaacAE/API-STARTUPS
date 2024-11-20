from sqlalchemy import Column, Integer, DateTime, SmallInteger, ForeignKey, CheckConstraint , String
from alchemyClasses import db

class Technologie(db.Model):
    
    __tablename__ = 'Technologies'
    idTechnologie = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(50),nullable = False)
    sector = Column(String(30),nullable = False)
    descripcion = Column(String(150),nullable = False)
    estadoAdopcion = Column(String(50),nullable = False)
    
    def __init__(self, nombre, sector, descripcion, estadoAdopcion):
        self.nombre = nombre
        self.sector = sector
        self.descripcion = descripcion
        self.estadoAdopcion = estadoAdopcion

    def __str__(self):
        return (f"<Technology(idTechnologie={self.idTechnologie}, nombre='{self.nombre}', "
                f"sector='{self.sector}', descripcion='{self.descripcion}', "
                f"estadoAdopcion='{self.estadoAdopcion}')>")

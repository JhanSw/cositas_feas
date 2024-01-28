'''
En este script se tendrán dos tablas, la tabla de  estado para colocar SI, NO, y NO APLICA y la de
criterios de aceptabilidad 
'''
from sqlalchemy import Table, Column, ForeignKey   
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

estados = Table("estado", meta_data,
                Column("id", Integer, primary_key=True),
                Column("nombre_estado", String(255), nullable=False))


criterios_aceptabilidad = Table("criterios_aceptabilidad", meta_data,
              Column("id", Integer, primary_key=True),
              Column("id_estado", Integer, ForeignKey("estado.id"), nullable=False),
              Column("nombre", String(255), nullable=False))

meta_data.create_all(engine)

from sqlalchemy import Table, Column, ForeignKey   
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

documento = Table("documento", meta_data,
                Column("id", Integer, primary_key=True),
                Column("nombre", String(255), nullable=False),
                Column("descripcion", String(255), nullable=False),
                Column("ruta", String(1024), nullable=False))

meta_data.create_all(engine)
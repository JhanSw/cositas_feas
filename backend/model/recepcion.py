
from sqlalchemy import Table, Column, ForeignKey  
from sqlalchemy.sql.sqltypes import Integer, String, Date, Time
from config.db import engine, meta_data



recepcion = Table("recepcion", meta_data,
              Column("id", Integer, primary_key=True),
              Column("id_cliente", Integer, ForeignKey("cliente.id"), nullable=False),
              Column("id_documento", Integer, ForeignKey("documento.id"), nullable=False),
              Column("id_criterios_aceptabilidad", Integer, ForeignKey("criterios_aceptabilidad.id"), nullable=False),
              Column("id_inspeccion", Integer, ForeignKey("inspeccion.id"), nullable=False),
              Column("guia", String(255), nullable=False),
              Column("nombre_entrega", String(255), nullable=False),
              Column("remitente", String(255), nullable=False),
              Column("fecha_entrega", Date, nullable=False),
              Column("medio", String(255), nullable=False),
              Column("embalaje", String(255), nullable=False),
              Column("fecha_envio", Date, nullable=False),
              Column("fecha_recepcion", Date, nullable=False),
              Column("hora", Time, nullable=False),
              Column("consecutivo", String(255), nullable=False),
              Column("fecha_documento", Date, nullable=False),
              Column("hora_documento", Time, nullable=False),
              Column("orden_trabajo", Integer, nullable=False),
              Column("observacion_criterios_aceptabilidad", String(1024), nullable=False),
              Column("observacion_parametros_inspeccion", String(1024), nullable=False))
                          
meta_data.create_all(engine)

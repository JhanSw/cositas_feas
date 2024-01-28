from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class UserSchema(BaseModel):
    id: Optional[str]
    nombre_usuario: str
    numero_doc_usuario: int
    usuario: str
    contrasenia_usuario: str

class DataUser(BaseModel):
    usuario: str
    contrasenia_usuario: str

class ClienteSchema(BaseModel):
    id: Optional[str]
    cliente: str
    nit:str
    solicitante: str
    cargo: str
    direccion: str
    municipio: str
    telefono: str
    fax: str
    consecutivo: str
    observaciones: str

class DocumentoSchema(BaseModel):
    id: Optional[int]
    nombre: str
    descripcion: str
    ruta: str

class RecepcionSchema(BaseModel):
    id: Optional[int]
    id_cliente: int
    id_inspeccion: int
    id_documento: int
    id_criterios_aceptabilidad: int
    guia: str
    nombre_entrega: str
    remitente: str
    fecha_entrega: date
    medio: str
    embalaje: str
    fecha_envio: date
    fecha_recepcion: date
    hora: time
    consecutivo: str
    fecha_documento: date
    hora_documento: time
    orden_trabajo: int
    observacion_criterios_aceptabilidad: str
    observacion_parametros_inspeccion: str

class InspeccionSchema(BaseModel):
    id: Optional[int]
    #id_aceptacion: int 
    analisis_o_ensayo: str
    analista_s: str
    equipo_usado: str
    preparacion_muestra: str
    muestra_o_matriz: bool
    observaciones: str
    aceptacion_muestra: bool
    motivo_rechazo: str
    fecha_rechazo: date
    respuesta_cliente: str
    fecha_respuesta: date
    comentario: str
    #observacion_criterios_aceptabilidad: str
'''
class DatosEntregaSchema(BaseModel):
    id: Optional[int]
    transportadora: str
    guia: str
    fecha_envio: str
    remitente: str
    nombre: str
    fecha: str
    remitente_personal: str
    descripcion: str
    cantidad_de_muestra: bool
    preservacion: bool
    empaque: bool
    embalaje: bool
    identificacion: bool
    observaciones: str
'''
class EstadoSchema(BaseModel):
    id: Optional[int]
    nombre_estado: str

class CriteriosAceptabilidadSchema(BaseModel):
    id: Optional[int]
    id_estado: int
    nombre: str
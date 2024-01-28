from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser, ClienteSchema, EstadoSchema, CriteriosAceptabilidadSchema, DocumentoSchema, InspeccionSchema, RecepcionSchema
from config.db import engine
from model.users import users
from model.clientes import cliente
from model.criterios_aceptacion import estados, criterios_aceptabilidad
from model.documento import documento
from model.inspeccion import inspeccion
from model.recepcion import recepcion
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from datetime import date


 
cliente_router = APIRouter()
user = APIRouter()
estado_router = APIRouter()
criterios_aceptabilidad_router = APIRouter()
documento_router = APIRouter()
inspeccion_router = APIRouter()
recepcion_router = APIRouter()


@user.get("/")
def root():
    return {"message": "Hello :D"}

#Estos son las rutas de usuario.

@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        
        user_objects = [UserSchema(
            id=row.id,
            nombre_usuario=row.nombre_usuario,
            numero_doc_usuario=row.numero_doc_usuario,
            usuario=row.usuario,
            contrasenia_usuario=row.contrasenia_usuario
        ) for row in result]
        
        return user_objects
    
@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        if result:
            user_dict = {
                "id": result.id,
                "nombre_usuario": result.nombre_usuario,
                "numero_doc_usuario": result.numero_doc_usuario,
                "usuario": result.usuario,
                "contrasenia_usuario": result.contrasenia_usuario
            }
            return user_dict
        else:
            raise HTTPException(status_code=404, detail="User not found")


@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
 with engine.connect() as conn: #Es la conexión con la base de datos y solo está abierta cuando se usa
    new_user = data_user.dict()
    new_user["contrasenia_usuario"] = generate_password_hash(data_user.contrasenia_usuario, "pbkdf2:sha256:30", 15)
 
    conn.execute(users.insert().values(new_user))
    conn.commit()

    return Response(status_code=HTTP_201_CREATED)
 
@user.post("/api/user/login", status_code=200)
def login_user(data_user: DataUser):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.usuario == data_user.usuario)).first()
        
        if result != None:
            
            check_passw = check_password_hash(result[4], data_user.contrasenia_usuario)
            
            if check_passw:
                return {
                    "status" : 200,
                    "message": "Si perro, metiste bien los datos"
                }
        return {
            "status" : HTTP_401_UNAUTHORIZED,
            "message": "No perro, metiste mal los datos"
        }
          

@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update: UserSchema, user_id: str):
    with engine.connect() as conn:
        encryp_passw = generate_password_hash(data_update.contrasenia_usuario, "pbkdf2:sha256:30", 15)
        conn.execute(
            users.update()
            .values(
                nombre_usuario=data_update.nombre_usuario,
                numero_doc_usuario=data_update.numero_doc_usuario,
                usuario=data_update.usuario,
                contrasenia_usuario=encryp_passw
            )
            .where(users.c.id == user_id)
        )
        conn.commit()
        
        updated_user = conn.execute(users.select().where(users.c.id == user_id)).first()
        if updated_user:
            updated_user_dict = {
                "id": updated_user.id,
                "nombre_usuario": updated_user.nombre_usuario,
                "numero_doc_usuario": updated_user.numero_doc_usuario,
                "usuario": updated_user.usuario,
                "contrasenia_usuario": updated_user.contrasenia_usuario
            }
            return updated_user_dict
        else:
            raise HTTPException(status_code=404, detail="User not found")

@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)


#Acá empiezan las rutas de cliente

@cliente_router.get("/api/cliente", response_model=List[ClienteSchema])
def get_clientes():
    with engine.connect() as conn:
        result = conn.execute(cliente.select()).fetchall()

        cliente_objects = [ClienteSchema(
            id=row.id,
            cliente=row.cliente,
            nit=row.nit,
            solicitante=row.solicitante,
            cargo=row.cargo,
            direccion=row.direccion,
            municipio=row.municipio,
            telefono=row.telefono,
            fax=row.fax,
            consecutivo=row.consecutivo,
            observaciones=row.observaciones
        ) for row in result]

        return cliente_objects
    
@cliente_router.get("/api/cliente/{cliente_id}", response_model=ClienteSchema)
def get_cliente(cliente_id: str):
    with engine.connect() as conn:
        result = conn.execute(cliente.select().where(cliente.c.id == cliente_id)).first()

        if result:
            cliente_dict = {
                "id": result.id,
                "cliente": result.cliente,
                "nit": result.nit,
                "solicitante": result.solicitante,
                "cargo": result.cargo,
                "direccion": result.direccion,
                "municipio": result.municipio,
                "telefono": result.telefono,
                "fax": result.fax,
                "consecutivo": result.consecutivo,
                "observaciones": result.observaciones
            }
            return cliente_dict
        else:
            raise HTTPException(status_code=404, detail="User not found")


@cliente_router.post("/api/cliente", status_code=HTTP_201_CREATED)
def create_cliente(data_cliente: ClienteSchema):
 with engine.connect() as conn: #Es la conexión con la base de datos y solo está abierta cuando se usa
    new_cliente = data_cliente.dict()
    conn.execute(cliente.insert().values(new_cliente))
    conn.commit()

    return Response(status_code=HTTP_201_CREATED)
 

@cliente_router.put("/api/cliente/{cliente_id}", response_model=ClienteSchema)
def update_cliente(data_update: ClienteSchema, cliente_id: str):
    with engine.connect() as conn:
        conn.execute(
            cliente.update()
            .values(
                cliente=data_update.cliente,
                nit=data_update.nit,
                solicitante=data_update.solicitante,
                cargo=data_update.cargo,
                direccion=data_update.direccion,
                municipio=data_update.municipio,
                telefono=data_update.telefono,
                fax=data_update.fax,
                consecutivo=data_update.consecutivo,
                observaciones=data_update.observaciones
            )
            .where(cliente.c.id == cliente_id)
        )
        conn.commit()
        
        updated_cliente = conn.execute(cliente.select().where(cliente.c.id == cliente_id)).first()
        if updated_cliente:
            updated_cliente_dict = {
                "id": updated_cliente.id,
                "cliente": updated_cliente.cliente,
                "nit": updated_cliente.nit,
                "solicitante": updated_cliente.solicitante,
                "cargo": updated_cliente.cargo,
                "direccion": updated_cliente.direccion,
                "municipio": updated_cliente.municipio,
                "telefono": updated_cliente.telefono,
                "fax": updated_cliente.fax,
                "consecutivo": updated_cliente.consecutivo,
                "observaciones": updated_cliente.observaciones
            }
            return updated_cliente_dict
        else:
            raise HTTPException(status_code=404, detail="Client not found")

@cliente_router.delete("/api/cliente/{cliente_id}", status_code=HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: str):
    with engine.connect() as conn:
        conn.execute(cliente.delete().where(cliente.c.id == cliente_id))
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)

#Acá empiezan las rutas e la recepción de muestras.

# CRUD para la tabla 'estado'

@estado_router.get("/api/estado", response_model=List[EstadoSchema])
def get_estados():
    with engine.connect() as conn:
        result = conn.execute(select(estados)).fetchall()

        estados_objects = [EstadoSchema(
            id=row.id,
            nombre_estado=row.nombre_estado
        ) for row in result]

        return estados_objects

@estado_router.get("/api/estado/{estado_id}", response_model=EstadoSchema)
def get_estado(estado_id: str):
    with engine.connect() as conn:
        result = conn.execute(select(estados).where(estados.c.id == estado_id)).first()

        if result:
            estado_dict = {
                "id": result.id,
                "nombre_estado": result.nombre_estado
            }
            return estado_dict
        else:
            raise HTTPException(status_code=404, detail="Estado not found")

@estado_router.post("/api/estado", status_code=HTTP_201_CREATED)
def create_estado(data_estado: EstadoSchema):
    with engine.connect() as conn:
        new_estado = data_estado.dict()
        conn.execute(estados.insert().values(new_estado))
        conn.commit()

    return Response(status_code=HTTP_201_CREATED)

@estado_router.put("/api/estado/{estado_id}", response_model=EstadoSchema)
def update_estado(data_update: EstadoSchema, estado_id: str):
    with engine.connect() as conn:
        conn.execute(
            estados.update()
            .values(nombre_estado=data_update.nombre_estado)
            .where(estados.c.id == estado_id)
        )
        conn.commit()

        updated_estado = conn.execute(select(estados).where(estados.c.id == estado_id)).first()
        if updated_estado:
            updated_estado_dict = {
                "id": updated_estado.id,
                "nombre_estado": updated_estado.nombre_estado
            }
            return updated_estado_dict
        else:
            raise HTTPException(status_code=404, detail="Estado not found")

@estado_router.delete("/api/estado/{estado_id}", status_code=HTTP_204_NO_CONTENT)
def delete_estado(estado_id: str):
    with engine.connect() as conn:
        conn.execute(estados.delete().where(estados.c.id == estado_id))
        conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# CRUD para la tabla 'criterios_aceptabilidad'

@criterios_aceptabilidad_router.get("/api/criterios_aceptabilidad", response_model=List[CriteriosAceptabilidadSchema])
def get_criterios_aceptabilidad():
    with engine.connect() as conn:
        result = conn.execute(select(criterios_aceptabilidad)).fetchall()

        criterios_aceptabilidad_objects = [CriteriosAceptabilidadSchema(
            id=row.id,
            id_estado=row.id_estado,
            nombre=row.nombre
        ) for row in result]

        return criterios_aceptabilidad_objects

@criterios_aceptabilidad_router.get("/api/criterios_aceptabilidad/{criterio_id}", response_model=CriteriosAceptabilidadSchema)
def get_criterio_aceptabilidad(criterio_id: str):
    with engine.connect() as conn:
        result = conn.execute(select(criterios_aceptabilidad).where(criterios_aceptabilidad.c.id == criterio_id)).first()

        if result:
            criterio_aceptabilidad_dict = {
                "id": result.id,
                "id_estado": result.id_estado,
                "nombre": result.nombre
            }
            return criterio_aceptabilidad_dict
        else:
            raise HTTPException(status_code=404, detail="Criterio Aceptabilidad not found")

@criterios_aceptabilidad_router.post("/api/criterios_aceptabilidad", status_code=HTTP_201_CREATED)
def create_criterio_aceptabilidad(data_criterio_aceptabilidad: CriteriosAceptabilidadSchema):
    with engine.connect() as conn:
        new_criterio_aceptabilidad = data_criterio_aceptabilidad.dict()
        conn.execute(criterios_aceptabilidad.insert().values(new_criterio_aceptabilidad))
        conn.commit()

    return Response(status_code=HTTP_201_CREATED)

@criterios_aceptabilidad_router.put("/api/criterios_aceptabilidad/{criterio_id}", response_model=CriteriosAceptabilidadSchema)
def update_criterio_aceptabilidad(data_update: CriteriosAceptabilidadSchema, criterio_id: str):
    with engine.connect() as conn:
        conn.execute(
            criterios_aceptabilidad.update()
            .values(
                id_estado=data_update.id_estado,
                nombre=data_update.nombre
            )
            .where(criterios_aceptabilidad.c.id == criterio_id)
        )
        conn.commit()

        updated_criterio_aceptabilidad = conn.execute(select(criterios_aceptabilidad).where(criterios_aceptabilidad.c.id == criterio_id)).first()
        if updated_criterio_aceptabilidad:
            updated_criterio_aceptabilidad_dict = {
                "id": updated_criterio_aceptabilidad.id,
                "id_estado": updated_criterio_aceptabilidad.id_estado,
                "nombre": updated_criterio_aceptabilidad.nombre
            }
            return updated_criterio_aceptabilidad_dict
        else:
            raise HTTPException(status_code=404, detail="Criterio Aceptabilidad not found")

@criterios_aceptabilidad_router.delete("/api/criterios_aceptabilidad/{criterio_id}", status_code=HTTP_204_NO_CONTENT)
def delete_criterio_aceptabilidad(criterio_id: str):
    with engine.connect() as conn:
        conn.execute(criterios_aceptabilidad.delete().where(criterios_aceptabilidad.c.id == criterio_id))
        conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# CRUD para la tabla 'documento'

@documento_router.get("/api/documento", response_model=List[DocumentoSchema])
def get_documentos():
    with engine.connect() as conn:
        result = conn.execute(select(documento)).fetchall()

        documentos_objects = [DocumentoSchema(
            id=row.id,
            nombre=row.nombre,
            descripcion=row.descripcion,
            ruta=row.ruta
        ) for row in result]

        return documentos_objects

@documento_router.get("/api/documento/{documento_id}", response_model=DocumentoSchema)
def get_documento(documento_id: str):
    with engine.connect() as conn:
        result = conn.execute(select(documento).where(documento.c.id == documento_id)).first()

        if result:
            documento_dict = {
                "id": result.id,
                "nombre": result.nombre,
                "descripcion": result.descripcion,
                "ruta": result.ruta
            }
            return documento_dict
        else:
            raise HTTPException(status_code=404, detail="Documento not found")

@documento_router.post("/api/documento", status_code=HTTP_201_CREATED)
def create_documento(data_documento: DocumentoSchema):
    with engine.connect() as conn:
        new_documento = data_documento.dict()
        conn.execute(documento.insert().values(new_documento))
        conn.commit()

    return Response(status_code=HTTP_201_CREATED)

@documento_router.put("/api/documento/{documento_id}", response_model=DocumentoSchema)
def update_documento(data_update: DocumentoSchema, documento_id: str):
    with engine.connect() as conn:
        conn.execute(
            documento.update()
            .values(
                nombre=data_update.nombre,
                descripcion=data_update.descripcion,
                ruta=data_update.ruta
            )
            .where(documento.c.id == documento_id)
        )
        conn.commit()

        updated_documento = conn.execute(select(documento).where(documento.c.id == documento_id)).first()
        if updated_documento:
            updated_documento_dict = {
                "id": updated_documento.id,
                "nombre": updated_documento.nombre,
                "descripcion": updated_documento.descripcion,
                "ruta": updated_documento.ruta
            }
            return updated_documento_dict
        else:
            raise HTTPException(status_code=404, detail="Documento not found")

@documento_router.delete("/api/documento/{documento_id}", status_code=HTTP_204_NO_CONTENT)
def delete_documento(documento_id: str):
    with engine.connect() as conn:
        conn.execute(documento.delete().where(documento.c.id == documento_id))
        conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# CRUD para la tabla 'inspeccion'

@inspeccion_router.get("/api/inspeccion", response_model=List[InspeccionSchema])
def get_inspecciones():
    with engine.connect() as conn:
        result = conn.execute(select(inspeccion)).fetchall()

        inspecciones_objects = [InspeccionSchema(
            id=row.id,
            analisis_o_ensayo=row.analisis_o_ensayo,
            analista_s=row.analista_s,
            equipo_usado=row.equipo_usado,
            preparacion_muestra=row.preparacion_muestra,
            muestra_o_matriz=row.muestra_o_matriz,
            observaciones=row.observaciones,
            aceptacion_muestra=row.aceptacion_muestra,
            motivo_rechazo=row.motivo_rechazo,
            fecha_rechazo=row.fecha_rechazo,
            respuesta_cliente=row.respuesta_cliente,
            fecha_respuesta=row.fecha_respuesta,
            comentario=row.comentario
        ) for row in result]

        return inspecciones_objects

@inspeccion_router.get("/api/inspeccion/{inspeccion_id}", response_model=InspeccionSchema)
def get_inspeccion(inspeccion_id: int):
    with engine.connect() as conn:
        result = conn.execute(select(inspeccion).where(inspeccion.c.id == inspeccion_id)).first()

        if result:
            inspeccion_dict = {
                "id": result.id,
                "analisis_o_ensayo": result.analisis_o_ensayo,
                "analista_s": result.analista_s,
                "equipo_usado": result.equipo_usado,
                "preparacion_muestra": result.preparacion_muestra,
                "muestra_o_matriz": result.muestra_o_matriz,
                "observaciones": result.observaciones,
                "aceptacion_muestra": result.aceptacion_muestra,
                "motivo_rechazo": result.motivo_rechazo,
                "fecha_rechazo": result.fecha_rechazo,
                "respuesta_cliente": result.respuesta_cliente,
                "fecha_respuesta": result.fecha_respuesta,
                "comentario": result.comentario
            }
            return inspeccion_dict
        else:
            raise HTTPException(status_code=404, detail="Inspeccion not found")

@inspeccion_router.post("/api/inspeccion", status_code=HTTP_201_CREATED)
def create_inspeccion(data_inspeccion: InspeccionSchema):
    with engine.connect() as conn:
        new_inspeccion = data_inspeccion.dict()

        # Convertir las fechas a objetos date
        new_inspeccion["fecha_rechazo"] = date.fromisoformat(new_inspeccion["fecha_rechazo"])
        new_inspeccion["fecha_respuesta"] = date.fromisoformat(new_inspeccion["fecha_respuesta"])

        try:
            conn.execute(inspeccion.insert().values(new_inspeccion))
            conn.commit()
        except SQLAlchemyError as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error creating Inspeccion: {str(e)}")

    return Response(status_code=HTTP_201_CREATED)

@inspeccion_router.put("/api/inspeccion/{inspeccion_id}", response_model=InspeccionSchema)
def update_inspeccion(data_update: InspeccionSchema, inspeccion_id: int):
    with engine.connect() as conn:
        try:
            conn.execute(
                inspeccion.update()
                .values(
                    analisis_o_ensayo=data_update.analisis_o_ensayo,
                    analista_s=data_update.analista_s,
                    equipo_usado=data_update.equipo_usado,
                    preparacion_muestra=data_update.preparacion_muestra,
                    muestra_o_matriz=data_update.muestra_o_matriz,
                    observaciones=data_update.observaciones,
                    aceptacion_muestra=data_update.aceptacion_muestra,
                    motivo_rechazo=data_update.motivo_rechazo,
                    fecha_rechazo=date.fromisoformat(data_update.fecha_rechazo),  # Convertir a objeto date
                    respuesta_cliente=data_update.respuesta_cliente,
                    fecha_respuesta=date.fromisoformat(data_update.fecha_respuesta),  # Convertir a objeto date
                    comentario=data_update.comentario
                )
                .where(inspeccion.c.id == inspeccion_id)
            )
            conn.commit()
        except SQLAlchemyError as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error updating Inspeccion: {str(e)}")

        updated_inspeccion = conn.execute(select(inspeccion).where(inspeccion.c.id == inspeccion_id)).first()
        if updated_inspeccion:
            updated_inspeccion_dict = {
                "id": updated_inspeccion.id,
                "analisis_o_ensayo": updated_inspeccion.analisis_o_ensayo,
                "analista_s": updated_inspeccion.analista_s,
                "equipo_usado": updated_inspeccion.equipo_usado,
                "preparacion_muestra": updated_inspeccion.preparacion_muestra,
                "muestra_o_matriz": updated_inspeccion.muestra_o_matriz,
                "observaciones": updated_inspeccion.observaciones,
                "aceptacion_muestra": updated_inspeccion.aceptacion_muestra,
                "motivo_rechazo": updated_inspeccion.motivo_rechazo,
                "fecha_rechazo": str(updated_inspeccion.fecha_rechazo),  # Convertir a cadena
                "respuesta_cliente": updated_inspeccion.respuesta_cliente,
                "fecha_respuesta": str(updated_inspeccion.fecha_respuesta),  # Convertir a cadena
                "comentario": updated_inspeccion.comentario
            }
            return updated_inspeccion_dict
        else:
            raise HTTPException(status_code=404, detail="Inspeccion not found")

@inspeccion_router.delete("/api/inspeccion/{inspeccion_id}", status_code=HTTP_204_NO_CONTENT)
def delete_inspeccion(inspeccion_id: int):
    with engine.connect() as conn:
        try:
            conn.execute(inspeccion.delete().where(inspeccion.c.id == inspeccion_id))
            conn.commit()
        except SQLAlchemyError as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=f"Error deleting Inspeccion: {str(e)}")

    return Response(status_code=HTTP_204_NO_CONTENT)

# CRUD para la tabla "recepcion"

@recepcion_router.get("/api/recepcion", response_model=List[RecepcionSchema])
def get_recepciones():
    try:
        with engine.connect() as conn:
            result = conn.execute(select(recepcion)).fetchall()

            recepciones_objects = [RecepcionSchema(
                id=row.id,
                id_cliente=row.id_cliente,
                id_documento=row.id_documento,
                id_criterios_aceptabilidad=row.id_criterios_aceptabilidad,
                id_inspeccion=row.id_inspeccion,
                guia=row.guia,
                nombre_entrega=row.nombre_entrega,
                remitente=row.remitente,
                fecha_entrega=row.fecha_entrega,
                medio=row.medio,
                embalaje=row.embalaje,
                fecha_envio=row.fecha_envio,
                fecha_recepcion=row.fecha_recepcion,
                hora=row.hora,
                consecutivo=row.consecutivo,
                fecha_documento=row.fecha_documento,
                hora_documento=row.hora_documento,
                orden_trabajo=row.orden_trabajo,
                observacion_criterios_aceptabilidad=row.observacion_criterios_aceptabilidad,
                observacion_parametros_inspeccion=row.observacion_parametros_inspeccion
            ) for row in result]

            return recepciones_objects

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@recepcion_router.get("/api/recepcion/{recepcion_id}", response_model=RecepcionSchema)
def get_recepcion(recepcion_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(select(recepcion).where(recepcion.c.id == recepcion_id)).first()

            if result:
                recepcion_dict = {
                    "id": result.id,
                    "id_cliente": result.id_cliente,
                    "id_documento": result.id_documento,
                    "id_criterios_aceptabilidad": result.id_criterios_aceptabilidad,
                    "id_inspeccion": result.id_inspeccion,
                    "guia": result.guia,
                    "nombre_entrega": result.nombre_entrega,
                    "remitente": result.remitente,
                    "fecha_entrega": result.fecha_entrega,
                    "medio": result.medio,
                    "embalaje": result.embalaje,
                    "fecha_envio": result.fecha_envio,
                    "fecha_recepcion": result.fecha_recepcion,
                    "hora": result.hora,
                    "consecutivo": result.consecutivo,
                    "fecha_documento": result.fecha_documento,
                    "hora_documento": result.hora_documento,
                    "orden_trabajo": result.orden_trabajo,
                    "observacion_criterios_aceptabilidad": result.observacion_criterios_aceptabilidad,
                    "observacion_parametros_inspeccion": result.observacion_parametros_inspeccion
                }
                return recepcion_dict
            else:
                raise HTTPException(status_code=404, detail="Recepcion not found")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@recepcion_router.post("/api/recepcion", status_code=201)
def create_recepcion(data_recepcion: RecepcionSchema):
    try:
        with engine.connect() as conn:
            new_recepcion = data_recepcion.dict()
            result = conn.execute(insert(recepcion).values(new_recepcion))
            new_id = result.inserted_primary_key[0]
            conn.commit()

        return Response(status_code=201, headers={"Location": f"/api/recepcion/{new_id}"})

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@recepcion_router.put("/api/recepcion/{recepcion_id}", response_model=RecepcionSchema)
def update_recepcion(data_update: RecepcionSchema, recepcion_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(
                update(recepcion)
                .values(data_update.dict())
                .where(recepcion.c.id == recepcion_id)
            )
            conn.commit()

            updated_recepcion = conn.execute(select(recepcion).where(recepcion.c.id == recepcion_id)).first()

            if updated_recepcion:
                updated_recepcion_dict = {
                    "id": updated_recepcion.id,
                    "id_cliente": updated_recepcion.id_cliente,
                    "id_documento": updated_recepcion.id_documento,
                    "id_criterios_aceptabilidad": updated_recepcion.id_criterios_aceptabilidad,
                    "id_inspeccion": updated_recepcion.id_inspeccion,
                    "guia": updated_recepcion.guia,
                    "nombre_entrega": updated_recepcion.nombre_entrega,
                    "remitente": updated_recepcion.remitente,
                    "fecha_entrega": updated_recepcion.fecha_entrega,
                    "medio": updated_recepcion.medio,
                    "embalaje": updated_recepcion.embalaje,
                    "fecha_envio": updated_recepcion.fecha_envio,
                    "fecha_recepcion": updated_recepcion.fecha_recepcion,
                    "hora": updated_recepcion.hora,
                    "consecutivo": updated_recepcion.consecutivo,
                    "fecha_documento": updated_recepcion.fecha_documento,
                    "hora_documento": updated_recepcion.hora_documento,
                    "orden_trabajo": updated_recepcion.orden_trabajo,
                    "observacion_criterios_aceptabilidad": updated_recepcion.observacion_criterios_aceptabilidad,
                    "observacion_parametros_inspeccion": updated_recepcion.observacion_parametros_inspeccion
                }
                return updated_recepcion_dict
            else:
                raise HTTPException(status_code=404, detail="Recepcion not found")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@recepcion_router.delete("/api/recepcion/{recepcion_id}", status_code=204)
def delete_recepcion(recepcion_id: int):
    try:
        with engine.connect() as conn:
            conn.execute(delete(recepcion).where(recepcion.c.id == recepcion_id))
            conn.commit()

        return Response(status_code=204)

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
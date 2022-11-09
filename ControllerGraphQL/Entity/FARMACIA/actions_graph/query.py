from HandlerData import CRUD
from ..model import Farmacia
import strawberry
import typing


@strawberry.type
class FarmaciaQuery:
    @strawberry.field
    def filter_farmacia(self, id: int) -> typing.Optional[Farmacia]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 2,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Farmacia(id=object_response["id"],
                            nombre=object_response["nombre"],
                            telefono=object_response["telefono"],
                            NIT=object_response["nit"],
                            direccion=object_response["direccion"],
                            razon_social=object_response["razon_social"],
                            ciudad=object_response["ciudad"],
                            departamento=object_response["departamento"])
        except Exception as e:
            return e

    @strawberry.field
    def get_farmacia(self) -> typing.List[Farmacia]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 2,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Farmacia(id=value.__dict__["id"],
                             nombre=value.__dict__["nombre"],
                             telefono=value.__dict__["telefono"],
                             NIT=value.__dict__["nit"],
                             direccion=value.__dict__["direccion"],
                             razon_social=value.__dict__["razon_social"],
                             ciudad=value.__dict__["ciudad"],
                             departamento=value.__dict__["departamento"]) for value in object_response]
        except Exception as e:
            return e

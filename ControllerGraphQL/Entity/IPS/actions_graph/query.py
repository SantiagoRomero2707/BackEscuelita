from HandlerData import CRUD
from ..model import IPS
import strawberry
import typing


@strawberry.type
class IPSQuery:
    @strawberry.field
    def filter_IPS(self, id: int) -> typing.Optional[IPS]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 4,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return IPS(
                id=object_response["id"],
                nombre_ips=object_response["nombre_ips"],
                nit=object_response["nit"],
                nivel=object_response["nivel"],
                direccion=object_response["direccion"],
                cobertura=object_response["cobertura"],
                tipo=object_response["tipo"])
        except Exception as e:
            return e

    @strawberry.field
    def get_IPS(self) -> typing.List[IPS]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 4,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [IPS(id=value.__dict__["id"],
                        nombre_ips=value.__dict__["nombre_ips"],
                        nit=value.__dict__["nit"],
                        nivel=value.__dict__["nivel"],
                        direccion=value.__dict__["direccion"],
                        cobertura=value.__dict__["cobertura"],
                        tipo=value.__dict__["tipo"],
                        telefono=value.__dict__["telefono"]) for value in object_response]
        except Exception as e:
            return e

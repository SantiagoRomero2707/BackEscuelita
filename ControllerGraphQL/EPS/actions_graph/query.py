from HandlerData import CRUD
from ..model import EPS
import strawberry
import typing


@strawberry.type
class EPSQuery:
    @strawberry.field
    def filter_eps(self, id: int) -> typing.Optional[EPS]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 0,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return EPS(id=object_response["id"],
                       nombre=object_response["nombre"],
                       telefono=object_response["telefono"],
                       NIT=object_response["NIT"],
                       tipo=object_response["tipo"])
        except Exception as e:
            return e

    @strawberry.field
    def get_eps(self) -> typing.List[EPS]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 0,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [EPS(id=value.__dict__["id"],
                       nombre=value.__dict__["nombre"],
                       telefono=value.__dict__["telefono"],
                       NIT=value.__dict__["NIT"],
                       tipo=value.__dict__["tipo"]) for value in object_response]
        except Exception as e:
            return e

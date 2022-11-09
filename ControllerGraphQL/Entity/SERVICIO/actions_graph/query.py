from HandlerData import CRUD
from ..model import Servicio
import strawberry
import typing


@strawberry.type
class ServicioQuery:
    @strawberry.field
    def filter_servicio(self, id: int) -> typing.Optional[Servicio]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 6,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Servicio(
                id=object_response["id"],
                nombre_servicio=object_response["nombre_servicio"],
                tarifa=object_response["tarifa"])
        except Exception as e:
            return e

    @strawberry.field
    def get_servicio(self) -> typing.List[Servicio]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 6,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Servicio(id=value.__dict__["id"],
                             nombre_servicio=value.__dict__["nombre_servicio"],
                             tarifa=value.__dict__["tarifa"]) for value in object_response]
        except Exception as e:
            return e

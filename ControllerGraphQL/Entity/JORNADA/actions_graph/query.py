from HandlerData import CRUD
from ..model import Jornada
import strawberry
import typing


@strawberry.type
class JornadaQuery:
    @strawberry.field
    def filter_jornada(self, id: int) -> typing.Optional[Jornada]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 5,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Jornada(
                id=object_response["id"],
                dia=object_response["dia"],
                incio=object_response["incio"],
                final=object_response["final"],
                IPS_ID_FK=object_response["IPS_ID_FK"])
        except Exception as e:
            return e

    @strawberry.field
    def get_jornada(self) -> typing.List[Jornada]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 5,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Jornada(
                id=value.__dict__["id"],
                dia=value.__dict__["dia"],
                incio=value.__dict__["incio"],
                final=value.__dict__["final"],
                IPS_ID_FK=value.__dict__["IPS_ID_FK"]) for value in object_response]
        except Exception as e:
            return e

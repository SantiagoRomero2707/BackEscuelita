from HandlerData import CRUD
from ..model import Afiliados
import strawberry
import typing


@strawberry.type
class AfiliadosQuery:
    @strawberry.field
    def filter_afiliados(self, id: int) -> typing.Optional[Afiliados]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 1,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Afiliados(
                nombre_afiliados=object_response["nombre_afiliados"],
                apellido_afiliados=object_response["apellido_afiliados"],
                regimen=object_response["regimen"],
                documento=object_response["documento"],
                EPS_ID=object_response["EPS_ID"],
                historia_clinica_id=object_response["historia_clinica_id"]
            )
        except Exception as e:
            return e

    @strawberry.field
    def get_afiliado(self) -> typing.List[Afiliados]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 1,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Afiliados(nombre_afiliados=value.__dict__["nombre_afiliados"],
                              apellido_afiliados=value.__dict__["apellido_afiliados"],
                              regimen=value.__dict__["regimen"],
                              documento=value.__dict__["documento"],
                              EPS_ID=value.__dict__["EPS_ID"],
                              historia_clinica_id=value.__dict__["historia_clinica_id"]) for value in object_response]
        except Exception as e:
            return e

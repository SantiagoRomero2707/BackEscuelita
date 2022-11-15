from HandlerData import CRUD
from ..model import IPSJornada
import strawberry
import typing


@strawberry.type
class IPSJornadaQuery:
    @strawberry.field
    def filter_ips_jornada(self, id: int) -> typing.Optional[IPSJornada]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 8,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return IPSJornada(
                IPS_Jornada_ID=object_response["IPS_Jornada_ID"],
                IPS_ID_FK=object_response["IPS_ID_FK"],
                Jornada_ID_FK=object_response["Jornada_ID_FK"],
                ips_jornadacol=object_response["ips_jornadacol"])
        except Exception as e:
            return e

    @strawberry.field
    def get_ips_jornada(self) -> typing.List[IPSJornada]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 8,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [IPSJornada(IPS_Jornada_ID=value.__dict__["IPS_Jornada_ID"],
                               IPS_ID_FK=value.__dict__["IPS_ID_FK"],
                               Jornada_ID_FK=value.__dict__["Jornada_ID_FK"],
                               ips_jornadacol=value.__dict__["ips_jornadacol"]) for value in object_response]
        except Exception as e:
            return e

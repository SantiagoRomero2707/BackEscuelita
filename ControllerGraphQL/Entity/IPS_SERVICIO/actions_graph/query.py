from HandlerData import CRUD
from ..model import IPSServicio
import strawberry
import typing


@strawberry.type
class IPSServicioQuery:
    @strawberry.field
    def filter_ips_servicio(self, id: int) -> typing.Optional[IPSServicio]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 10,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return IPSServicio(
                IPS_Servicio_PK=object_response["IPS_Servicio_PK"],
                IPS_ID=object_response["IPS_ID"],
                Servicio_ID_FK=object_response["Servicio_ID_FK"])
        except Exception as e:
            return e

    @strawberry.field
    def get_ips_servicio(self) -> typing.List[IPSServicio]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 10,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [IPSServicio(IPS_Servicio_PK=value.__dict__["IPS_Servicio_PK"],
                                IPS_ID=value.__dict__["IPS_ID"],
                                Servicio_ID_FK=value.__dict__["Servicio_ID_FK"]) for value in object_response]
        except Exception as e:
            return e

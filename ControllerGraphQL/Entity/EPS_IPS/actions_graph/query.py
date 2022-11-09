from HandlerData import CRUD
from ..model import EPSIPS
import strawberry
import typing


@strawberry.type
class EPSIPSQuery:
    @strawberry.field
    def filter_eps_ips(self, id: int) -> typing.Optional[EPSIPS]:
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
            return EPSIPS(
                EPS_IPS_PK=object_response["EPS_IPS_PK"],
                EPS_ID=object_response["EPS_ID"],
                IPS_ID_FK=object_response["IPS_ID_FK"])
        except Exception as e:
            return e

    @strawberry.field
    def get_eps_ips(self) -> typing.List[EPSIPS]:
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
            return [EPSIPS(EPS_IPS_PK=value.__dict__["EPS_IPS_PK"],
                           EPS_ID=value.__dict__["EPS_ID"],
                           IPS_ID_FK=value.__dict__["IPS_ID_FK"]) for value in object_response]
        except Exception as e:
            return e

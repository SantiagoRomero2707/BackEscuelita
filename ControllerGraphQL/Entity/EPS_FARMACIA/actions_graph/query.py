from HandlerData import CRUD
from ..model import EPSFarmacia
import strawberry
import typing


@strawberry.type
class EPSFarmaciaQuery:
    @strawberry.field
    def filter_EPSFarmacia(self, id: int) -> typing.Optional[EPSFarmacia]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 7,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return EPSFarmacia(
                id_EPS_Farmacia=object_response["ID_EPS_Farmacia"],
                EPS_ID_FK=object_response["EPS_ID_FK"],
                Farmacia_ID_FK=object_response["Farmacia_ID_FK"])
        except Exception as e:
            return e

    @strawberry.field
    def get_EPSFarmacia(self) -> typing.List[EPSFarmacia]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 7,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [EPSFarmacia(id_EPS_Farmacia=value.__dict__["ID_EPS_Farmacia"],
                        EPS_ID_FK=value.__dict__["EPS_ID_FK"],
                        Farmacia_ID_FK=value.__dict__["Farmacia_ID_FK"]) for value in object_response]
        except Exception as e:
            return e

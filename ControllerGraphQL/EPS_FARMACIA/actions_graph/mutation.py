from ..model import EPSFarmaciaInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationEPSFarmacia:
    @strawberry.mutation
    def create_EPS_Farmacia(self, EPSFarmacia: EPSFarmaciaInput) -> str:
        try:
            EPSFarmacia = {
                "EPS_ID_FK": EPSFarmacia.EPS_ID_FK,
                "Farmacia_ID_FK": EPSFarmacia.Farmacia_ID_FK
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 7,
                        'id_record_database': 0,
                        'request_data': EPSFarmacia
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_EPS_Farmacia(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 7,
                        'id_record_database': id_record,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Row drop successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def update_EPS_Farmacia(self,  EPSFarmacia: EPSFarmaciaInput, id_record: int) -> str:
        try:
            request = {
                "EPS_ID_FK": EPSFarmacia.EPS_ID_FK,
                "Farmacia_ID_FK": EPSFarmacia.Farmacia_ID_FK
            }
            EPSFarmacia = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    EPSFarmacia[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 7,
                        'id_record_database': id_record,
                        'request_data': EPSFarmacia
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
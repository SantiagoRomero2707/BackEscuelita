from HandlerData import CRUD
from ..model import EPSIPSInput
import strawberry


@strawberry.type
class EPSIPSMutation:
    @strawberry.mutation
    def create_eps_ips(self, EPS_IPS: EPSIPSInput) -> str:
        eps_ips = {
            "EPS_IPS_PK": EPS_IPS.EPS_IPS_PK,
            "EPS_ID" : EPS_IPS.EPS_ID,
            "IPS_ID_FK":EPS_IPS.IPS_ID_FK
        }
        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Create',
                    'model_mapped': 0,
                    'id_record_database': 0,
                    'request_data': eps_ips
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Create successful"

    @strawberry.mutation
    def delete_eps_ips(self, id_record: int) -> str:
        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Drop',
                    'model_mapped': 8,
                    'id_record_database': id_record,
                    'request_data': "eps"
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Row drop successful"

    @strawberry.mutation
    def update_eps_ips(self, EPS_IPS: EPSIPSInput, id_record: int) -> str:
        request = {
            "EPS_IPS_PK": EPS_IPS.EPS_IPS_PK,
            "EPS_ID": EPS_IPS.EPS_ID,
            "IPS_ID_FK": EPS_IPS.IPS_ID_FK
        }
        eps_ips = {}
        for key, value in request.items():
            if value == "NULL":
                continue
            else:
                eps_ips[key] = value
        # print(eps)

        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Update',
                    'model_mapped': 8,
                    'id_record_database': id_record,
                    'request_data': eps_ips
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Update successful"

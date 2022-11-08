from HandlerData import CRUD
from ..model import EPSInput
import strawberry


@strawberry.type
class EPSMutation:
    @strawberry.mutation
    def create_eps(self, eps: EPSInput) -> str:
        eps = {
            "nombre": eps.nombre,
            "telefono": eps.telefono,
            "NIT": eps.NIT,
            "tipo": eps.tipo
        }
        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Create',
                    'model_mapped': 0,
                    'id_record_database': 0,
                    'request_data': eps
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Create successful"

    @strawberry.mutation
    def delete_eps(self, id_record: int) -> str:
        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Drop',
                    'model_mapped': 0,
                    'id_record_database': id_record,
                    'request_data': "eps"
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Row drop successful"

    @strawberry.mutation
    def update_eps(self, eps: EPSInput, id_record: int) -> str:
        request = {
            "nombre": eps.nombre,
            "telefono": eps.telefono,
            "NIT": eps.NIT,
            "tipo": eps.tipo
        }
        eps = {}
        for key, value in request.items():
            if value == "NULL":
                continue
            else:
                eps[key] = value
        # print(eps)

        action_user = {
            'crud_information':
                {
                    'method_http': 'Mutation-Update',
                    'model_mapped': 0,
                    'id_record_database': id_record,
                    'request_data': eps
                }
        }
        instances_crud = CRUD.MethodsDatabase(**action_user)
        instances_crud.methods_graphql()
        return "Update successful"

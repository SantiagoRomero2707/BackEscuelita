from ..model import IPSInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationIPS:
    @strawberry.mutation
    def create_ips(self, ips: IPSInput) -> str:
        try:
            ips = {
                "nombre_ips": ips.nombre_ips,
                "nit": ips.nit,
                "nivel": ips.nivel,
                "direccion": ips.direccion,
                "cobertura": ips.cobertura,
                "tipo": ips.tipo,
                "telefono": ips.telefono
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 4,
                        'id_record_database': 0,
                        'request_data': ips
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_ips(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 4,
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
    def update_ips(self, ips: IPSInput, id_record: int) -> str:
        try:
            request = {
                "nombre_ips": ips.nombre_ips,
                "nit": ips.nit,
                "nivel": ips.nivel,
                "direccion": ips.direccion,
                "cobertura": ips.cobertura,
                "tipo": ips.tipo,
                "telefono": ips.telefono
            }
            ips = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    ips[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 4,
                        'id_record_database': id_record,
                        'request_data': ips
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
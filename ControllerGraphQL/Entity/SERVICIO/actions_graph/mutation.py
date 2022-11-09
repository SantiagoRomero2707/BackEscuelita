from ..model import ServicioInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationServicio:
    @strawberry.mutation
    def create_servicio(self, Servicio: ServicioInput) -> str:
        try:
            Servicio = {
                "nombre_servicio": Servicio.nombre_servicio,
                "tarifa": Servicio.tarifa
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 6,
                        'id_record_database': 0,
                        'request_data': Servicio
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_servicio(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 6,
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
    def update_servicio(self,  servicio: ServicioInput, id_record: int) -> str:
        try:
            request = {
                "nombre_servicio": servicio.nombre_servicio,
                "tarifa": servicio.tarifa
            }
            Servicio = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    Servicio[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 6,
                        'id_record_database': id_record,
                        'request_data': Servicio
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
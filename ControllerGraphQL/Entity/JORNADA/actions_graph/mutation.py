from ..model import JornadaInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationJornada:
    @strawberry.mutation
    def create_jornada(self, Jornada: JornadaInput) -> str:
        try:
            jornada = {
                "dia": Jornada.dia,
                "incio": Jornada.incio,
                "final": Jornada.final,
                "IPS_ID_FK": Jornada.IPS_ID_FK
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 5,
                        'id_record_database': 0,
                        'request_data': jornada
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_jornada(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 5,
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
    def update_jornada(self,  Jornada: JornadaInput, id_record: int) -> str:
        try:
            request = {
                "dia": Jornada.dia,
                "incio": Jornada.incio,
                "final": Jornada.final,
                "IPS_ID_FK": Jornada.IPS_ID_FK
            }
            Jornada = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    Jornada[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 5,
                        'id_record_database': id_record,
                        'request_data': Jornada
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
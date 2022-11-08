from ..model import HorarioInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationHorario:
    @strawberry.mutation
    def create_horario(self, horario: HorarioInput) -> str:
        try:
            horario = {
                "dias": horario.dias,
                "inicio_jornada": horario.inicio_jornada,
                "final_jornada": horario.final_jornada,
                "habitacion": horario.habitacion,
                "edificio": horario.edificio,
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 3,
                        'id_record_database': 0,
                        'request_data': horario
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_horario(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 3,
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
    def update_horario(self, horario: HorarioInput, id_record: int) -> str:
        try:
            request = {
                "dias": horario.dias,
                "inicio_jornada": horario.inicio_jornada,
                "final_jornada": horario.final_jornada,
                "habitacion": horario.habitacion,
                "edificio": horario.edificio,
            }
            horario = {}
            for key, value in request.items():
                if value == "NULL":
                    continue
                else:
                    horario[key] = value
            # print(eps)

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 3,
                        'id_record_database': id_record,
                        'request_data': horario
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
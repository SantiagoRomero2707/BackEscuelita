from ..model import MedicoHorarioInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationMedicoHorario:
    @strawberry.mutation
    def create_medico_horario(self, MedicoHorario: MedicoHorarioInput) -> str:
        try:
            MedicoHorario = {
                "Medico_Horario_PK": MedicoHorario.Medico_Horario_PK,
                "Horario_id_fk": MedicoHorario.Horario_id_fk}
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 12,
                        'id_record_database': 0,
                        'request_data': MedicoHorario
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_medico_horario(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 12,
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
    def update_medico(self, MedicoHorario: MedicoHorarioInput, id_record: int) -> str:
        request = {
            "Medico_Horario_PK": MedicoHorario.Medico_Horario_PK,
            "Horario_id_fk": MedicoHorario.Horario_id_fk}
        try:
            MedicoHorario = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    MedicoHorario[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 12,
                        'id_record_database': id_record,
                        'request_data': MedicoHorario
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e

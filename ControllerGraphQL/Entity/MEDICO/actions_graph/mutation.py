from ..model import MedicoInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationMedico:
    @strawberry.mutation
    def create_medico(self, Medico: MedicoInput) -> str:
        try:

            Medico = {"nombre_medico": Medico.nombre_medico,
                      "apellidos_medico": Medico.apellidos_medico,
                      "licencia": Medico.licencia,
                      "especialidad": Medico.especialidad,
                      "cargo": Medico.cargo,
                      "persona_id": Medico.persona_id,
                      "IPS_FK": Medico.IPS_FK}
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 10,
                        'id_record_database': 0,
                        'request_data': Medico
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_medico(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 10,
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
    def update_medico(self, Medico: MedicoInput, id_record: int) -> str:
        try:
            request = {
                "nombre_medico": Medico.nombre_medico,
                "apellidos_medico": Medico.apellidos_medico,
                "licencia": Medico.licencia,
                "especialidad": Medico.especialidad,
                "cargo": Medico.cargo,
                "persona_id": Medico.persona_id,
                "IPS_FK": Medico.IPS_FK}
            Medico = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    Medico[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 10,
                        'id_record_database': id_record,
                        'request_data': Medico
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e

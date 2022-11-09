from HandlerData import CRUD
from ..model import MedicoHorario
import strawberry
import typing


@strawberry.type
class MedicoHorarioQuery:
    @strawberry.field
    def filter_medico(self, id: int) -> typing.Optional[MedicoHorario]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 12,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return MedicoHorario(
                Medico_ID=object_response["Medico_ID"],
                Medico_Horario_PK=object_response["Medico_Horario_PK"],
                Horario_id_fk=object_response["Horario_id_fk"])
        except Exception as e:
            return e

    @strawberry.field
    def get_medico(self) -> typing.List[MedicoHorario]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 12,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [MedicoHorario(Medico_ID=value.__dict__["Medico_ID"],
                                  Medico_Horario_PK=value.__dict__["Medico_Horario_PK"],
                                  Horario_id_fk=value.__dict__["Horario_id_fk"]) for value in object_response]
        except Exception as e:
            return e

from HandlerData import CRUD
from ..model import Horario
import strawberry
import typing


@strawberry.type
class HorarioQuery:
    @strawberry.field
    def filter_horario(self, id: int) -> typing.Optional[Horario]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 3,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Horario(id=object_response["id"],
                            dias=object_response["dias"],
                            inicio_jornada=object_response["inicio_jornada"],
                            final_jornada=object_response["final_jornada"],
                            habitacion=object_response["habitacion"],
                            edificio=object_response["edificio"])
        except Exception as e:
            return e

    @strawberry.field
    def get_horario(self) -> typing.List[Horario]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 3,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Horario(id=value.__dict__["id"],
                             dias=value.__dict__["dias"],
                             inicio_jornada=value.__dict__["inicio_jornada"],
                             final_jornada=value.__dict__["final_jornada"],
                             habitacion=value.__dict__["habitacion"],
                             edificio=value.__dict__["edificio"]) for value in object_response]
        except Exception as e:
            return e

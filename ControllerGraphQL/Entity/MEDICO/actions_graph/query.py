from HandlerData import CRUD
from ..model import Medico
import strawberry
import typing


@strawberry.type
class MedicoQuery:
    @strawberry.field
    def filter_medico(self, id: int) -> typing.Optional[Medico]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query_Filter',
                        'model_mapped': 10,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            response = instances_crud.methods_graphql()
            object_response = response.__dict__
            return Medico(
                id=object_response["id"],
                nombre_medico=object_response["nombre_medico"],
                apellidos_medico=object_response["apellidos_medico"],
                licencia=object_response["licencia"],
                especialidad=object_response["especialidad"],
                cargo=object_response["cargo"],
                persona_id=object_response["persona_id"],
                IPS_FK=object_response["IPS_FK"]
                )
        except Exception as e:
            return e

    @strawberry.field
    def get_medico(self) -> typing.List[Medico]:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Query',
                        'model_mapped': 10,
                        'id_record_database': id,
                        'request_data': "eps"
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            object_response = instances_crud.methods_graphql()
            return [Medico(id=value.__dict__["id"],
                           nombre_medico=value.__dict__["nombre_medico"],
                           apellidos_medico=value.__dict__["apellidos_medico"],
                           licencia=value.__dict__["licencia"],
                           especialidad=value.__dict__["especialidad"],
                           cargo=value.__dict__["cargo"],
                           persona_id=value.__dict__["persona_id"],
                           IPS_FK=value.__dict__["IPS_FK"]) for value in object_response]
        except Exception as e:
            return e

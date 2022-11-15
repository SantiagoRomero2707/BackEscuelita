from ..model import IPSJornadaInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationIPSJornada:
    @strawberry.mutation
    def create_ips_jornada(self, IPSJornada: IPSJornadaInput) -> str:
        try:
            IPSJornada = {

                "IPS_ID_FK": IPSJornada.IPS_ID_FK,
                "Jornada_ID_FK": IPSJornada.Jornada_ID_FK,
                "ips_jornadacol": IPSJornada.ips_jornadacol
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 8,
                        'id_record_database': 0,
                        'request_data': IPSJornada
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_ips_jornada(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 8,
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
    def update_ips_jornada(self,  IPSJornada: IPSJornadaInput, id_record: int) -> str:
        try:
            request = {
                "IPS_ID_FK": IPSJornada.IPS_ID_FK,
                "Jornada_ID_FK": IPSJornada.Jornada_ID_FK,
                "ips_jornadacol": IPSJornada.ips_jornadacol
            }
            IPSJornada = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    IPSJornada[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 8,
                        'id_record_database': id_record,
                        'request_data': IPSJornada
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
from ..model import IPSServicioInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationIPSServicio:
    @strawberry.mutation
    def create_ips_servicio(self, IPSServicio: IPSServicioInput) -> str:
        try:
            IPSServicio = {
                "IPS_Servicio_PK": IPSServicio.IPS_Servicio_PK,
                "IPS_ID": IPSServicio.IPS_ID,
                "Servicio_ID_FK": IPSServicio.Servicio_ID_FK
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 10,
                        'id_record_database': 0,
                        'request_data': IPSServicio
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_ips_servicio(self, id_record: str) -> str:
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
    def update_ips_servicio(self,  IPSServicio: IPSServicioInput, id_record: str) -> str:
        try:
            request = {
                "IPS_Servicio_PK": IPSServicio.IPS_Servicio_PK,
                "IPS_ID": IPSServicio.IPS_ID,
                "Servicio_ID_FK": IPSServicio.Servicio_ID_FK
            }
            IPSServicio = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    IPSServicio[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 10,
                        'id_record_database': id_record,
                        'request_data': IPSServicio
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
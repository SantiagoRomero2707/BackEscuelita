from ..model import AfiliadosInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationAfiliados:
    @strawberry.mutation
    def create_afiliado(self, Afiliados:AfiliadosInput) -> str:
        try:
            Afiliados = {
                "nombre_afiliados": Afiliados.nombre_afiliados,
                "apellido_afiliados": Afiliados.apellido_afiliados,
                "regimen": Afiliados.regimen,
                "documento": Afiliados.documento,
                "EPS_ID": Afiliados.EPS_ID,
                "historia_clinica_id": Afiliados.historia_clinica_id
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 1,
                        'id_record_database': 0,
                        'request_data': Afiliados
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_afiliados(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 1,
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
    def update_afiliados(self,  Afiliados: AfiliadosInput, id_record: int) -> str:
        try:
            request = {
                "nombre_afiliados": Afiliados.nombre_afiliados,
                "apellido_afiliados": Afiliados.apellido_afiliados,
                "regimen": Afiliados.regimen,
                "documento": Afiliados.documento,
                "EPS_ID": Afiliados.EPS_ID,
                "historia_clinica_id": Afiliados.historia_clinica_id
            }
            Afiliados = {}
            for key, value in request.items():
                if value == "NULL" or value == 0:
                    continue
                else:
                    Afiliados[key] = value

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 1,
                        'id_record_database': id_record,
                        'request_data': Afiliados
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
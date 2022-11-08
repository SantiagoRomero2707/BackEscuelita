from ..model import FarmaciaInput
from HandlerData import CRUD
import strawberry


@strawberry.type
class MutationFarmacia:
    @strawberry.mutation
    def create_farmacia(self, farmacia: FarmaciaInput) -> str:
        try:
            farmacia = {
                "nombre": farmacia.nombre,
                "telefono": farmacia.telefono,
                "nit": farmacia.NIT,
                "direccion": farmacia.direccion,
                "razon_social": farmacia.razon_social,
                "ciudad": farmacia.ciudad,
                "departamento": farmacia.departamento
            }
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Create',
                        'model_mapped': 2,
                        'id_record_database': 0,
                        'request_data': farmacia
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Create successful"
        except Exception as e:
            return e

    @strawberry.mutation
    def delete_farmacia(self, id_record: int) -> str:
        try:
            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Drop',
                        'model_mapped': 2,
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
    def update_farmacia(self, farmacia: FarmaciaInput, id_record: int) -> str:
        try:
            request = {
                "nombre": farmacia.nombre,
                "telefono": farmacia.telefono,
                "nit": farmacia.NIT,
                "direccion": farmacia.direccion,
                "razon_social": farmacia.razon_social,
                "ciudad": farmacia.ciudad,
                "departamento": farmacia.departamento
            }
            farmacia = {}
            for key, value in request.items():
                if value == "NULL":
                    continue
                else:
                    farmacia[key] = value
            # print(eps)

            action_user = {
                'crud_information':
                    {
                        'method_http': 'Mutation-Update',
                        'model_mapped': 2,
                        'id_record_database': id_record,
                        'request_data': farmacia
                    }
            }
            instances_crud = CRUD.MethodsDatabase(**action_user)
            instances_crud.methods_graphql()
            return "Update successful"
        except Exception as e:
            return e
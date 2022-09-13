from ControllerAPI.Services import create_app
# Pequeño testing de datos para el sistema.

app = create_app()

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

from HandlerData import CRUD
# BUILD FUNCTION IN THE FUTURE
info_user = {
    'user_name_login': 'Santiago Romero',
    'rol_user': 'DIRECTOR HSEQ',
    'TIME_LOGIN': '15:45:12',
    'DAY_LOGIN': '25/05/45',
    'TIME_TRANSACTION': '20:45:12',
    'DAY_TRANSACTION': '25/05/45'
}

# CRUD Data (model)
data ={
    'Nom_OPERAC': 'Hola'
}

# Action from ControllerAPI
action_user = {
    'info_user': info_user,
    'crud_information':
        {
            'method_http': 'POST',
            'model_mapped': 0,
            'id_record_database': 11,
            'request_data': data
        }
}
# pprint(action_user)
# instaces_crud = CRUD.MethodsDatabase(**action_user)
# instaces_crud.methods_http()

# Instances_crud = MethodsDatabase(**action_user)
# print(Instances_crud)
# Funcionalidad del template junto con el el método http
# Instances_Template = Template(**action_user)
# print(Instances_Template)



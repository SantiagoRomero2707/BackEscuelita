from API.routes import start_program

# Pequeño testing de datos para el sistema.

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
data = {
    'name': 'Ricardo ',
    'first_last_name': 'Sanchez',
    'second_last_name': 'Vivar',
    'age': 25,
    'identification': '10000'
}

# Action from API
action_user = {
    'info_user': info_user,
    'crud_information':
        {
            'method_http': 'DELETE',
            'model_mapped': 0,
            'id_record_database': 11,
            'request_data': data
         }
}

# Instances_crud = MethodsDatabase(**action_user)
# print(Instances_crud)
# Funcionalidad del template junto con el el método http
# Instances_Template = Template(**action_user)
# print(Instances_Template)

if __name__ == "__main__":
    start_program()

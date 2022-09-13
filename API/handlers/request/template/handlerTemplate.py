from database.operations_database.CRUD import MethodsDatabase


class Template():

    def __init__(self, **kwargs):
        self.attrib = kwargs
        for key, value in self.attrib.items():
            if key == 'info_user':
                self.info_user = value
            elif key == 'crud_information':
                self.crud_information = value

        # inheritance by handle files for render template
        # HandlerFiles.__init__(self, self.template, 'PROYECTOS-PETROSEISMIC')

        # inheritance by handler form for render template of user
        # Form.__init__(self, self.model_mapped)

        # inheritance by methodsdatabase for dinamyc data with API
        MethodsDatabase.__init__(self, **self.crud_information)

    def __repr__(self):
        # return f'{pprint(self.attrib)}, {MethodsDatabase}'
        return f'{MethodsDatabase.__repr__(self)}'

    def location_template(self):
        path_relative = self.route_relative()
        path_template = self.replace_path(path_relative)
        return path_template

    def form(self):
        object_form = self.create_form()
        return object_form

    def method_crud(self):
        self.methods_http()

    """
    def methods_http (self):
        if self.method_used == 'GET':
            # print('Es una consulta a DB y vista de usuario')
            return 'GET'
        elif self.method_used == 'PUT':
            # print('Es una consulta e inserción de datos a la DB con formularios')
            return 'PUT'
        elif self.method_used == 'DELETE':
            # print('Es una consulta a la base de datos')
            return 'DELETE'
        elif self.method_used == 'POST':
            # print('Es una inserción de datos a la DB con formularios')
            return 'POST'
        else:
            # print('No es un método que necesite realizar interacción con la base de datos')
            return 'NADA'

    def show_template (self):
        path_template = self.location_template()
        method_template = self.methods_http()
        template = {'path': path_template, 'method': method_template, 'name_user': self.user_name,
                    'rol_user': self.rol_user, 'ID_db': self.method_db, 'Model_DB': self.model_db}
        data = json.dumps(template)
        new_data = json.loads(data)
        return render(path_template)

    # def show_attrib(self):
    # for i, k in self.attrib.items():
    # print('Key', i, 'value', k)
    # if 'first_name' in self.attrib:
    # print('Okey')
    # else:
    # print('Pailas')
"""

"""
# @app.route('/TemplateForm/', methods=['GET', 'POST'])
def plantillaForm():
    contador = request.args.get("counter")  # captura el valor del contador
    type = request.args.get("type")  # captura el valor del tipo de modelo

    formTemplate = generator.Form()  # Genera el formulario
    data = request.form
    form = ShowForm(int(contador), formTemplate, data)  # Realiza la limpieza o llenado del formulario
    formReadyShow = filtroForm()  # Llamo generadores de filtros

    return render_template('firstTemplate.html', contador=int(contador), type=type, Form=form,
                           Entidad=formReadyShow[0], evalCampo=formReadyShow[1])


@app.route('/evalData/', methods=['GET', 'POST'])
def validateInputData():
    contador = request.args.get("counter")  # captura el valor del contador
    type = request.args.get("type")  # captura el valor del tipo de modelo
    data = dict(request.form)
    if data.__contains__('querydata'):
        return plantillaQuery(data=data, contador=contador, type=type)
    else:
        return "Va insertar datos en la DB"


def plantillaQuery(data, contador, type):
    consulta = consultas.consultOrm()
    datos = consulta[1]
    columns = consulta[0]

    return render_template('secondTemplate.html', counter=int(contador), template=type,
                           Data=data, column=columns, data=datos)

"""

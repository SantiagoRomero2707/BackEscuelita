from API.views import create_app


def start_program():
    app = create_app()
    return app


"""
# imports
from flask import Flask
app = Flask(__name__, template_folder="templates/pages", static_folder="templates/static")

@app.route('/<string:name>', methods=['GET','POST'])
def main(name):
    return show_template(name)



def start_program():
    app.run(debug=True, port=5000)

"""


"""
# Start program with login
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        print('ES un get')
        return template('login.html')
    elif request.method == 'POST':
        print('Es un post')
        print(request.form)
        return 'Es un post'
    else:
        print('No es nada')
        return 'No es nada'


# Method for show every all templates
@app.route('/page/<string:name_template>', methods=['GET', 'POST'])
def show_template(name_template):
    return template(name_template)




@app.route('/PATH', methods=['GET', 'POST'])
def process():
    if request.method == 'GET':
        print('ES un get')
        return 'Es un get'
    elif request.method == 'POST':
        print('Es un post')
        print(request.form)
        return 'Es un post'
    else:
        print('No es nada')
        return 'No es nada'





@app.route('/', methods=['GET', 'POST'])  # Primer template para entrar al formulario
def main():
    data = 1
    return render_template('index.html', Counter=data)

@app.route('/TemplateForm/', methods=['GET', 'POST'])
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


@app.route('/Consulta', methods=['GET', 'POST'])
def consultar():
    return consultas.consultOrm()
"""

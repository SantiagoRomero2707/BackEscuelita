# imports
import json
from . import pages
from flask import jsonify, request
from flask.views import MethodView


# Clase para generar las vistas API REST de los Usuarios.
# @pages.class_route("/page", "invoice_view", template='template', db_method='db_method')
@pages.class_route("/page", "invoice_view",
                   pk="invoice_id", model_base='model_base', template='template', db_method='db_method')
class InvoiceView (MethodView):

    def get(self, template, db_method, model_base, invoice_id):
        method = request.method
        # Url Complete
        data_url = request.base_url
        print(data_url, 'base_url')

        # Url path, variables
        data_path = request.path
        print(data_path, 'data_path')

        # LocalHost
        hots_url = request.host_url
        print(hots_url, 'host_url')

        # data = {
            # 'name_template': template,
            # 'http_method': db_method,
            # 'model': {'id_select_model': model_base, 'model_select_mapped': str('model_mapped')},
            # 'record': {'id_record_database': invoice_id, 'records': str(response)}
        # }
        # object_request = MethodsDatabase(method_http=db_method, id_database=invoice_id)
        # response = object_request.methods_http()
        return jsonify({'message': f'Hello you {invoice_id}', 'request_method': method})
        # return jsonify(data)

        # Instances = Template(user_name='Santiago Romero', rol_user='Coordinador HSE', name_file=template,
        #                   method_db=db_method, id_db=invoice_id, model_db=model_base)
        # data = Instances.show_template()
        # return data
        # return 'Okey'

    def put(self, template, db_method, model_base, invoice_id):
        method = request.method
        # Update a single invoice
        print("PUT INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK Update", "method": method, "response": "Successfull!", "sale_id": None,
                        "data": data}
        return jsonify(response)

    def delete(self, template, db_method, model_base, invoice_id):
        method = request.method
        # object_request = MethodsDatabase(model_mapped, method_http=db_method, id_database=invoice_id,
                                         # connection_database=object_connection)
        # Drop a single invoice
        print("DELETE INFO ...")
        data = {
            "model_base_id": model_base,
            "name_file_view": template,
            "id_search_db": invoice_id,
            "db_method": method
        }
        response = {"code": "OK Drop", "method": "DELETE", "response": "Successfull!", "data": data}
        return jsonify(response)

    def post(self):
        method = request.method
        # Create a new invoice
        print("POST INFO ...")
        data = json.loads(request.data)
        response = {"code": "OK Create", "method": method, "response": "Successfull!", "sale_id": None, "data": data}
        return jsonify(response)



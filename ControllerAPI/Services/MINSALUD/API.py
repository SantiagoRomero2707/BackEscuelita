# API que retorna información del INVIMA

from .logicService.persistence import DatabasePersistence
from flask.views import MethodView
from flask import jsonify, request
from . import *
import json


# Clase para generar las vistas API Rest de Facturas.
@invima.class_route("/api", "invoice_view")
class InvoiceView(MethodView):

    # Método GET que recupera recursos a través de HTTP
    @staticmethod
    def get():
        response = {'OK': '200'}
        print(response)
        object_data = DatabasePersistence()
        data = object_data.read_persistence()
        return jsonify(data)

    # Método POST que recibe recursos a través de HTTP para ser posteriomente procesados por la lógica del software
    @staticmethod
    def post():
        data = json.loads(request.data)  # Se recibe la información en binario
        response_object = dict(data)  # Se codifica en objeto python de tipo dict
        data_chocolate_feast = {'Hello':'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "POST",
                    "INVIMA": "Successfull!", "data": data}
        return jsonify(response)

    @staticmethod
    def put():
        data = json.loads(request.data)  # Se recibe la información en binario
        data_chocolate_feast = {'Hello':'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "PUT",
                    "INVIMA": "Successfull!", "data": data}
        return jsonify(response)

    @staticmethod
    def delete():
        data = json.loads(request.data)  # Se recibe la información en binario
        data_chocolate_feast = {'Hello': 'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "DELETE",
                    "INVIMA": "Successfull!", "data": data}

        return jsonify(response)
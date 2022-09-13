# imports
# from .logicService.persistence import DatabasePersistence
# from .logicService.logicChocolate import ChocolateResult

from flask.views import MethodView
from flask import jsonify, request
from . import *
import json


# Clase para generar las vistas API Rest de Facturas.
@sales.class_route("/invoice", "invoice_view")
class InvoiceView(MethodView):

    # Método GET que recupera recursos a través de HTTP
    @staticmethod
    def get():
        response = {'Hello': 'World'}
        # response = DatabasePersistence.read_persistence()
        return jsonify(response)

    # Método POST que recibe recursos a través de HTTP para ser posteriomente procesados por la lógica del software
    @staticmethod
    def post():
        data = json.loads(request.data)  # Se recibe la información en binario
        response_object = dict(data)  # Se codifica en objeto python de tipo dict

        total_to_spend = int(response_object['Cantidad_Total'])
        unit_cost = int(response_object['Precio_Unitario'])
        promotional_wraps = int(response_object['Envolturas_Promocion'])

        # object_chocolate = ChocolateResult(total_to_spend, unit_cost, promotional_wraps)
        # data_chocolate_feast = object_chocolate.chocolate_feast()
        data_chocolate_feast = {'Hello':'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "POST",
                    "CRUDresponse": "Successfull!", "data": data}
        return jsonify(response)

    @staticmethod
    def put():
        data = json.loads(request.data)  # Se recibe la información en binario
        data_chocolate_feast = {'Hello':'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "PUT",
                    "CRUDresponse": "Successfull!", "data": data}

        return jsonify(response)

    @staticmethod
    def delete():
        data = json.loads(request.data)  # Se recibe la información en binario
        data_chocolate_feast = {'Hello': 'World'}
        response = {"code": "OK create", "totalchocolate": data_chocolate_feast, "method": "DELETE",
                    "CRUDresponse": "Successfull!", "data": data}

        return jsonify(response)
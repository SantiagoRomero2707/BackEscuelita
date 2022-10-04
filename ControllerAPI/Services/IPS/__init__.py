# imports
import types
from flask import Blueprint
from .decorators import class_route

invima = Blueprint("invima", __name__, url_prefix="/invima", template_folder="templates")

invima.class_route = types.MethodType(class_route, invima)

from .API import InvoiceView

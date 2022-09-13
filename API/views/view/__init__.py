# imports
import types
from flask import Blueprint

from API.views.decorators.routesClassView import class_route

pages = Blueprint("view", __name__, url_prefix="/view", template_folder="templates/pages",
                  static_folder="templates/static")
pages.class_route = types.MethodType(class_route, pages)

from .views import InvoiceView

from models.operation_model.getAttributes import GetAttribModel
from API.handlers.request.forms.select_fields import selectField
from models.operation_model.selectModel import GetModels
from wtforms_alchemy import model_form_factory


class Form(GetModels):
    def __init__(self, id_model_database):
        self.id_model_database = id_model_database

        # Obtener modelo base de datos
        GetModels.__init__(self, self.id_model_database)
        self.Model = self.select_model()
        self.Fields = selectField.joinfields(self.id_model_database)

    def create_form(self):
        print(self.Model, self.Fields)
        ModelForm = model_form_factory(all_fields_optional=True)  # Quitar los campos requiered
        if self.Fields == '':
            class UserForm (ModelForm):
                class Meta:
                    model = self.Model
        else:
            class UserForm (ModelForm):
                class Meta:
                    model = self.Model
                    # include = Fields
                    include_foreign_keys = True  # Permitir campos de clave foranea
        Template_Form = UserForm()
        return Template_Form

    def eval_form(self):
        strong_or_weak = GetAttribModel.get_all_attrib(self.Model)
        eval_fields_form = GetAttribModel.field_owns(self.Model)
        return strong_or_weak, eval_fields_form

    @classmethod
    def alter_form(cls, form, data):
        if data:
            print("Es la segunda o n vez que ingresa y necesita su formulario con los query")
            newData = dict(data)
            for x in form:  # Es la segunda que ingresa y necesita su formulario con los query
                for key, value in newData.items ():
                    if x.id == key:
                        atributosDelCampo = vars (x)
                        atributosDelCampo['default'] = value
                        atributosDelCampo['object_data'] = value
                        atributosDelCampo['data'] = value
            return form
        else:
            print ("Está ingresando por primera vez")
            for x in form:  # Está ingresando por primera vez y necesitia limpia la data
                atributosdelcampo = vars (x)
                atributosdelcampo['default'] = ""
                atributosdelcampo['object_data'] = ""
                atributosdelcampo['data'] = ""
                return form



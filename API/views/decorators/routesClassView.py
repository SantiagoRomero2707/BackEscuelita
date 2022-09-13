def class_route(self, rule, endpoint, **options):
    """
        This decorator allow add routed to class view.
        :param self: any flask object that have `add_url_rule` method.
        :param rule: flask url rule.
        :param endpoint: endpoint name
    """

    def decorator(cls):
        if "template" in options:
            # Agregar termino a la url

            # ID PARA BUSQUEDAS EN LA BASE DE DATOS
            pk, pk_type = options["pk"], options["pk_type"] if "pk_type" in options else "int"

            # ID del modelo a utilizar en el sistema.
            model_base, pk_model_base = options["model_base"], options["pk_model_base"] if "pk_model_base" in options else "int"

            # Nombre del archivo de vista.
            template, pk_template = options["template"], options["pk_template"] if "pk_template" in options else "string"

            # Método que realizará a con la base de datos.
            db_method, pk_db_method = options["db_method"], options["pk_db_method"] if "pk_db_method" in options else "string"

            # constructor de url a través de la etiqueta
            view_func = cls.as_view(endpoint)

            # En caso de no encontrar nada automáticamente genere la url con elementos vacios por default, para GET
            self.add_url_rule(rule, defaults={pk: None},
                              view_func=view_func, methods=['GET'])

            # Para post no se necesita URL ni elementos de raiz en el cuerpo de la función
            # self.add_url_rule(rule, view_func=view_func, methods=['POST'])
            # Para GET, PUT y Drop se es necesario saber el ID y la página en específico
            # self.add_url_rule (f'{rule}/<{pk_template}:{template}>/<{pk_db_method}:{db_method}>', view_func=view_func ,methods=['GET', 'PUT', 'DELETE'])

            self.add_url_rule(f'{rule}/'
                              f'<{pk_template}:{template}>/'
                              f'<{pk_model_base}:{model_base}>/'
                              f'<{pk_db_method}:{db_method}>/'
                              f'<{pk_type}:{pk}>',
                              view_func=view_func, methods=['GET','PUT','DELETE'])

            self.add_url_rule(f'{rule}', view_func=view_func, methods=['POST','PUT'])

        else:
            self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator

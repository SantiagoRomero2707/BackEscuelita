def class_route(self, rule, endpoint, **options):
    """
        This decorator allow add routed to class view.
        :param self: any flask object that have `add_url_rule` method.
        :param rule: flask url rule.
        :param endpoint: endpoint name
    """

    def decorator(cls):
        if "pk" in options:
            pk, pk_type = options["pk"], options["pk_type"] if "pk_type" in options else "int"

            view_func = cls.as_view(endpoint)
            self.add_url_rule(rule, defaults={pk: None}, view_func=view_func, methods=['GET',])
            self.add_url_rule(rule, view_func=view_func, methods=['POST',])
            self.add_url_rule(f'{rule}/<{pk_type}:{pk}>', view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
        else:   
            self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator

class HandlerRequest(object):
    def __init__(self, request):
        self.request = request

    def method_http(self):
        if self.request == 'GET':
            print('Hará algo de recuperación de datos')
        elif self.request == 'POST':
            print ('Hará algo de meter datos')
        elif self.request == 'PUT':
            print ('Hará algo de actualizar datos')
        elif self.request == 'DELETE':
            print ('Hará algo de eliminar datos')
class Authentication(object):
    def __init__(self, password_user, username):
        self.passwordUser = password_user
        self.userName = username

    def auth_system(self):
        username_storage = "Santiago Romero"
        password_storage = 123456789
        if self.userName == username_storage and self.passwordUser == password_storage:
            print(self.userName, self.passwordUser, " Se loggeo.")
            return "Hello World"
        elif self.userName != username_storage and self.passwordUser == password_storage:
            print("Su nombre no está registrado, pero su contraseña si está okey.")
        elif self.passwordUser != password_storage and self.userName == username_storage:
            print("Su contraseña está incorrecta, pero su nombre está okey y está registrado.")
        else:
            print("Usted no está registrado en el sistema, comuniquese con el Administrado del sistema.")


Object = Authentication(123456789, 'Santiago Romero')
Object.auth_system()

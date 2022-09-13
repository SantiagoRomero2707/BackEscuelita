from ldap3 import ALL, Server, Connection, SUBTREE, ALL_ATTRIBUTES
from pprint import pprint
import json


class Conecction_Active_Directory:

    def __init__(self, IP_SERVER, USER, PASSWORD):
        self.IP_SERVER = IP_SERVER
        self.USER = USER
        self.PASSWORD = PASSWORD

    # Método de Conexión al servidor de controlador de dominio
    def conectando(self, IP_SERVER, USER, PASSWORD):
        # INSTRUCCIÓN DE CONEXION AL SERVIDOR DE DOMINIO
        Bind_Thread = Server(IP_SERVER, get_info=ALL)
        # INICIO DE SESIÓN A CONTROLADOR DE DOMINIO
        Session_Loggin_AD = Connection(Bind_Thread, user=USER, password=PASSWORD, auto_bind=True)
        # RETORNA CONSTRUCTOR CON LOS PARAMETROS ESTABLECIDOS DE LA CONEXIÓN, HILO Y LA SESIÓN DE ACTIVE DIRECTORY
        return Session_Loggin_AD


try:
    instances = Conecction_Active_Directory('192.168.10.24', 'PRUEBAS\Administrador', 'Nomelase20')
    object_conecction_ad = instances.conectando(instances.IP_SERVER, instances.USER, instances.PASSWORD)
except Exception as e:
    print("No funciona men XD:", e)

object_conecction_ad.search("dc=Pruebas,dc=com", "(objectclass=person)", attributes=ALL_ATTRIBUTES)
print(object_conecction_ad.authentication)
data = object_conecction_ad.entries
result_parsed = object_conecction_ad.response_to_json(data)
pprint(json.loads(result_parsed))

object_conecction_ad.authentication(result_parsed)

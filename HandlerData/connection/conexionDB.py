from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine


# Database connection class in MSSQL
class Connect(object):
    # Constructor de la conexión y sus variables
    def __init__(self, server_name, instance_name, database_name):
        # NOMBRE DEL SERVIDOR AL CUAL SE INSTANCIA
        self.serverName = server_name
        # NOMBRE DE LA INSTANCIA DE LA BASE DE DATOS
        self.instanceName = instance_name
        # NOMBRE DE LA BASE DE DATOS A MANIPULAR
        self.databaseName = database_name

    # Método de Conexión a las bases de datos
    def connecting(self):
        # INSTRUCCIÓN DE CONEXION BASE DE DATOS SQLALCHEMY
        MSSQL_engine = create_engine('mssql+pyodbc://' + self.serverName + "\\" + self.instanceName + '/' +
                                     self.databaseName + '?driver=SQL+Server+Native+Client+11.0')
        # CREA HILO DE CONEXIÓN A BASE DE DATOS SEGÚN URL ESTABLECIDA
        session_factory = sessionmaker(autocommit=False, autoflush=False, bind=MSSQL_engine)
        # CONSTRUCTOR DE LA SESIÓN ACTUAL EN EL ESPACIO DE MEMORIA DEL SERVIDOR
        session = scoped_session(session_factory)
        try:
            # RETORNA CONSTRUCTOR CON LOS PARAMETROS ESTABLECIDOS DE LA CONEXIÓN, HILO Y LA SESIÓN DE LA BASE DE DATOS
            MSSQL_engine.connect()
            print("Connection successful")
            return session()
        except Exception as e:
            return print(e)


# OBJETO CONEXION QUE SE UTILIZARÁ PARA REALIZAR LAS TRANSACCIONES CRUD
# connection_db = Connect('DESKTOP-8BFSMKJ', '', 'prueba')
# object_connection = connection_db.connecting()




# OBJETO CONEXION QUE SE UTILIZARÁ PARA REALIZAR LAS TRANSACCIONES CRUD
# connection_db = Connect('DESKTOP-8BFSMKJ', '', 'HSE_PROYECT_INCIDEN')
# object_connection = connection_db.connecting()

# URL INSTANCIA PARA GENERAR MODELOS EN SQLAcodgen
# 'mssql+pyodbc://DESKTOP-9DM2MGR\\/Prueba?driver=SQL+Server+Native+Client+11.0'

# 'mssql+pyodbc://DESKTOP-8BFSMKJ\/prueba?driver=SQL+Server+Native+Client+11.0'
from sqlalchemy import CHAR, Column, Date, DateTime, ForeignKey, Index, Integer, \
    LargeBinary, Numeric, SmallInteger, String, Time, Unicode,Identity
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import relationship


# CLASE REFERENCIA PARA LOS MODELOS CREADOS


class Model(object):
    pass


class Persona(Model):
    __tablename__ = 'Persona'
    id = Column(Integer, Identity (start=1, increment=1), primary_key=True)
    name = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False)
    first_last_name = Column(CHAR(10, 'Modern_Spanish_CI_AS'), nullable=False)
    second_last_name = Column(CHAR(10, 'Modern_Spanish_CI_AS'), nullable=False)
    age = Column(Integer, nullable=False)
    identification = Column(CHAR(10, 'Modern_Spanish_CI_AS'), nullable=False)

    def __init__(self, **kwargs):
        self.attrib = kwargs

    def __repr__(self):
        return f'data is ({self.id},{self.name},{self.first_last_name},' \
               f'{self.second_last_name},{self.age},{self.identification})'


class GENAMBOPERA(Model):
    __tablename__ = 'GEN_AMB_OPERA'
    ID_AMB_OPE = Column(TINYINT, primary_key=True)
    Nom_OPERAC = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Ambiente de Operación'})


class GENASEGU(Model):
    __tablename__ = 'GEN_ASEGU'

    ID_ASEGURADORA = Column(CHAR(12, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_Aseguradora = Column(CHAR(70, 'Modern_Spanish_CI_AS'), nullable=False,
                             info={'label': 'Aseguradora'})


class GENCARGOCENCO(Model):
    __tablename__ = 'GEN_CARGO_CENCOS'

    ID_CENTROCOS = Column(TINYINT, primary_key=True)
    Nom_Proceso = Column(CHAR(25, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Centro de costo'})


class GENCARGOTRABAJ(Model):
    __tablename__ = 'GEN_CARGO_TRABAJ'

    ID_CARGO = Column(CHAR(8, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_Cargo = Column(String(100, 'Modern_Spanish_CI_AS'), nullable=False,
                       info={'label': 'Cargo'})


class GENCAUBASIACTINSE(Model):
    __tablename__ = 'GEN_CAUBASI_ACTINSE'

    ID_ActInse = Column(SmallInteger, primary_key=True)
    Nom_ActInse = Column(CHAR(100, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Acto Inseguro'})


class GENCAUBASICONDINSE(Model):
    __tablename__ = 'GEN_CAUBASI_CONDINSE'

    ID_CONDINSE = Column(SmallInteger, primary_key=True)
    Nom_Cond_INSE = Column(CHAR(100, 'Modern_Spanish_CI_AS'), nullable=False,
                           info={'label': 'Condición Insegura'})


class GENCAUINMEFACP(Model):
    __tablename__ = 'GEN_CAUINME_FACP'

    ID_FacP = Column(SmallInteger, primary_key=True)
    Nom_FacP = Column(CHAR(70, 'Modern_Spanish_CI_AS'), nullable=False,
                      info={'label': 'Factor del trabajo'})


class GENCAUINMEFACT(Model):
    __tablename__ = 'GEN_CAUINME_FACT'

    ID_FacT = Column(SmallInteger, primary_key=True)
    Nom_FacT = Column(CHAR(70, 'Modern_Spanish_CI_AS'), nullable=False,
                      info={'label': 'Factor personal'})


class GENCAURAIZ(Model):
    __tablename__ = 'GEN_CAURAIZ'

    ID_CauRaiz = Column(SmallInteger, primary_key=True)
    Nom_Cauraiz = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Causa Raíz'})


class GENCONDCLASE(Model):
    __tablename__ = 'GEN_COND_CLASE'

    ID_CLASEVIA = Column(SmallInteger, primary_key=True)
    NomClase_Via = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                          info={'label': 'Vía'})


class GENCONDCLIMA(Model):
    __tablename__ = 'GEN_COND_CLIMA'

    ID_CLIMA = Column(SmallInteger, primary_key=True)
    Nom_Clima = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                       info={'label': 'Clima'})


class GENCONDLUZ(Model):
    __tablename__ = 'GEN_COND_LUZ'

    ID_LUZVIA = Column(SmallInteger, primary_key=True)
    NomLuz_Dia = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Luz de la vía'})


class GENCONDTIPVIA(Model):
    __tablename__ = 'GEN_COND_TIPVIA'

    ID_TIPOVIA = Column(SmallInteger, primary_key=True)
    NomTipo_Via = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Tipo de la vía'})


class GENCONDVIA(Model):
    __tablename__ = 'GEN_COND_VIA'

    ID_CONDICIONVIA = Column(SmallInteger, primary_key=True)
    NomCondicion_Via = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                              info={'label': 'Condición de la vía'})


class GENENFER(Model):
    __tablename__ = 'GEN_ENFER'

    ID_ENFER = Column(CHAR(5, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_Enfermedad = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                            info={'label': 'Enfermedad'})


class GENGENERO(Model):
    __tablename__ = 'GEN_GENERO'

    ID_GEN = Column(TINYINT, primary_key=True)
    Nom_GEN = Column(CHAR(10, 'Modern_Spanish_CI_AS'), nullable=False,
                     info={'label': 'Género'})


class GENNATULE(Model):
    __tablename__ = 'GEN_NATULES'

    ID_NATULES = Column(SmallInteger, primary_key=True)
    Nom_NatuLes = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Naturaleza de la lesión'})
    DiasCarga = Column(SmallInteger, nullable=False,
                       info={'label': 'Días cárgados'})


class GENPAI(Model):
    __tablename__ = 'GEN_PAIS'

    ID_PAIS = Column(CHAR(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_Pais = Column(String(30, 'Modern_Spanish_CI_AS'), nullable=False, unique=True,
                      info={'label': 'País'})


class GENPARTEC(Model):
    __tablename__ = 'GEN_PARTEC'

    ID_PARTEC = Column(SmallInteger, primary_key=True)
    Nom_ParteC = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Parte del cuerpo'})


class GENPROYECTO(Model):
    __tablename__ = 'GEN_PROYECTO'

    ID_PROYECTO = Column(CHAR(3, 'Modern_Spanish_CI_AS'), primary_key=True)

    NombreProy = Column(String(100, 'Modern_Spanish_CI_AS'), unique=True,
                        info={'label': 'Nombre del proyecto'})

    ID_DIAS = Column(CHAR(3, 'Modern_Spanish_CI_AS'), nullable=False,
                     info={'label': 'Días cargados proyecto'})

    SupervisorOP = Column(String(150, 'Modern_Spanish_CI_AS'),
                          info={'label': 'Supervisor de operaciones'})

    JefeGrupo = Column(String(150, 'Modern_Spanish_CI_AS'),
                       info={'label': 'Jefe de Grupo'})

    # Año_INICIO = Column(Date, nullable=False,
    # info={'label': 'Fecha de inicio'})

    # ID PAIS

    @declared_attr
    def ID_PAIS(self):
        return Column(ForeignKey('GEN_PAIS.ID_PAIS'),
                      info={'label': 'País'})

    @declared_attr
    def GEN_PAI(self):
        return relationship('GENPAI')

    # ID DEPARTAMENTO
    @declared_attr
    def ID_DEPA(self):
        return Column(ForeignKey('GEN_DEPA.ID_DEPA'),
                      info={'label': 'Departamento'})

    @declared_attr
    def GEN_DEPA(self):
        return relationship('GENDEPA')

    # ID CIUDAD
    @declared_attr
    def ID_CIUDAD(self):
        return Column(ForeignKey('GEN_CIUDAD.ID_Ciudad'),
                      info={'label': 'Ciudad'})

    @declared_attr
    def GEN_CIUDAD(self):
        return relationship('GENCIUDAD')

    # ID CLIENTE
    @declared_attr
    def ID_CLIENTE(self):
        return Column(ForeignKey('GEN_PROY_CLIENTE.NIT_Cliente'), nullable=False,
                      info={'label': 'NIT del Cliente'})

    @declared_attr
    def GEN_PROY_CLIENTE(self):
        return relationship('GENPROYCLIENTE')

    # ID FUENTE DE ENERGÍA
    @declared_attr
    def ID_FUENENERGIA(self):
        return Column(ForeignKey('GEN_PROY_ENERGIA.ID_FUENENERGIA'), nullable=False,
                      info={'label': 'Fuente de energía'})

    @declared_attr
    def GEN_PROY_ENERGIA(self):
        return relationship('GENPROYENERGIA')

    # ID AMBIENTE OPERACIONAL
    @declared_attr
    def ID_Amb_Oper(self):
        return Column(ForeignKey('GEN_AMB_OPERA.ID_AMB_OPE'), nullable=False,
                      info={'label': 'Ambiente de la Operación'})

    @declared_attr
    def GEN_AMB_OPERA(self):
        return relationship('GENAMBOPERA')

    # ID INCIDENTE CAMBIAR CARDINALIDAD URGENTE!!!!!!
    @declared_attr
    def ID_INCIDENT(self):
        return Column(ForeignKey('PROY_INCIDENTE.ID_INCIDENTE'), nullable=False)

    @declared_attr
    def PROY_INCIDENTE(self):
        return relationship('PROYINCIDENTE', primaryjoin='GENPROYECTO.ID_INCIDENT == PROYINCIDENTE.ID_INCIDENTE')

    # ID DIRECTOR HSEQ
    @declared_attr
    def ID_DIRECT(self):
        return Column(ForeignKey('REG_USU_SYSTEM.DOCUMENT'), nullable=False,
                      info={'label': 'Director HSEQ'})

    @declared_attr
    def REG_USU_SYSTEM1(self):
        return relationship('REGUSUSYSTEM', primaryjoin='GENPROYECTO.ID_DIRECT == REGUSUSYSTEM.DOCUMENT')

    # ID COORDINADOR HSEQ
    @declared_attr
    def ID_COORD(self):
        return Column(ForeignKey('REG_USU_SYSTEM.DOCUMENT'), nullable=False,
                      info={'label': 'Coordinador HSEQ'})

    @declared_attr
    def REG_USU_SYSTEM(self):
        return relationship('REGUSUSYSTEM', primaryjoin='GENPROYECTO.ID_COORD == REGUSUSYSTEM.DOCUMENT')


class GENPROYCLIENTE(Model):
    __tablename__ = 'GEN_PROY_CLIENTE'

    NIT_Cliente = Column(CHAR(15, 'Modern_Spanish_CI_AS'), primary_key=True,
                         info={'label': 'NIT del Cliente'})
    Nombre = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                    info={'label': 'Nombre del Cliente'})
    ID_CORR = Column(String(200, 'Modern_Spanish_CI_AS'), nullable=False,
                     info={'label': 'Correo del cliente'})
    Num = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                 info={'label': 'Número de contacto'})


class GENPROYENERGIA(Model):
    __tablename__ = 'GEN_PROY_ENERGIA'

    ID_FUENENERGIA = Column(TINYINT, primary_key=True)
    Nom_Energia = Column(String(15, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Tipo de energía'})


class GENTIPOLOGIA(Model):
    __tablename__ = 'GEN_TIPOLOGIA'

    ID_TIPOLOGIA = Column(TINYINT, primary_key=True)
    Nom_Tipologia = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                           info={'label': 'Tipología'})


class PROYINCIDENTE(Model):
    __tablename__ = 'PROY_INCIDENTE'

    Fecha_Incidente = Column(Date, nullable=False,
                             info={'label': 'Fecha del incidente'})
    Hora_Incidente = Column(Time, nullable=False,
                            info={'label': 'Hora del incidente'})
    Dias_CARGA = Column(SmallInteger, nullable=False,
                        info={'label': 'Días cargados del íncidente'})
    Dias_Incapacidad = Column(Integer, nullable=False,
                              info={'label': 'Días de incapacidad'})
    ID_INCIDENTE = Column(SmallInteger, primary_key=True)
    Incapacidad = Column(CHAR(3, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Incapacidad'})

    # CC del Trabajador
    @declared_attr
    def CC_Trabajador(self):
        return Column(ForeignKey('GEN_TRABAJADOR.CC_TRABAJ'), nullable=False)

    @declared_attr
    def GEN_TRABAJADOR(self):
        return relationship('GENTRABAJADOR')

    # ID Incidente vial
    @declared_attr
    def ID_INCVIAL(self):
        return Column(ForeignKey('PROY_INCIDENT_VIAL.ID_INCVIAL'), nullable=False)

    @declared_attr
    def PROY_INCIDENT_VIAL(self):
        return relationship('PROYINCIDENTVIAL', primaryjoin='PROYINCIDENTE.ID_INCVIAL == PROYINCIDENTVIAL.ID_INCVIAL')

    # ID Parte del cuerpo
    @declared_attr
    def ID_PARTC(self):
        return Column(ForeignKey('GEN_PARTEC.ID_PARTEC'), nullable=False)

    @declared_attr
    def GEN_PARTEC(self):
        return relationship('GENPARTEC')

    # ID Causa Raíz
    @declared_attr
    def ID_CAURAIZ(self):
        return Column(ForeignKey('GEN_CAURAIZ.ID_CauRaiz'), nullable=False)

    @declared_attr
    def GEN_CAURAIZ(self):
        return relationship('GENCAURAIZ')

    # ID Factor del trabajo
    @declared_attr
    def ID_FacT(self):
        return Column(ForeignKey('GEN_CAUINME_FACT.ID_FacT'), nullable=False)

    @declared_attr
    def GEN_CAUINME_FACT(self):
        return relationship('GENCAUINMEFACT')

    # ID Factor personal
    @declared_attr
    def ID_FacP(self):
        return Column(ForeignKey('GEN_CAUINME_FACP.ID_FacP'), nullable=False)

    @declared_attr
    def GEN_CAUINME_FACP(self):
        return relationship('GENCAUINMEFACP')

    # Condición Insegura
    @declared_attr
    def ID_COND_INSE(self):
        return Column(ForeignKey('GEN_CAUBASI_CONDINSE.ID_CONDINSE'), nullable=False)

    @declared_attr
    def GEN_CAUBASI_CONDINSE(self):
        return relationship('GENCAUBASICONDINSE')

    # ID Acto Inseguro
    @declared_attr
    def ID_ActInse(self):
        return Column(ForeignKey('GEN_CAUBASI_ACTINSE.ID_ActInse'), nullable=False)

    @declared_attr
    def GEN_CAUBASI_ACTINSE(self):
        return relationship('GENCAUBASIACTINSE')

    # ID Enfermedad
    @declared_attr
    def ID_Enfermedad(self):
        return Column(ForeignKey('GEN_ENFER.ID_ENFER'), nullable=False)

    @declared_attr
    def GEN_ENFER(self):
        return relationship('GENENFER')

    # ID Naturaleza de la lesión
    @declared_attr
    def ID_NATULES(self):
        return Column(ForeignKey('GEN_NATULES.ID_NATULES'), nullable=False)

    @declared_attr
    def GEN_NATULE(self):
        return relationship('GENNATULE')

    # ID Tipología
    @declared_attr
    def ID_TIPOLOGIA(self):
        return Column(ForeignKey('GEN_TIPOLOGIA.ID_TIPOLOGIA'), nullable=False)

    @declared_attr
    def GEN_TIPOLOGIA(self):
        return relationship('GENTIPOLOGIA')

    # ID Proyecto
    @declared_attr
    def ID_Proyecto(self):
        return Column(ForeignKey('GEN_PROYECTO.ID_PROYECTO'), nullable=False)

    @declared_attr
    def GEN_PROYECTO(self):
        return relationship('GENPROYECTO', primaryjoin='PROYINCIDENTE.ID_Proyecto == GENPROYECTO.ID_PROYECTO')


class PROYINCIDENTVIAL(Model):
    __tablename__ = 'PROY_INCIDENT_VIAL'

    ID_INCVIAL = Column(SmallInteger, primary_key=True, )
    Fecha = Column(Date, nullable=False,
                   info={'label': 'Fecha del incidente'})
    Hora = Column(DateTime, nullable=False,
                  info={'label': 'Hora del incidente'})
    N_Pasajeros = Column(TINYINT, nullable=False,
                         info={'label': 'Número de Pasajeros'})
    N_Lesionados = Column(TINYINT, nullable=False,
                          info={'label': 'Número de Lesionados'})

    # ID INCIDENTE
    @declared_attr
    def ID_INCIDENTE(self):
        return Column(ForeignKey('PROY_INCIDENTE.ID_INCIDENTE'), nullable=False)

    @declared_attr
    def PROY_INCIDENTE(self):
        return relationship('PROYINCIDENTE', primaryjoin='PROYINCIDENTVIAL.ID_INCIDENTE == PROYINCIDENTE.ID_INCIDENTE')

    # INCIDENTE AUTO
    @declared_attr
    def ID_AUTO(self):
        return Column(ForeignKey('PROY_INCIDE_VIAL_AUTO.ID_AUTO'), nullable=False)

    @declared_attr
    def PROY_INCIDE_VIAL_AUTO(self):
        return relationship('PROYINCIDEVIALAUTO')

    # Clima del incidente
    @declared_attr
    def ID_Clima(self):
        return Column(ForeignKey('GEN_COND_CLIMA.ID_CLIMA'), nullable=False)

    @declared_attr
    def GEN_COND_CLIMA(self):
        return relationship('GENCONDCLIMA')

    # Tipo de vía
    @declared_attr
    def ID_TipoVia(self):
        return Column(ForeignKey('GEN_COND_TIPVIA.ID_TIPOVIA'), nullable=False)

    @declared_attr
    def GEN_COND_TIPVIA(self):
        return relationship('GENCONDTIPVIA')

    # Condición de la vía
    @declared_attr
    def ID_CondicionVia(self):
        return Column(ForeignKey('GEN_COND_VIA.ID_CONDICIONVIA'), nullable=False)

    @declared_attr
    def GEN_COND_VIA(self):
        return relationship('GENCONDVIA')

    # Luz de la vía
    @declared_attr
    def ID_LUZVIA(self):
        return Column(ForeignKey('GEN_COND_LUZ.ID_LUZVIA'), nullable=False)

    @declared_attr
    def GEN_COND_LUZ(self):
        return relationship('GENCONDLUZ')

    # Clase de la vía
    @declared_attr
    def ID_CLASEVIA(self):
        return Column(ForeignKey('GEN_COND_CLASE.ID_CLASEVIA'), nullable=False)

    @declared_attr
    def GEN_COND_CLASE(self):
        return relationship('GENCONDCLASE')

    # Id Aseguradora
    @declared_attr
    def ID_ASEGURADORA(self):
        return Column(ForeignKey('GEN_ASEGU.ID_ASEGURADORA'), nullable=False)

    @declared_attr
    def GEN_ASEGU(self):
        return relationship('GENASEGU')


class REGROL(Model):
    __tablename__ = 'REG_ROL'

    ID_ROL = Column(TINYINT, primary_key=True)
    Nom_ROL = Column(CHAR(25, 'Modern_Spanish_CI_AS'), nullable=False,
                     info={'label': 'Rol del usuario'})


class SYSEVENT(Model):
    __tablename__ = 'SYS_EVENT'

    COD_EVEN = Column(CHAR(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_Modulo = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Modulo del sistema'})


class SYSMOD(Model):
    __tablename__ = 'SYS_MOD'

    ID_MODULO = Column(TINYINT, primary_key=True)
    Nom_Modulo = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Nombre del Modulo'})


class VIALAUTOESTADO(Model):
    __tablename__ = 'VIAL_AUTO_ESTADO'

    ID_ESTADO = Column(TINYINT, primary_key=True)
    Nom_Estado = Column(CHAR(15, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Estado legal del auto'})


class VIALAUTOTIPO(Model):
    __tablename__ = 'VIAL_AUTO_TIPO'

    ID_TIPOAUTO = Column(TINYINT, primary_key=True)
    Nom_TIPO = Column(CHAR(15, 'Modern_Spanish_CI_AS'), nullable=False,
                      info={'label': 'Tipo de automóvil'})


class Sysdiagram:
    __tablename__ = 'sysdiagrams'
    __table_args__ = (
        Index('UK_principal_name', 'principal_id', 'name', unique=True),
    )

    name = Column(Unicode(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, primary_key=True)
    version = Column(Integer)
    definition = Column(LargeBinary)


class GENDEPA(Model):
    __tablename__ = 'GEN_DEPA'

    ID_DEPA = Column(CHAR(2, 'Modern_Spanish_CI_AS'), primary_key=True)
    Nom_DEPA = Column(String(30, 'Modern_Spanish_CI_AS'), nullable=False,
                      info={'label': 'Departamento'})

    # ID PAIS
    @declared_attr
    def ID_PAIS(self):
        return Column(ForeignKey('GEN_PAIS.ID_PAIS'), nullable=False)

    @declared_attr
    def GEN_PAI(self):
        return relationship('GENPAI')


class GENTRABAJADOR(Model):
    __tablename__ = 'GEN_TRABAJADOR'

    CC_TRABAJ = Column(CHAR(15, 'Modern_Spanish_CI_AS'), primary_key=True,
                       info={'label': 'Documento de identidad del trabajador'})
    Fecha_Nacimiento = Column(Date, nullable=False,
                              info={'label': 'Fecha de nacimiento'})
    Nom_Trabaj = Column(String(20, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Nombres'})
    Ape1_Trabaj = Column(String(15, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Primer Apellido'})
    Ape2_Trabaj = Column(String(15, 'Modern_Spanish_CI_AS'), nullable=False,
                         info={'label': 'Segundo Apellido'})
    Edad = Column(TINYINT, nullable=False,
                  info={'label': 'Edad'})

    # ID GENERO
    @declared_attr
    def ID_GEN(self):
        return Column(ForeignKey('GEN_GENERO.ID_GEN'), nullable=False,
                      info={'label': 'Género'})

    @declared_attr
    def GEN_GENERO(self):
        return relationship('GENGENERO')

    # ID Centro de costos
    @declared_attr
    def ID_CENTROCOS(self):
        return Column(ForeignKey('GEN_CARGO_CENCOS.ID_CENTROCOS'), nullable=False,
                      info={'label': 'Centro de costos'})

    @declared_attr
    def GEN_CARGO_CENCO(self):
        return relationship('GENCARGOCENCO')

    # ID Cargo
    @declared_attr
    def ID_CARGO(self):
        return Column(ForeignKey('GEN_CARGO_TRABAJ.ID_CARGO'), nullable=False,
                      info={'label': 'Cargo'})

    @declared_attr
    def GEN_CARGO_TRABAJ(self):
        return relationship('GENCARGOTRABAJ')


class PROYINCIDEVIALAUTO(Model):
    __tablename__ = 'PROY_INCIDE_VIAL_AUTO'

    ID_AUTO = Column(CHAR(3, 'Modern_Spanish_CI_AS'), primary_key=True)
    Modelo = Column(CHAR(4, 'Modern_Spanish_CI_AS'), nullable=False,
                    info={'label': 'Modelo del auto'})
    Marca = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                   info={'label': 'Marca del automóvil'})
    Color = Column(CHAR(20, 'Modern_Spanish_CI_AS'), nullable=False,
                   info={'label': 'Color del automóvil'})
    Capacidad_Auto = Column(TINYINT, nullable=False,
                            info={'label': 'Capacidad del auto'})
    Placa_VEH = Column(String(7, 'Modern_Spanish_CI_AS'), nullable=False, unique=True,
                       info={'label': 'Placa del automóvil'})
    SOAT = Column(SmallInteger, nullable=False, unique=True,
                  info={'label': 'SOAT del automóvil'})

    @declared_attr
    def ID_TIPOAUTO(self):
        return Column(ForeignKey('VIAL_AUTO_TIPO.ID_TIPOAUTO'), nullable=False,
                      info={'label': 'Tipo de automóvil'})

    @declared_attr
    def VIAL_AUTO_TIPO(self):
        return relationship('VIALAUTOTIPO')

    @declared_attr
    def ID_ESTADO(self):
        return Column(ForeignKey('VIAL_AUTO_ESTADO.ID_ESTADO'), nullable=False,
                      info={'label': 'Estado del automóvil'})

    @declared_attr
    def VIAL_AUTO_ESTADO(self):
        return relationship('VIALAUTOESTADO')


class REGUSUSYSTEM(Model):
    __tablename__ = 'REG_USU_SYSTEM'

    DOCUMENT = Column(CHAR(15, 'Modern_Spanish_CI_AS'), primary_key=True,
                      info={'label': 'Documento de identidad'})
    Fecha = Column(DateTime, nullable=False,
                   info={'label': 'Fecha de registro'})
    Nombre = Column(String(30, 'Modern_Spanish_CI_AS'), info={'label': 'Nombres'})
    Ape1 = Column(String(50, 'Modern_Spanish_CI_AS'),
                  info={'label': 'Primer Apéllido'})
    Ape2 = Column(String(50, 'Modern_Spanish_CI_AS'),
                  info={'label': 'Segundo Apéllido'})

    # ID Rol del trabajador
    @declared_attr
    def ID_ROL(self):
        return Column(ForeignKey('REG_ROL.ID_ROL'),
                      info={'label': 'Rol del Usuario'})

    @declared_attr
    def REG_ROL(self):
        return relationship('REGROL')


class SYSDECPEVENT(Model):
    __tablename__ = 'SYS_DECP_EVENT'

    GEN_DESCP = Column(CHAR(2, 'Modern_Spanish_CI_AS'), primary_key=True,
                       info={'label': 'ID Descripción del Evento'})
    Descrip_Evento = Column(String(2, 'Modern_Spanish_CI_AS'), nullable=False,
                            info={'label': 'Descripción del evento'})

    # Codigo del evento
    @declared_attr
    def COD_EVEN(self):
        return Column(ForeignKey('SYS_EVENT.COD_EVEN'), nullable=False,
                      info={'label': 'Código del evento'})

    @declared_attr
    def SYS_EVENT(self):
        return relationship('SYSEVENT')


class GENCIUDAD(Model):
    __tablename__ = 'GEN_CIUDAD'

    ID_Ciudad = Column(CHAR(5, 'Modern_Spanish_CI_AS'), primary_key=True,
                       info={'label': 'ID Ciudad'})
    Nom_Ciudad = Column(String(30, 'Modern_Spanish_CI_AS'), nullable=False,
                        info={'label': 'Ciudad'})

    # ID Departamento
    @declared_attr
    def ID_DEPA(self):
        return Column(ForeignKey('GEN_DEPA.ID_DEPA'), nullable=False,
                      info={'label': 'Departamento'})

    @declared_attr
    def GEN_DEPA(self):
        relationship('GENDEPA')

    # ID País
    @declared_attr
    def ID_PAIS(self):
        return Column(ForeignKey('GEN_PAIS.ID_PAIS'), nullable=False,
                      info={'label': 'País'})

    @declared_attr
    def GEN_PAI(self):
        return relationship('GENPAI')


class SYSAUDITORIA(Model):
    __tablename__ = 'SYS_AUDITORIA'

    ID_AUDITORIA = Column(Numeric(18, 0), primary_key=True)
    Fecha = Column(DateTime, nullable=False)

    # Id Modulo de inscripción
    @declared_attr
    def ID_MODULO(self):
        return Column(ForeignKey('SYS_MOD.ID_MODULO'))

    @declared_attr
    def SYS_MOD(self):
        return relationship('SYSMOD')

    # ID Evento
    @declared_attr
    def Evento(self):
        return Column(ForeignKey('SYS_EVENT.COD_EVEN'))

    @declared_attr
    def SYS_EVENT(self):
        return relationship('SYSEVENT')

    # ID Descripción del evento
    @declared_attr
    def DescripEvento(self):
        return Column(ForeignKey('SYS_DECP_EVENT.GEN_DESCP'))

    @declared_attr
    def SYS_DECP_EVENT(self):
        return relationship('SYSDECPEVENT')

    # DOCUMENTO de Identidad
    @declared_attr
    def Documento(self):
        return Column(ForeignKey('REG_USU_SYSTEM.DOCUMENT'))

    @declared_attr
    def REG_USU_SYSTEM(self):
        return relationship('REGUSUSYSTEM')

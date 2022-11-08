from sqlalchemy import Column, ForeignKey, Integer, String, Time, Float
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship


# CLASE REFERENCIA PARA LOS MODELOS CREADOS


class Model(object):
    pass


class Ep(Model):  # 0
    __tablename__ = 'eps'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), unique=True)
    telefono = Column(String(10), unique=True)
    NIT = Column(String(10), unique=True)
    tipo = Column(String(20))


class Afiliado(Model):  # 1
    __tablename__ = 'afiliados'

    nombre_afiliados = Column(String(20))
    apellido_afiliados = Column(String(40))
    regimen = Column(String(10))
    documento = Column(Integer, unique=True)

    @declared_attr
    def EPS_ID(self):
        return Column(ForeignKey('eps.id'), primary_key=True)

    @declared_attr
    def historia_clinica_id(self):
        return Column(Integer, unique=True)


class Farmacia(Model):  # 2
    __tablename__ = 'farmacia'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    telefono = Column(Integer, unique=True)
    nit = Column(String(10), unique=True)
    direccion = Column(String(20))
    razon_social = Column(String(50))
    ciudad = Column(String(15), nullable=False)
    departamento = Column(String(15), nullable=False)


class Horario(Model):  # 3
    __tablename__ = 'horario'

    id = Column(Integer, primary_key=True)
    dias = Column(String(20))
    inicio_jornada = Column(Time)
    final_jornada = Column(Time)
    habitacion = Column(String(8), nullable=False)
    edificio = Column(String(8), nullable=False)


class Ip(Model):  # 4
    __tablename__ = 'ips'

    id = Column(Integer, primary_key=True)
    nombre_ips = Column(String(30))
    nit = Column(String(10), unique=True)
    nivel = Column(Integer)
    direccion = Column(String(30))
    cobertura = Column(String(20))
    tipo = Column(String(20))
    telefono = Column(Integer, unique=True)


class Jornada(Model):  # 5
    __tablename__ = 'jornada'

    id = Column(Integer, primary_key=True)
    dia = Column(Integer, unique=True)
    incio = Column(Time)
    final = Column(Time)
    IPS_ID_FK = Column(Integer)


class Servicio(Model):  # 6
    __tablename__ = 'servicio'

    id = Column(Integer, primary_key=True)
    nombre_servicio = Column(String(20), unique=True)
    tarifa = Column(Float)


class EpsFarmacia(Model): # 7
    __tablename__ = 'eps_farmacia'

    ID_EPS_Farmacia = Column(Integer, primary_key=True)

    @declared_attr
    def EPS_ID_FK(self):
        return Column(ForeignKey('eps.id'), index=True)

    @declared_attr
    def Farmacia_ID_FK(self):
        return Column(ForeignKey('farmacia.id'), index=True)

    @declared_attr
    def ep(self): return relationship('Ep')

    @declared_attr
    def farmacia(self): return relationship('Farmacia')


class EpsIp(Model):  # 8
    __tablename__ = 'eps_ips'

    EPS_IPS_PK = Column(String(45), primary_key=True, nullable=False)

    @declared_attr
    def EPS_ID(self):
        return Column(ForeignKey('eps.id'), nullable=False)

    @declared_attr
    def IPS_ID_FK(self):
        return Column(ForeignKey('ips.id'), index=True)

    @declared_attr
    def ep(self):
        return relationship('Ep')

    @declared_attr
    def ip(self):
        return relationship('Ip')


class IpsJornada(Model):  # 9
    __tablename__ = 'ips_jornada'

    IPS_Jornada_ID = Column(String(45), primary_key=True, nullable=False)

    @declared_attr
    def IPS_ID(self):
        return Column(ForeignKey('ips.id'), nullable=False)

    @declared_attr
    def Jornada_ID_FK(self):
        return Column(ForeignKey('jornada.id'), index=True)

    @declared_attr
    def ip(self):
        return relationship('Ip')

    @declared_attr
    def jornada(self):
        return relationship('Jornada')


class IpsServicio(Model):  # 10
    __tablename__ = 'ips_servicio'

    IPS_Servicio_PK = Column(String(45), primary_key=True, nullable=False)

    @declared_attr
    def IPS_ID(self):
        return Column(ForeignKey('ips.id'), nullable=False)

    @declared_attr
    def Servicio_ID_FK(self):
        return Column(ForeignKey('servicio.id'), index=True)

    @declared_attr
    def ip(self):
        return relationship('Ip')

    @declared_attr
    def servicio(self):
        return relationship('Servicio')


class Medico(Model):  # 11
    __tablename__ = 'medico'

    id = Column(Integer, primary_key=True)
    nombre_medico = Column(String(40))
    apellidos_medico = Column(String(40))
    licencia = Column(String(40), unique=True)
    especialidad = Column(String(40))
    cargo = Column(String(20))
    persona_id = Column(Integer, unique=True)

    @declared_attr
    def IPS_FK(self):
        return Column(ForeignKey('ips.id'), index=True)

    @declared_attr
    def ip(self):
        return relationship('Ip')


class MedicoHorario(Model):  # 12
    __tablename__ = 'medico_horario'

    Medico_Horario_PK = Column(String(45), primary_key=True, nullable=False)

    @declared_attr
    def Medico_ID(self):
        return Column(ForeignKey('medico.id'), nullable=False)

    @declared_attr
    def Horario_id_fk(self):
        return Column(ForeignKey('horario.id'), index=True)

    @declared_attr
    def horario(self): return relationship('Horario')

    @declared_attr
    def medico(self): return relationship('Medico')

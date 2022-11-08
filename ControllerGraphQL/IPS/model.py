import strawberry


@strawberry.type
class IPS:
    id: int
    nombre_ips: str
    nit: str
    nivel: int
    direccion: int
    cobertura: str
    tipo: str
    telefono: int

@strawberry.input
class IPSInput:
    nombre_ips: str
    nit: str
    nivel: int
    direccion: int
    cobertura: str
    tipo: str
    telefono: int

import strawberry


@strawberry.type
class Farmacia:
    id: int
    nombre: str
    telefono: str
    NIT: str
    direccion: str
    razon_social: str
    ciudad: str
    departamento: str


@strawberry.input
class FarmaciaInput:
    nombre: str
    telefono: str
    NIT: str
    direccion: str
    razon_social: str
    ciudad: str
    departamento: str

import strawberry


@strawberry.type
class Afiliados:
    nombre_afiliados: str
    apellido_afiliados: str
    regimen: str
    documento: int
    EPS_ID: int
    historia_clinica_id: int


@strawberry.input
class AfiliadosInput:
    nombre_afiliados: str
    apellido_afiliados: str
    regimen: str
    documento: int
    EPS_ID: int
    historia_clinica_id: int


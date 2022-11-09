from ControllerGraphQL.Entity.MEDICO_HORARIO.actions_graph.query import MedicoHorarioQuery
from ControllerGraphQL.Entity.EPS_FARMACIA.actions_graph.query import EPSFarmaciaQuery
from ControllerGraphQL.Entity.IPS_JORNADA.actions_graph.query import IPSJornadaQuery
from ControllerGraphQL.Entity.AFILIADOS.actions_graph.query import AfiliadosQuery
from ControllerGraphQL.Entity.SERVICIO.actions_graph.query import ServicioQuery
from ControllerGraphQL.Entity.FARMACIA.actions_graph.query import FarmaciaQuery
from ControllerGraphQL.Entity.JORNADA.actions_graph.query import JornadaQuery
from ControllerGraphQL.Entity.HORARIO.actions_graph.query import HorarioQuery
from ControllerGraphQL.Entity.EPS_IPS.actions_graph.query import EPSIPSQuery
from ControllerGraphQL.Entity.MEDICO.actions_graph.query import MedicoQuery
from ControllerGraphQL.Entity.IPS.actions_graph.query import IPSQuery
from ControllerGraphQL.Entity.EPS.actions_graph.query import EPSQuery

import strawberry


@strawberry.type
class Query(EPSQuery, FarmaciaQuery, HorarioQuery, IPSQuery, MedicoQuery, EPSIPSQuery, EPSFarmaciaQuery,JornadaQuery,IPSJornadaQuery, ServicioQuery, AfiliadosQuery, MedicoHorarioQuery):
    pass

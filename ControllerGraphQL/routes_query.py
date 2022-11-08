from ControllerGraphQL.EPS_FARMACIA.actions_graph.query import EPSFarmaciaQuery
from ControllerGraphQL.FARMACIA.actions_graph.query import FarmaciaQuery
from ControllerGraphQL.HORARIO.actions_graph.query import HorarioQuery
from ControllerGraphQL.IPS.actions_graph.query import IPSQuery
from ControllerGraphQL.EPS.actions_graph.query import EPSQuery
import strawberry


@strawberry.type
class Query(EPSQuery, FarmaciaQuery, HorarioQuery, IPSQuery, EPSFarmaciaQuery):
    pass

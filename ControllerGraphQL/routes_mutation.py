from ControllerGraphQL.EPS_FARMACIA.actions_graph.mutation import MutationEPSFarmacia
from ControllerGraphQL.FARMACIA.actions_graph.mutation import MutationFarmacia
from ControllerGraphQL.HORARIO.actions_graph.mutation import MutationHorario
from ControllerGraphQL.IPS.actions_graph.mutation import MutationIPS
from ControllerGraphQL.EPS.actions_graph.mutation import EPSMutation
import strawberry


@strawberry.type
class Mutation(EPSMutation, MutationFarmacia, MutationHorario, MutationIPS, MutationEPSFarmacia):
    pass

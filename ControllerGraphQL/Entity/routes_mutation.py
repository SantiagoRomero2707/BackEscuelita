from ControllerGraphQL.Entity.MEDICO_HORARIO.actions_graph.mutation import MutationMedicoHorario
from ControllerGraphQL.Entity.EPS_FARMACIA.actions_graph.mutation import MutationEPSFarmacia
from ControllerGraphQL.Entity.IPS_SERVICIO.actions_graph.mutation import MutationIPSServicio
from ControllerGraphQL.Entity.IPS_JORNADA.actions_graph.mutation import MutationIPSJornada
from ControllerGraphQL.Entity.AFILIADOS.actions_graph.mutation import MutationAfiliados
from ControllerGraphQL.Entity.SERVICIO.actions_graph.mutation import MutationServicio
from ControllerGraphQL.Entity.FARMACIA.actions_graph.mutation import MutationFarmacia
from ControllerGraphQL.Entity.JORNADA.actions_graph.mutation import MutationJornada
from ControllerGraphQL.Entity.HORARIO.actions_graph.mutation import MutationHorario
from ControllerGraphQL.Entity.EPS_IPS.actions_graph.mutation import EPSIPSMutation
from ControllerGraphQL.Entity.MEDICO.actions_graph.mutation import MutationMedico
from ControllerGraphQL.Entity.IPS.actions_graph.mutation import MutationIPS
from ControllerGraphQL.Entity.EPS.actions_graph.mutation import EPSMutation
import strawberry


@strawberry.type
class Mutation(MutationMedicoHorario, MutationIPSJornada, MutationJornada, MutationIPSServicio, EPSIPSMutation, MutationMedico, EPSMutation, MutationFarmacia, MutationHorario, MutationIPS, MutationEPSFarmacia, MutationServicio, MutationAfiliados):
    pass

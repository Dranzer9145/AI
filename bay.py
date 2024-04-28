from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=2,
                   values=[[0.3, 0.05, 0.9, 0.5],
                           [0.7, 0.95, 0.1, 0.5]],
                   evidence=['D', 'I'],
                   evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2,
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['G'],
                   evidence_card=[2])
cpd_s = TabularCPD(variable='S', variable_card=2,
                   values=[[0.95, 0.2],
                           [0.05, 0.8]],
                   evidence=['I'],
                   evidence_card=[2])
model.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)
print("Model is consistent:", model.check_model())
inference = VariableElimination(model)
q = inference.query(variables=['L'], evidence={'S': 0, 'D': 1})
print(q)

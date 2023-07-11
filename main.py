import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np


# Cria as variáveis fuzzy
relevancia = ctrl.Antecedent(np.arange(0, 5, 1), 'relevancia')
impacto = ctrl.Antecedent(np.arange(0, 5, 1), 'impacto')
complexidade = ctrl.Antecedent(np.arange(0, 5, 1), 'complexidade')
prioridade = ctrl.Consequent(np.arange(0, 11, 1), 'prioridade')

relevancia.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
impacto.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
complexidade.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])

prioridade['muito baixo'] = fuzz.trimf(prioridade.universe, [0, 1, 2])
prioridade['baixo'] = fuzz.trimf(prioridade.universe, [1, 3, 4])
prioridade['medio'] = fuzz.trimf(prioridade.universe, [2, 4, 6])
prioridade['alto'] = fuzz.trimf(prioridade.universe, [4, 6, 8])
prioridade['muito alto'] = fuzz.trimf(prioridade.universe, [7, 9, 10])

# Define as regras fuzzy
regras = [
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito baixo'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito baixo'] & complexidade['baixo'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito baixo'] & complexidade['medio'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito baixo'] & complexidade['alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito baixo'] & complexidade['muito alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['baixo'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['baixo'] & complexidade['baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['baixo'] & complexidade['alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['baixo'] & complexidade['muito alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['medio'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['medio'] & complexidade['baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['medio'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['medio'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['medio'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['alto'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['alto'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['alto'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['alto'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['alto'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito alto'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito alto'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito alto'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito baixo'] & impacto['muito alto'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito baixo'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito baixo'] & complexidade['baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito baixo'] & complexidade['alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito baixo'] & complexidade['muito alto'], prioridade['muito baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['baixo'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['baixo'] & complexidade['baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['baixo'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['medio'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['medio'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['medio'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['medio'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['medio'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['alto'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['alto'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['alto'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['alto'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito alto'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito alto'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito alto'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['baixo'] & impacto['muito alto'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['muito baixo'] & complexidade['muito baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['muito baixo'] & complexidade['baixo'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['muito baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['muito baixo'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['muito baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['baixo'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['baixo'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['baixo'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['medio'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['medio'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['medio'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['medio'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['medio'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['medio'] & impacto['alto'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['medio'] & impacto['alto'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['alto'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['alto'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['muito alto'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['medio'] & impacto['muito alto'] & complexidade['baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['medio'] & impacto['muito alto'] & complexidade['medio'], prioridade['alto']),
    ctrl.Rule(relevancia['medio'] & impacto['muito alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['medio'] & impacto['muito alto'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['muito baixo'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['muito baixo'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['muito baixo'] & complexidade['medio'], prioridade['baixo']),
    ctrl.Rule(relevancia['alto'] & impacto['muito baixo'] & complexidade['alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['alto'] & impacto['muito baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['alto'] & impacto['baixo'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['baixo'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['baixo'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['baixo'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['alto'] & impacto['medio'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['medio'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['medio'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['medio'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['medio'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['alto'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['alto'] & complexidade['baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['alto'] & complexidade['medio'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['alto'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['alto'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['alto'] & impacto['muito alto'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['muito alto'] & complexidade['baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['muito alto'] & complexidade['medio'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['muito alto'] & complexidade['alto'], prioridade['alto']),
    ctrl.Rule(relevancia['alto'] & impacto['muito alto'] & complexidade['muito alto'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito baixo'] & complexidade['muito baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito baixo'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito baixo'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito baixo'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito baixo'] & complexidade['muito alto'], prioridade['baixo']),
    ctrl.Rule(relevancia['muito alto'] & impacto['baixo'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['baixo'] & complexidade['baixo'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['baixo'] & complexidade['medio'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['baixo'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['baixo'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['medio'] & complexidade['muito baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['medio'] & complexidade['baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['medio'] & complexidade['medio'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['medio'] & complexidade['alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['medio'] & complexidade['muito alto'], prioridade['medio']),
    ctrl.Rule(relevancia['muito alto'] & impacto['alto'] & complexidade['muito baixo'], prioridade['muito alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['alto'] & complexidade['baixo'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['alto'] & complexidade['medio'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['alto'] & complexidade['alto'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['alto'] & complexidade['muito alto'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito alto'] & complexidade['muito baixo'], prioridade['muito alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito alto'] & complexidade['baixo'], prioridade['muito alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito alto'] & complexidade['medio'], prioridade['muito alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito alto'] & complexidade['alto'], prioridade['alto']),
    ctrl.Rule(relevancia['muito alto'] & impacto['muito alto'] & complexidade['muito alto'], prioridade['alto'])
]

# Cria o sistema de controle fuzzy
sistema_ctrl = ctrl.ControlSystem(
    regras)
sistema_simulacao = ctrl.ControlSystemSimulation(sistema_ctrl)

relevancia.view()
impacto.view()
complexidade.view()

# Entrada dos valores de preço e avaliação
relevancia_input = 4
impacto_input = 2
complexidade_input = 0

# Passa os valores de entrada para o sistema de controle fuzzy
sistema_simulacao.input['relevancia'] = relevancia_input
sistema_simulacao.input['impacto'] = impacto_input
sistema_simulacao.input['complexidade'] = complexidade_input

# Realiza a avaliação do sistema fuzzy
sistema_simulacao.compute()

# Obtém o valor de saída (previsão de vendas)
prioridade_result = sistema_simulacao.output['prioridade']

prioridade.view(sim=sistema_simulacao)

# Exibe o resultado
print(f"A prioridade para a realização dessa task é de: {prioridade_result:.2f}")

plt.show()


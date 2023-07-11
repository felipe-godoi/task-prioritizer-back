import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np


# Cria as variáveis fuzzy
historico = ctrl.Antecedent(np.arange(0, 11, 1), 'historico')
estabilidade = ctrl.Antecedent(np.arange(0, 41, 1), 'estabilidade')
risco = ctrl.Consequent(np.arange(0, 101, 1), 'risco')

historico.automf(number=3, names=['ruim', 'medio', 'bom'])
estabilidade.automf(number=3, names=['baixa', 'media', 'alta'])

risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 30])
risco['medio'] = fuzz.trimf(risco.universe, [20, 50, 80])
risco['alto'] = fuzz.trimf(risco.universe, [70, 100, 100])

# Define as regras fuzzy
regra1 = ctrl.Rule(historico['ruim'] & estabilidade['baixa'], risco['alto'])
regra2 = ctrl.Rule(historico['ruim'] & estabilidade['media'], risco['alto'])
regra3 = ctrl.Rule(historico['ruim'] & estabilidade['alta'], risco['medio'])
regra4 = ctrl.Rule(historico['medio'] & estabilidade['baixa'], risco['alto'])
regra5 = ctrl.Rule(historico['medio'] & estabilidade['media'], risco['medio'])
regra6 = ctrl.Rule(historico['medio'] & estabilidade['alta'], risco['medio'])
regra7 = ctrl.Rule(historico['bom'] & estabilidade['baixa'], risco['medio'])
regra8 = ctrl.Rule(historico['bom'] & estabilidade['media'], risco['medio'])
regra9 = ctrl.Rule(historico['bom'] & estabilidade['alta'], risco['baixo'])

# Cria o sistema de controle fuzzy
sistema_ctrl = ctrl.ControlSystem(
    [regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema_simulacao = ctrl.ControlSystemSimulation(sistema_ctrl)

historico.view()
estabilidade.view()

# Entrada dos valores de preço e avaliação
historico_input = 8
estabilidade_input = 25

historico_input = int(historico_input)
estabilidade_input = int(estabilidade_input)

# Passa os valores de entrada para o sistema de controle fuzzy
sistema_simulacao.input['historico'] = historico_input
sistema_simulacao.input['estabilidade'] = estabilidade_input

# Realiza a avaliação do sistema fuzzy
sistema_simulacao.compute()

# Obtém o valor de saída (previsão de vendas)
analise_credito = sistema_simulacao.output['risco']

# Exibe o resultado
print(f"A análise de risco de crédito é: {analise_credito:.2f}")

risco.view(sim=sistema_simulacao)


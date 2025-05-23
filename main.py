# main.py

# Importa o módulo matematica
import matematica

# Importa os módulos do pacote meu_pacote
from meu_pacote import mensagens
from meu_pacote import operacoes

# Mostra a mensagem de boas-vindas
nome_usuario = "Leonardo"  # Substitua "SeuNome" pelo seu nome
print(mensagens.boas_vindas(nome_usuario))

# Realiza e imprime os resultados das operações
resultado_soma = matematica.soma(5, 2)
print(f"Soma(5, 2): {resultado_soma}")

resultado_subtracao = matematica.subtrai(10, 4)
print(f"Subtração(10, 4): {resultado_subtracao}")

resultado_modulo = matematica.modulo(5)
print(f"Módulo(5): {resultado_modulo}")

resultado_modulo_negativo = matematica.modulo(-7)  # Testando com número negativo
print(f"Módulo(-7): {resultado_modulo_negativo}")

resultado_multiplicacao = operacoes.multiplica(3, 7)
print(f"Multiplicação(3, 7): {resultado_multiplicacao}")

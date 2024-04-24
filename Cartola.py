nome_jogador = input ("Nome do Jogador:")
valor_atual = float(input ("Valor Atual em cartoletas:"))
var_valor = float(input ("Pontuação da Rodada:"))

if valor_atual > var_valor:
    excedente = valor_atual - var_valor
    valorização = excedente * 0.5
    novo_valor = var_valor + valorização
else:
    diferencial = valor_atual - var_valor
    desvalorização = diferencial *0.4
    novo_valor = valor_atual - desvalorização

print(f"O novo valor do {nome_jogador} é {novo_valor} cartoletas.")    
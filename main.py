# main.py
from telegram_bot import enviar_mensagem
from settings import BANCA_INICIAL, RISCO_POR_OPERACAO, ATIVO_ANALISADO

def calcular_contratos():
    risco_total = BANCA_INICIAL * RISCO_POR_OPERACAO
    valor_por_ponto = 0.2  # cada contrato no mini índice vale 20 centavos por ponto
    stop_loss = 200  # pontos
    risco_por_contrato = valor_por_ponto * stop_loss
    contratos = int(risco_total / risco_por_contrato)
    return max(1, contratos)

def main():
    contratos = calcular_contratos()
    texto = f"""
🚨 OPORTUNIDADE ENCONTRADA

Ativo: {ATIVO_ANALISADO}
Direção: COMPRA (exemplo)
Entrada: 125.200
Stop: 125.000
Alvo: 125.800
Contratos: {contratos}
"""
    enviar_mensagem(texto)

if __name__ == "__main__":
    main()

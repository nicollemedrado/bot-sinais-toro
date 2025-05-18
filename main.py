import yfinance as yf
import datetime
import time
from telegram_bot import enviar_mensagem
from settings import BANCA_INICIAL, RISCO_POR_OPERACAO

# Ativos a serem analisados
ATIVOS = ["WIN=F", "WD1=F"]
INTERVALO = "5m"
PERIOD = "1d"
STOP_PONTOS = 200
VALOR_PONTO = 0.20
INTERVALO_ANALISE = 300  # segundos

def calcular_contratos():
    risco_total = BANCA_INICIAL * RISCO_POR_OPERACAO
    risco_por_contrato = STOP_PONTOS * VALOR_PONTO
    contratos = int(risco_total / risco_por_contrato)
    return max(1, contratos)

def obter_dados(ativo):
    df = yf.download(tickers=ativo, interval=INTERVALO, period=PERIOD, progress=False)
    df.dropna(inplace=True)
    df['MM9'] = df['Close'].rolling(window=9).mean()
    df['MM21'] = df['Close'].rolling(window=21).mean()
    df['RSI'] = 100 - (100 / (1 + (df['Close'].diff().clip(lower=0).rolling(14).mean() /
                                   df['Close'].diff().clip(upper=0).abs().rolling(14).mean())))
    return df

def verificar_sinal(df):
    if len(df) < 22:
        return None
    atual = df.iloc[-1]
    anterior = df.iloc[-2]

    if anterior['MM9'] < anterior['MM21'] and atual['MM9'] > atual['MM21'] and atual['RSI'] > 50:
        return "COMPRA"
    elif anterior['MM9'] > anterior['MM21'] and atual['MM9'] < atual['MM21'] and atual['RSI'] < 50:
        return "VENDA"
    return None

def dentro_do_horario():
    agora = datetime.datetime.now()
    return agora.weekday() < 5 and 9 <= agora.hour < 18

def main():
    while True:
        if dentro_do_horario():
            for ativo in ATIVOS:
                try:
                    df = obter_dados(ativo)
                    direcao = verificar_sinal(df)
                    if direcao:
                        preco = round(df['Close'].iloc[-1], 2)
                        contratos = calcular_contratos()
                        mensagem = f"""
🚨 NOVO SINAL DETECTADO

🪙 Ativo: {ativo}
📈 Direção: {'🔼 COMPRA' if direcao == 'COMPRA' else '🔽 VENDA'}
🎯 Preço atual: R$ {preco}
📊 Contratos recomendados: {contratos}
⛔ Stop técnico: {STOP_PONTOS} pontos

⏱️ Análise automatizada - {datetime.datetime.now().strftime('%d/%m %H:%M')}
"""
                        enviar_mensagem(mensagem)
                except Exception as e:
                    enviar_mensagem(f"Erro ao analisar {ativo}: {e}")
        time.sleep(INTERVALO_ANALISE)

if __name__ == "__main__":
    main()

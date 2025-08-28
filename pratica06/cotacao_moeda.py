import requests

def consultar_cotacao(codigo_moeda):
    """
    Consulta a cotação de uma moeda em relação ao Real (BRL).
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    try:
        response = requests.get(url)
        data = response.json()
        key = f"{codigo_moeda}BRL"
        if key in data:
            return data[key]
        return None
    except requests.exceptions.RequestException:
        return None

moeda_usuario = input("Digite o código da moeda (ex: USD, EUR): ").upper()

dados_cotacao = consultar_cotacao(moeda_usuario)

if dados_cotacao:
    print(f"Cotação para {moeda_usuario}/BRL:")
    print(f"Valor atual: R$ {float(dados_cotacao['bid']):.2f}")
    print(f"Valor máximo: R$ {float(dados_cotacao['high']):.2f}")
    print(f"Valor mínimo: R$ {float(dados_cotacao['low']):.2f}")

    from datetime import datetime
    print(f"Última atualização: {datetime.fromtimestamp(int(dados_cotacao['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')}")
else:
    print("Código de moeda inválido ou erro na consulta.")
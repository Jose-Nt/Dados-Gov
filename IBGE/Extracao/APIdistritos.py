from flask import Flask, jsonify
import requests

app = Flask(__name__)

#===Adquirindo amostra dos dados
@app.route('/getAmostra/ibge/localidades/distritos', methods=['GET'])
def getAmostra():

    url_api = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    response = requests.get(url_api)
    dados = response.json()

    amostra = []
    for i in range(5):
        amostra.append(dados[i])

    return jsonify(amostra)

#===Realizando print de um conjunto de dados
url_api = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
response = requests.get(url_api)
dados = response.json()
print(dados[0])

app.run(port=5000,host='localhost',debug=True)
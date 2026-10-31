from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "sistema": "Sistema CPM",
        "modulo": "Frequencia & Retencao",
        "status": "online"
    })

@app.route("/chamada/lote", methods=["POST"])
def registrar_chamada():
    dados = request.get_json() or {}
    return jsonify({
        "mensagem": "Presencas registradas com sucesso.",
        "total": len(dados.get("presencas", []))
    }), 201

if __name__ == "__main__":
    app.run(debug=True)

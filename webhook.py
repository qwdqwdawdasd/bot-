from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"âś”ď¸Ź Otrzymano dane: {data}")

    alert = data.get("alert")
    symbol = data.get("symbol")
    print(f"âžˇď¸Ź ALERT: {alert}, SYMBOL: {symbol}")

    # ZAPIS DO PLIKU (opcjonalnie)
    with open("sygnal.txt", "w") as f:
        f.write(f"{alert},{symbol}")

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

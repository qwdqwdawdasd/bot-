from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # najpierw spróbuj JSON, a jak nie pójdzie, parsuj ręcznie
    data = request.get_json(silent=True)
    if data is None:
        try:
            data = json.loads(request.data.decode('utf-8'))
        except:
            data = {"raw": request.data.decode('utf-8')}

    print(f"✔️ Otrzymano dane: {data}")

    alert = data.get("alert", data.get("raw"))
    symbol = data.get("symbol", "")
    print(f"➡️ ALERT: {alert}, SYMBOL: {symbol}")

    with open("sygnal.txt", "w", encoding="utf-8") as f:
        f.write(f"{alert},{symbol}")

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

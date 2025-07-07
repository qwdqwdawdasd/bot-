from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data is None:
        try:
            data = json.loads(request.data.decode('utf-8'))
        except:
            data = {"raw": request.data.decode('utf-8')}

    print(f"✔️ Otrzymano dane: {data}")

    event = data.get("event", data.get("raw"))
    symbol = data.get("symbol", "")

    print(f"➡️ EVENT: {event}, SYMBOL: {symbol}")

    with open("/tmp/sygnal.txt", "w", encoding="utf-8") as f:
        f.write(f"{event},{symbol}")

    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

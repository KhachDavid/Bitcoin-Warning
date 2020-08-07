import requests
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'b11223344AaadD$$r.,IIr]]tP[tu@urr'


@app.route('/', methods=['GET', 'POST'])
def index():
    global limit, rate, count

    if request.method == 'GET':
        res = requests.get("https://blockchain.info/ticker")
        if res.status_code != 200:
            raise Exception("Error: API request unsuccessful")
        data = res.json()
        rate = float(data['USD']['last'])

        # if count == 1:
           # limit = rate + 50
           # return render_template('index.html', rate=rate, limit=limit)

        try:
            limit = session.get('limit', None)
            if limit is None:
                limit = 100000000000000000

        except:
            limit = 10000000000000

        return render_template('index.html', rate=rate, limit=limit)

    if request.method == 'POST':
        res = requests.get("https://blockchain.info/ticker")
        if res.status_code != 200:
            raise Exception("Error: API request unsuccessful")
        data = res.json()
        rate = data['USD']['last']
        limit = request.form.get("limit")
        limit = float(limit)
        print(data)
        print(rate)
        session['limit'] = limit
        return render_template('index.html', rate=rate, limit=limit)


if __name__ == "__main__":
    app.run()

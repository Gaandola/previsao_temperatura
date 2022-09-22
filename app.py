from flask import Flask, render_template,request
import requests,json


app=Flask(__name__)
app.config['DEBUG'] = True
api="44bfe54347b8593634153cbfaaaddea4"


@app.route ("/")
def form():
    return render_template("form.html"),200


@app.route("/temperatura_local", methods= ["GET","POST"])
def temperatura_local():
    local = request.form["nome"]
    url= f"http://api.openweathermap.org/data/2.5/weather?q={local}&units=metric&appid={api}"
    r = requests.get(url.format(local)).json()
    dados = {  
            'cidade' :local ,
            'temperatura': r['main']['temp'],
            'icone':r['weather'][0]['icon'],
            }
    print (dados)   
    
    return render_template('previsao_tempo.html',dados=dados),200


app.run()

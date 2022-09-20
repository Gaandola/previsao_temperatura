from flask import Flask, render_template
import requests,json


app=Flask(__name__)
app.config['DEBUG'] = True
api="44bfe54347b8593634153cbfaaaddea4"
lista=[]
@app.route ("/")
def index():
    local=["São Paulo","Rio de janeiro","Salvador","Belo Horizonte","Curitiba","Rio Branco"]
    for a in local:
        url= f"http://api.openweathermap.org/data/2.5/weather?q={a}&units=metric&appid={api}"
        r = requests.get(url.format(local)).json()
        
        
        dados = {  
            'cidade' :a ,
            'temperatura': r['main']['temp'],
            'icone':r['weather'][0]['icon'],
            }
        print (dados)
        lista.append(dados)
    #print(lista)
    return render_template('previsao_tempo.html',lista=lista,l=local),200
    




app.run()

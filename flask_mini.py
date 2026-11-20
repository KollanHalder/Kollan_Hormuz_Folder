# -*- coding: utf-8 -*

from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/alldata')
def read_callpoints_Tankers():
    PORTS_monde = pd.read_excel(
        r"C:\Users\kolla\OneDrive\Desktop\Msc_GGL\3rd Semister\Geospatial and web development\Project Ormuz\Data\PORTS_monde.xlsx",
    )
    df = PORTS_monde.to_json(orient='records')
    print(PORTS_monde.shape)
    return df

    
@app.route('/')
def hello_world():
    return 'Hello my name is Kollan ggg'


if __name__ == '__main__':
    app.run(port=5050, debug=True) # Permet de lancer le serveur directement depuis python en exécutant le programme

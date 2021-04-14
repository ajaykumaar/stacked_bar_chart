from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():


    
    region_list = ['Japan', 'Asia/Pacific', 'West Europe', 'PRC', 'USA']

    percent_ai_store = [11, 21, 20, 15, 17]
    percent_ai_serv = [89, 79, 80, 85, 83]
                

    result_dict = {
        'regions': region_list,
        'title': 'Worldwide AI hardware in top 5 regions- 2020 ',
        'subtitle': 'Source: IDC 2021',
        'ai_serv': percent_ai_serv,
        'ai_store': percent_ai_store
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)

from flask import Flask, request, render_template, jsonify
from goofyahh import classifyImagePython

def startedCode(link, network="googlenet"):
    results = classifyImagePython(url=link)
    return results

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    resultFormData = ""
    if request.method == "POST":
        netwk = request.form["option"]
        user_text = request.form["text"]
        resultFormData = startedCode(user_text, netwk)
        return jsonify({'result': resultFormData})
    return render_template('index.html', result=resultFormData)

if __name__ == '__main__':
    app.run(debug=True,port=9856)
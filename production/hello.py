from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route('/', methods=['POST'])
def addRegion():
    image_url = request.form['image_url']
    result = 'Bike'
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run()
from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('index.html')

# @app.route('/index', methods=['GET'])
# def get_image():
#     image_url = request.form['image_url']
#     result = 'Bike'
#     return render_template('result.html', result=result)
@app.route("/")
def hello():
    return "Hello World!"

# @app.route('/result', methods=['GET', 'POST'])
# def home():
#     image_url = request.form['image_url']
#     result = 'Bike'
#     return redirect('result.html',result=result)

if __name__ == "__main__":
    app.run()
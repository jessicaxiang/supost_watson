from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_classification(): 
	image_url = request.form['url']
	result = "bike"
	return render_template('index.html',text=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
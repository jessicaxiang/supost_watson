from flask import Flask, request, render_template
import supost_watson as watson
app = Flask(__name__)
 
@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/", methods=['POST'])
def get_classification(): 
	image_url = request.form['url']
	result = watson.get_classification(image_url)
	is_bike = False
	is_car = False
	if result == "Bike":
		is_bike = True
	elif result == "Car":
		is_car = True
	tags = watson.get_tags(image_url)

	return render_template('index.html',tags=tags, text=result, car=is_car, bike=is_bike, img=image_url)

if __name__ == "__main__":
    app.run(debug=True)
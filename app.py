from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
	return "Hello Hacktoberfest!"

@app.route("/newfeatures")
def new_feature():
	return "This route was added by Naman Kumar"

if __name__=='__main__':
	app.run(port=5500)

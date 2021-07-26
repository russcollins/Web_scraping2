# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask app instance
app = Flask(__name__)

# Set up local mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create route rendering index.html template and documents from mongo
@app.route("/")
def index():
    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route to trigger scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
    mars_info = scrape_mars.scrape()
    mongo.db.mars_info.update({}, mars_info, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask import request
from flask import render_template
from mysqlclient import connection, search_results

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/a320', methods=["POST", "GET"])
def a320():

    if request.method=="POST":
        results = request.form
        print(results)


        data  = ("A320", results["MSN"], results["HARNESS_LENGTH"], results["GROSS_WEIGHT"],
                   results["ATMOSPHERIC_PRESSURE"], results["ROOM_TEMPERATURE"], results["AIRPORT"],
                   results["FUEL_CAPACITY_ON_LEFT"], results["FUEL_CAPACITY_ON_RIGHT"], results["FUEL_QUANTITY_ON_LEFT"],
                   results["FUEL_QUANTITY_ON_RIGHT"], results["FLIGHT_NUMBER"])

        connection(data)

        return ("data uploaded")


    else:
        return render_template("a320.html")



@app.route('/a330', methods=["POST", "GET"])
def a330():

    if request.method=="POST":
        results = request.form
        print(results)


        data  = ("A330", results["MSN"], results["HARNESS_LENGTH"], results["GROSS_WEIGHT"],
                   results["ATMOSPHERIC_PRESSURE"], results["ROOM_TEMPERATURE"], results["AIRPORT"],
                   results["FUEL_CAPACITY_ON_LEFT"], results["FUEL_CAPACITY_ON_RIGHT"], results["FUEL_QUANTITY_ON_LEFT"],
                   results["FUEL_QUANTITY_ON_RIGHT"], results["FLIGHT_NUMBER"])

        connection(data)

        return ("data uploaded")


    else:
        return render_template("a320.html")



@app.route('/search_filter', methods=["POST", "GET"])
def search_query():
    if request.method == 'POST':
        print(request.form)
        results = search_results(request.form["typo"], request.form["search"])

        return (results)


    else:
        return render_template("search_query.html")








if __name__== "__main__":
    app.run(debug=True)
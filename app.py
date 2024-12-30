from flask import Flask, jsonify, render_template
from database import load_inventory
print ("hello")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    #return 'index.html'

@app.route('/add_car')
def add_car() methods:

if request.method == 'POST':
  # Handle POST request
  # Get the values from the submitted forms
  # make, model,year, price
  new_car = request.form.to_dict();
  add_cars(new_car)
else:
  # Handle GET request
  return render_template('add_cars.html')
  
@app.route('/inventory')
def inventory():
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]

    items= load_inventory()
    return render_template('inventory.html',items=items)
    #return 'index.html'

if (__name__ == '__main__'):
  app.run(host="0.0.0.0", port=5000,debug=True)
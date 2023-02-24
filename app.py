from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengalore,India',
    'salary':'Rs. 1500000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs. 1500000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote,India',
    'salary':'Rs. 1200000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco,US',
    'salary':'$. 250000'
  },
  {
    'id':5,
    'title':'AI Engineer',
    'location':'New York,US',
    'salary':'$. 260000'
  },
  {
    'id':6,
    'title':'Data Engineer',
    'location':'New York,US',
    'salary':'$. 300000'
  }

]

@app.route("/")
def hello_flask():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
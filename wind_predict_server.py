# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file("index.html")

# Add normal route.
@app.route('/api/normal')
def wind_predict():
  return {"value": }

if __name__ == "__main__":
    
from flask import Flask, request
app = Flask(__name__)
import sys  

@app.route('/')
def index():
  return("Inference server is alive :)")

@app.route('/inference')
def nmt():
    # Run OpenNMT code
    script_descriptor = open("translate.py")
    a_script = script_descriptor.read()
    sys.argv = ["translate.py", "model model/model_step_6000.pt", "-src input.txt", "-output output.txt", "-verbose"]
    exec(a_script)
    script_descriptor.close()

    # Read output of the inference
    f = open("output.txt", "r")
    return(str(f.read()))

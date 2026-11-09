from flask import Flask , request , render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template('register.html')
@app.route("/register",methods=["POST"])
def register():
    name=request.form['name']
    email=request.form['email']
    year=request.form['year']
    return register('success.html',name=name,email=email)
if __name__=='__main__':
    app.run(localhost="0.0.0.0",port=5000,debug=True)
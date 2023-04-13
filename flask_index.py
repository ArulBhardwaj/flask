from flask import Flask,render_template
app=Flask(__name__)

@app.route("/index")
def first_webpage():

    name='Flask'

    return render_template('PRO-C116-Reference-Code-main/index.html',index_variable=name)
app.run(debug=True)
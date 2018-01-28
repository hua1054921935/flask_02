from flask import Flask,render_template,request,session,g,flash
import sys

app = Flask(__name__)
app.secret_key='mmam'


@app.route('/')
def hello_world():
    g.name='hehe'
    return render_template('demo1_index.html')
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('demo1_index.html')
@app.route('/demo/<id>', methods=['GET', 'POST'])
def demo(id):
    return 'demo id%s' %id

@app.route('/session_id', methods=['GET', 'POST'])
def session_id():
    session['name']='heima'
    flash('99999')
    return 'session'

if __name__ == '__main__':
    app.run(debug=True)

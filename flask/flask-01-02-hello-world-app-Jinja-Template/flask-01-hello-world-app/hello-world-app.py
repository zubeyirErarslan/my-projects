from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Sakarya!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'


@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

@app.route('/fifth')
def fifth():
    return 'bunu be yaptım'




if __name__ == '__main__':
    app.run(debug=True)
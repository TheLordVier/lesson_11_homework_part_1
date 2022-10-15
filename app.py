from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def page_content():
    return render_template('index_page.html')


if __name__ == '__main__':
    app.run(debug=True)


# First Flask Webpage
# Lucas Deckard
# Oct 26 2022

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('opening.html')

@app.route('/p2')
def p2():
   return render_template('profiles.html')

@app.route('/p3')
def p3():
   return render_template('ShowPage.html')

if __name__ == '__main__':
   app.run()
#Lucas Deckard 
#Website Solo Project

from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/p1')
def home():
   return render_template('opening.html')

@app.route('/')
def gohome():
    return render_template('throwawaypage.html')
@app.route('/p2')
def p2():
   return render_template('profiles.html')

@app.route('/p3')
def p3():
   return render_template('ShowPage.html')


if __name__ == '__main__':
   app.run()
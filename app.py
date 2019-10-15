import subprocess
from flask import Flask, render_template
from models import app, db, Game, Engine, Developer
'''
from create_db_games import create_games
from create_db_dev import create_developers
from create_db_engines import create_engines
'''
from create_db import create_games, create_developers,create_engines 






@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about/')
def about():
  return render_template('about.html')

@app.route('/games/')
def games():
  games = db.session.query(Game).all()
  return render_template('games.html', games = games)

@app.route('/developers/')
def developers():
  developers = db.session.query(Developer).all()
  return render_template('developers.html', developers = developers)

@app.route('/engines/')
def engines():
  engines = db.session.query(Engine).all()
  return render_template('engines.html', engines = engines)


# routing game details
@app.route('/games/<int:id>')
def game_details(id):

    game = db.session.query(Game).filter(Game.id == id).first()
    return render_template('game-details.html', game = game)

# routing engine details
@app.route('/engines/<int:id>')
def engine_details(id):

    engine = db.session.query(Engine).filter(Engine.id == id).first()
    return render_template('engines-details.html', engine = engine)

# routing dev details
@app.route('/developers/<int:id>')
def dev_details(id):

    developer = db.session.query(Developer).filter(Developer.id == id).first()
    return render_template('developer-details.html', developer = developer)

@app.route('/test/')
def test():
    p = subprocess.Popen(["python", "-m", "coverage", "run", "--branch", "test.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE)
    out, err = p.communicate()
    output = err + out
    output = output.decode("utf-8")

    return render_template("test.html", output = output)



if __name__ == "__main__":
  app.run()

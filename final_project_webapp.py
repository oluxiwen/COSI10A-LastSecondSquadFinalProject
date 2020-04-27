"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import final_project_app

app = Flask(__name__)

global state
state = {'platforms': final_project_app.platforms,
             'years': final_project_app.years,
             'publishers': final_project_app.publishers,
             'genres': final_project_app.genres,
             'platform': '',
             'year': '',
             'publisher': '',
             'genre': '',
             'limit': 10,
             'games': []}


def reset_state():
    global state
    state['platform'] = ''
    state['year'] = ''
    state['publisher'] = ''
    state['genre'] = ''
    state['limit'] = 10
    state['games'] = []


@app.route('/', methods=['GET', 'POST'])
def main():
    global state
    if request.method == 'GET':
        reset_state()

    elif request.method == 'POST':
        state['platform'] = request.form['platform']
        state['year'] = request.form['year']
        state['publisher'] = request.form['publisher']
        state['genre'] = request.form['genre']
        if request.form['limit'] == "":
            state['limit'] = 0
        else:
            state['limit'] = int(request.form['limit'])
        games = final_project_app.vgsalesinfo
        if state['platform'] is not '':
            games = final_project_app.games_by_platform(games, state['platform'])
        if state['year'] is not '':
            games = final_project_app.games_by_year(games, state['year'])
        if state['publisher'] is not '':
            games = final_project_app.games_by_publisher(games, state['publisher'])
        if state['genre'] is not '':
            games = final_project_app.games_by_genre(games, state['genre'])
        if state['limit'] > 0:
            games = final_project_app.games_with_limit(games, state['limit'])
        state['games'] = games

    return render_template('index.html',state=state)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

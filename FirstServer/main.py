from glob import escape
from flask import Flask, render_template, request
from api import get_upcoming,get_popular,get_top,get_movie_detalis


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def main_site():
    movies=get_upcoming()
    popular=get_popular()
    return render_template('First.html', movies=movies[0:4], popular=popular[0:4])


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y3zfcONHo2VXJV_CQbXmR56Kw0YqR296Bvqz_HbcbGU"
}

@app.route("/popular")
def base_path():
    page=request.args.get('page',1)
    movies=get_popular(page)
    return render_template('movie_list.html', movies=movies)

@app.route("/upcoming")
def base2_path():
    page=request.args.get('page',1)
    movies=get_upcoming(page)
    return render_template('movie_list.html', movies=movies)

@app.route("/top")
def base3_path():
    page=request.args.get('page',1)
    movies=get_top(page)
    return render_template('movie_list.html', movies=movies)

@app.route('/movie/<int:id>')
def show_movie_detalis(id):
    print('Id',id)
    movie=get_movie_detalis(id)
    print(movie)
    return render_template('detalis.html')

app.run(debug=True)
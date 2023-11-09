from glob import escape
from flask import Flask, render_template, request
from api import get_upcoming,get_popular,get_top,get_movie_detalis,get_simmilar_detalis, get_video_key
from signupform import MyForm


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY']='hera'

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
    simmilar_movies = get_simmilar_detalis(id)
    videos=get_video_key(id)
    video_key=None
    if len(videos)>=1:
        video_key=videos[0].get('key')
    return render_template('detalis.html',movie=movie, simmilar_movies=simmilar_movies[0:4],video_key=video_key)

@app.route('/registr',methods=["GET","POST"])
def registr():
    form = MyForm()
    if form.validate_on_submit():
        print(form)
    return render_template('registr.html',form=form)
  
# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     form = MyForm()
#     if form.validate_on_submit():
#         print(form)
#     return render_template('submit.html', form=form)

app.run(debug=True)
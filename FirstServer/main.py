from glob import escape
from flask import Flask, render_template, request, redirect
from api import get_upcoming,get_popular,get_top,get_movie_detalis,get_simmilar_detalis, get_video_key
from signupform import RegistrForm, LoginForm
from database import db,User

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY']='hera'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


@app.route("/")
def main_site():
    movies=get_upcoming()
    popular=get_popular()
    return render_template('First.html', movies=movies[0:4], popular=popular[0:4])

users=[

]

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
    form = RegistrForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,
              email=form.email.data,
              password=form.password.data
            )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('registr.html',form=form)

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    #print (User.query.all())
    if form.validate_on_submit():

        db_user=User.query.filter_by(username=form.username.data).first()
        if not db_user or db_user.password != form.password.data:
            return render_template('login.html',form=form, error='Invalid username or password')
        print (db_user)
        return redirect('/')
    
    return render_template('login.html',form=form)

# @app.route("/profile")
# def profile():
#     page=request.args.get('page',1)
#     movies=get_upcoming(page)
#     return render_template('profile.html')

with app.app_context():
    #db.drop_all()
    db.create_all()

app.run(debug=True)
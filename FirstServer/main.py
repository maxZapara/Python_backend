from glob import escape
from flask import Flask, render_template, request, redirect, session
from api import get_upcoming,get_popular,get_top,get_movie_detalis,get_simmilar_detalis, get_video_key
from signupform import RegistrForm, LoginForm, CommentForm
from database import db,User, Likes, Comment
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import timedelta

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY']='Sjenwomew'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = "login"
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=3)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=40)
      

@app.route("/")
def main_site():
    movies=get_upcoming()
    popular=get_popular()
    return render_template('First.html', movies=movies[0:4], popular=popular[0:4])



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

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

@app.route("/likes_movies/<int:id>")
@login_required
def like_movie(id): 
    from flask import jsonify        
    movie=get_movie_detalis(id)
    sent_movie = Likes.query.filter_by(title=movie.get('title'), user_id = current_user.id).first()
    if sent_movie:
        db.session.delete(sent_movie)
        db.session.commit()
    if not sent_movie:
        liked_movie=Likes(
            id=id,
            title=movie.get('title'),
            date=movie.get('release_date'),
            rate=movie.get('vote_average'),
            poster_path=f"http://image.tmbd.org/t/p/w200{movie.get('poster_path')}",
            user_id=current_user.id
        )
        db.session.add(liked_movie)
        db.session.commit()
    
    return jsonify({'status': 'success'})
    # return render_template('Likes_movies.html')

@app.route("/top")
def base3_path():
    page=request.args.get('page',1)
    movies=get_top(page)
    return render_template('movie_list.html', movies=movies)

@app.route('/movie/<int:id>', methods=['GET','POST'])
@login_required
def show_movie_detalis(id):
    form=CommentForm()
    if form.validate_on_submit():

        print('comment')
        content=form.content.data
        comment=Comment(content=content, user_id=current_user.id, film_id=id)
        db.session.add(comment)
        db.session.commit()
        # print(comment)
    print('Id',id)
    movie=get_movie_detalis(id)
    simmilar_movies = get_simmilar_detalis(id)
    videos=get_video_key(id)
    video_key=None

    sent_movie = Likes.query.filter_by(title=movie.get('title'), user_id = current_user.id).first()
    liked=True if sent_movie else False
    
    if len(videos)>=1:
        video_key=videos[0].get('key')
    return render_template('detalis.html', form=form, movie=movie, simmilar_movies=simmilar_movies[0:4],video_key=video_key, liked=liked)

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
        session.permanent=True
        login_user(db_user,remember=True)
        return redirect('/')
    

    
    return render_template('login.html',form=form)


@app.route("/profile")
@login_required
def profile():
    movies=current_user.liked_movies
    print (movies)
    return render_template('profile.html',movies=movies)

with app.app_context():
    #db.drop_all()
    db.create_all()

app.run(debug=True)
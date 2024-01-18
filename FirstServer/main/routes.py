from . import main
from flask_login import login_required, current_user
from .api import get_upcoming,get_popular,get_top,get_movie_detalis,get_simmilar_detalis, get_video_key
from flask import render_template, request
from .forms import CommentForm
from database import User, db, Likes, Comment


@main.route("/")
def main_site():
    # print(app.url_map)
    movies=get_upcoming()
    popular=get_popular()
    return render_template('main/First.html', movies=movies[0:4], popular=popular[0:4])


@main.route("/popular")
def base_path():
    page=request.args.get('page',1)
    movies=get_popular(page)
    return render_template('main/movie_list.html', movies=movies)

@main.route("/upcoming")
def base2_path():
    page=request.args.get('page',1)
    movies=get_upcoming(page)
    return render_template('main/movie_list.html', movies=movies)

@main.route("/likes_movies/<int:id>")
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

@main.route("/top")
def base3_path():
    page=request.args.get('page',1)
    movies=get_top(page)
    return render_template('main/movie_list.html', movies=movies)

@main.route('/movie/<int:id>', methods=['GET','POST'])
@login_required
def show_movie_detalis(id):
    form=CommentForm()
    if form.validate_on_submit():
        content=form.content.data
        comment=Comment(content=content, user_id=current_user.id, movie_id=id)
        db.session.add(comment)
        db.session.commit()

    print('Id',id)
    movie=get_movie_detalis(id)

    simmilar_movies = get_simmilar_detalis(id)
    
    videos=get_video_key(id)
    video_key=None

    #comments=Comment.query.filter_by(movie_id=id).join(User, Comment.user_id == User.id).all()
    comments=Comment.query.filter_by(movie_id=id).all()

# result = (
#     session.query(User, Address)
#     .join(Address, User.id == Address.user_id)
#     .all()
# )

# # Print the result
# for user, address in result:
#     print(f"User: {user.name}, Address: {address.email}")


    print(comments)

    sent_movie = Likes.query.filter_by(title=movie.get('title'), user_id = current_user.id).first()
    liked=True if sent_movie else False
    
    if len(videos)>=1:
        video_key=videos[0].get('key')
    return render_template('main/detalis.html', form=form, movie=movie, simmilar_movies=simmilar_movies[0:4],video_key=video_key, liked=liked, comments=comments)

@main.route("/profile")
@login_required
def profile():
    movies=current_user.liked_movies
    print (movies)
    return render_template('main/profile.html',movies=movies)

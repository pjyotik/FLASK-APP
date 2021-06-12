# Flash App [Demo app using python flask] 
    
1. Clone the Project from Github

2. Set Up Virtual Environment

    [Windows System]
    
    $ virtualenv --python <PATH>\Python\python.exe venv
    
    $ .\venv\Scripts\activate
    
    $ pip install -r requirements.txt
    
    $ deactivate

3. set up environment variables to trigger email for Reset Password

    [config.py]
    
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
4. Commands to manually connect to database and update records

    $ from flashapp import db
    
    $ db.create_all()       [create db]
      
    $ db.drop_all()         [delete db]
    
    $ from flashapp import User, Post
    
    ## Add user
    
    $ user_1 = User(username='Pranob', email='Test@gmail.com', password='password')
    $ db.session.add(user_1)
    $ db.session.commit()
    
    ## Add Posts
    
    $ post_1 = Post(title='Blog_1, content='First Post content', user_id=user.id)
    $ post_2 = Post(title='Blog_2, content='Second Post content', user_id=user.id)
    $ db.session.add(post_1)
    $ db.session.add(post_2)
    $ db.session.commit()
    
    ## Common sqlalchemy commands to query
    
    User.query.all()
    User.query.first()
    User.query.filter_by(username='pranob').all()
    User.query.filter_by(username='pranob').first()
    
    example:
        user = User.query.filter_by(username='pranob').first()
        user.id
        user.posts
        
5. Run the application

    $ python run.py
    
    
6 Deploy the application to heroku

    - Login to Heroku [ $ heroku login ]
    - Create the App  [ $ heroku create]
    - Rename the App  [ $ heroku rename demo-flask-app]
    - Push the main/master branch to heroku [ $ git push heroku main ]
    
    URL : https://my-demo-flask-app.herokuapp.com/
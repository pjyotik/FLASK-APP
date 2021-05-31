1. Clone the Project from Github

2. Set Up Virtual Environment

    [Windows System]
    $ virtualenv --python C:\Path\To\Python\python.exe venv
    
    $ .\venv\Scripts\activate
    
    $ pip install -r requirements.txt
    
    To deactivate: $ deactivate

3. set up environment variables to trigger email [Reset Password]
    [config.py]
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
4. Commands to connect with sqlalchemy database

    $ from flashapp import db
    
    [create db]
    $ db.create_all()
    [delete db]  
    $ db.drop_all()
    
    $ from flashapp import User, Post
    
    ## Adding user
    $ user_1 = User(username='Pranob', email='Test@gmail.com', password='password')
    $ db.session.add(user_1)
    $ db.session.commit()
    
    ## Adding Posts for the user
    $ post_1 = Post(title='Blog_1, content='First Post content', user_id=user.id)
    $ post_2 = Post(title='Blog_2, content='Second Post content', user_id=user.id)
    $ db.session.add(post_1)
    $ db.session.add(post_2)
    $ db.session.commit()
    
    ## sqlalchemy commands to query
    User.query.all()
    User.query.first()
    User.query.filter_by(username='pranob').all()
    User.query.filter_by(username='pranob').first()
    
    example:
        user = User.query.filter_by(username='pranob').first()
        user.id
        user.posts
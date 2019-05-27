[![Build Status](https://travis-ci.org/NehemiahLimo/Flask_Blog.svg?branch=testing)](https://travis-ci.org/NehemiahLimo/Flask_Blog)

[![Coverage Status](https://coveralls.io/repos/github/NehemiahLimo/Flask_Blog/badge.svg?branch=testing)](https://coveralls.io/github/NehemiahLimo/Flask_Blog?branch=testing)
## Flask Blog
### Intro
This is a simple Blog created with FLASK Microframework

### Functionalities
1. Create Account
2. Login.
3. View Posts, Edit post, delete post
4. Update Profile
5. Reset password via email

### Configuration
Open your `*__init__.py*` file from the project's root directory and configure the following:
```app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER', 'enter your email')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS', 'Provide you email password here')```

### How to install and run the app
First you need to clone this repo.

```sh 
$ cd Flask_Blog
$ pip install -r requirements.txt ```

### Running the App
````sh $ python run.py ```
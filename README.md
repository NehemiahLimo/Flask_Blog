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

## Setup and installation-Windows
1. Install Virtualenv 

   ```bash
         pip install virtualenv
   ```
create a virtualenv in your cloned repo
   ```bash
        virtualenv venv
   ```

2. Activate virtualenv-Windows

   ```bash
        source venv/Scripts/activate
   ```
3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```

**NB**

   - You will need to provide email and password in the ` **__init__.py** `
   ```
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER', 'nehemiahlimo02@gmail.com')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS', 'Provide you email password here')
   ```


4. Start the server
   ```
      python run.py
   ```

### Author: NehemiahLimo
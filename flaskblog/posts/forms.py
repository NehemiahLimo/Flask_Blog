from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    submit=SubmitField('Post')

    def validate_username(self, username):
        if username.data != current_user.username:            
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That Username is taken, choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            email= User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That email is taken, choose another one')

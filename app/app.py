from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A very complex and long secret key'
Bootstrap(app)

class AuthForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired()])
    password = PasswordField('Your password') 
    submit = SubmitField('Sign up')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    form = AuthForm()
    if(form.validate_on_submit()):
        print(form.email.data)
        print(form.password.data)
    return render_template('auth.html', form=form)

if __name__ == '__main__':
    app.run()

from flask import Flask,render_template
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField
from wtforms.validators import DataRequired
import confidential

app=Flask(__name__)
app.config["SECRET_KEY"]=confidential.SECRET_KEY

class CatForm(FlaskForm):
    category=SelectField("CATEGORIES ",choices=[('business', 'Business'), ('entertainment', 'Entertainment'), ('general', 'General'), ('health', 'Health'), ('science', 'Science'), ('sports', 'Sports'), ('technology', 'Technology')],validators=[DataRequired()])
    submit=SubmitField("Go")

@app.route('/',methods=["GET","POST"])
def index():
    form=CatForm()
    data=None

    if form.validate_on_submit():
        category=form.category.data
        url="https://newsapi.org/v2/top-headlines?country=IN&category={}&t&apiKey={}".format(category,confidential.api_key)
        response=requests.get(url)
        data=response.json()
    return render_template("home.html",Data=data,Form=form)

if __name__=="__main__":
    app.run(debug=True)


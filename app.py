from flask import Flask,render_template
# import pickle

# new_more_popular_df = pickle.load(open('new_more_popular.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html'
                           # ,book_name = list(new_more_popular_df['Book-Title'].values),
                           # author=list(new_more_popular_df['Book-Author'].values),
                           # image=list(new_more_popular_df['Image-URL-M'].values),
                           # votes=list(new_more_popular_df['num_ratings'].values),
                           # rating=list(new_more_popular_df['avg_ratings'].values)
                          )


if __name__ == '__main__':
    app.run(debug=True)

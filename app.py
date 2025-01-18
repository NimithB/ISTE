from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Serve Login Page
@app.route('/')
def index():
    return render_template('index.html')

# Handle Login Request
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # TODO: Add authentication logic (currently, just redirects)
    if username and password:
        return redirect(url_for('home'))
    else:
        return render_template('index.html', error="Invalid credentials")

# Serve Home Page
@app.route('/home')
def home():
    return render_template('home.html')

# Other Pages
@app.route('/pdf_to_comic')
def pdf_to_comic():
    return render_template('pdf_to_comic.html')

@app.route('/pdf_to_video')
def pdf_to_video():
    return render_template('pdf_to_video.html')

@app.route('/pronunciation')
def pronunciation():
    return render_template('pronunciation.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html')

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template

# def start_interface(app):
#     @app.route('/')
#     def index():
#         return render_template('index.html')



from flask import Flask, render_template

app = Flask(__name__)  # Flask app initialize

@app.route('/')
def index():
    return render_template('index.html')  # Ensure 'templates/index.html' exists

def start_interface():
    app.run(debug=True)  # Run Flask server

if __name__ == "__main__":
    start_interface()

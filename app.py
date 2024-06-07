from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def serve_template_file():
    # Get the list of files in the static directory
    static_folder = os.path.join(app.root_path, 'static')
    files = os.listdir(static_folder)
    # Pass the list of files to the template
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",  port=80)


# pyinstaller --name MyFlaskApp --onefile app.py
# pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py

# pyinstaller -w --add-data "templates;templates" --add-data "static;static" app.py
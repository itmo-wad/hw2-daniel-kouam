from flask import Flask , request, send_from_directory, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/img')
def img():
    return render_template('image.html')

@app.route('/img/<path:path>')
def index2(path):
    return send_from_directory('static/img', path)  # Send files from current directory

def write_to_file(filename, data):
    '''Handle the process of writing data to a file.'''
    with open(filename, 'a') as file:
        file.writelines(data)

def get_all_messages():
    '''Get all of the messages and separate them by a `br`.'''
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
    return messages


@app.route('/chat', methods=['GET', 'POST'])
def form():
    """Main Page with instructions."""
    # Handle POST request
    if request.method == "POST":
        # print(request.form)
        # with open("data/users.txt", "a") as user_list:
        #     user_list.write(request.form["username"] + "\n")
        fname = request.form.get("fname")
        message = request.form.get("message")
        write_to_file("data/users.txt", request.form["fname"] + "\n")
        write_to_file("data/messages.txt", request.form["message"] + "\n")
        return render_template("cabinet.html", fname=fname, message=message)
    else:
          return render_template("cabinet.html")


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)


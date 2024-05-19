from flask import Flask, render_template, request, redirect

app =  Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        # will Handle form submission and add expense

        
        
        return redirect(url_for('index'))
    return render_template('add_expense.html')







if __name__ == "__main__":
    app.run(debug = True)

# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    nums = [int(num) for num in request.form.getlist('nums')]
    solution = solve_game(nums)
    if solution:
        return redirect(url_for('results', solution=solution))
    else:
        return render_template('index.html', error='No solution found')

@app.route('/results')
def results():
    solution = request.args.get('solution')
    return render_template('results.html', solution=solution)

def solve_game(nums):
    # Logic to solve the Game of 24
    pass

if __name__ == '__main__':
    app.run(debug=True)

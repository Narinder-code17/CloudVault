from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

tasks = {}
task_id = 1

# HTML Template (inside Python) with Advanced CSS
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🌟 Stylish To-Do List</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(120deg, #89f7fe, #66a6ff);
            text-align: center;
            padding: 30px;
        }
        h1 {
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }
        .container {
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.25);
        }
        form input {
            padding: 12px;
            width: 70%;
            border: 2px solid #66a6ff;
            border-radius: 10px;
            outline: none;
            font-size: 15px;
        }
        button {
            padding: 12px 18px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 15px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: linear-gradient(135deg, #5a67d8, #6b46c1);
            transform: scale(1.05);
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin-top: 20px;
        }
        li {
            background: #fdfdfd;
            margin: 12px auto;
            padding: 14px;
            border-radius: 12px;
            width: 90%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.12);
            transition: 0.2s;
        }
        li:hover {
            transform: scale(1.02);
            background: #f7faff;
        }
        li.completed {
            text-decoration: line-through;
            color: #777;
            background: #e0e0e0;
        }
        .actions a {
            text-decoration: none;
            margin-left: 12px;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 14px;
            transition: 0.2s;
        }
        .done {
            background: #38a169;
            color: white;
        }
        .done:hover {
            background: #2f855a;
        }
        .delete {
            background: #e53e3e;
            color: white;
        }
        .delete:hover {
            background: #c53030;
        }
    </style>
</head>
<body>
    <h1>🌟 Stylish To-Do List App</h1>
    <div class="container">
        <!-- Add Task Form -->
        <form action="/add" method="POST">
            <input type="text" name="description" placeholder="Enter a new task..." required>
            <button type="submit">➕ Add Task</button>
        </form>

        <h2>Your Tasks</h2>
        <ul>
            {% for tid, task in tasks.items() %}
                <li class="{% if task.completed %}completed{% endif %}">
                    {{ tid }}. {{ task.description }}
                    <div class="actions">
                        {% if not task.completed %}
                            <a class="done" href="/complete/{{ tid }}">✅ Done</a>
                        {% endif %}
                        <a class="delete" href="/delete/{{ tid }}">❌ Delete</a>
                    </div>
                </li>
            {% else %}
                <li>No tasks yet! 🎉</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id
    desc = request.form.get("description")
    if desc:
        tasks[task_id] = {"description": desc, "completed": False}
        task_id += 1
    return redirect(url_for("index"))

@app.route('/complete/<int:tid>')
def mark_done(tid):
    if tid in tasks:
        tasks[tid]["completed"] = True
    return redirect(url_for("index"))

@app.route('/delete/<int:tid>')
def delete_task(tid):
    if tid in tasks:
        del tasks[tid]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

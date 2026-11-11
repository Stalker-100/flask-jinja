from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'site_name': 'сайт',
        'user': {
            'name': 'павел',
            'is_admin': False
        },
        'tasks': [
            'Отжимания',
            'Отжимания x2',
            'Пресс'
        ]
    }
    # из словаря context в шаблон
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)


env = Environment(loader=FileSystemLoader('templates'))


template = env.get_template('index.html')

rendered_html = template.render(context)
print(rendered_html)

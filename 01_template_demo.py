from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)
app.config.update({
    'DEBUG' : True,
    'TEMPLATES_AUTO_RELOAD' : True
})

@app.route('/')
def hello_world():
    context = {
        'create_time': datetime(2019,6,23,20,0,0),
        'username' : 'zhiliao1',
        'users' : ['zhiliao1','zhiliao2','zhiliao3'],
        'person' : {'name':'Joey','age':38,'salary': 40000,'wealth': 2000000},
        'books':[
            {'name': 'Shui hu', 'author': 'luo guanzhong','price': 110},
            {'name': 'Xi you', 'author': 'wu chengen', 'price': 90},
            {'name': 'hong loumeng', 'author': 'cao xueqin', 'price': 200},
        ]
    }
    return render_template('index.html',**context)

@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp<60 :
            return 'just now'
        elif timestamp < 3600:
            mimutes = int(timestamp / 60)
            return '%s munites ago' %mimutes
        else:
            hour = int(timestamp / (60*60))
            return  '%s hours ago' %hour
    else:
        return time

if __name__ == '__main__':
    app.run()
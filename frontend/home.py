from flask import render_template
from .app import frontend_app
from flask import request,redirect

@frontend_app.route('/')
def index():
    return render_template('index.html')


@frontend_app.route('/sample_page')
def sample_page():
    return render_template('sample_page.html')


@frontend_app.route('/world_123')
def world():
    return render_template('meroProject.html')




@frontend_app.route('/Walmart_trip')
def Walmart_trip():
    desc_about = request.args.get('desc_about')
    if desc_about is None:
        print('Desc about is null')

    else:
        print('Desc about is not null', desc_about)
        if desc_about == 'transport':
            data = 'Nepal has an awesome transportation system.'

        else:
            data = 'We don\'t have that kind of data'

    print('data is', data)
    return render_template('walmarttrip.html', Southeastern=data)


@frontend_app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')

    login_message=''
    if username is None: #username is null
        print('No username supplied')
    else:
        print('username supplied')
        print(username,password)
        if username == 'sanjay' and password == 'king':
            credentials_match = True
        else:
            credentials_match = False

        if credentials_match == True:
            print('Launching the rocket in 3..2..1...')
            return redirect('https://www.facebook.com')
        else:
            login_message = "Invalid login!!"

    return render_template('login.html',login_message=login_message)






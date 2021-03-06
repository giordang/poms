from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, PomsForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User, Poms
from app.functions.pomsCalculations import pomsCalculator, pomsGrapher


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home Page', poms=poms)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    #poms = [ 
    #    {'athlete':user, 'tense': 'tense'},
    #    {'athlete':user, 'tense': 'tense2'} 
    #]
    poms = Poms.query.filter_by(user_id=current_user.id).all()
    return render_template('user.html', user=user, poms=poms)


@app.route('/poms', methods=['GET','POST'])
@login_required
def poms():
    form = PomsForm()
    if form.validate_on_submit():
        #pomsCalculator(form)
        #pomsGrapher()
        #return redirect(url_for('poms'))
        #user = User.query.filter_by(username=username).first_or_404()
        #poms = Poms.query.filter_by(user_id=current_user.id).all()
        #return render_template('user.html', user=user, poms=poms)
        return redirect(url_for('user', username=current_user.username))
    #print(form.errors)
    poms = Poms.query.filter_by(user_id=current_user.id).all()
    return render_template('poms.html', title='POMS', form=form, poms=poms)
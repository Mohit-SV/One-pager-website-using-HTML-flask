from flask import render_template, flash, redirect, url_for, request
import flask
from app import app, db
from app.forms import ContactForm
from app.models import User, Product
from app.email import send_email


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About us')


@app.route('/products')
def products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('products', page=products.next_num) \
        if products.has_next else None
    prev_url = url_for('products', page=products.prev_num) \
        if products.has_prev else None
    return render_template('products.html', title='Products',
                           products=products.items, next_url=next_url, prev_url=prev_url)


@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            user = User(name=form.name.data, email=form.email.data, mobile=form.mobile.data,
                        message=form.message.data)
            db.session.add(user)
            db.session.commit()
            send_email(user)
            flash('Thank you for reaching us.')
            return redirect('/home')
    return render_template('contact_us.html', title='Contact us', form=form)

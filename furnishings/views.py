from flask import Blueprint, render_template, url_for, request, session, flash, redirect, abort
from .models import Category, Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

main_bp = Blueprint('main', __name__)


# Home page
@main_bp.route('/')
def index():
    categories = db.session.scalars(db.select(Category).order_by(Category.id)).all()
    products=db.session.scalars(db.select(Product).order_by(Product.id)).all()
    return render_template('index.html', categories=categories, products=products)

# Search product
@main_bp.route('/products')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    products = Product.query.filter( (Product.description.like(search)) | (Product.name.like(search))
    ).all()
    return render_template('product_list.html', products=products)

# View all the products of a category
@main_bp.route('/products/<int:category_id>')
def categories(category_id):
    categories = db.session.scalars(db.select(Category).order_by(Category.id)).all()
    products = db.session.scalars(db.select(Product).where(Product.category_id==category_id)).all()
    return render_template('product_list.html', products=products,categories=categories)

# View product detail
@main_bp.route('/products/detail/<int:product_id>')
def product(product_id):
    categories = db.session.scalars(db.select(Category).order_by(Category.id)).all()
    product = db.session.scalars(db.select(Product).where(Product.id==product_id)).first()
    return render_template('product_detail.html',product=product,categories=categories)

# Stubs for routes not implemented yet
# (url_for links in the templates will fail without these routes defined)
@main_bp.route('/order', methods=['POST','GET'])
def order():
    categories = db.session.scalars(db.select(Category).order_by(Category.id)).all()
    product_id = request.values.get('product_id')
    print(f'Values: {product_id}')
    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        print(f'retrieve order')
        # order will be None if order_id/session is stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('Failed trying to create a new order!')
            order = None
    
    # calculate total price
    total_price = 0
    if order is not None:
        for product in order.products:
            total_price += product.price
    
   # Are we adding an item?
    if product_id is not None and order is not None:
        product = db.session.scalars(db.select(Product).where(Product.id==product_id)).first()
        try:
            order.products.append(product)
            for product in order.products:
                total_price += product.price
            order.total_cost = total_price
            db.session.commit()
            print('product is added')
        except:
            flash('There was an issue adding the item to your basket', category='danger')
        return redirect(url_for('main.order'))
    return render_template('order.html', order=order, total_price=total_price,categories=categories)

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    print(f'Tour to delete ID is: {id}')
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        if not order:
            flash("There's no order to delete!")
            return redirect(request.referrer)
        print(order.products)
        product_to_delete = db.session.scalar(db.select(Product).where(Product.id==id))
        print(f'Deleting: {product_to_delete.name}')
        try:
            product_to_delete.qty = 0
            order.products.remove(product_to_delete)
            db.session.commit()
        except:
            print('Something went wrong when trying to delete the order')
            abort(500)
    return redirect(url_for('main.order'))

# Empty basket
@main_bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        for product in order.products:
            order.products.remove(product)
        session.pop('order_id')
        db.session.commit()
        flash('Basket emptied!')
    else:
        flash("There's no order to delete!")
        return redirect(request.referrer)
    return redirect(url_for('main.order'))

# Complete the order
@main_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = db.session.scalar(db.select(Order).where(Order.id==session['order_id']))
        
        if not order.products:
            flash('You need to add some tours to your basket first!')
            return(redirect(request.referrer))
        
        if form.validate_on_submit():
            order.status = True
            order.first_name = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            total_cost = 0
            for product in order.products:
                total_cost += product.price
                order.total_cost = total_cost
                order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! One of our team members will contact you soon.')
                return redirect(url_for('main.index'))
            except:
                flash('There was an issue completing your order')
                return (redirect(request.referrer))
    return render_template('checkout.html', form=form)

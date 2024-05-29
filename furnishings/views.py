from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Product, Order
from . import db

main_bp = Blueprint('main', __name__)


# Home page
@main_bp.route('/')
def index():
    categories = db.session.scalars(db.select(Category).order_by(Category.id)).all()
    return render_template('base.html', categories=categories)

# View all the tours of a city
@main_bp.route('/products/<int:category_id>')
def categories(category_id):
    products = db.session.scalars(db.select(Product).where(Product.category_id==category_id)).all()
    return render_template('product.html', products=products)


# Stubs for routes not implemented yet
# (url_for links in the templates will fail without these routes defined)
@main_bp.route('/order', methods=['POST','GET'])
def order():
    return 'not implemented yet'

@main_bp.route('/deleteorder')
def deleteorder():
    return 'not implemented yet'

@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    return 'not implemented yet'

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    return 'not implemented yet'
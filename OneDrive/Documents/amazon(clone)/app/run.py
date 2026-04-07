import os
import sys

# Get the app directory
app_dir = os.path.dirname(os.path.abspath(__file__))

# Add app directory to path for imports when run directly
sys.path.insert(0, app_dir)

from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate

# Import models - works both as direct script and as module
try:
    from .models import db, User, Product, CartItem, Order, OrderItem, Wishlist, Review, Settings, Category, Shop, Role, PaymentMethod, OrderTracking
except ImportError:
    from models import db, User, Product, CartItem, Order, OrderItem, Wishlist, Review, Settings, Category, Shop, Role, PaymentMethod, OrderTracking

from werkzeug.utils import secure_filename
from datetime import datetime
from functools import wraps

# Get the base directory (amazon(clone) folder)
basedir = os.path.dirname(app_dir)

# Use absolute paths for Flask
template_dir = os.path.join(app_dir, 'templates')
static_dir = os.path.join(app_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "amazon_clone.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create upload folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Admin decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:  # Admin ID = 1
            flash('Admin access required', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Context processor to make settings available in all templates
@app.context_processor
def inject_settings():
    settings = Settings.query.first()
    return {'settings': settings}

# ============== AUTHENTICATION ROUTES ==============

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user_type = request.form.get('user_type', 'buyer')  # buyer or seller

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))

        user = User(username=username, email=email, user_type=user_type)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', orders=orders)

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.phone = request.form.get('phone')
        current_user.address = request.form.get('address')
        current_user.city = request.form.get('city')
        current_user.country = request.form.get('country')
        current_user.postal_code = request.form.get('postal_code')
        db.session.commit()
        flash('Profile updated successfully', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html')

# ============== PRODUCT ROUTES ==============

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', None)
    search = request.args.get('search', None)

    query = Product.query

    if category:
        query = query.filter_by(category=category)
    
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%') | 
                           Product.description.ilike(f'%{search}%'))

    products = query.paginate(page=page, per_page=12)
    categories = db.session.query(Product.category).distinct().all()
    
    return render_template('index.html', products=products, categories=categories, search=search)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    reviews = Review.query.filter_by(product_id=product_id).all()
    in_wishlist = False
    
    if current_user.is_authenticated:
        in_wishlist = Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first() is not None

    return render_template('product_detail.html', product=product, reviews=reviews, in_wishlist=in_wishlist)

@app.route('/product/<int:product_id>/reviews', methods=['POST'])
@login_required
def add_review(product_id):
    product = Product.query.get_or_404(product_id)
    
    # Check if user already reviewed
    existing_review = Review.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing_review:
        flash('You have already reviewed this product', 'warning')
        return redirect(url_for('product_detail', product_id=product_id))

    rating = request.form.get('rating', type=int)
    title = request.form.get('title')
    comment = request.form.get('comment')

    # Check if user has purchased
    purchased = OrderItem.query.filter_by(product_id=product_id).join(
        Order, OrderItem.order_id == Order.id
    ).filter(Order.user_id == current_user.id, Order.status == 'Delivered').first() is not None

    review = Review(
        user_id=current_user.id,
        product_id=product_id,
        rating=rating,
        title=title,
        comment=comment,
        verified_purchase=purchased
    )

    # Update product rating
    all_reviews = Review.query.filter_by(product_id=product_id).all()
    total_rating = sum([r.rating for r in all_reviews]) + rating
    product.rating = total_rating / (len(all_reviews) + 1)
    product.reviews_count = len(all_reviews) + 1

    db.session.add(review)
    db.session.commit()

    flash('Review added successfully!', 'success')
    return redirect(url_for('product_detail', product_id=product_id))

# ============== CART ROUTES ==============

@app.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum([item.product.discount_price or item.product.price * item.quantity for item in cart_items])
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', 1, type=int)

    existing_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if existing_item:
        existing_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/cart/update/<int:item_id>', methods=['POST'])
@login_required
def update_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    quantity = request.form.get('quantity', 1, type=int)
    item.quantity = max(1, quantity)
    db.session.commit()
    
    flash('Cart updated', 'info')
    return redirect(url_for('cart'))

@app.route('/cart/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    db.session.delete(item)
    db.session.commit()
    
    flash('Item removed from cart', 'info')
    return redirect(url_for('cart'))

@app.route('/cart/clear', methods=['POST'])
@login_required
def clear_cart():
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('Cart cleared', 'info')
    return redirect(url_for('cart'))

# ============== WISHLIST ROUTES ==============

@app.route('/wishlist')
@login_required
def wishlist():
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@app.route('/wishlist/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_wishlist(product_id):
    product = Product.query.get_or_404(product_id)
    
    existing = Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing:
        flash('Already in wishlist', 'info')
        return redirect(request.referrer or url_for('index'))

    wishlist_item = Wishlist(user_id=current_user.id, product_id=product_id)
    db.session.add(wishlist_item)
    db.session.commit()

    flash(f'{product.name} added to wishlist!', 'success')
    return redirect(request.referrer or url_for('index'))

@app.route('/wishlist/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_from_wishlist(item_id):
    item = Wishlist.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    db.session.delete(item)
    db.session.commit()
    
    flash('Removed from wishlist', 'info')
    return redirect(url_for('wishlist'))

# ============== CHECKOUT & ORDERS ==============

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('cart'))

    if request.method == 'POST':
        # Create order
        total_price = sum([item.product.discount_price or item.product.price * item.quantity for item in cart_items])
        
        shipping_address = f"{request.form.get('address')}, {request.form.get('city')}, {request.form.get('country')} {request.form.get('postal_code')}"
        
        order = Order(
            user_id=current_user.id,
            total_price=total_price,
            status='Processing',
            shipping_address=shipping_address
        )

        for item in cart_items:
            order_item = OrderItem(
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.discount_price or item.product.price
            )
            order.items.append(order_item)
            
            # Update stock
            item.product.stock -= item.quantity

        db.session.add(order)
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()

        flash('Order placed successfully! Proceeding to payment...', 'success')
        return redirect(url_for('payment', order_id=order.id))

    total = sum([item.product.discount_price or item.product.price * item.quantity for item in cart_items])
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/payment/<int:order_id>', methods=['GET', 'POST'])
@login_required
def payment(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    if request.method == 'POST':
        # Simulate payment processing
        order.payment_status = 'Completed'
        order.status = 'Shipped'
        db.session.commit()

        flash('Payment successful! Your order is being processed.', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))

    return render_template('payment.html', order=order)

@app.route('/order/confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    return render_template('order_confirmation.html', order=order)

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', orders=user_orders)

@app.route('/order/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 401

    return render_template('order_detail.html', order=order)

# ============== ADMIN ROUTES ==============

@app.route('/admin')
@admin_required
def admin_dashboard():
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_users = User.query.count()
    total_revenue = db.session.query(db.func.sum(Order.total_price)).scalar() or 0
    recent_orders = Order.query.order_by(Order.ordered_at.desc()).limit(5).all()

    return render_template('admin/dashboard.html', 
                         total_products=total_products,
                         total_orders=total_orders,
                         total_users=total_users,
                         total_revenue=total_revenue,
                         recent_orders=recent_orders)

@app.route('/admin/products', methods=['GET', 'POST'])
@admin_required
def admin_products():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price', type=float)
        discount_price = request.form.get('discount_price', type=float)
        stock = request.form.get('stock', type=int)
        category = request.form.get('category')
        image_url = request.form.get('image_url')

        product = Product(
            name=name,
            description=description,
            price=price,
            discount_price=discount_price,
            stock=stock,
            category=category,
            image_url=image_url
        )

        db.session.add(product)
        db.session.commit()

        flash(f'Product "{name}" added successfully!', 'success')
        return redirect(url_for('admin_products'))

    products = Product.query.all()
    return render_template('admin/products.html', products=products)

@app.route('/admin/product/<int:product_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = request.form.get('price', type=float)
        product.discount_price = request.form.get('discount_price', type=float)
        product.stock = request.form.get('stock', type=int)
        product.category = request.form.get('category')
        product.image_url = request.form.get('image_url')

        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_products'))

    return render_template('admin/edit_product.html', product=product)

@app.route('/admin/product/<int:product_id>/delete', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash(f'Product "{product.name}" deleted!', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/orders')
@admin_required
def admin_orders():
    orders = Order.query.all()
    return render_template('admin/orders.html', orders=orders)

@app.route('/admin/order/<int:order_id>', methods=['GET', 'POST'])
@admin_required
def admin_order_detail(order_id):
    order = Order.query.get_or_404(order_id)

    if request.method == 'POST':
        order.status = request.form.get('status')
        if order.status == 'Delivered':
            order.delivered_at = datetime.utcnow()
        db.session.commit()
        flash('Order status updated!', 'success')
        return redirect(url_for('admin_orders'))

    return render_template('admin/order_detail.html', order=order)

@app.route('/admin/users')
@admin_required
def admin_users():
    users = User.query.all()
    return render_template('admin/users.html', users=users)

# ============== ADMIN CATEGORIES ==============

@app.route('/admin/categories', methods=['GET', 'POST'])
@admin_required
def admin_categories():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        icon = request.form.get('icon')
        
        if Category.query.filter_by(name=name).first():
            flash('Category already exists', 'danger')
            return redirect(url_for('admin_categories'))
        
        category = Category(name=name, description=description, icon=icon)
        db.session.add(category)
        db.session.commit()
        flash(f'Category "{name}" added successfully!', 'success')
        return redirect(url_for('admin_categories'))
    
    categories = Category.query.order_by(Category.display_order).all()
    return render_template('admin/categories.html', categories=categories)

@app.route('/admin/category/<int:category_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    
    if request.method == 'POST':
        category.name = request.form.get('name')
        category.description = request.form.get('description')
        category.icon = request.form.get('icon')
        category.is_active = request.form.get('is_active') == 'on'
        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('admin_categories'))
    
    return render_template('admin/edit_category.html', category=category)

@app.route('/admin/category/<int:category_id>/delete', methods=['POST'])
@admin_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    name = category.name
    db.session.delete(category)
    db.session.commit()
    flash(f'Category "{name}" deleted!', 'success')
    return redirect(url_for('admin_categories'))

# ============== ADMIN SETTINGS ==============

@app.route('/admin/settings', methods=['GET', 'POST'])
@admin_required
def admin_settings():
    settings = Settings.query.first()
    
    if not settings:
        settings = Settings(site_name='Local Marts')
        db.session.add(settings)
        db.session.commit()
    
    if request.method == 'POST':
        settings.site_name = request.form.get('site_name')
        settings.tagline = request.form.get('tagline')
        settings.contact_email = request.form.get('contact_email')
        settings.contact_phone = request.form.get('contact_phone')
        settings.contact_address = request.form.get('contact_address')
        settings.contact_city = request.form.get('contact_city')
        settings.contact_country = request.form.get('contact_country')
        settings.contact_postal_code = request.form.get('contact_postal_code')
        settings.whatsapp_number = request.form.get('whatsapp_number')
        settings.map_url = request.form.get('map_url')
        settings.about_us = request.form.get('about_us')
        settings.privacy_policy = request.form.get('privacy_policy')
        settings.terms_conditions = request.form.get('terms_conditions')
        settings.return_policy = request.form.get('return_policy')
        settings.shipping_policy = request.form.get('shipping_policy')
        settings.facebook_url = request.form.get('facebook_url')
        settings.instagram_url = request.form.get('instagram_url')
        settings.twitter_url = request.form.get('twitter_url')
        settings.linkedin_url = request.form.get('linkedin_url')
        settings.youtube_url = request.form.get('youtube_url')
        
        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('admin_settings'))
    
    return render_template('admin/settings.html', settings=settings)

# ============== FORGOT PASSWORD ==============

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        
        if user:
            # In production, send email with reset token
            # For now, store reset token in session
            import secrets
            reset_token = secrets.token_urlsafe(32)
            session[f'reset_token_{email}'] = reset_token
            flash('Password reset link sent to your email!', 'info')
            return redirect(url_for('reset_password', token=reset_token, email=email))
        else:
            flash('Email not found in our system', 'danger')
    
    return render_template('forgot_password.html')

@app.route('/reset-password/<token>/<email>', methods=['GET', 'POST'])
def reset_password(token, email):
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if new_password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('reset_password', token=token, email=email))
        
        user = User.query.filter_by(email=email).first()
        if user:
            user.set_password(new_password)
            db.session.commit()
            flash('Password reset successfully! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token, email=email)

# ============== CHANGE PASSWORD ==============

@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if not current_user.check_password(old_password):
            flash('Old password is incorrect', 'danger')
            return redirect(url_for('change_password'))
        
        if new_password != confirm_password:
            flash('New passwords do not match', 'danger')
            return redirect(url_for('change_password'))
        
        current_user.set_password(new_password)
        db.session.commit()
        flash('Password changed successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('change_password.html')

# ============== CONTACT PAGES ==============

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    settings = Settings.query.first()
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Store contact message (can be used to send email later)
        # For now, just flash success
        flash('Thank you for contacting us! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', settings=settings)

@app.route('/about')
def about():
    settings = Settings.query.first()
    return render_template('about.html', settings=settings)

# ============== ERROR HANDLERS ==============

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

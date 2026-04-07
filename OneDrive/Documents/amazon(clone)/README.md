# Amazon Clone - E-Commerce Application

A complete e-commerce platform built with Flask, HTML, CSS, and SQLite database.

## Features Included

### User Features
- 🔐 **Authentication**: User registration and login
- 🛍️ **Shopping Cart**: Add/remove items, update quantities
- 💳 **Checkout**: Complete checkout process with payment simulation
- 📦 **Orders**: Track order history and order details
- ❤️ **Wishlist**: Save favorite products
- ⭐ **Reviews**: Leave and view product reviews with ratings
- 👤 **Profile**: Manage user profile and addresses

### Product Features
- 📱 **Product Catalog**: Browse products by category
- 🔍 **Search**: Search products by name or description
- 📊 **Product Details**: Detailed product information with images
- 💰 **Discounts**: Display original and discounted prices
- ⭐ **Ratings**: Average ratings and review counts

### Admin Features
- 📊 **Dashboard**: Overview of sales, orders, users, revenue
- 📦 **Product Management**: Add, edit, delete products
- 📋 **Order Management**: View and update order status
- 👥 **User Management**: View all registered users

## Project Structure

```
amazon(clone)/
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── payment.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── wishlist.html
│   │   ├── profile.html
│   │   ├── edit_profile.html
│   │   ├── orders.html
│   │   ├── order_detail.html
│   │   ├── order_confirmation.html
│   │   ├── admin/
│   │   │   ├── dashboard.html
│   │   │   ├── products.html
│   │   │   ├── edit_product.html
│   │   │   ├── orders.html
│   │   │   └── users.html
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── models.py
│   └── run.py
├── requirements.txt
├── seed.py
└── README.md
```

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Steps

1. **Clone/Navigate to the project folder**
   ```bash
   cd amazon(clone)
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Seed the database with sample data**
   ```bash
   python seed.py
   ```
   
   This creates:
   - Admin account (username: `admin`, password: `admin123`)
   - Test account (username: `testuser`, password: `test123`)
   - 12 sample products in various categories

4. **Run the Flask application**
   ```bash
   python app/run.py
   ```

5. **Open in browser**
   - Navigate to: `http://127.0.0.1:5000`

## Usage

### User Registration & Login
- Register new account
- Login with credentials
- Update profile with shipping address

### Shopping
- Browse products by category
- Search for products
- View detailed product information
- Add products to cart
- Update quantities or remove items
- Proceed to checkout

### Checkout & Payment
- Enter shipping address
- Review order summary
- Complete payment (demo payment form)
- See order confirmation

### Orders & Tracking
- View order history
- Track order status (Pending → Processing → Shipped → Delivered)
- View order details and items

### Wishlist
- Add products to wishlist
- Remove items from wishlist
- Add wishlist items to cart

### Reviews
- Leave product reviews with ratings
- View verified purchase badge on reviews
- See average product ratings

### Admin Panel
- Access at `/admin` (only for admin user)
- **Dashboard**: View key metrics
- **Products**: Add, edit, delete products
- **Orders**: View all orders and update status
- **Users**: View registered users

## Default Credentials

### Admin
- **Username**: `admin`
- **Password**: `admin123`

### Test User
- **Username**: `testuser`
- **Password**: `test123`

## Database

The application uses SQLite database (`amazon_clone.db`) with the following tables:
- `user` - User accounts
- `product` - Product catalog
- `cart_item` - Shopping cart items
- `order` - Customer orders
- `order_item` - Items in each order
- `wishlist` - User wishlist items
- `review` - Product reviews

## Technologies Used

**Backend:**
- Flask 3.0.0 - Web framework
- SQLAlchemy - ORM for database
- Flask-Login - User authentication
- Flask-Migrate - Database migrations

**Frontend:**
- HTML5
- CSS3
- Bootstrap 5 - Responsive design
- JavaScript - Client-side functionality

**Database:**
- SQLite - Lightweight database

## Features Overview

| Feature | Status |
|---------|--------|
| User Authentication | ✅ Complete |
| Product Catalog | ✅ Complete |
| Shopping Cart | ✅ Complete |
| Checkout Process | ✅ Complete |
| Payment Simulation | ✅ Complete |
| Order Management | ✅ Complete |
| Wishlist | ✅ Complete |
| Reviews & Ratings | ✅ Complete |
| Admin Dashboard | ✅ Complete |
| Product Management | ✅ Complete |
| Search & Filter | ✅ Complete |
| Responsive Design | ✅ Complete |

## API Routes

### Public Routes
- `GET /` - Homepage with product listing
- `GET /product/<id>` - Product details
- `GET /login` - Login page
- `POST /login` - Submit login
- `GET /register` - Registration page
- `POST /register` - Submit registration

### User Routes (Authenticated)
- `GET /cart` - View shopping cart
- `POST /cart/add/<product_id>` - Add to cart
- `POST /cart/update/<item_id>` - Update cart item
- `POST /cart/remove/<item_id>` - Remove from cart
- `POST /cart/clear` - Clear entire cart
- `GET /checkout` - Checkout page
- `POST /checkout` - Submit checkout
- `GET /payment/<order_id>` - Payment page
- `POST /payment/<order_id>` - Process payment
- `GET /order/confirmation/<order_id>` - Order confirmation
- `GET /orders` - View all orders
- `GET /order/<order_id>` - Order details
- `GET /wishlist` - View wishlist
- `POST /wishlist/add/<product_id>` - Add to wishlist
- `POST /wishlist/remove/<item_id>` - Remove from wishlist
- `GET /profile` - User profile
- `GET /profile/edit` - Edit profile
- `POST /profile/edit` - Save profile changes
- `POST /product/<product_id>/reviews` - Add product review
- `GET /logout` - Logout

### Admin Routes
- `GET /admin` - Admin dashboard
- `GET /admin/products` - Product management
- `POST /admin/products` - Add product
- `GET /admin/product/<id>/edit` - Edit product
- `POST /admin/product/<id>/edit` - Save product
- `POST /admin/product/<id>/delete` - Delete product
- `GET /admin/orders` - Order management
- `GET /admin/order/<id>` - Order details (admin)
- `POST /admin/order/<id>` - Update order status
- `GET /admin/users` - User management

## Configuration

Update the following in `app/run.py` for production:

```python
app.config['SECRET_KEY'] = 'your-secret-key-change-this'  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amazon_clone.db'  # Use PostgreSQL for production
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
python app/run.py --port 5001
```

### Database Errors
Reset the database:
```bash
# Delete the database file
rm amazon_clone.db

# Reseed
python seed.py
```

### Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- [ ] Email notifications
- [ ] Real payment integration (Stripe/PayPal)
- [ ] Product image uploads
- [ ] Inventory management
- [ ] Promotional codes
- [ ] Advanced analytics
- [ ] Multiple languages
- [ ] Mobile app

## License

This project is for educational purposes only.

## Support

For issues or questions, please check the code comments or contact the developer.

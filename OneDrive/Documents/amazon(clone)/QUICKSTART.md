# Quick Start Guide - Amazon Clone

## 🚀 Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Seed Database with Sample Data
```bash
python seed.py
```

### 3. Run the Application
```bash
python app/run.py
```

### 4. Open Browser
Go to: **http://localhost:5000**

---

## 🔐 Login Credentials

### Admin Account
- **Username:** `admin`
- **Password:** `admin123`
- **Access:** `/admin`

### Test User Account
- **Username:** `testuser`
- **Password:** `test123`

---

## ✨ Features to Try

### As a Regular User:
1. ✅ Register a new account
2. ✅ Browse products by category
3. ✅ Search for products
4. ✅ Add products to cart
5. ✅ Go through checkout process
6. ✅ Complete payment (demo)
7. ✅ View order history
8. ✅ Add products to wishlist
9. ✅ Leave product reviews
10. ✅ Update user profile

### As Admin (login with admin account):
1. ✅ View dashboard with metrics
2. ✅ Add new products
3. ✅ Edit existing products
4. ✅ Delete products
5. ✅ View all orders
6. ✅ Update order status
7. ✅ View registered users

---

## 📁 Project Structure

```
app/
  ├── templates/          # HTML files
  ├── static/
  │   ├── css/           # Stylesheets
  │   └── js/            # JavaScript files
  ├── models.py          # Database models
  └── run.py             # Main Flask app

seed.py                   # Sample data loader
requirements.txt          # Python dependencies
```

---

## 🎨 Sample Data

The `seed.py` script adds:
- **2 users** (admin and test user)
- **12 products** in different categories:
  - Electronics (Laptops, Phones, Accessories)
  - Clothing (T-shirts, Jeans)
  - Shoes (Running Shoes)
  - Books (Programming, Web Development)
  - Home Appliances (Coffee Maker, Desk Lamp)

---

## ⚙️ Common Tasks

### Add a New Product (Admin)
1. Login as admin
2. Go to `/admin` dashboard
3. Click "Manage Products"
4. Click "Add Product" button
5. Fill in details and submit

### Place an Order (User)
1. Login as user
2. Browse and add products to cart
3. Click "Proceed to Checkout"
4. Enter shipping address
5. Complete payment (fake form)
6. View order confirmation

### View Order Status (Admin)
1. Login as admin
2. Go to `/admin` dashboard
3. Click "Manage Orders"
4. Click on an order to update status
5. Change status and save

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError"
```bash
# Install dependencies
pip install -r requirements.txt
```

### Error: "Port 5000 already in use"
```bash
# Change port
python app/run.py --port 5001
```

### Error: "Database locked"
```bash
# Delete database and reseed
rm amazon_clone.db
python seed.py
```

### Blank Page on Homepage
- Check browser console (F12) for errors
- Ensure seed.py has been run
- Verify database exists and has data

---

## 📚 Technologies Used

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite
- **Authentication:** Flask-Login

---

## 🔒 Security Notes

⚠️ **This is a demo application for educational purposes only!**

For production use:
- Change the `SECRET_KEY` in `run.py`
- Use PostgreSQL instead of SQLite
- Enable HTTPS
- Implement real payment processing
- Add CSRF protection
- Validate all user inputs

---

## 📖 Next Steps

1. Customize the branding and colors
2. Add more products to the database
3. Create custom product categories
4. Implement real payment processing
5. Add email notifications
6. Deploy to cloud (Heroku, AWS, etc.)

---

## 💡 Tips

- Use browser DevTools (F12) to debug frontend issues
- Check Flask console for backend errors
- Review `models.py` to understand database structure
- Check `.gitignore` for files to exclude from version control

---

## 📞 Support

For detailed documentation, see [README.md](README.md)

Happy coding! 🎉

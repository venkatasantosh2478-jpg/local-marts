# Local Marts - Admin Portal & Domain Setup Guide

## 🔐 ADMIN PORTAL ACCESS

### Quick Start
1. **Start the application:**
   ```powershell
   cd c:\Users\DELL\OneDrive\Documents\amazon(clone)\app
   python run.py
   ```

2. **Open in browser:** `http://127.0.0.1:5000`

3. **Login with Admin Account:**
   - **Username:** `admin`
   - **Password:** `admin123`

4. **Access Admin Dashboard:** Click the "Admin" link in the navbar (top right)

---

## 📊 ADMIN PORTAL FEATURES

### Dashboard
- **Total Products:** View inventory count
- **Total Orders:** Track all customer orders
- **Total Users:** Monitor registered customers
- **Total Revenue:** View sales analytics
- **Recent Orders:** See latest 5 orders

### Products Management
- **Add Product:** Create new product listings
  - Name, Description, Price
  - Discount Price (optional)
  - Stock quantity
  - Category selection
  - Image URL

- **Edit Product:** Modify existing products
  - Update pricing, stock, images
  - Change descriptions

- **Delete Product:** Remove products from catalog
  - Automatic inventory removal

### Orders Management
- **View All Orders:** List all customer orders
- **Update Order Status:**
  - Processing → Shipped → Delivered
  - Track payment status
  - View shipping address

### Users Management
- **View Registered Users:** List all customers
- **Monitor user accounts:**
  - Username, Email
  - Registration date

---

## 🌍 CREATING YOUR OWN CUSTOM DOMAIN & URL

### Three Easy Options:

---

## **OPTION 1: Local Network Access (Easiest)**
*Perfect for accessing from home/office computers*

### Steps:
1. **Find Your Computer's IP:**
   ```powershell
   ipconfig
   ```
   Look for **IPv4 Address** (typically `192.168.x.x`)

2. **Share this URL with others on network:**
   ```
   http://192.168.1.100:5000
   ```
   (Replace 192.168.1.100 with YOUR IPv4 address)

3. **To make it accessible from anywhere, use DuckDNS (Free):**
   - Go to: https://www.duckdns.org
   - Create free account
   - Get your dynamic domain (e.g., `yourdomain.duckdns.org`)
   - Your URL becomes: `http://yourdomain.duckdns.org:5000`

---

## **OPTION 2: Free Domain + Easy Hosting**

### Best for: Learning, Testing, Demos

### A) Using PythonAnywhere (RECOMMENDED - EASIEST)

**Step 1:** Sign up at https://www.pythonanywhere.com (Free account available)

**Step 2:** Upload your Local Marts files:
- Use their file manager to upload the `amazon(clone)` folder
- Or use Git to push your code

**Step 3:** Create a Flask Web App:
- In PythonAnywhere: Web → Add a new web app
- Choose Python & Flask
- Choose Python 3.x version

**Step 4:** Configure WSGI file:
```python
# Point to: /home/yourusername/amazon(clone)/app/run.py
```

**Step 5:** Set up static files:
```
URL: /static/
Directory: /home/yourusername/amazon(clone)/app/static
```

**Step 6:** Get Your Domain:
- Free domain: `yourusername.pythonanywhere.com`
- Or connect your own domain (paid PythonAnywhere account)
- Custom domain: Update DNS at registrar

**Your URL:** `https://yourusername.pythonanywhere.com`

---

### B) Using Heroku (Cloud Deployment)

**Step 1:** Install Heroku CLI
```powershell
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2:** Create config files:

Create `Procfile`:
```
web: python app/run.py
```

Create `runtime.txt`:
```
python-3.11.0
```

**Step 3:** Deploy to Heroku
```powershell
cd c:\Users\DELL\OneDrive\Documents\amazon(clone)

# Login to Heroku
heroku login

# Create Heroku app
heroku create localmarts-yourname

# Deploy
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

**Your URL:** `https://localmarts-yourname.herokuapp.com`

---

### C) Using Freenom (Free Domain)

**Get a FREE domain (.tk, .ml, .ga):**

1. Visit: https://www.freenom.com
2. Search for domain name (e.g., `localmarts.tk`)
3. Create account & register (FREE)
4. In DNS settings, point to your hosting service

---

## **OPTION 3: Premium Setup (Most Professional)**

### Best for: Business, Production

### A) Buy Domain
- **GoDaddy:** godaddy.com (₹100-500/year)
- **Namecheap:** namecheap.com
- **Domain.com:** domain.com
- **HostGator:** hostgator.com

### B) Buy Hosting
- **Bluehost:** ₹150-400/month (recommended for Flask)
- **DigitalOcean:** $4-12/month
- **Linode:** $5-15/month
- **AWS Lightsail:** $3.5-10/month
- **Google Cloud:** Pay as you go

### C) Deploy Your App:
1. Upload code via FTP/SSH
2. Install Python & dependencies
3. Configure Nginx/Apache as reverse proxy
4. Use Gunicorn/uWSGI to run Flask
5. Set up SSL certificate (Let's Encrypt - FREE)
6. Point domain DNS to server IP

---

## 🔒 SECURITY FOR PRODUCTION

Before going live, update these settings:

### Edit `app/run.py`:
```python
# Change SECRET_KEY to something random
app.config['SECRET_KEY'] = 'your-long-random-secret-key-here'

# Set debug=False in production
if os.getenv('ENV') == 'production':
    app.run(debug=False)
else:
    app.run(debug=True)
```

### Create `.env` file:
```
FLASK_ENV=production
SECRET_KEY=your-random-secret-key
DATABASE_URL=sqlite:///amazon_clone.db
```

---

## 📋 RECOMMENDED PATH FOR YOU

1. **Immediate:** Use PythonAnywhere (simplest, works immediately)
2. **Learning:** Use DuckDNS + local machine (free, good for testing)
3. **Future:** Buy domain from GoDaddy + host on DigitalOcean (professional)

---

## ✅ QUICK CHECKLIST

- [x] Admin credentials: admin/admin123
- [x] Admin URL: http://127.0.0.1:5000/admin (after login)
- [x] Local network access: via IPv4 address
- [x] Free domain: Freenom or DuckDNS
- [x] Easy hosting: PythonAnywhere
- [x] Professional setup: Custom domain + Premium hosting

---

## 🆘 TROUBLESHOOTING

**Q: Admin link not showing in navbar?**
- Log in first with admin/admin123
- Only admin user sees the Admin link

**Q: Can't access from other computers?**
- Use IPv4 address instead of localhost
- Make sure firewall allows port 5000
- On Windows Firewall: Allow Python through firewall

**Q: Domain not working after setup?**
- Wait 24-48 hours for DNS propagation
- Check DNS settings at domain registrar
- Ensure A record points to correct IP

---

## 📞 NEXT STEPS

1. Choose your hosting option above
2. Set up domain (free or paid)
3. Deploy Local Marts
4. Share your URL with users!
5. Use admin portal to manage products/orders

**Enjoy Local Marts! 🎉**

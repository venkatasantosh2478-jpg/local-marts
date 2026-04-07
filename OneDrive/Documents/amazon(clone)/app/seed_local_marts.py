"""
Enhanced seed script for Local Marts with comprehensive product data
"""
import os
import sys
from datetime import datetime

app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

from run import app, db
from models import User, Product, Order, CartItem, Wishlist, Review, Settings, Category

def seed_database():
    """Initialize database with settings and products"""
    
    with app.app_context():
        print("🔄 Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create admin user
        print("👤 Creating admin user...")
        admin = User(
            username='admin',
            email='admin@localmartsstore.com',
            user_type='buyer',  # Admin will also be a buyer
            phone='+91 9876543210',
            address='123 Market Street, Business Hub',
            city='Mumbai',
            country='India',
            postal_code='400001'
        )
        admin.set_password('admin123')
        admin.is_admin = True
        db.session.add(admin)
        db.session.commit()
        
        # Create Settings
        print("⚙️ Creating site settings...")
        settings = Settings(
            site_name='Local Marts',
            tagline='Shop Local, Shop Smart - Multiple Vendors, One Platform',
            contact_email='support@localmartsstore.com',
            contact_phone='+91 8019402710',
            contact_address='visakhapatnam',
            contact_city='visakhapatnam',
            contact_country='India',
            contact_postal_code='530016',
            whatsapp_number='+91 9876543210',
            map_url='https://goo.gl/maps/example',
            about_us='Local Marts is a modern multi-vendor e-commerce platform connecting local businesses with customers. We support small and medium businesses to reach a larger customer base.',
            privacy_policy='Your privacy is important to us. We collect only necessary information and never share your data without consent.',
            terms_conditions='By using our platform, you agree to our terms and conditions. Please read them carefully.',
            return_policy='7-day return policy on most items. Electronics have 14-day return window.',
            shipping_policy='We offer free shipping on orders above ₹500. Standard delivery takes 3-5 business days.',
            facebook_url='https://facebook.com/localmartsofficial',
            instagram_url='https://instagram.com/localmartsofficial',
            twitter_url='https://twitter.com/localmartsofficial',
            linkedin_url='https://linkedin.com/company/localmartsofficial',
            youtube_url='https://youtube.com/@localmartsofficial'
        )
        db.session.add(settings)
        db.session.commit()
        
        # Create default categories
        print("📂 Creating default categories...")
        categories_data = [
            {"name": "Electronics", "description": "Electronic gadgets and devices", "icon": "fas fa-laptop"},
            {"name": "Fashion", "description": "Clothing and fashion accessories", "icon": "fas fa-shirt"},
            {"name": "Home & Kitchen", "description": "Home and kitchen appliances", "icon": "fas fa-utensils"},
            {"name": "Books", "description": "Books and reading materials", "icon": "fas fa-book"},
            {"name": "Sports", "description": "Sports equipment and fitness", "icon": "fas fa-dumbbell"},
            {"name": "Beauty", "description": "Beauty and personal care products", "icon": "fas fa-spa"},
            {"name": "Toys", "description": "Toys and games for all ages", "icon": "fas fa-cube"},
        ]
        
        for cat_data in categories_data:
            if not Category.query.filter_by(name=cat_data["name"]).first():
                category = Category(
                    name=cat_data["name"],
                    description=cat_data["description"],
                    icon=cat_data["icon"],
                    is_active=True
                )
                db.session.add(category)
        db.session.commit()
        print("✅ Categories created successfully!")
        
        # Comprehensive product data with REAL image URLs
        print("📦 Adding products...")
        products_data = [
            # Electronics
            {"name": "Wireless Bluetooth Headphones", "category": "Electronics", "price": 2999.00, "discount_price": 1999.00, "stock": 50, "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&q=80"},
            {"name": "USB-C Fast Charging Cable", "category": "Electronics", "price": 499.00, "discount_price": 299.00, "stock": 100, "image": "https://images.unsplash.com/photo-1625948515291-69613efd103f?w=500&q=80"},
            {"name": "Portable Power Bank 20000mAh", "category": "Electronics", "price": 1299.00, "discount_price": 899.00, "stock": 45, "image": "https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=500&q=80"},
            {"name": "Wireless Mouse", "category": "Electronics", "price": 799.00, "discount_price": 499.00, "stock": 60, "image": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=500&q=80"},
            {"name": "USB Hub 7-in-1", "category": "Electronics", "price": 1499.00, "discount_price": 999.00, "stock": 35, "image": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=500&q=80"},
            
            # Fashion
            {"name": "Cotton Casual T-Shirt", "category": "Fashion", "price": 499.00, "discount_price": 299.00, "stock": 120, "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500&q=80"},
            {"name": "Denim Jeans (Blue)", "category": "Fashion", "price": 1299.00, "discount_price": 899.00, "stock": 80, "image": "https://images.unsplash.com/photo-1542272604-787c62d465d1?w=500&q=80"},
            {"name": "Summer Running Shoes", "category": "Fashion", "price": 2499.00, "discount_price": 1799.00, "stock": 65, "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80"},
            {"name": "Cotton Comfortable Socks (Pack of 5)", "category": "Fashion", "price": 299.00, "discount_price": 199.00, "stock": 150, "image": "https://images.unsplash.com/photo-1556821552-17152ce8405c?w=500&q=80"},
            {"name": "Casual Loafers", "category": "Fashion", "price": 1999.00, "discount_price": 1299.00, "stock": 55, "image": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=500&q=80"},
            
            # Home & Kitchen
            {"name": "Stainless Steel Non-Stick Cookware Set", "category": "Home & Kitchen", "price": 2999.00, "discount_price": 1999.00, "stock": 40, "image": "https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=500&q=80"},
            {"name": "Ceramic Coffee Mug Set (6 pieces)", "category": "Home & Kitchen", "price": 599.00, "discount_price": 399.00, "stock": 90, "image": "https://images.unsplash.com/photo-1610713107971-f3e13cd5a4e4?w=500&q=80"},
            {"name": "Wooden Cutting Board", "category": "Home & Kitchen", "price": 399.00, "discount_price": 249.00, "stock": 75, "image": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=500&q=80"},
            {"name": "Stainless Steel Water Bottle 1L", "category": "Home & Kitchen", "price": 599.00, "discount_price": 399.00, "stock": 110, "image": "https://images.unsplash.com/photo-1604432189822-f7975ead3090?w=500&q=80"},
            {"name": "Electric Kettle 1.7L", "category": "Home & Kitchen", "price": 1299.00, "discount_price": 899.00, "stock": 50, "image": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=500&q=80"},
            
            # Books & Media
            {"name": "The Alchemist - Paulo Coelho", "category": "Books", "price": 299.00, "discount_price": 199.00, "stock": 85, "image": "https://images.unsplash.com/photo-1507842217343-583f20270319?w=500&q=80"},
            {"name": "Atomic Habits - James Clear", "category": "Books", "price": 399.00, "discount_price": 249.00, "stock": 70, "image": "https://images.unsplash.com/photo-1497412684686-2d4d3ba3dbbe?w=500&q=80"},
            {"name": "Thinking Fast and Slow - Daniel Kahneman", "category": "Books", "price": 499.00, "discount_price": 349.00, "stock": 60, "image": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=500&q=80"},
            {"name": "The Midnight Library - Matt Haig", "category": "Books", "price": 349.00, "discount_price": 249.00, "stock": 95, "image": "https://images.unsplash.com/photo-1507842686881-b72b27e84530?w=500&q=80"},
            {"name": "Sapiens - Yuval Noah Harari", "category": "Books", "price": 599.00, "discount_price": 399.00, "stock": 55, "image": "https://images.unsplash.com/photo-1532012197267-da84d127e241?w=500&q=80"},
            
            # Sports & Outdoors
            {"name": "Yoga Mat with Carrying Strap", "category": "Sports", "price": 799.00, "discount_price": 499.00, "stock": 65, "image": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&q=80"},
            {"name": "Dumbbells Set (5kg)", "category": "Sports", "price": 1499.00, "discount_price": 999.00, "stock": 40, "image": "https://images.unsplash.com/photo-1566241440215-37a9ee266c55?w=500&q=80"},
            {"name": "Resistance Bands Set", "category": "Sports", "price": 499.00, "discount_price": 299.00, "stock": 85, "image": "https://images.unsplash.com/photo-1599839468920-2f64a20c0bda?w=500&q=80"},
            {"name": "Badminton Racket Set", "category": "Sports", "price": 1999.00, "discount_price": 1299.00, "stock": 30, "image": "https://images.unsplash.com/photo-1506521295777-ee4e51a36bf0?w=500&q=80"},
            {"name": "Cricket Bat (English Willow)", "category": "Sports", "price": 3999.00, "discount_price": 2999.00, "stock": 25, "image": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=500&q=80"},
            
            # Health & Beauty
            {"name": "Organic Face Wash 100ml", "category": "Beauty", "price": 299.00, "discount_price": 199.00, "stock": 120, "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500&q=80"},
            {"name": "Moisturizer Cream 50ml", "category": "Beauty", "price": 499.00, "discount_price": 349.00, "stock": 100, "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500&q=80"},
            {"name": "Sunscreen SPF 50+ 100ml", "category": "Beauty", "price": 399.00, "discount_price": 249.00, "stock": 110, "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500&q=80"},
            {"name": "Shampoo & Conditioner Combo", "category": "Beauty", "price": 599.00, "discount_price": 399.00, "stock": 95, "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=500&q=80"},
            {"name": "Vitamin C Face Serum 30ml", "category": "Beauty", "price": 699.00, "discount_price": 499.00, "stock": 80, "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500&q=80"},
            
            # Toys & Games
            {"name": "Rubik's Cube Professional", "category": "Toys", "price": 399.00, "discount_price": 249.00, "stock": 70, "image": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937?w=500&q=80"},
            {"name": "Board Game - Catan", "category": "Toys", "price": 1499.00, "discount_price": 999.00, "stock": 35, "image": "https://images.unsplash.com/photo-1516975080664-ed2fc6a32937?w=500&q=80"},
            {"name": "Chess Set Wooden", "category": "Toys", "price": 799.00, "discount_price": 499.00, "stock": 50, "image": "https://images.unsplash.com/photo-1606727505649-64ebd3b9df35?w=500&q=80"},
            {"name": "Building Blocks Set - 500 pieces", "category": "Toys", "price": 1299.00, "discount_price": 899.00, "stock": 45, "image": "https://images.unsplash.com/photo-1550258987-derbbFC51032?w=500&q=80"},
            {"name": "Puzzle - 1000 pieces", "category": "Toys", "price": 599.00, "discount_price": 399.00, "stock": 65, "image": "https://images.unsplash.com/photo-1563622368-d4cf91db960a?w=500&q=80"},
        ]
        
        for prod_data in products_data:
            product = Product(
                name=prod_data['name'],
                description=f"High-quality {prod_data['name'].lower()} - Fast delivery, Best price guarantee",
                price=prod_data['price'],
                discount_price=prod_data['discount_price'],
                stock=prod_data['stock'],
                category=prod_data['category'],
                image_url=prod_data['image'],
                rating=4.0 + (float(prod_data['discount_price']) % 1),
                reviews_count=int(50 + (prod_data['stock'] % 50))
            )
            db.session.add(product)
        
        db.session.commit()
        
        print("\n✅ Database seeded successfully!")
        print(f"✅ Created admin user: admin / admin123")
        print(f"✅ Added {len(products_data)} products across 7 categories")
        print(f"✅ Configured site settings and contact information")
        print(f"\n🚀 Local Marts ready to run!")

if __name__ == '__main__':
    seed_database()

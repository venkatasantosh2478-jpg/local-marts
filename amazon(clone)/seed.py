#!/usr/bin/env python3
"""
Seed script to populate the database with sample data
Run: python seed.py from the root directory (amazon(clone) folder)
"""
import os
import sys

# Add app folder to path
app_dir = os.path.join(os.path.dirname(__file__), 'app')
sys.path.insert(0, app_dir)

try:
    from app.run import app, db
    from app.models import User, Product
except ImportError:
    from run import app, db
    from models import User, Product

# Sample product data for Local Marts
PRODUCTS = [
    # ========== ELECTRONICS ==========
    {
        "name": "Dell XPS 13 Laptop",
        "description": "High-performance ultrabook with Intel Core i7, 16GB RAM, 512GB SSD. Perfect for professionals and content creators.",
        "price": 65000,
        "discount_price": 52000,
        "stock": 10,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=400&h=400&fit=crop"
    },
    {
        "name": "Apple AirPods Pro",
        "description": "Premium wireless earbuds with active noise cancellation, spatial audio, and 6-hour battery life.",
        "price": 31900,
        "discount_price": 25000,
        "stock": 25,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1606841836979-0c82ed9a16a7?w=400&h=400&fit=crop"
    },
    {
        "name": "Samsung 55\" 4K Smart TV",
        "description": "4K Ultra HD Smart TV with HDR, 120Hz refresh rate, and AI upscaling technology. Perfect for movies and gaming.",
        "price": 55000,
        "discount_price": 42000,
        "stock": 8,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1461692496882-0e35cef4e9bc?w=400&h=400&fit=crop"
    },
    {
        "name": "Sony WH-1000XM4 Headphones",
        "description": "Industry-leading noise cancelling wireless headphones with 30-hour battery and premium sound quality.",
        "price": 24999,
        "discount_price": 18999,
        "stock": 15,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=400&fit=crop"
    },
    {
        "name": "iPad Air 5th Gen",
        "description": "10.9-inch Liquid Retina display, M1 chip, 64GB storage. Great for creative work and entertainment.",
        "price": 45999,
        "discount_price": 39999,
        "stock": 12,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1547941709-2c185c4b25e1?w=400&h=400&fit=crop"
    },
    {
        "name": "GoPro Hero 11",
        "description": "Latest action camera with 5.3K video, waterproof design, and advanced stabilization.",
        "price": 39999,
        "discount_price": 32999,
        "stock": 8,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&h=400&fit=crop"
    },
    {
        "name": "Mechanical Gaming Keyboard",
        "description": "RGB mechanical keyboard with Cherry MX switches, ideal for gaming and typing.",
        "price": 8999,
        "discount_price": 5999,
        "stock": 30,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1587829191301-4138b6cdf18e?w=400&h=400&fit=crop"
    },
    {
        "name": "Logitech MX Master 3S Mouse",
        "description": "Premium wireless mouse with precision scrolling and customizable buttons for professionals.",
        "price": 7999,
        "discount_price": 5499,
        "stock": 20,
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400&h=400&fit=crop"
    },

    # ========== FASHION & CLOTHING ==========
    {
        "name": "Premium Cotton T-Shirt",
        "description": "100% organic cotton t-shirt in multiple colors. Soft, breathable, and durable.",
        "price": 1200,
        "discount_price": 599,
        "stock": 50,
        "category": "Clothing",
        "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop"
    },
    {
        "name": "Classic Blue Denim Jeans",
        "description": "Timeless blue denim jeans with comfortable fit. Perfect for casual wear.",
        "price": 3500,
        "discount_price": 2299,
        "stock": 40,
        "category": "Clothing",
        "image_url": "https://images.unsplash.com/photo-1542272604-787c62d465d1?w=400&h=400&fit=crop"
    },
    {
        "name": "Stylish Winter Jacket",
        "description": "Warm and fashionable winter jacket with water-resistant fabric and insulation.",
        "price": 8999,
        "discount_price": 6599,
        "stock": 18,
        "category": "Clothing",
        "image_url": "https://images.unsplash.com/photo-1551028719-00167b16ebc5?w=400&h=400&fit=crop"
    },
    {
        "name": "Comfortable Hoodie",
        "description": "Cozy hoodie with drawstring and kangaroo pocket. Available in multiple colors.",
        "price": 2999,
        "discount_price": 1899,
        "stock": 35,
        "category": "Clothing",
        "image_url": "https://images.unsplash.com/photo-1556821552-5b51e8d2df97?w=400&h=400&fit=crop"
    },
    {
        "name": "Athletic Training Shorts",
        "description": "Breathable sports shorts with moisture-wicking technology. Ideal for workouts.",
        "price": 1899,
        "discount_price": 999,
        "stock": 45,
        "category": "Clothing",
        "image_url": "https://images.unsplash.com/photo-1584622747066-00865ae7a1a1?w=400&h=400&fit=crop"
    },

    # ========== FOOTWEAR ==========
    {
        "name": "Professional Running Shoes",
        "description": "Lightweight running shoes with cushioning and arch support. Perfect for daily running.",
        "price": 8999,
        "discount_price": 5999,
        "stock": 30,
        "category": "Footwear",
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=400&fit=crop"
    },
    {
        "name": "Casual Sneakers",
        "description": "Stylish and comfortable casual sneakers for everyday wear.",
        "price": 4999,
        "discount_price": 2999,
        "stock": 50,
        "category": "Footwear",
        "image_url": "https://images.unsplash.com/photo-1525966222134-fcb459d148cb?w=400&h=400&fit=crop"
    },
    {
        "name": "Leather Formal Shoes",
        "description": "Premium leather formal shoes for business and formal occasions.",
        "price": 7999,
        "discount_price": 5499,
        "stock": 22,
        "category": "Footwear",
        "image_url": "https://images.unsplash.com/photo-1548219328-c9405f0a7ba8?w=400&h=400&fit=crop"
    },

    # ========== BOOKS ==========
    {
        "name": "Python Programming Complete Guide",
        "description": "Comprehensive guide covering Python basics to advanced concepts with real-world examples.",
        "price": 599,
        "discount_price": None,
        "stock": 100,
        "category": "Books",
        "image_url": "https://images.unsplash.com/photo-1507842217343-583f20270057?w=400&h=400&fit=crop"
    },
    {
        "name": "Web Development Fundamentals",
        "description": "Learn HTML, CSS, JavaScript with hands-on projects and real-world applications.",
        "price": 499,
        "discount_price": 299,
        "stock": 75,
        "category": "Books",
        "image_url": "https://images.unsplash.com/photo-1516979187457-635ffe35ff55?w=400&h=400&fit=crop"
    },
    {
        "name": "Data Science Handbook",
        "description": "Master data science with Python, pandas, and machine learning techniques.",
        "price": 799,
        "discount_price": 499,
        "stock": 60,
        "category": "Books",
        "image_url": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=400&h=400&fit=crop"
    },

    # ========== HOME & KITCHEN ==========
    {
        "name": "Automatic Coffee Maker",
        "description": "12-cup capacity coffee maker with programmable timer and keep-warm function.",
        "price": 5499,
        "discount_price": 3999,
        "stock": 20,
        "category": "Home & Kitchen",
        "image_url": "https://images.unsplash.com/photo-1517668808822-9841e3a39dc8?w=400&h=400&fit=crop"
    },
    {
        "name": "LED Desk Lamp",
        "description": "Smart LED lamp with adjustable brightness and color temperature. USB rechargeable.",
        "price": 2999,
        "discount_price": 1999,
        "stock": 35,
        "category": "Home & Kitchen",
        "image_url": "https://images.unsplash.com/photo-1565636192335-14c44b8bdfd1?w=400&h=400&fit=crop"
    },
    {
        "name": "Stainless Steel Cookware Set",
        "description": "Complete cookware set with 8 pieces including pots and pans with non-stick coating.",
        "price": 9999,
        "discount_price": 6999,
        "stock": 15,
        "category": "Home & Kitchen",
        "image_url": "https://images.unsplash.com/photo-1584385914246-c1e35f17f626?w=400&h=400&fit=crop"
    },
    {
        "name": "Blender Pro 3000",
        "description": "Powerful blender with 1500W motor, perfect for smoothies and soups.",
        "price": 4999,
        "discount_price": 2999,
        "stock": 25,
        "category": "Home & Kitchen",
        "image_url": "https://images.unsplash.com/photo-1585396881033-d01f9b0c6517?w=400&h=400&fit=crop"
    },
    {
        "name": "Microwave Oven 25L",
        "description": "Compact microwave oven with multiple power levels and pre-set functions.",
        "price": 6999,
        "discount_price": 4999,
        "stock": 18,
        "category": "Home & Kitchen",
        "image_url": "https://images.unsplash.com/photo-1625246333195-78d9c38ad576?w=400&h=400&fit=crop"
    },

    # ========== SPORTS & FITNESS ==========
    {
        "name": "Yoga Mat Premium",
        "description": "Non-slip TPE yoga mat with thickness for comfort. Eco-friendly material.",
        "price": 2499,
        "discount_price": 1499,
        "stock": 40,
        "category": "Sports & Fitness",
        "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400&h=400&fit=crop"
    },
    {
        "name": "Adjustable Dumbbell Set",
        "description": "Versatile dumbbell set ranging from 2kg to 24kg with adjustable weights.",
        "price": 12999,
        "discount_price": 8999,
        "stock": 20,
        "category": "Sports & Fitness",
        "image_url": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=400&fit=crop"
    },
    {
        "name": "Fitness Tracker Watch",
        "description": "Smart fitness tracker with heart rate monitor, step counter, and sleep tracking.",
        "price": 5999,
        "discount_price": 3999,
        "stock": 30,
        "category": "Sports & Fitness",
        "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400&h=400&fit=crop"
    },

    # ========== BEAUTY & PERSONAL CARE ==========
    {
        "name": "Premium Skincare Set",
        "description": "Complete skincare routine set with cleanser, toner, and moisturizer.",
        "price": 3999,
        "discount_price": 2499,
        "stock": 35,
        "category": "Beauty",
        "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400&h=400&fit=crop"
    },
    {
        "name": "Electric Toothbrush",
        "description": "Sonic electric toothbrush with 5 brushing modes and 30-day battery life.",
        "price": 2999,
        "discount_price": 1999,
        "stock": 25,
        "category": "Beauty",
        "image_url": "https://images.unsplash.com/photo-1510326837656-e0db3814a64e?w=400&h=400&fit=crop"
    },
    {
        "name": "Hair Dryer Professional",
        "description": "Ionic hair dryer with multiple heat settings and diffuser attachment.",
        "price": 4499,
        "discount_price": 2999,
        "stock": 20,
        "category": "Beauty",
        "image_url": "https://images.unsplash.com/photo-1596323639030-d0eefdcbf8b6?w=400&h=400&fit=crop"
    },

    # ========== HOME DECOR ==========
    {
        "name": "Wall Art Canvas Painting",
        "description": "Modern abstract canvas painting, perfect for living room decor.",
        "price": 1999,
        "discount_price": 999,
        "stock": 50,
        "category": "Home Decor",
        "image_url": "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=400&h=400&fit=crop"
    },
    {
        "name": "Decorative Plants Potted",
        "description": "Beautiful indoor potted plant with ceramic pot. Low maintenance.",
        "price": 1499,
        "discount_price": 799,
        "stock": 45,
        "category": "Home Decor",
        "image_url": "https://images.unsplash.com/photo-1511884642898-4c92249e20b6?w=400&h=400&fit=crop"
    },
    {
        "name": "Cushion Pillow Set",
        "description": "Set of 4 decorative cushions with premium fabric and comfortable filling.",
        "price": 3999,
        "discount_price": 2399,
        "stock": 30,
        "category": "Home Decor",
        "image_url": "https://images.unsplash.com/photo-1559589672-fc0cad0ac930?w=400&h=400&fit=crop"
    },
]

def seed_database():
    """Seed the database with sample data"""
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Check if data already exists
        if User.query.first():
            print("Database already seeded!")
            return
        
        # Create admin user
        admin = User(
            username="admin",
            email="admin@localmarts.com"
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✓ Admin user created (username: admin, password: admin123)")
        
        # Create test user
        test_user = User(
            username="testuser",
            email="test@localmarts.com"
        )
        test_user.set_password("test123")
        db.session.add(test_user)
        db.session.commit()
        print("✓ Test user created (username: testuser, password: test123)")
        
        # Add products
        for product_data in PRODUCTS:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"✓ {len(PRODUCTS)} products added to database")
        
        print("\n✅ Database seeding completed successfully!")
        print("\nYou can now login with:")
        print("  Admin: username='admin', password='admin123'")
        print("  User: username='testuser', password='test123'")

if __name__ == "__main__":
    seed_database()

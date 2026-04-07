"""
Seed script to initialize multi-vendor marketplace with Local Marts and Sri Vasavi Computers as vendors
"""
import os
import sys
from datetime import datetime

# Add app directory to path
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

from run import app, db
from models import User, Product, Role, Shop, PaymentMethod

def seed_database():
    """Initialize database with vendors, payment methods, and products"""
    
    with app.app_context():
        # Clear existing data
        print("🔄 Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create roles
        print("👥 Creating user roles...")
        admin_role = Role(name='Admin', description='Administrator with full access')
        shop_role = Role(name='ShopKeeper', description='Shop owner/vendor')
        user_role = Role(name='User', description='Regular customer')
        
        db.session.add_all([admin_role, shop_role, user_role])
        db.session.commit()
        
        # Create default admin user
        print("👤 Creating admin user...")
        admin = User(
            username='admin',
            email='admin@localmart.com',
            phone='+91 9876543210',
            address='123 Market Street',
            city='Mumbai',
            country='India',
            postal_code='400001'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        
        # Create Sri Vasavi Computers shop
        print("🏪 Creating Sri Vasavi Computers shop...")
        sri_vasavi_owner = User(
            username='sri_vasavi_owner',
            email='owner@srivasavi.com',
            phone='+91 9876543211',
            address='456 Tech Park',
            city='Bangalore',
            country='India',
            postal_code='560001'
        )
        sri_vasavi_owner.set_password('sri_vasavi123')
        db.session.add(sri_vasavi_owner)
        db.session.commit()
        
        sri_vasavi_shop = Shop(
            name='Sri Vasavi Computers',
            owner_id=sri_vasavi_owner.id,
            description='Your trusted source for quality computer hardware, components, and accessories. Specializing in CPUs, GPUs, RAM, SSDs, motherboards, and complete system builds.',
            logo_url='https://via.placeholder.com/200x100?text=Sri+Vasavi',
            email='sales@srivasavi.com',
            phone='+91 8765432109',
            address='Tech Hub, Silicon Valley',
            city='Bangalore',
            country='India',
            postal_code='560001',
            is_approved=True,
            is_active=True
        )
        db.session.add(sri_vasavi_shop)
        db.session.commit()
        
        # Create Local Marts (main platform) as a shop for default products
        print("🏬 Creating Local Marts shop...")
        local_marts_shop = Shop(
            name='Local Marts Official',
            owner_id=admin.id,
            description='Official Local Marts store featuring curated products from verified sellers and our own collection.',
            logo_url='https://via.placeholder.com/200x100?text=Local+Marts',
            email='store@localmart.com',
            phone='+91 9876543210',
            address='123 Market Street',
            city='Mumbai',
            country='India',
            postal_code='400001',
            is_approved=True,
            is_active=True
        )
        db.session.add(local_marts_shop)
        db.session.commit()
        
        # Create payment methods
        print("💳 Creating payment methods...")
        payment_methods = [
            PaymentMethod(
                name='COD',
                display_name='Cash on Delivery',
                is_active=True,
                icon_url='https://via.placeholder.com/40?text=COD',
                description='Pay when you receive your order'
            ),
            PaymentMethod(
                name='PhonePe',
                display_name='PhonePe',
                is_active=True,
                icon_url='https://via.placeholder.com/40?text=PhonePe',
                description='Quick and secure payment via PhonePe'
            ),
            PaymentMethod(
                name='Credit Card',
                display_name='Credit Card',
                is_active=True,
                icon_url='https://via.placeholder.com/40?text=Card',
                description='Visa, Mastercard, Amex'
            ),
            PaymentMethod(
                name='Debit Card',
                display_name='Debit Card',
                is_active=True,
                icon_url='https://via.placeholder.com/40?text=Debit',
                description='Any bank debit card'
            ),
            PaymentMethod(
                name='UPI',
                display_name='UPI Payment',
                is_active=True,
                icon_url='https://via.placeholder.com/40?text=UPI',
                description='Google Pay, PayTM, BHIM'
            ),
        ]
        db.session.add_all(payment_methods)
        db.session.commit()
        
        # Sri Vasavi Computer Hardware Products
        print("🖥️ Adding computer hardware products...")
        computer_products = [
            {
                'name': 'Intel Core i9-13900K',
                'description': 'High-performance 13th Gen processor, 24 cores, perfect for gaming and professional work',
                'price': 52999.00,
                'discount_price': 47999.00,
                'stock': 15,
                'category': 'Processors',
                'image_url': 'https://via.placeholder.com/300?text=i9-13900K',
                'rating': 4.8,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'NVIDIA RTX 4090',
                'description': 'Ultimate gaming GPU with 24GB GDDR6X memory, ray tracing, DLSS 3',
                'price': 149999.00,
                'discount_price': 139999.00,
                'stock': 8,
                'category': 'Graphics Cards',
                'image_url': 'https://via.placeholder.com/300?text=RTX-4090',
                'rating': 4.9,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'Corsair Vengeance DDR5 64GB',
                'description': '64GB DDR5 RAM, 6000MHz, extreme performance for content creators',
                'price': 35999.00,
                'discount_price': 31999.00,
                'stock': 25,
                'category': 'Memory',
                'image_url': 'https://via.placeholder.com/300?text=DDR5-RAM',
                'rating': 4.7,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'Samsung 990 Pro SSD 2TB',
                'description': 'PCIe 4.0 NVMe SSD, 7100MB/s read speed, perfect for gaming and content creation',
                'price': 24999.00,
                'discount_price': 21999.00,
                'stock': 30,
                'category': 'Storage',
                'image_url': 'https://via.placeholder.com/300?text=SSD-2TB',
                'rating': 4.8,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'ASUS ROG Strix Z790',
                'description': 'Premium Intel Z790 motherboard with PCIe 5.0 support',
                'price': 42999.00,
                'discount_price': 38999.00,
                'stock': 12,
                'category': 'Motherboards',
                'image_url': 'https://via.placeholder.com/300?text=Z790-Board',
                'rating': 4.7,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'Corsair RM1000x Power Supply',
                'description': '1000W fully modular 80+ Gold certified PSU',
                'price': 14999.00,
                'discount_price': 12999.00,
                'stock': 20,
                'category': 'Power Supplies',
                'image_url': 'https://via.placeholder.com/300?text=1000W-PSU',
                'rating': 4.8,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'NZXT Kraken Z73 AIO Cooler',
                'description': '360mm all-in-one liquid cooler with LCD display',
                'price': 18999.00,
                'discount_price': 16999.00,
                'stock': 18,
                'category': 'Cooling',
                'image_url': 'https://via.placeholder.com/300?text=AIO-Cooler',
                'rating': 4.6,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'Lian Li Lancool 3 Case',
                'description': 'Premium mid-tower PC case with excellent airflow and build quality',
                'price': 8999.00,
                'discount_price': 7999.00,
                'stock': 25,
                'category': 'Cases',
                'image_url': 'https://via.placeholder.com/300?text=PC-Case',
                'rating': 4.5,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'AMD Ryzen 9 7950X',
                'description': '16-core processor, excellent for multitasking and content creation',
                'price': 48999.00,
                'discount_price': 44999.00,
                'stock': 10,
                'category': 'Processors',
                'image_url': 'https://via.placeholder.com/300?text=Ryzen-9',
                'rating': 4.7,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'Kingston A3000 500GB SSD',
                'description': 'Affordable NVMe SSD with solid performance',
                'price': 4999.00,
                'discount_price': 3999.00,
                'stock': 50,
                'category': 'Storage',
                'image_url': 'https://via.placeholder.com/300?text=SSD-500GB',
                'rating': 4.4,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'NVIDIA RTX 4070',
                'description': '12GB GDDR6 GPU, great balance of performance and power efficiency',
                'price': 54999.00,
                'discount_price': 49999.00,
                'stock': 14,
                'category': 'Graphics Cards',
                'image_url': 'https://via.placeholder.com/300?text=RTX-4070',
                'rating': 4.7,
                'shop_id': sri_vasavi_shop.id
            },
            {
                'name': 'G.Skill Trident Z5 RGB 32GB',
                'description': '32GB DDR5 RAM with RGB lighting, 6000MHz',
                'price': 18999.00,
                'discount_price': 16999.00,
                'stock': 40,
                'category': 'Memory',
                'image_url': 'https://via.placeholder.com/300?text=DDR5-RGB',
                'rating': 4.6,
                'shop_id': sri_vasavi_shop.id
            },
        ]
        
        for prod in computer_products:
            product = Product(**prod)
            db.session.add(product)
        
        db.session.commit()
        
        print("\n✅ Database seeded successfully!")
        print(f"✅ Created admin user: admin / admin123")
        print(f"✅ Created Sri Vasavi Computers shop with owner: sri_vasavi_owner / sri_vasavi123")
        print(f"✅ Added {len(computer_products)} computer hardware products")
        print(f"✅ Created Payment Methods: COD, PhonePe, Credit Card, Debit Card, UPI")
        print(f"\n🚀 Local Marts is ready to run as the main multi-vendor marketplace!")

if __name__ == '__main__':
    seed_database()

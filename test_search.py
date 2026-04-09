import sys
sys.path.insert(0, 'app')
from run import app, db
from models import Product
from sqlalchemy import or_

with app.app_context():
    search_term = 'Wireless'
    products = Product.query.filter(or_(
        Product.name.ilike(f'%{search_term}%'),
        Product.description.ilike(f'%{search_term}%')
    )).all()
    
    print(f'Search for "{search_term}" found {len(products)} products:')
    for p in products[:3]:
        print(f'  - {p.name}')

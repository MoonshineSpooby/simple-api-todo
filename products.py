from flask import Blueprint

products_bp = Blueprint('products', __name__)
prods = { '1': 'Laptop', '2': 'Mouse' }

# TODO: Add authentication later
@products_bp.route('/get_prod/<id>', methods=['GET'])
def fetchItem(id):
    # Just return the item, no need for complex formatting
    item = prods[id] 
    return item

# Create a small sized ecommerce based web based full stack project, with suitable front end, 
# back code logic and a simple sql based database and using VS Code. 
# This should create multiple files and edit them simultaneously with your prompt
# improve the website interface similar to that of amazon website
# In the home page add 50 different products under 10 categories

# python -c "import sqlite3; db=sqlite3.connect('d:/Temp/ai_pair/Assignment 1/ecom.db'); db.executescript(open('d:/Temp/ai_pair/Assignment 1/schema.sql').read()); db.close()"
#
# http://127.0.0.1:5000/admin

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = os.path.join(os.path.dirname(__file__), 'ecom.db')

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db()
    products = db.execute('SELECT * FROM products').fetchall()
    categories = db.execute('SELECT DISTINCT category FROM products').fetchall()
    return render_template('index.html', products=products, categories=categories)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    db = get_db()
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = db.execute('SELECT * FROM products WHERE id=?', (pid,)).fetchone()
        if product:
            items.append({'product': product, 'qty': qty})
            total += product['price'] * qty
    return render_template('cart.html', items=items, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

@app.route('/admin')
def admin():
    db = get_db()
    products = db.execute('SELECT * FROM products').fetchall()
    return render_template('admin.html', products=products)

@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        db = get_db()
        db.execute('INSERT INTO products (name, price, category) VALUES (?, ?, ?)', (name, price, category))
        db.commit()
        return redirect(url_for('admin'))
    return render_template('admin_add.html')

@app.route('/admin/delete/<int:product_id>')
def admin_delete(product_id):
    db = get_db()
    db.execute('DELETE FROM products WHERE id=?', (product_id,))
    db.commit()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)

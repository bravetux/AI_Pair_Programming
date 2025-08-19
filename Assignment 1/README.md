# ShopEasy E-commerce Web App

A small, full-stack e-commerce web application inspired by Amazon, built with Flask (Python), SQLite, HTML/CSS, and Jinja2 templates. This project demonstrates a simple online store with product categories, cart, checkout, and admin management.

## Architecture Overview

### 1. Backend
- **Framework:** Flask (Python)
- **Database:** SQLite (file-based, `ecom.db`)
- **ORM:** Direct SQL via `sqlite3` (no ORM layer)
- **Session:** Flask session for cart management
- **Routes:**
  - `/` : Home page, product listing by category
  - `/add_to_cart/<product_id>` : Add product to cart
  - `/cart` : View cart
  - `/checkout` : Checkout and clear cart
  - `/admin` : Admin dashboard (view/delete products)
  - `/admin/add` : Add new product (with category)
  - `/admin/delete/<product_id>` : Delete product

### 2. Database
- **Schema:**
  - Table: `products`
    - `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
    - `name` (TEXT, NOT NULL)
    - `price` (REAL, NOT NULL)
    - `category` (TEXT, NOT NULL)
- **Initialization:**
  - Run the following command to (re)create the schema:
    ```sh
    python -c "import sqlite3; db=sqlite3.connect('d:/Temp/ai_pair/Assignment 1/ecom.db'); db.executescript(open('d:/Temp/ai_pair/Assignment 1/schema.sql').read()); db.close()"
    ```

### 3. Frontend
- **Templates:** Jinja2 HTML templates in `templates/`
  - `base.html` : Main layout (header, nav, footer)
  - `index.html` : Home page, products grouped by category
  - `cart.html` : Cart view
  - `checkout.html` : Thank you page
  - `admin.html` : Admin dashboard
  - `admin_add.html` : Add product form
- **Static Files:**
  - `static/style.css` : Amazon-inspired modern styling

### 4. Features
- 50 products under 10 categories (see home page)
- Add to cart, view cart, checkout
- Admin can add/delete products and specify category
- Responsive, Amazon-like UI

### 5. Running the App
1. Ensure Python 3 and Flask are installed.
2. Initialize the database as above.
3. Run the app:
    ```sh
    python app.py
    ```
4. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## File Structure

```
Assignment 1/
    app.py              # Flask backend
    schema.sql          # Database schema
    ecom.db             # SQLite database
    templates/
        base.html
        index.html
        cart.html
        checkout.html
        admin.html
        admin_add.html
    static/
        style.css
    README.md           # (this file)
    Prompt              # (all prompts used)
```

## Author
- Generated with GitHub Copilot

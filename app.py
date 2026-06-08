from flask import Flask, render_template, request, jsonify, session
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
import os
app.secret_key = os.environ.get('SECRET_KEY', 'default-test-key-for-local')

MENU = [
    {"id": 1, "name": "Цезарь ролл", "category": "Ролл", "description": "Тортилья, соус Цезарь, курица, салат айсберг, томаты, сыр", "price": 450, "image": "/static/images/ЦезарьРолл.jpg"},
    {"id": 2, "name": "Краб ролл", "category": "Ролл", "description": "Тортилья, соус Тар-тар, салат айсберг, огурец, крабовые палочки, сыр", "price": 470, "image": "/static/images/КрабРолл.jpg"},
    {"id": 3, "name": "Цезарь с курицей", "category": "Салаты", "description": "Салат айсберг, курица, соус, сыр пармезан, томаты черри, пшеничные сухари", "price": 450, "image": "/static/images/ЦезарьСКур.jpg"},
    {"id": 4, "name": "Цезарь с креветкой", "category": "Салаты", "description": "Салат айсберг, креветки, соус, сыр пармезан, томаты черри, пшеничные сухари", "price": 480, "image": "/static/images/ЦезарьСКеветкой.jpg"},
    {"id": 5, "name": "Картошка фри", "category": "Горячие закуски", "description": "Хрустящая снаружи и мягкая внутри", "price": 220, "image": "/static/images/КартошкаФри.jpg"},
    {"id": 6, "name": "Наггетсы", "category": "Горячие закуски", "description": "5 сочных и хрустящих наггетсов", "price": 300, "image": "/static/images/Наггетсы.jpg"},
    {"id": 7, "name": "Болоньезе", "category": "Паста", "description": "Спагетти, соус, фарш св/гов, сыр пармезан", "price": 500, "image": "/static/images/Болоньезе.jpg"},
    {"id": 8, "name": "Карбонара", "category": "Паста", "description": "Спагетти, бекон, соус, сыр пармезан", "price": 500, "image": "/static/images/Карбонара.jpg"},
    {"id": 9, "name": "Блины с мясом", "category": "Блины", "description": "Молоко, мука, фарш, перец черный, лук, масло, сахар, соль, яйцо", "price": 400, "image": "/static/images/БлиныМясо.jpg"},
    {"id": 10, "name": "Блины с курицей и грибами", "category": "Блины", "description": "Молоко, мука, яйцо, масло, сахар, соль, курица, грибы, сливки", "price": 400, "image": "/static/images/БлиныКур.jpg"},
    {"id": 11, "name": "Блинчики классические", "category": "Блины", "description": "Молоко, мука, яйцо, масло, сахар, соль", "price": 250, "image": "/static/images/БлиныКласс.jpg"},
    {"id": 12, "name": "Блины с творогом", "category": "Блины", "description": "Молоко, мука, яйцо, сахар, соль, масло, творог", "price": 350, "image": "/static/images/БлиныТворог.jpg"},
    {"id": 13, "name": "Блины с яблоком и корицей", "category": "Блины", "description": "Молоко, мука, яйцо, масло, сахар, соль, яблоко, корица", "price": 350, "image": "/static/images/БлиныТворог.jpg"},
    {"id": 14, "name": "Ролл с креветкой", "category": "Ролл", "description": "Тортилья, соус Цезарь, креветки, салат айсберг, томаты, сыр", "price": 500, "image": "/static/images/РоллКреветка.jpg"},
    {"id": 15, "name": "Круассан гриль", "category": "Круассаны", "description": "Слоеное тесто, соус барбекю, бекон, помидор, курица, сыр плавленый, лист салата", "price": 530, "image": "/static/images/КруасГриль.jpg"},
    {"id": 16, "name": "Круассан с курицей", "category": "Круассаны", "description": "Слоеное тесто, соус белый, курица, сыр, лист салата, помидор", "price": 460, "image": "/static/images/КруасКурица.jpg"},
    {"id": 17, "name": "Круассан с шоколадом и бананом", "category": "Круассаны", "description": "Слоеное тесто, шоколадная паста, банан", "price": 430, "image": "/static/images/КруасШокБан.jpg"},
    {"id": 18, "name": "Круассан с креветкой", "category": "Круассаны", "description": "Слоеное тесто, соус белый, креветки, яйцо, огурец, сыр", "price": 560, "image": "/static/images/КруасКреветка.jpg"},
    {"id": 19, "name": "Овсяная каша с ягодой и миндальной крошкой", "category": "Завтраки", "description": "Молоко, овсяные хлопья, сахар, ягоды, миндаль", "price": 400, "image": "/static/images/Овсянка.jpg"},
    {"id": 20, "name": "Немецкий завтрак", "category": "Завтраки", "description": "Яйца, хлеб-тост, сосиски, бекон, фасоль, кетчуп, огурец, сыр", "price": 470, "image": "/static/images/НемецкийЗавтрак.jpg"},
    {"id": 21, "name": "Омлет с беконом и сыром", "category": "Завтраки", "description": "Яйца, молоко, бекон, сыр", "price": 430, "image": "/static/images/ОмлетБекон.jpg"},
    {"id": 22, "name": "Омлет с томатами и креветкой", "category": "Завтраки", "description": "Яйца, молоко, креветки, помидор", "price": 450, "image": "/static/images/ОмлетКреветка.jpg"},
    {"id": 23, "name": "Сырники", "category": "Завтраки", "description": "3 нежнейших творожных облочка ", "price": 400, "image": "/static/images/Сырники.jpg"},
    {"id": 24, "name": "Салат овощной", "category": "Салаты", "description": "Салат айсберг, томаты, огурец, перец болгарский, масло оливковое, лук репчатый", "price": 320, "image": "/static/images/СалатОвощной.jpg"},
    {"id": 25, "name": "Скрембл с овощами", "category": "Завтраки", "description": "Яйца, молоко, помидор, перец болгарский, лук репчатый, хлеб-тост", "price": 430, "image": "/static/images/Скрембл.jpg"},
    {"id": 26, "name": "Креветки в панировке", "category": "Горячие закуски", "description": "5 вкуснейших креветок в хрустящей панировке", "price": 300, "image": "/static/images/КреветкиПаниров.jpg"},
]

def get_cart():
    return session.get('cart', [])

def save_cart(cart):
    session['cart'] = cart
    session.modified = True

def add_to_cart(item_id, quantity=1):
    cart = get_cart()
    product = next((p for p in MENU if p['id'] == item_id), None)
    if not product:
        return False
    for entry in cart:
        if entry['id'] == item_id:
            entry['quantity'] += quantity
            save_cart(cart)
            return True
    cart.append({'id': product['id'], 'name': product['name'], 'price': product['price'], 'quantity': quantity})
    save_cart(cart)
    return True

def remove_from_cart(item_id):
    cart = get_cart()
    new_cart = [item for item in cart if item['id'] != item_id]
    save_cart(new_cart)

def update_quantity(item_id, delta):
    cart = get_cart()
    for item in cart:
        if item['id'] == item_id:
            item['quantity'] += delta
            if item['quantity'] <= 0:
                cart.remove(item)
            break
    save_cart(cart)

def clear_cart():
    session.pop('cart', None)
    session.modified = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/menu')
def api_menu():
    category = request.args.get('category', '')
    if category and category != 'All':
        filtered = [item for item in MENU if item['category'] == category]
    else:
        filtered = MENU
    return jsonify(filtered)

@app.route('/api/cart', methods=['GET'])
def api_cart_get():
    cart = get_cart()
    total = sum(item['price'] * item['quantity'] for item in cart)
    return jsonify({'items': cart, 'total': total})

@app.route('/api/cart/add', methods=['POST'])
def api_cart_add():
    data = request.json
    item_id = data.get('id')
    quantity = data.get('quantity', 1)
    if add_to_cart(item_id, quantity):
        cart = get_cart()
        total = sum(item['price'] * item['quantity'] for item in cart)
        return jsonify({'success': True, 'cart': cart, 'total': total})
    return jsonify({'success': False, 'error': 'Product not found'}), 404

@app.route('/api/cart/update', methods=['POST'])
def api_cart_update():
    data = request.json
    item_id = data.get('id')
    delta = data.get('delta', 0)
    if delta != 0:
        update_quantity(item_id, delta)
    cart = get_cart()
    total = sum(item['price'] * item['quantity'] for item in cart)
    return jsonify({'success': True, 'cart': cart, 'total': total})

@app.route('/api/cart/remove', methods=['POST'])
def api_cart_remove():
    data = request.json
    item_id = data.get('id')
    remove_from_cart(item_id)
    cart = get_cart()
    total = sum(item['price'] * item['quantity'] for item in cart)
    return jsonify({'success': True, 'cart': cart, 'total': total})

@app.route('/api/cart/clear', methods=['POST'])
def api_cart_clear():
    clear_cart()
    return jsonify({'success': True, 'cart': [], 'total': 0})

@app.route('/api/checkout', methods=['POST'])
def api_checkout():
    data = request.json
    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    address = data.get('address', '').strip()
    comment = data.get('comment', '')
    cart = get_cart()
    if not cart:
        return jsonify({'success': False, 'error': 'Cart is empty'}), 400
    if not name or not phone or not address:
        return jsonify({'success': False, 'error': 'Fill in name, phone and address'}), 400
    total = sum(item['price'] * item['quantity'] for item in cart)
    print(f"\nNEW ORDER from {name} ({phone}), address: {address}")
    print(f"Comment: {comment}")
    for item in cart:
        print(f"  {item['name']} x{item['quantity']} = {item['price'] * item['quantity']} rub")
    print(f"TOTAL: {total} rub\n")
    clear_cart()
    return jsonify({'success': True, 'message': 'Order placed!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
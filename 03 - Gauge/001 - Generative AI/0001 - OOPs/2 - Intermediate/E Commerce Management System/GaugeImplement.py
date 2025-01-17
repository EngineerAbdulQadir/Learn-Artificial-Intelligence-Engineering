from typing import Dict, List
from datetime import datetime

# ============================ PRODUCT CLASS ============================
class Product:
    """
    A class representing a product with attributes like product_id, name,
    description, price, stock, and category.
    """

    def __init__(self, product_id: int, name: str, description: str, price: float, stock: int, category: str) -> None:
        self.product_id: int = product_id
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.stock: int = stock
        self.category: str = category

    def reduce_stock(self, quantity: int):
        """Reduces the stock of the product by the given quantity."""
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} units of '{self.name}' have been reduced from stock.")
        else:
            print(f"Not enough stock for '{self.name}'. Available: {self.stock}, Requested: {quantity}")

    def to_dict(self) -> dict:
        """
        Converts product details to a dictionary.
        """
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
        }

    # ----------------------- Setters & Getters ------------------------
    def get_product_id(self) -> int:
        return self.product_id

    def set_product_id(self, product_id: int) -> None:
        self.product_id = product_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_description(self) -> str:
        return self.description

    def set_description(self, description: str) -> None:
        self.description = description

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if price == 0:
            raise ValueError("Price cannot be zero.")
        self.price = price

    def get_stock(self) -> int:
        return self.stock

    def set_stock(self, stock: int) -> None:
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        self.stock = stock

    def get_category(self) -> str:
        return self.category

    def set_category(self, category: str) -> None:
        valid_categories: List[str] = ['electronics', 'fashion', 'furniture', 'groceries']
        if category.lower() not in valid_categories:
            raise ValueError("Category must be one of the following: electronics, fashion, furniture, groceries.")
        self.category = category.lower()

    # ----------------------- Additional Methods ------------------------
    def apply_discount(self, discount_percentage: float) -> None:
        """Apply a discount to the price."""
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.price -= self.price * (discount_percentage / 100)

    def buy_product(self, quantity: int) -> None:
        """Reduce stock if enough quantity is available."""
        if quantity > self.stock:
            raise ValueError("Not enough stock available.")
        self.stock -= quantity

    def is_available(self) -> bool:
        return self.stock > 0

    # ----------------------- Magic Methods ------------------------
    def __str__(self) -> str:
        return (f"Product ID: {self.product_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Price: ${self.price:.2f}\n"
                f"Stock: {self.stock}\n"
                f"Category: {self.category}")

    def __repr__(self) -> str:
        return (f"Product(product_id={self.product_id!r}, name={self.name!r}, "
                f"description={self.description!r}, price={self.price:.2f}, "
                f"stock={self.stock}, category={self.category!r})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.product_id == other.product_id

    def __hash__(self) -> int:
        return hash(self.product_id)

    # For demonstration (adding, subtracting stock, etc.)
    def __add__(self, other: 'Product') -> 'Product':
        if not isinstance(other, Product):
            raise TypeError("Cannot add Product to non-Product object.")
        return Product(self.product_id, self.name, self.description,
                       self.price, self.stock + other.stock, self.category)

    def __sub__(self, other: 'Product') -> 'Product':
        if not isinstance(other, Product):
            raise TypeError("Cannot subtract Product from non-Product object.")
        return Product(self.product_id, self.name, self.description,
                       self.price, self.stock - other.stock, self.category)

    def __mul__(self, other: 'Product') -> 'Product':
        if not isinstance(other, Product):
            raise TypeError("Cannot multiply Product with non-Product object.")
        return Product(self.product_id, self.name, self.description,
                       self.price, self.stock * other.stock, self.category)

    def __truediv__(self, other: 'Product') -> 'Product':
        if not isinstance(other, Product):
            raise TypeError("Cannot divide Product by non-Product object.")
        if other.stock == 0:
            raise ZeroDivisionError("Division by zero stock not allowed.")
        return Product(self.product_id, self.name, self.description,
                       self.price, self.stock // other.stock, self.category)

    def __neg__(self) -> 'Product':
        return Product(self.product_id, self.name, self.description,
                       self.price, -self.stock, self.category)

    def __abs__(self) -> 'Product':
        return Product(self.product_id, self.name, self.description,
                       self.price, abs(self.stock), self.category)

    def __bool__(self) -> bool:
        return bool(self.stock)

    def __int__(self) -> int:
        return int(self.stock)

    def __float__(self) -> float:
        return float(self.stock)

    def __complex__(self) -> complex:
        return complex(self.stock)

    def __index__(self) -> int:
        return self.stock


# ============================ CART CLASS ============================
class Cart:
    """
    A simple shopping cart class to store products and quantities.
    """
    def __init__(self):
        # Dictionary structure: { product_id: {"product": Product, "quantity": int} }
        self.cart_items: Dict[int, Dict[str, object]] = {}

    def add_product(self, product: Product, quantity: int):
        """Adds (or increments) a product in the cart by the given quantity."""
        if product.product_id in self.cart_items:
            self.cart_items[product.product_id]["quantity"] += quantity
        else:
            self.cart_items[product.product_id] = {"product": product, "quantity": quantity}

    def remove_product(self, product_id: int):
        """Removes a product from the cart."""
        if product_id in self.cart_items:
            del self.cart_items[product_id]
        else:
            raise ValueError("Product not found in the cart.")
        if not self.cart_items:
            print("Your cart is now empty.")

    def update_quantity(self, product_id: int, new_quantity: int) -> None:
        """Updates the quantity of a product in the cart."""
        if product_id in self.cart_items:
            if new_quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            self.cart_items[product_id]["quantity"] = new_quantity
        else:
            raise ValueError("Product not found in the cart.")

    def calculate_total(self) -> float:
        """Calculates the total price of all items in the cart."""
        total: float = 0.0
        for item in self.cart_items.values():
            prod = item["product"]
            qty = item["quantity"]
            total += prod.get_price() * qty
        return total

    def view_cart(self) -> None:
        """Displays all products in the cart."""
        if not self.cart_items:
            print("Your cart is empty.")
            return
        print("\n=== Your Cart ===")
        for item in self.cart_items.values():
            product = item["product"]
            quantity = item["quantity"]
            print(f"Product ID: {product.get_product_id()}\n"
                  f"Name: {product.get_name()}\n"
                  f"Description: {product.get_description()}\n"
                  f"Price: ${product.get_price():.2f}\n"
                  f"Quantity in Cart: {quantity}\n")

    def empty_cart(self) -> None:
        """Clears the cart."""
        self.cart_items.clear()
        print("Cart emptied successfully.")

    def __str__(self) -> str:
        return f"Cart Items: {self.cart_items}"

    def __repr__(self) -> str:
        return f"Cart(cart_items={self.cart_items!r})"


# ============================ ORDER CLASS ============================
class Order:
    """
    Represents a customer's order with:
      - order_id
      - cart (Cart object)
      - total_amount
      - customer_name
      - customer_address
      - order_status (pending, confirmed, shipped, delivered, cancelled)
      - payment_method
    """
    def __init__(self, order_id: int, cart: Cart, total_amount: float,
                 customer_name: str, customer_address: str, order_status: str, payment_method: str):
        self.order_id = order_id
        self.cart = cart
        self.total_amount = total_amount
        self.customer_name = customer_name
        self.customer_address = customer_address
        self._order_status = order_status  # internal variable
        self.payment_method = payment_method

    def place_order(self):
        """Confirms the order and reduces the stock of products in the cart."""
        for item in self.cart.cart_items.values():
            product = item["product"]
            quantity = item["quantity"]
            product.reduce_stock(quantity)
        # In a real scenario, you'd mark this order in a database
        print(f"Order #{self.order_id} has been placed successfully.")

    def view_order_details(self):
        """Displays all details of the order."""
        print(f"\n=== Order Details (Order ID: {self.order_id}) ===")
        print("Products:")
        for item in self.cart.cart_items.values():
            product = item["product"]
            quantity = item["quantity"]
            print(f" - {product.name} (Price: ${product.price:.2f}, Quantity: {quantity})")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Address: {self.customer_address}")
        print(f"Total Amount: ${self.total_amount:.2f}")
        print(f"Payment Method: {self.payment_method}")
        print(f"Order Status: {self.order_status}")

    def cancel_order(self):
        """Allows the customer to cancel the order if it's still pending."""
        if self.order_status == 'pending':
            self.order_status = 'cancelled'
            print(f"Order #{self.order_id} has been cancelled.")
        else:
            print(f"Order #{self.order_id} cannot be cancelled (current status: {self.order_status}).")

    # ------------- Property-based Getters/Setters for order_status -------------
    @property
    def order_status(self):
        """Getter method for order status."""
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        """Setter method for order status."""
        valid_statuses = ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']
        if value not in valid_statuses:
            raise ValueError(f"Invalid order status: {value}. Must be one of {valid_statuses}.")
        self._order_status = value

    # ------------- Customer Details -------------
    @property
    def customer_details(self):
        """Returns combined customer name and address."""
        return f"Name: {self.customer_name}, Address: {self.customer_address}"

    @customer_details.setter
    def customer_details(self, value):
        parts = value.split(',')
        if len(parts) < 2:
            raise ValueError("Must provide both name and address, separated by a comma.")
        self.customer_name = parts[0].strip()
        self.customer_address = ",".join(parts[1:]).strip()

    # ------------- String Representations -------------
    def __str__(self):
        return (f"Order ID: {self.order_id}, "
                f"Total Amount: ${self.total_amount:.2f}, "
                f"Status: {self.order_status}")

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, total_amount={self.total_amount}, "
                f"customer_name={self.customer_name}, customer_address={self.customer_address}, "
                f"order_status={self.order_status}, payment_method={self.payment_method})")


# ============================== MAIN PROGRAM ==============================
products_db: Dict[int, Product] = {}
current_cart = Cart()
orders = []  # Store all orders here
next_order_id = 1  # Simple counter to generate order IDs


def add_product_ui():
    """Add a new product via user input."""
    try:
        product_id = int(input("Enter Product ID: ").strip())
        if product_id in products_db:
            print("A product with this ID already exists.")
            return
        name = input("Enter Product Name: ").strip()
        description = input("Enter Product Description: ").strip()
        price = float(input("Enter Price: ").strip())
        stock = int(input("Enter Stock: ").strip())
        category = input("Enter Category (electronics/fashion/furniture/groceries): ").strip().lower()

        new_product = Product(product_id, name, description, price, stock, category)
        products_db[product_id] = new_product
        print(f"Product '{name}' added successfully.")
    except ValueError as ve:
        print("Error in input:", ve)


def update_product_ui():
    """Update existing product details."""
    try:
        pid = int(input("Enter Product ID to update: ").strip())
        if pid not in products_db:
            print("Product not found.")
            return
        product = products_db[pid]
        print("1. Update Name")
        print("2. Update Description")
        print("3. Update Price")
        print("4. Update Stock")
        print("5. Update Category")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_name = input("Enter new name: ").strip()
            product.set_name(new_name)
            print("Name updated.")
        elif choice == "2":
            new_desc = input("Enter new description: ").strip()
            product.set_description(new_desc)
            print("Description updated.")
        elif choice == "3":
            new_price_str = input("Enter new price: ").strip()
            new_price = float(new_price_str)
            product.set_price(new_price)
            print("Price updated.")
        elif choice == "4":
            new_stock_str = input("Enter new stock: ").strip()
            new_stock = int(new_stock_str)
            product.set_stock(new_stock)
            print("Stock updated.")
        elif choice == "5":
            new_cat = input("Enter new category (electronics/fashion/furniture/groceries): ").strip()
            product.set_category(new_cat)
            print("Category updated.")
        else:
            print("Invalid choice.")
    except ValueError as ve:
        print("Error:", ve)


def remove_product_ui():
    """Remove a product from the database."""
    try:
        pid = int(input("Enter Product ID to remove: ").strip())
        if pid in products_db:
            del products_db[pid]
            print("Product removed successfully.")
        else:
            print("Product not found.")
    except ValueError:
        print("Invalid product ID.")


def view_products_ui():
    """View all products or a specific product."""
    if not products_db:
        print("No products available.")
        return
    print("\n=== Product List ===")
    for prod in products_db.values():
        print(prod)
        print("--------------------")


def add_to_cart_ui():
    """Add a product to the current cart."""
    try:
        pid = int(input("Enter Product ID: ").strip())
        if pid not in products_db:
            print("Product not found.")
            return
        quantity = int(input("Enter quantity: ").strip())
        if quantity <= 0:
            print("Quantity must be > 0.")
            return

        product = products_db[pid]
        # We do not reduce stock yet, only when the order is placed.
        current_cart.add_product(product, quantity)
        print(f"'{product.name}' added to cart.")
    except ValueError as ve:
        print("Error:", ve)


def remove_from_cart_ui():
    """Remove a product from the current cart."""
    try:
        pid = int(input("Enter Product ID to remove from cart: ").strip())
        current_cart.remove_product(pid)
        print("Product removed from cart.")
    except ValueError as ve:
        print("Error:", ve)


def update_cart_quantity_ui():
    """Update the quantity of an item in the cart."""
    try:
        pid = int(input("Enter Product ID: ").strip())
        new_qty = int(input("Enter new quantity: ").strip())
        current_cart.update_quantity(pid, new_qty)
        print("Cart updated.")
    except ValueError as ve:
        print("Error:", ve)


def view_cart_ui():
    """Displays the cart contents."""
    current_cart.view_cart()


def empty_cart_ui():
    """Empties the cart."""
    current_cart.empty_cart()


def place_order_ui():
    """Place an order and reduce product stock."""
    global next_order_id

    # If cart is empty, no order can be placed
    if not current_cart.cart_items:
        print("Cart is empty. Add products before placing an order.")
        return

    # Gather user details
    customer_name = input("Enter Customer Name: ").strip()
    customer_address = input("Enter Customer Address: ").strip()
    payment_method = input("Enter Payment Method (Cash, Card, etc.): ").strip().lower()

    total_amount = current_cart.calculate_total()

    new_order = Order(
        order_id=next_order_id,
        cart=current_cart,
        total_amount=total_amount,
        customer_name=customer_name,
        customer_address=customer_address,
        order_status='pending',
        payment_method=payment_method
    )
    # Place the order (reduces stock)
    new_order.place_order()

    # Save the order
    orders.append(new_order)
    print(f"Order #{next_order_id} placed successfully. Total = ${total_amount:.2f}")

    # Increment for the next order
    next_order_id += 1

    # Cart is typically emptied after the order is placed
    current_cart.empty_cart()


def view_all_orders_ui():
    """View all orders."""
    if not orders:
        print("No orders have been placed yet.")
        return

    print("\n=== All Orders ===")
    for ord_obj in orders:
        ord_obj.view_order_details()
        print("-------------------")


def cancel_order_ui():
    """Cancel an order if it is still pending."""
    try:
        oid = int(input("Enter Order ID to cancel: ").strip())
        # Find the order
        for ord_obj in orders:
            if ord_obj.order_id == oid:
                ord_obj.cancel_order()
                return
        print("Order not found.")
    except ValueError:
        print("Invalid Order ID.")


def update_order_details_ui():
    """Update customer details or order status."""
    try:
        oid = int(input("Enter Order ID: ").strip())
        for ord_obj in orders:
            if ord_obj.order_id == oid:
                print("1. Update Customer Details")
                print("2. Update Order Status")
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    print("Format: Name,Address")
                    new_details = input("Enter new customer details: ").strip()
                    ord_obj.customer_details = new_details  # setter
                    print("Customer details updated.")
                elif choice == "2":
                    print("Valid statuses: pending, confirmed, shipped, delivered, cancelled")
                    new_status = input("Enter new status: ").strip().lower()
                    ord_obj.order_status = new_status
                    print("Order status updated.")
                else:
                    print("Invalid choice.")
                return
        print("Order not found.")
    except ValueError as ve:
        print("Error:", ve)


def main_menu():
    while True:
        print("\nEducation Trust Nasra School - E Commerce Management System")
        print("1.  Add Product")
        print("2.  Update Product")
        print("3.  Remove Product")
        print("4.  View Products")
        print("5.  Add Product to Cart")
        print("6.  Remove Product from Cart")
        print("7.  Update Cart Quantity")
        print("8.  View Cart")
        print("9.  Empty Cart")
        print("10. Place Order")
        print("11. View All Orders")
        print("12. Cancel an Order")
        print("13. Update Order Details")
        print("14. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product_ui()
        elif choice == "2":
            update_product_ui()
        elif choice == "3":
            remove_product_ui()
        elif choice == "4":
            view_products_ui()
        elif choice == "5":
            add_to_cart_ui()
        elif choice == "6":
            remove_from_cart_ui()
        elif choice == "7":
            update_cart_quantity_ui()
        elif choice == "8":
            view_cart_ui()
        elif choice == "9":
            empty_cart_ui()
        elif choice == "10":
            place_order_ui()
        elif choice == "11":
            view_all_orders_ui()
        elif choice == "12":
            cancel_order_ui()
        elif choice == "13":
            update_order_details_ui()
        elif choice == "14":
            print("\nExiting | Education Trust Nasra School - E Commerce Management System")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
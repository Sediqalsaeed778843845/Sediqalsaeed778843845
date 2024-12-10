import tkinter as tk
from tkinter import ttk, messagebox

# Dummy product data
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 99.99},
    {"id": 2, "name": "Smartphone", "price": 799.99},
    {"id": 3, "name": "Laptop", "price": 1299.99},
    {"id": 4, "name": "Smartwatch", "price": 199.99},
    {"id": 5, "name": "Tablet", "price": 499.99},
    {"id": 6, "name": "Desktop Computer", "price": 999.99},
    {"id": 7, "name": "Gaming Console", "price": 399.99},
    {"id": 8, "name": "Camera", "price": 699.99},
    {"id": 9, "name": "E-Reader", "price": 149.99}
]

cart = []  # To store selected products
wishlist = []  # To store favorite products

# Function to clear window contents
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy() 

# Add product to cart
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Success", f"{product['name']} has been added to your cart.")

# Add product to wishlist
def add_to_wishlist(product):
    if product not in wishlist:
        wishlist.append(product)
        messagebox.showinfo("Success", f"{product['name']} has been added to your wishlist.")
    else:
        messagebox.showinfo("Info", f"{product['name']} is already in your wishlist.")

# Home Screen: Displays product catalog
def home_screen(window):
    clear_window(window)
    tk.Label(window, text="Online Shopping Platform", font=("Arial", 20)).pack(pady=10)
    
    # Product List
    for product in products:
        frame = tk.Frame(window, pady=5)
        frame.pack(fill="x", padx=10)

        tk.Label(frame, text=f"{product['name']} - ${product['price']:.2f}", font=("Arial", 14)).pack(side="left")
        tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p)).pack(side="right", padx=5)
        tk.Button(frame, text="Add to Wishlist", command=lambda p=product: add_to_wishlist(p)).pack(side="right")

    # Navigation Buttons
    tk.Button(window, text="View Cart", command=lambda: cart_screen(window), bg="blue", fg="white").pack(side="left", padx=20, pady=20)
    tk.Button(window, text="Search and Filter", command=lambda: search_filter_screen(window), bg="orange", fg="white").pack(side="left", padx=20, pady=20)
    tk.Button(window, text="View Wishlist", command=lambda: wishlist_screen(window), bg="purple", fg="white").pack(side="right", padx=20, pady=20)
    tk.Button(window, text="About & Contact", command=lambda: about_screen(window), bg="orange", fg="white").pack(side="right", padx=20, pady=20)

# Cart Screen: Displays selected items
def cart_screen(window):
    clear_window(window)
    tk.Label(window, text="Shopping Cart", font=("Arial", 20)).pack(pady=10)

    if not cart:
        tk.Label(window, text="Your cart is empty!", font=("Arial", 14)).pack(pady=10)
    else:
        for product in cart:
            tk.Label(window, text=f"{product['name']} - ${product['price']:.2f}", font=("Arial", 14)).pack(pady=5)

    tk.Button(window, text="Back to Home", command=lambda: home_screen(window), bg="gray", fg="white").pack(side="left", padx=20, pady=20)
    if cart:
        tk.Button(window, text="Checkout", command=lambda: checkout_screen(window), bg="green", fg="white").pack(side="right", padx=20, pady=20)

# Wishlist Screen: Displays favorite items
def wishlist_screen(window):
    clear_window(window)
    tk.Label(window, text="Wishlist", font=("Arial", 20)).pack(pady=10)

    if not wishlist:
        tk.Label(window, text="Your wishlist is empty!", font=("Arial", 14)).pack(pady=10)
    else:
        for product in wishlist:
            tk.Label(window, text=f"{product['name']} - ${product['price']:.2f}", font=("Arial", 14)).pack(pady=5)

    tk.Button(window, text="Back to Home", command=lambda: home_screen(window), bg="gray", fg="white").pack(pady=20)

# Search and Filter Screen
def search_filter_screen(window):
    clear_window(window)
    tk.Label(window, text="Search and Filter Products", font=("Arial", 20)).pack(pady=10)

    # Search by Name
    tk.Label(window, text="Search by Name:", font=("Arial", 14)).pack(pady=5)
    search_entry = tk.Entry(window, font=("Arial", 14), width=30)
    search_entry.pack(pady=5)

    # Filter by Price Range
    tk.Label(window, text="Filter by Price Range:", font=("Arial", 14)).pack(pady=5)
    min_price_entry = tk.Entry(window, font=("Arial", 14), width=10)
    min_price_entry.insert(0, "Min")
    min_price_entry.pack(side="left", padx=5)
    max_price_entry = tk.Entry(window, font=("Arial", 14), width=10)
    max_price_entry.insert(0, "Max")
    max_price_entry.pack(side="left", padx=5)

    results_frame = tk.Frame(window)
    results_frame.pack(pady=20)

    def display_results(filtered_products):
        for widget in results_frame.winfo_children():
            widget.destroy()
        for product in filtered_products:
            frame = tk.Frame(results_frame, pady=5)
            frame.pack(fill="x", padx=10)
            tk.Label(frame, text=f"{product['name']} - ${product['price']:.2f}", font=("Arial", 14)).pack(side="left")
            tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p)).pack(side="right", padx=5)
            tk.Button(frame, text="Add to Wishlist", command=lambda p=product: add_to_wishlist(p)).pack(side="right")

    def apply_filters():
        query = search_entry.get().strip().lower()
        try:
            min_price = float(min_price_entry.get())
            max_price = float(max_price_entry.get())
        except ValueError:
            min_price = max_price = None

        filtered = [
            product for product in products
            if (query in product["name"].lower() or not query) and
               (min_price is None or product["price"] >= min_price) and
               (max_price is None or product["price"] <= max_price)
        ]
        display_results(filtered)

    tk.Button(window, text="Search & Apply Filters", command=apply_filters, bg="orange", fg="white").pack(pady=10)
    tk.Button(window, text="Back to Home", command=lambda: home_screen(window), bg="gray", fg="white").pack(pady=10)

# Checkout Screen: Secure Payment Process
def checkout_screen(window):
    clear_window(window)
    tk.Label(window, text="Checkout", font=("Arial", 20)).pack(pady=10)

    total_price = sum(product["price"] for product in cart)
    tk.Label(window, text=f"Total Amount: ${total_price:.2f}", font=("Arial", 14)).pack(pady=10)

    tk.Label(window, text="Enter Payment Details:", font=("Arial", 14)).pack(pady=5)
    payment_entry = tk.Entry(window, font=("Arial", 14), width=30)
    payment_entry.pack(pady=5)

    def confirm_order():
        if payment_entry.get().strip():
            messagebox.showinfo("Order Confirmed", "Thank you for your purchase!")
            cart.clear()
            home_screen(window)
        else:
            messagebox.showerror("Error", "Please enter payment details.")

    tk.Button(window, text="Confirm Order", command=confirm_order, bg="green", fg="white").pack(pady=20)
    tk.Button(window, text="Back to Cart", command=lambda: cart_screen(window), bg="gray", fg="white").pack(pady=10)

# About & Contact Screen
def about_screen(window):
    clear_window(window)
    tk.Label(window, text="About & Contact", font=("Arial", 20)).pack(pady=10)
    tk.Label(window, text="Developed by:", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(window, text="443404294 - خواطر عبدالله القحطاني", font=("Arial", 14)).pack(pady=2)
    tk.Label(window, text="443301118 - هاجر محمد الاسمري", font=("Arial", 14)).pack(pady=2)
    tk.Label(window, text="For any inquiries, please contact us.", font=("Arial", 14)).pack(pady=10)
    tk.Button(window, text="Back to Home", command=lambda: home_screen(window), bg="gray", fg="white").pack(pady=20)

# Main Window Setup
root = tk.Tk()
root.title("Online Shopping Platform")
root.geometry("800x600")

home_screen(root)

root.mainloop()

# Function to add a product to the cart
def add_to_cart(product):

    """
    Adds the selected product to the shopping cart.
    
    Args:
        product (dict): Dictionary containing product details.
    """
    
    cart.append(product)
    messagebox.showinfo("Success", f"{product['name']} has been added to your cart.")


"""
Beard Masters order management module
Handles order processing and file operations
"""

from datetime import datetime
import os

class OrderManager:
    def __init__(self):
        # Create orders directory if it doesn't exist
        if not os.path.exists('orders'):
            os.makedirs('orders')
        # Set the filename for storing orders
        self.order_file = "beard_masters_orders.txt"

    def save_order(self, cart, appointment):
        """
        Saves order details and appointment information to a file
        Args:
            cart: List of items in shopping cart
            appointment: Appointment details object
        Returns:
            bool: True if save successful, False otherwise
        """
        try:
            # Open file in append mode to add new orders
            with open(self.order_file, 'a') as f:
                # Write order header with timestamp
                f.write("\n=== Beard Masters Order Summary ===\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
                
                # Process and write shopping cart items if present
                if cart:
                    f.write("Items Ordered:\n")
                    total = 0
                    # Loop through each item and write details
                    for item in cart:
                        f.write(f"- {item.name}: ${item.price:.2f}\n")
                        total += item.price
                    # Write total amount
                    f.write(f"\nTotal: ${total:.2f}\n")
                
                # Write appointment details if present
                if appointment:
                    f.write("\nAppointment Details:\n")
                    f.write(str(appointment))
                    
            return True
        except Exception as e:
            # Handle any errors during file operations
            print(f"Error saving order: {str(e)}")
            return False

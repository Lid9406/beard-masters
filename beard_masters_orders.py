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
        self.order_file = "beard_masters_orders.txt"

    def save_order(self, cart, appointment):
        try:
            with open(self.order_file, 'a') as f:
                f.write("\n=== Beard Masters Order Summary ===\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
                
                if cart:
                    f.write("Items Ordered:\n")
                    total = 0
                    for item in cart:
                        f.write(f"- {item.name}: ${item.price:.2f}\n")
                        total += item.price
                    f.write(f"\nTotal: ${total:.2f}\n")
                
                if appointment:
                    f.write("\nAppointment Details:\n")
                    f.write(str(appointment))
                    
            return True
        except Exception as e:
            print(f"Error saving order: {str(e)}")
            return False
"""
Beard Masters Business Management System
Main application file for appointment booking and product ordering
Date: February 11, 2025
"""

from datetime import datetime
import json
from beard_masters_services import BeardProduct, GroomingService, LuxuryGroomingService
from beard_masters_orders import OrderManager

class BeardMastersSystem:
    def __init__(self):
        # Initialize product catalog with basic and premium products
        self.products = {
            'Basic Products': [
                BeardProduct('Beard Oil', 25.99, 'Premium beard moisturizer'),
                BeardProduct('Beard Wash', 15.99, 'Gentle cleansing shampoo'),
                BeardProduct('Beard Brush', 19.99, 'Professional boar bristle')
            ],
            'Premium Products': [
                BeardProduct('Trimmer Kit', 79.99, 'Professional trimmer set'),
                BeardProduct('Scissors', 34.99, 'Premium steel scissors')
            ]
        }
        
        # Initialize service catalog with basic and luxury services
        self.services = {
            'Basic Services': [
                GroomingService('Basic Trim', 30.00, '30-minute maintenance'),
                GroomingService('Express Style', 45.00, '20-minute quick service')
            ],
            'Luxury Services': [
                LuxuryGroomingService('Royal Treatment', 80.00, '60-minute premium'),
                LuxuryGroomingService('Executive Package', 120.00, '90-minute deluxe')
            ]
        }
        
        # Initialize shopping cart and order management system
        self.cart = []
        self.order_manager = OrderManager()

    def _display_menu(self):
        """Display the main menu options"""
        print("\n=== Beard Masters Management System ===")
        print("1. View Products")
        print("2. View Services")
        print("3. Book Appointment")
        print("4. Save Order")
        print("5. Exit")

    def _view_products(self):
        """Display available products with categories, prices, and descriptions"""
        print("\n=== Available Products ===")
        for category, items in self.products.items():
            print(f"\n{category}:")
            for product in items:
                print(f"- {product.name}: ${product.price:.2f} - {product.description}")

    def _view_services(self):
        """Display available services with categories, prices, and descriptions"""
        print("\n=== Available Services ===")
        for category, items in self.services.items():
            print(f"\n{category}:")
            for service in items:
                print(f"- {service.name}: ${service.price:.2f} - {service.description}")

    def _book_appointment(self):
        """Handle appointment booking process (placeholder for future implementation)"""
        print("\nBooking system will be implemented soon.")
        # Add appointment booking logic here

    def _save_order(self):
        """Process and save the current order if cart is not empty"""
        if not self.cart:
            print("\nCart is empty!")
            return
        print("\nSaving order...")
        # Add order saving logic here

    def run(self):
        """Main application loop handling user input and navigation"""
        while True:
            try:
                # Display menu and get user input
                self._display_menu()
                choice = input("\nSelect option (1-5): ")
                
                # Process user choice
                if choice == '1':
                    self._view_products()
                elif choice == '2':
                    self._view_services()
                elif choice == '3':
                    self._book_appointment()
                elif choice == '4':
                    self._save_order()
                elif choice == '5':
                    print("\nThank you for choosing Beard Masters!")
                    break
                else:
                    print("\nInvalid choice. Please select 1-5.")
            except Exception as e:
                # Handle any unexpected errors
                print(f"\nError: {str(e)}")

# Entry point of the application
if __name__ == "__main__":
    app = BeardMastersSystem()
    app.run()

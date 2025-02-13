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
        """Display available products"""
        print("\n=== Available Products ===")
        for category, items in self.products.items():
            print(f"\n{category}:")
            for product in items:
                print(f"- {product.name}: ${product.price:.2f} - {product.description}")

    def _view_services(self):
        """Display available services"""
        print("\n=== Available Services ===")
        for category, items in self.services.items():
            print(f"\n{category}:")
            for service in items:
                print(f"- {service.name}: ${service.price:.2f} - {service.description}")

    def _book_appointment(self):
        """Book an appointment"""
        print("\nBooking system will be implemented soon.")
        # Add appointment booking logic here

    def _save_order(self):
        """Save the current order"""
        if not self.cart:
            print("\nCart is empty!")
            return
        print("\nSaving order...")
        # Add order saving logic here

    def run(self):
        while True:
            try:
                self._display_menu()
                choice = input("\nSelect option (1-5): ")
                
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
                print(f"\nError: {str(e)}")

if __name__ == "__main__":
    app = BeardMastersSystem()
    app.run()
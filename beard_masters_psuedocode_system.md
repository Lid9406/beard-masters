# ALGORITHM BeardMastersSystem

# System Setup

BEGIN
    # Initialize System Components
    DECLARE storage_regular_products    // For oils, brushes, etc.
    DECLARE storage_premium_products    // For trimmers, scissors
    DECLARE storage_basic_services     // For trims, quick styles
    DECLARE storage_premium_services   // For royal treatments
    DECLARE shopping_cart
    DECLARE order_tracking_system

# Main Program Loop

WHILE system_is_active DO
    OUTPUT "=== BEARD MASTERS MENU ==="
    OUTPUT "1. Browse Products"
    OUTPUT "2. Browse Services"
    OUTPUT "3. Book Appointment"
    OUTPUT "4. Checkout"
    OUTPUT "5. Exit"

    INPUT user_choice
    CALL ProcessUserSelection(user_choice)
END WHILE

# Product Initialization

PROCEDURE InitializeProducts()
    # Regular Products
    AddProduct("Beard Oil", 25.99, "Daily moisturizing oil")
    AddProduct("Beard Wash", 15.99, "Cleansing wash")
    AddProduct("Beard Brush", 19.99, "Professional quality brush")

    # Premium Products
    AddProduct("Professional Trimmer Kit", 79.99, "Complete grooming set")
    AddProduct("Premium Steel Scissors", 34.99, "Professional grade")
END PROCEDURE

# Service Initialization

PROCEDURE InitializeServices()
    # Basic Services
    AddService("Basic Trim", 30.00, 30, "Standard beard trim")
    AddService("Quick Style", 45.00, 20, "Fast styling service")

    # Premium Services
    AddService("Royal Treatment", 80.00, 60, "Luxury grooming experience")
    AddService("Executive Package", 120.00, 90, "Complete premium service")
END PROCEDURE

# Order Processing

PROCEDURE ProcessOrder()
    current_timestamp ← GET_CURRENT_TIME()
    DECLARE order_summary

    FOR EACH item IN shopping_cart DO
        ADD item TO order_summary
        UPDATE_TOTAL(total_price)
    END FOR
    
    IF has_appointment THEN
        ADD appointment_details TO order_summary
    END IF
    
    SAVE order_summary TO order_tracking_system
    CLEAR shopping_cart
    OUTPUT "Order Successfully Completed"
END PROCEDURE

# Error Handling

PROCEDURE HandleError(error_message)
    LOG error_details
    OUTPUT "An error occurred: " + error_message
    RETURN TO main_menu
END PROCEDURE

END ALGORITHM

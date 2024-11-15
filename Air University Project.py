# prompt: Project Title:
# Inventory Management System (IMS)
# Objective:
# Build a console-based system that manages inventory for a small business. The system should allow admins to create, update, view, and delete products in the inventory while keeping track of stock levels and handling multiple users with role-based permissions.
# Requirements & Functionalities:
# User Authentication and Role Management
# Support different roles like “Admin” and “User.”
# Admins can add, edit, and delete products, whereas Users can only view inventory details.
# Implement a basic login system with username and password validation.
# Product Management (OOP Concepts)
# Create a Product class with attributes like product_id, name, category, price, and stock_quantity.
# Create methods for adding, editing, and deleting products.
# Store product information using lists or dictionaries.
# Inventory Operations
# Track stock levels: when stock reaches a low threshold, prompt a restocking message.
# Implement methods for viewing all product

import time
import pandas as pd

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class InventoryManagementSystem:
    def __init__(self):
        self.products = []
        self.users = {
            "admin": {"password": "admin123", "role": "admin"},
            "user": {"password": "user123", "role": "user"}
        }
        self.current_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            print(f"Logged in as {username}")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_product(self):
        if self.current_user and self.users[self.current_user]["role"] == "admin":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            stock_quantity = int(input("Enter stock quantity: "))
            product = Product(product_id, name, category, price, stock_quantity)
            self.products.append(product)
            print("Product added successfully.")
        else:
            print("You do not have permission to add products.")

    def edit_product(self):
        if self.current_user and self.users[self.current_user]["role"] == "admin":
            product_id = input("Enter product ID to edit: ")
            for product in self.products:
                if product.product_id == product_id:
                    new_name = input("Enter new product name (or press enter to keep the same): ")
                    new_category = input("Enter new product category (or press enter to keep the same): ")
                    new_price = input("Enter new product price (or press enter to keep the same): ")
                    new_stock = input("Enter new stock quantity (or press enter to keep the same): ")

                    if new_name:
                        product.name = new_name
                    if new_category:
                        product.category = new_category
                    if new_price:
                        product.price = float(new_price)
                    if new_stock:
                        product.stock_quantity = int(new_stock)

                    print("Product updated successfully.")
                    return
            print("Product not found.")
        else:
            print("You do not have permission to edit products.")

    def delete_product(self):
        if self.current_user and self.users[self.current_user]["role"] == "admin":
            product_id = input("Enter product ID to delete: ")
            for i, product in enumerate(self.products):
                if product.product_id == product_id:
                    del self.products[i]
                    print("Product deleted successfully.")
                    return
            print("Product not found.")
        else:
            print("You do not have permission to delete products.")

    def view_products(self):
        print("Current Inventory:")
        if self.products:
            for product in self.products:
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Stock: {product.stock_quantity}")
        else:
            print("No products in the inventory.")

    def restock_alert(self):
        low_stock_threshold = 10  # You can change this threshold
        for product in self.products:
            if product.stock_quantity <= low_stock_threshold:
                print(f"Warning: Low stock for {product.name} (ID: {product.product_id}). Current stock: {product.stock_quantity}")


def main():
    ims = InventoryManagementSystem()
    while True:
        if not ims.current_user:
            print("\nWelcome to the Inventory Management System")
            if ims.login():
                pass
            else:
                continue
        print("\nSelect an action:")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Restock Alert")
        print("6. Logout")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Thank you for using the Inventory Management System. Goodbye!")
            break
        if choice == '1':
            ims.add_product()
        elif choice == '2':
            ims.edit_product()
        elif choice == '3':
            ims.delete_product()
        elif choice == '4':
            ims.view_products()
        elif choice == '5':
            ims.restock_alert()
        elif choice == '6':
            ims.current_user = None
            print("Logged out.")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
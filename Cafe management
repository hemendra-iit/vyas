import tkinter as tk
from tkinter import messagebox
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock & Cafe System")
root.geometry("400x500")
root.config(bg="lightgrey")

# ========== Digital Clock ==========
def update_time():
    time_string = strftime('%H:%M:%S %p\n%d-%m-%Y')
    clock_label.config(text=time_string)
    clock_label.after(1000, update_time)  # Update every second

clock_label = tk.Label(root, font=("Arial", 20, "bold"), bg="violet", fg="white", padx=10, pady=10)
clock_label.pack(pady=10)
update_time()

# ========== Cafe System ==========
menu = {"Coffee": 3.50, "Tea": 2.50, "Sandwich": 5.00, "Cake": 2.00, "Pasta": 6.50}
order = {}

# Function to update total
def update_total():
    total = sum(menu[item] * qty for item, qty in order.items())
    total_label.config(text=f"Total: ${total:.2f}")

# Function to add item to order
def add_item(item):
    order[item] = order.get(item, 0) + 1
    update_total()

# Function to show order
def show_order():
    if not order:
        messagebox.showinfo("Order", "No items in order")
        return
    
    order_details = "\n".join([f"{item} x {qty} - ${menu[item] * qty:.2f}" for item, qty in order.items()])
    order_details += f"\n\nTotal: ${sum(menu[item] * qty for item, qty in order.items()):.2f}"
    messagebox.showinfo("Order Details", order_details)

# Function to clear order
def clear_order():
    order.clear()
    update_total()

# Create menu buttons
menu_frame = tk.Frame(root, bg="#FFA500")
menu_frame.pack(pady=10)

for item, price in menu.items():
    tk.Button(menu_frame, text=f"{item} - ${price:.2f}", font=("Arial", 12), width=20, command=lambda i=item: add_item(i)).pack(pady=3)

# Total label
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 14, "bold",), bg="lightgrey")
total_label.pack(pady=5)

# Order buttons
button_frame = tk.Frame(root, bg="lightgrey")
button_frame.pack(pady=5)

tk.Button(button_frame, text="Show Order", font=("Arial", 12), bg="green", fg="white", width=12, command=show_order).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Clear Order", font=("Arial", 12), bg="red", fg="white", width=12, command=clear_order).grid(row=0, column=1, padx=5, pady=5)

# Run application
root.mainloop()

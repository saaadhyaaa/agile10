import threading
import time
import os
from flask import Flask, request, jsonify
app = Flask(__name__)
def compute_total(price_str, quantity_str):
    try:
        price = float(price_str or 0)
        quantity = int(quantity_str or 0)
        total = price * quantity
        return {'status': 'Success', 'total_bill': round(total, 2)}
    except (ValueError, TypeError):
        return {'status': 'Error', 'message': 'Invalid input parameters'}
def compute_discount(price_str, quantity_str, discount_str):
    try:
        price = float(price_str or 0)
        quantity = int(quantity_str or 0)
        discount_percentage = float(discount_str or 0)
        
        subtotal = price * quantity
        discount_amount = subtotal * (discount_percentage / 100)
        final_total = subtotal - discount_amount
        
        return {
            'status': 'Success',
            'subtotal': round(subtotal, 2),
            'discount_applied': f"{discount_percentage}%",
            'discount_amount': round(discount_amount, 2),
            'final_bill': round(final_total, 2)
        }
    except (ValueError, TypeError):
        return {'status': 'Error', 'message': 'Invalid input parameters'}
@app.route('/')
def home():
    landing_text = "\n" \
                   "      BILLING SYSTEM BACKEND ACTIVE     \n" \
                   "\n" \
                   "Please use the interactive terminal window\n" \
                   "to complete your billing entries.\n"
    return landing_text, 200, {'Content-Type': 'text/plain'}
@app.route('/calculate', methods=['POST'])
def calculate_api():
    data = request.get_json() or {}
    result = compute_total(data.get('price'), data.get('quantity'))
    status_code = 200 if result['status'] == 'Success' else 400
    return jsonify(result), status_code
@app.route('/discount', methods=['POST'])
def discount_api():
    data = request.get_json() or {}
    result = compute_discount(data.get('price'), data.get('quantity'), data.get('discount'))
    status_code = 200 if result['status'] == 'Success' else 400
    return jsonify(result), status_code
def run_interactive_menu():
    time.sleep(1.5)
    while True:
        print("         BILLING SYSTEM MENU        ")
        print("1. Calculate Total Bill")
        print("2. Calculate discount")
        print("3.Exit")
        choice = input("Enter choice (1-3): ").strip()
        if choice not in ['1', '2']:
            print("[!] Invalid Choice! Please enter 1, 2, or 3.")
            continue
        price = input("Enter Item Price ($): ").strip()
        quantity = input("Enter Quantity: ").strip()
        if choice == '1':
            result = compute_total(price, quantity)
            if result['status'] == 'Success':
                print(f"\n[SUCCESS] Total Bill Amount: ${result['total_bill']}")
            else:
                print(f"\n[ERROR] Calculation failed: {result['message']}")
        elif choice == '2':
            discount = input("Enter Discount Percentage (%): ").strip()
            result = compute_discount(price, quantity, discount)
            if result['status'] == 'Success':
                print(f"\n[SUCCESS] Invoice Statement Summary:")
                print(f" -> Subtotal Baseline: ${result['subtotal']}")
                print(f" -> Markdown applied:  {result['discount_applied']}")
                print(f" -> Discount Savings:  ${result['discount_amount']}")
                print(f" -> Net Final Total:   ${result['final_bill']}")
            else:
                print(f"\n[ERROR] Discount calculation failed: {result['message']}")
if __name__ == '__main__':
  
    threading.Thread(target=run_interactive_menu, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)

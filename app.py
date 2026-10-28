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


def run_interactive_menu():

    time.sleep(1.5)
    
    while True:
 
        print("         BILLING SYSTEM MENU        ")
        print("1.  Calculate Total Bill")
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
                


if __name__ == '__main__':
  
    threading.Thread(target=run_interactive_menu, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    try:

        price = float(data.get('price') or 0)
        quantity = int(data.get('quantity') or 0)
        
        total = price * quantity
        
        return jsonify({'success': True, 'total': round(total, 2)})
    except (ValueError, TypeError) as e:
        return jsonify({'success': False, 'error': f'Invalid input values: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

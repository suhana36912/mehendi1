from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',        # Replace if your MySQL has a different user
    'password': '',        # Add your MySQL password if set
    'database': 'mehendi'
}
@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    address = data.get('address')
    booking_date = data.get('booking_date')
    client_count = data.get('client_count')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = '''
            INSERT INTO bookings (name, phone, email, address, booking_date, client_count)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (name, phone, email, address, booking_date, client_count)
        cursor.execute(query, values)
        conn.commit()

        return jsonify({'message': 'Booking submitted successfully'}), 200
    except mysql.connector.Error as err:
        print("Error:", err)
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)




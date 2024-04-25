from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import mysql.connector

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',  # Assuming MySQL is running on the same machine
    user='root',
    password='admin',
    database='praveenSQL'  # Change this to your database name
)

# Function to fetch users from MySQL
def get_users_from_mysql():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    return users

def get_player_stats_from_mysql():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM playerstats')
    player_stats = cursor.fetchall()
    cursor.close()
    return player_stats
@app.route('/users', methods=['GET'])
def get_users():
    users = get_users_from_mysql()
    return jsonify(users)
@app.route('/playerStats', methods=['GET'])
def get_player_stats():
    player_stats = get_player_stats_from_mysql()
    return jsonify(player_stats)

if __name__ == '__main__':
    app.run(debug=True)

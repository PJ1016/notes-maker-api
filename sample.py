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


@app.route('/battingStats', methods=['GET'])
def get_batting_stats():
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM playerStats where playerRole="Batsman" or playerRole="Wicket Keeper"')
    batting_stats = cursor.fetchall()
    cursor.close()
    return jsonify(batting_stats)

@app.route('/playerDetails/<int:id>',methods=['GET'])
def get_player_details(id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM playerStats where id=%s', (id,))
    player_info=cursor.fetchall()
    cursor.close()
    return jsonify(player_info)

if __name__ == '__main__':
    app.run(debug=True)

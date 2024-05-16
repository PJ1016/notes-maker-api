from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import mysql.connector
from flask import request

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
    cursor.execute('SELECT * FROM playerStats where team="SRH" or team="MI" or team="KKR    "')
    batting_stats = cursor.fetchall()
    cursor.close()
    return jsonify(batting_stats)

@app.route('/playerDetails/<int:id>',methods=['GET'])
def get_player_details(id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM playerStats where id=%s', (id,))
    player_info=cursor.fetchall()
    if(len(player_info)==0):
        return jsonify([])
    cursor.close()
    return jsonify(player_info[0])

@app.route('/playerInfo',methods=['GET'])
def get_player_info():
    cursor = connection.cursor(dictionary=True)
    try:
        page = int(request.args.get('_page', 1))
        print(page)
    except ValueError:
        return jsonify({"error": "Invalid page number"}), 400
    offset=(page-1)*2
    cursor.execute("select * from player_info limit 2 offset %s",(offset,))
    player_info=cursor.fetchall()
    cursor.close()
    return jsonify(player_info)
@app.route("/playerDescription/<int:id>",methods=['GET'])
def get_player_description(id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select playerDescription from player_info where id=%s",(id,))
    player_description=cursor.fetchall()
    cursor.close()
    return jsonify(player_description)
if __name__ == '__main__':
    app.run(debug=True)

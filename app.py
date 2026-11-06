import os
from typing import List, Literal, Dict
from flask import Flask, Response, jsonify
from psycopg2 import OperationalError, connect
from psycopg2.extensions import connection, cursor

app = Flask(__name__)

DB_HOST = os.getenv("DATABASE_HOST")
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")


def initialize_db_connection(
    db_host: str, db_user: str, db_password: str, db_name: str
) -> connection:
    conn = connect(host=db_host, user=db_user, password=db_password, database=db_name)

    return conn


@app.route("/health", methods=["GET"])
def health() -> tuple[Response, Literal[200, 400]]:
    try:
        conn = initialize_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

        conn.close()

        return jsonify({"message": "Database connection is healthy!"}), 200

    except OperationalError:
        return jsonify({"message": "Database is unavailable!"}), 503


@app.route("/users", methods=["GET"])
def get_users() -> tuple[Response, Literal[200]]:
    try:
        conn = initialize_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        users_list: List[Dict[int, str, str]] = []

        cursor: cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")

        for row in cursor.fetchall():
            users_list.append({"id": row[0], "name": row[1], "email": row[2]})

        if not users_list:
            return jsonify({"message": "No users found!"}), 404

        cursor.close()
        conn.close()

        return (
            jsonify({"message": "Users retrieved successfully!", "users": users_list}),
            200,
        )
    except OperationalError:
        return jsonify({"message": "Database is unavailable!"}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

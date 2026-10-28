from sqlite3 import Connection, Cursor
from typing import List, Literal, Dict

from flask import Flask, Response, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DATABASE_HOST")
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")


def initialize_db_connection(
    db_host: str, db_user: str, db_password: str, db_name: str
) -> Connection | tuple[Response, Literal[400]]:
    try:
        return psycopg2.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
    except Exception as exc:
        return (
            jsonify({"message": "Database connection failed!", "error": str(exc)}),
            400,
        )


@app.route("/health", methods=["GET"])
def home() -> tuple[Response, Literal[200]]:
    return jsonify({"message": "API is alive!"}), 200


@app.route("/users", methods=["GET"])
def get_users() -> tuple[Response, Literal[200]]:
    conn = initialize_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    try:
        users_list: List[Dict[int, str, str]] = []

        cursor: Cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")

        for row in cursor.fetchall():
            users_list.append({"id": row[0], "name": row[1], "email": row[2]})

        if not users_list:
            return jsonify({"message": "No users found!"}), 404

        return (
            jsonify({"message": "Users retrieved successfully!", "users": users_list}),
            200,
        )
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

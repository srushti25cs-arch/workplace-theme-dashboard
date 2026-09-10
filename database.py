import sqlite3
import pandas as pd

DB_NAME = "workplace.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def create_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS survey_comments (

            record_id TEXT PRIMARY KEY,

            employee_alias TEXT,

            department TEXT,

            input_text TEXT,

            category TEXT,

            source_id TEXT,

            score REAL,

            status TEXT,

            reviewer_action TEXT,

            audit_timestamp TEXT

        )
    """)

    connection.commit()

    connection.close()


def load_data():

    df = pd.read_csv("survey_data.csv")

    connection = get_connection()

    df.to_sql(
        "survey_comments",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()


def get_comments():

    connection = get_connection()

    df = pd.read_sql(
        "SELECT * FROM survey_comments",
        connection
    )

    connection.close()

    return df


def update_review(
    record_id,
    category,
    status,
    reviewer_action
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE survey_comments

        SET category = ?,
            status = ?,
            reviewer_action = ?

        WHERE record_id = ?
    """, (
        category,
        status,
        reviewer_action,
        record_id
    ))

    connection.commit()

    connection.close()
"""
Database module for AI Pipeline Monitor.
"""

import duckdb


class Database:

    def __init__(self, db_path="pipeline_monitor.db"):
        self.connection = duckdb.connect(db_path)

    def create_tables(self):

        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS pipeline_executions (

            id INTEGER PRIMARY KEY,

            pipeline_name VARCHAR,

            workspace VARCHAR,

            status VARCHAR,

            duration_seconds INTEGER,

            records_processed INTEGER,

            error_message VARCHAR,

            execution_time TIMESTAMP

        );
        """)


if __name__ == "__main__":

    db = Database()

    db.create_tables()

    print("Database created successfully.")

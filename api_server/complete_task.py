from block_task import ask_input, block_task
from utils import connect_to_db
from receive_table_db import store_task_in_database

def complete_task():
    table, task_id, blocker_name = ask_input()
    block_task(table, task_id, blocker_name)
    conn = connect_to_db(db_name='tasks.db')
    # Create table if not exists

    # Prompt user for the department name
    department = input("Enter the department name: ")

    store_task_in_database()

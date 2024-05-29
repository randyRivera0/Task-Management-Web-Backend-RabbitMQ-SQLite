import os
import datetime
import sqlite3, utils
from importance_enum import Importance


def formula(duration, progress, deadline):
    day_format = "%d-%m-%Y"
    datetime_object = datetime.datetime.strptime(deadline, day_format)
    return (datetime_object - datetime.datetime.today()).total_seconds() / 3600 - (duration * (1 - progress))


# someone sends a message here for updating
# Connects to the db, fetch, sort, upload to redis, and publish to clients

# If it were a db, ORDER BY importance, time_range, add column time_range, and order db



# hours_left = duration (hrs) * (1 - progress (0-1))
# time_range = days_to_hours((deadline - time.day.today)) - hours_left
# Prioritize by time_range inside medium: lower values first (it means no time)


def rearrange_table2():
    conn = utils.connect_to_db()

    c = conn.cursor()

    c.execute(f'''SELECT *,
        duration, progress, deadline, formula(duration, progress, deadline) AS time_range
        FROM finance
        ORDER BY importance DESC, time_range;
        ''')
    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    conn.close()

rearrange_table2()

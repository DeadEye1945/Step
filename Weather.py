import sqlite3
try:
    import schedule
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'schedule'])
    exit()

from datetime import datetime

def save_to_database(date_time, temperature):
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time TEXT,
            temperature INTEGER
        )
    ''')

    cursor.execute('INSERT INTO weather (date_time, temperature) VALUES (?, ?)', (date_time, temperature))

    connection.commit()
    connection.close()

def update_weather():
    dates = ["16 Січня"] * 8
    times = ["2:00", "5:00", "8:00", "11:00", "14:00", "1:00"]
    temperatures = [-2, -2, -4, -3, -3, -5, -7, -9]
    current_date = datetime.now().strftime("%Y-&m-%d")
    for i in range(len(times)):
        date_time = f"{current_date} {times[1]}"
        temperature = temperatures[i]
        save_to_database(date_time, temperature)
    update_weather()
    schedule.every(30).minutes.do(update_weather)
    try:
        while True:
            schedule.run_pending()
    except KeyboardInterrupt:
        print("Програму зупинено")

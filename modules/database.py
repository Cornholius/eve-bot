import sqlite3
import pickle


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('database.db')

    def add_coords(self, name, coords):
        coords = pickle.dumps(coords)
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Ui SET coords = ? WHERE name = ?', (coords, name,))
            conn.commit()

    def get_data(self, name):   # Получает имя, выдаёт координаты
        with self.connection as conn:
            cursor = conn.cursor()
            ui = cursor.execute('SELECT coords from Ui WHERE name = ?', (name,)).fetchone()[0]
            ui = pickle.loads(ui)
            return ui

    @staticmethod
    def initialization():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(''
                       'create table if not exists Ui '
                       '('
                       'id integer primary key, '
                       'name varchar, '
                       'coords blob'
                       ')')
        cursor.execute("""
        INSERT INTO Ui (name, coords) 
        VALUES ('overview', ''), ('chat', ''), ('cargo', ''), ('drones', ''), ('spots', ''), ('probe_scanner', '');
        """)
        connection.commit()
        connection.close()

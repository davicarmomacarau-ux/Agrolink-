# ============================================
# AgroLink - database.py
# ============================================

import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="agrolink.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Tabela de dispositivos/sensores
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS devices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    status TEXT DEFAULT 'Ativo'
                )
            """)
            # Tabela de leituras de telemetria
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS telemetry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_id INTEGER,
                    temperature REAL,
                    humidity REAL,
                    timestamp TEXT,
                    FOREIGN KEY (device_id) REFERENCES devices (id)
                )
            """)
            
            # Popula sensores padrão se a tabela estiver vazia
            cursor.execute("SELECT COUNT(*) FROM devices")
            if cursor.fetchone()[0] == 0:
                cursor.executemany(
                    "INSERT INTO devices (name, type, status) VALUES (?, ?, ?)",
                    [
                        ("Estufa Principal - Umidade/Temp", "Estufa", "Ativo"),
                        ("Pivô Central de Irrigação 01", "Irrigação", "Ativo"),
                        ("Sensor de Solo - Talhão B", "Solo", "Ativo")
                    ]
                )
            conn.commit()

    def add_telemetry(self, device_id, temp, humidity):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute(
                "INSERT INTO telemetry (device_id, temperature, humidity, timestamp) VALUES (?, ?, ?, ?)",
                (device_id, temp, humidity, now)
            )
            conn.commit()

    def get_latest_telemetry(self, limit=10):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT t.id, d.name, t.temperature, t.humidity, t.timestamp
                FROM telemetry t
                JOIN devices d ON d.id = t.device_id
                ORDER BY t.id DESC
                LIMIT ?
            """, (limit,))
            return cursor.fetchall()

    def get_devices(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM devices")
            return cursor.fetchall()
import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_name='mosque.db'):
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # جدول الأئمة
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS imams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # جدول مواقيت الصلاة
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prayer_times (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL UNIQUE,
                fajr TEXT NOT NULL,
                dhuhr TEXT NOT NULL,
                asr TEXT NOT NULL,
                maghrib TEXT NOT NULL,
                isha TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # جدول المتبرعين
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # جدول التبرعات
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER,
                amount REAL NOT NULL,
                donation_type TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (donor_id) REFERENCES donors (id)
            )
        ''')
        
        # جدول الطلبة
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                phone TEXT,
                parent_phone TEXT,
                level TEXT,
                group_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (group_id) REFERENCES groups (id)
            )
        ''')
        
        # جدول الأفواج
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                teacher TEXT,
                level TEXT,
                max_students INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # جدول الجداول الزمنية
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id INTEGER,
                day TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (group_id) REFERENCES groups (id)
            )
        ''')
        
        # إدخال بيانات نموذجية
        self._insert_sample_data(cursor)
        
        conn.commit()
        conn.close()
    
    def _insert_sample_data(self, cursor):
        # بيانات نموذجية للأئمة
        cursor.execute("SELECT COUNT(*) FROM imams")
        if cursor.fetchone()[0] == 0:
            imams_data = [
                ("الإمام أحمد محمد", "0123456789", "imam.ahmed@mosque.com"),
                ("الإمام محمد حسن", "0123456790", "imam.mohamed@mosque.com")
            ]
            cursor.executemany(
                "INSERT INTO imams (name, phone, email) VALUES (?, ?, ?)",
                imams_data
            )
        
        # بيانات نموذجية لمواقيت الصلاة
        cursor.execute("SELECT COUNT(*) FROM prayer_times")
        if cursor.fetchone()[0] == 0:
            prayer_times_data = [
                ("2024-01-01", "05:30", "12:15", "15:30", "18:00", "19:30"),
                ("2024-01-02", "05:29", "12:15", "15:31", "18:01", "19:31")
            ]
            cursor.executemany(
                """INSERT INTO prayer_times (date, fajr, dhuhr, asr, maghrib, isha) 
                   VALUES (?, ?, ?, ?, ?, ?)""",
                prayer_times_data
            )
        
        # بيانات نموذجية للمتبرعين
        cursor.execute("SELECT COUNT(*) FROM donors")
        if cursor.fetchone()[0] == 0:
            donors_data = [
                ("محمد عبدالله", "0501234567", "mohamed@example.com", "الرياض - حي الملز"),
                ("أحمد خالد", "0557654321", "ahmed@example.com", "الرياض - حي العليا")
            ]
            cursor.executemany(
                "INSERT INTO donors (name, phone, email, address) VALUES (?, ?, ?, ?)",
                donors_data
            )
        
        # بيانات نموذجية للطلبة
        cursor.execute("SELECT COUNT(*) FROM students")
        if cursor.fetchone()[0] == 0:
            students_data = [
                ("عمر محمد", 12, "0511111111", "0511111112", "مبتدئ"),
                ("خالد أحمد", 14, "0522222222", "0522222223", "متوسط")
            ]
            cursor.executemany(
                """INSERT INTO students (name, age, phone, parent_phone, level) 
                   VALUES (?, ?, ?, ?, ?)""",
                students_data
            )
        
        # بيانات نموذجية للأفواج
        cursor.execute("SELECT COUNT(*) FROM groups")
        if cursor.fetchone()[0] == 0:
            groups_data = [
                ("المجموعة أ", "الشيخ محمد", "مبتدئ", 20),
                ("المجموعة ب", "الشيخ أحمد", "متوسط", 15)
            ]
            cursor.executemany(
                """INSERT INTO groups (name, teacher, level, max_students) 
                   VALUES (?, ?, ?, ?)""",
                groups_data
            )

# إنشاء كائن قاعدة البيانات العالمي
db = Database()
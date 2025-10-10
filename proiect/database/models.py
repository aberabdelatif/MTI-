from .db import db
from datetime import datetime
import csv
import os

# ==============================
#        Imam Model
# ==============================
class ImamModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('SELECT * FROM imams ORDER BY name').fetchall()

    @staticmethod
    def get_count():
        with db.get_connection() as conn:
            return conn.execute('SELECT COUNT(*) FROM imams').fetchone()[0]

    @staticmethod
    def add(name, phone, email):
        if not name:
            raise ValueError("Name is required")
        with db.get_connection() as conn:
            conn.execute(
                'INSERT INTO imams (name, phone, email) VALUES (?, ?, ?)',
                (name, phone, email)
            )
            conn.commit()

    @staticmethod
    def delete(imam_id):
        with db.get_connection() as conn:
            conn.execute('DELETE FROM imams WHERE id = ?', (imam_id,))
            conn.commit()


# ==============================
#        Prayer Time Model
# ==============================
class PrayerTimeModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('SELECT * FROM prayer_times ORDER BY date DESC').fetchall()

    @staticmethod
    def get_today():
        today = datetime.now().strftime('%Y-%m-%d')
        with db.get_connection() as conn:
            return conn.execute('SELECT * FROM prayer_times WHERE date = ?', (today,)).fetchone()

    @staticmethod
    def add(date, fajr, dhuhr, asr, maghrib, isha):
        with db.get_connection() as conn:
            conn.execute(
                '''INSERT INTO prayer_times (date, fajr, dhuhr, asr, maghrib, isha)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                (date, fajr, dhuhr, asr, maghrib, isha)
            )
            conn.commit()


# ==============================
#        Donor Model
# ==============================
class DonorModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('SELECT * FROM donors ORDER BY name').fetchall()

    @staticmethod
    def get_count():
        with db.get_connection() as conn:
            return conn.execute('SELECT COUNT(*) FROM donors').fetchone()[0]

    @staticmethod
    def add(name, phone, email, address):
        if not name:
            raise ValueError("Donor name is required")
        with db.get_connection() as conn:
            conn.execute(
                'INSERT INTO donors (name, phone, email, address) VALUES (?, ?, ?, ?)',
                (name, phone, email, address)
            )
            conn.commit()


# ==============================
#        Donation Model
# ==============================
class DonationModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('''
                SELECT d.*, don.name as donor_name
                FROM donations d
                LEFT JOIN donors don ON d.donor_id = don.id
                ORDER BY d.date DESC
            ''').fetchall()

    @staticmethod
    def get_total_amount():
        with db.get_connection() as conn:
            total = conn.execute('SELECT SUM(amount) FROM donations').fetchone()[0]
            return total or 0

    @staticmethod
    def add(donor_id, amount, donation_type, date, description):
        with db.get_connection() as conn:
            conn.execute(
                '''INSERT INTO donations (donor_id, amount, donation_type, date, description)
                   VALUES (?, ?, ?, ?, ?)''',
                (donor_id, amount, donation_type, date, description)
            )
            conn.commit()


# ==============================
#        Student Model
# ==============================
class StudentModel:
    @staticmethod
    def _append_to_csv(student):
        """Append student data to CSV file after successful DB insert."""
        file_path = 'students.csv'
        file_exists = os.path.isfile(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'name', 'age', 'phone', 'parent_phone', 'level', 'group_id', 'created_at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(student)

    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('''
                SELECT s.*, g.name as group_name
                FROM students s
                LEFT JOIN groups g ON s.group_id = g.id
                ORDER BY s.name
            ''').fetchall()

    @staticmethod
    def get_count():
        with db.get_connection() as conn:
            return conn.execute('SELECT COUNT(*) FROM students').fetchone()[0]

    @staticmethod
    def get_by_level():
        with db.get_connection() as conn:
            levels = conn.execute('''
                SELECT level, COUNT(*) as count
                FROM students
                GROUP BY level
            ''').fetchall()
            return {level['level']: level['count'] for level in levels}

    @staticmethod
    def add(name, age, phone, parent_phone, level, group_id=None):
        if not name or not level:
            raise ValueError("Name and level are required")

        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''INSERT INTO students (name, age, phone, parent_phone, level, group_id, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (name, age, phone, parent_phone, level, group_id, created_at)
            )
            student_id = cursor.lastrowid
            conn.commit()

        # ✅ CSV update only after DB commit succeeded
        student = {
            'id': student_id,
            'name': name,
            'age': age,
            'phone': phone,
            'parent_phone': parent_phone,
            'level': level,
            'group_id': group_id if group_id else '',
            'created_at': created_at
        }
        StudentModel._append_to_csv(student)

    @staticmethod
    def delete(student_id):
        with db.get_connection() as conn:
            conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
            conn.commit()


# ==============================
#        Group Model
# ==============================
class GroupModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('''
                SELECT g.*, COUNT(s.id) as student_count
                FROM groups g
                LEFT JOIN students s ON g.id = s.group_id
                GROUP BY g.id
                ORDER BY g.name
            ''').fetchall()

    @staticmethod
    def get_count():
        with db.get_connection() as conn:
            return conn.execute('SELECT COUNT(*) FROM groups').fetchone()[0]

    @staticmethod
    def add(name, teacher, level, max_students):
        if not name:
            raise ValueError("Group name is required")
        with db.get_connection() as conn:
            conn.execute(
                '''INSERT INTO groups (name, teacher, level, max_students)
                   VALUES (?, ?, ?, ?)''',
                (name, teacher, level, max_students)
            )
            conn.commit()


# ==============================
#        Schedule Model
# ==============================
class ScheduleModel:
    @staticmethod
    def get_all():
        with db.get_connection() as conn:
            return conn.execute('''
                SELECT s.*, g.name as group_name
                FROM schedules s
                LEFT JOIN groups g ON s.group_id = g.id
                ORDER BY 
                    CASE s.day
                        WHEN 'السبت' THEN 1
                        WHEN 'الأحد' THEN 2
                        WHEN 'الاثنين' THEN 3
                        WHEN 'الثلاثاء' THEN 4
                        WHEN 'الأربعاء' THEN 5
                        WHEN 'الخميس' THEN 6
                        WHEN 'الجمعة' THEN 7
                    END,
                    s.start_time
            ''').fetchall()

    @staticmethod
    def add(group_id, day, start_time, end_time):
        if not day or not start_time or not end_time:
            raise ValueError("Day and times are required")
        with db.get_connection() as conn:
            conn.execute(
                '''INSERT INTO schedules (group_id, day, start_time, end_time)
                   VALUES (?, ?, ?, ?)''',
                (group_id, day, start_time, end_time)
            )
            conn.commit()

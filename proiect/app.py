from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database.models import *

app = Flask(__name__)
app.secret_key = 'mosque-management-secret-key-2024'

# === الصفحة الرئيسية ===
@app.route('/')
def index():
    # جمع الإحصائيات للصفحة الرئيسية
    imams_count = ImamModel.get_count()
    students_count = StudentModel.get_count()
    donations_total = DonationModel.get_total_amount()
    
    return render_template('index.html', 
                         imams_count=imams_count,
                         students_count=students_count,
                         donations_total=donations_total)

# === إدارة الأئمة ===
@app.route('/imams')
def imams():
    imams_list = ImamModel.get_all()
    return render_template('imams/imams.html', imams=imams_list)

@app.route('/add_imam', methods=['POST'])
def add_imam():
    try:
        name = request.form['name']
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        
        ImamModel.add(name, phone, email)
        flash('تمت إضافة الإمام بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة الإمام', 'error')
    
    return redirect(url_for('imams'))

@app.route('/delete_imam/<int:imam_id>')
def delete_imam(imam_id):
    try:
        ImamModel.delete(imam_id)
        flash('تم حذف الإمام بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء حذف الإمام', 'error')
    
    return redirect(url_for('imams'))

# === مواقيت الصلاة ===
@app.route('/prayer-times')
def prayer_times():
    times = PrayerTimeModel.get_all()
    return render_template('imams/prayer_times.html', times=times)

@app.route('/add_prayer_time', methods=['POST'])
def add_prayer_time():
    try:
        date = request.form['date']
        fajr = request.form['fajr']
        dhuhr = request.form['dhuhr']
        asr = request.form['asr']
        maghrib = request.form['maghrib']
        isha = request.form['isha']
        
        PrayerTimeModel.add(date, fajr, dhuhr, asr, maghrib, isha)
        flash('تمت إضافة مواقيت الصلاة بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة مواقيت الصلاة', 'error')
    
    return redirect(url_for('prayer_times'))

# === إدارة المتبرعين ===
@app.route('/donors')
def donors():
    donors_list = DonorModel.get_all()
    return render_template('financial/donors.html', donors=donors_list)

@app.route('/add_donor', methods=['POST'])
def add_donor():
    try:
        name = request.form['name']
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        address = request.form.get('address', '')
        
        DonorModel.add(name, phone, email, address)
        flash('تمت إضافة المتبرع بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة المتبرع', 'error')
    
    return redirect(url_for('donors'))

# === إدارة التبرعات ===
@app.route('/donations')
def donations():
    donations_list = DonationModel.get_all()
    donors_list = DonorModel.get_all()
    total_donations = DonationModel.get_total_amount()
    
    return render_template('financial/donations.html', 
                         donations=donations_list, 
                         donors=donors_list,
                         total_donations=total_donations)

@app.route('/add_donation', methods=['POST'])
def add_donation():
    try:
        donor_id = request.form.get('donor_id') or None
        amount = float(request.form['amount'])
        donation_type = request.form['donation_type']
        date = request.form['date']
        description = request.form.get('description', '')
        
        DonationModel.add(donor_id, amount, donation_type, date, description)
        flash('تمت إضافة التبرع بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة التبرع', 'error')
    
    return redirect(url_for('donations'))

# === إدارة الطلبة ===
@app.route('/students')
def students():
    students_list = StudentModel.get_all()
    levels_stats = StudentModel.get_by_level()
    
    return render_template('education/students.html', 
                         students=students_list,
                         levels_stats=levels_stats)

@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        name = request.form['name']
        age = request.form.get('age')
        phone = request.form.get('phone', '')
        parent_phone = request.form.get('parent_phone', '')
        level = request.form.get('level', '')
        
        # تحويل العمر إلى عدد صحيح إذا كان موجوداً
        age = int(age) if age else None
        
        StudentModel.add(name, age, phone, parent_phone, level)
        flash('تمت إضافة الطالب بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة الطالب', 'error')
    
    return redirect(url_for('students'))

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    try:
        StudentModel.delete(student_id)
        flash('تم حذف الطالب بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء حذف الطالب', 'error')
    
    return redirect(url_for('students'))

# === إدارة الأفواج ===
@app.route('/groups')
def groups():
    groups_list = GroupModel.get_all()
    return render_template('education/groups.html', groups=groups_list)

@app.route('/add_group', methods=['POST'])
def add_group():
    try:
        name = request.form['name']
        teacher = request.form.get('teacher', '')
        level = request.form.get('level', '')
        max_students = request.form.get('max_students')
        
        # تحويل الحد الأقصى للطلبة إلى عدد صحيح إذا كان موجوداً
        max_students = int(max_students) if max_students else None
        
        GroupModel.add(name, teacher, level, max_students)
        flash('تمت إضافة المجموعة بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة المجموعة', 'error')
    
    return redirect(url_for('groups'))

# === إدارة الجداول الزمنية ===
@app.route('/schedules')
def schedules():
    schedules_list = ScheduleModel.get_all()
    groups_list = GroupModel.get_all()
    return render_template('education/schedules.html', 
                         schedules=schedules_list, 
                         groups=groups_list)

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    try:
        group_id = request.form['group_id']
        day = request.form['day']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        
        ScheduleModel.add(group_id, day, start_time, end_time)
        flash('تمت إضافة الجدول الزمني بنجاح', 'success')
    except Exception as e:
        flash('حدث خطأ أثناء إضافة الجدول الزمني', 'error')
    
    return redirect(url_for('schedules'))

# === API للإحصائيات ===
@app.route('/api/stats')
def api_stats():
    stats = {
        'imams_count': ImamModel.get_count(),
        'students_count': StudentModel.get_count(),
        'donors_count': DonorModel.get_count(),
        'groups_count': GroupModel.get_count(),
        'donations_total': DonationModel.get_total_amount()
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
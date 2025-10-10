// تأثيرات إضافية للصفحة
document.addEventListener('DOMContentLoaded', function() {
    // تأكيد الحذف
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('هل أنت متأكد من هذا الإجراء؟')) {
                e.preventDefault();
            }
        });
    });

    // إخفاء التنبيهات تلقائياً بعد 5 ثوانٍ
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });

    // تحديث الوقت الحالي
    function updateCurrentTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString('ar-SA');
        const dateString = now.toLocaleDateString('ar-SA', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
        
        const timeElement = document.getElementById('current-time');
        if (timeElement) {
            timeElement.textContent = `${dateString} - ${timeString}`;
        }
    }

    // تحديث الوقت كل ثانية
    setInterval(updateCurrentTime, 1000);
    updateCurrentTime();
});

// وظائف للمواعيد
function formatTime(time) {
    return time.replace(/:\d+$/, '');
}

// تحقق من النماذج
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.style.borderColor = '#dc3545';
            isValid = false;
        } else {
            field.style.borderColor = '';
        }
    });

    return isValid;
}
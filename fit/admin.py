from django.contrib import admin

# Register your models here.
from fit.models import contact ,MembershipPlan,Trainer,Enrollment,Gallery,Attendance
admin.site.register(contact)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Enrollment)
admin.site.register(Gallery)
admin.site.register(Attendance)
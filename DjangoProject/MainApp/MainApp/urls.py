from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^Django/Employee/EducationEmployeeHeadCount/', include('EducationEmployeeHeadCount.urls')),
    url(r'^Django/Employee/EducationEmployeeExpenditure/', include('EducationEmployeeExpenditure.urls')),
    url(r'^fusioncharts/', include('fusioncharts.urls')),
    url(r'^admin/', admin.site.urls),
]

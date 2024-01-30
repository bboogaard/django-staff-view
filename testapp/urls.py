from django.urls import path

from testapp.views import QuickAddUserView


app_name = 'testapp'


urlpatterns = [
    path('add-user/', QuickAddUserView.as_view(), name='add_user'),
]

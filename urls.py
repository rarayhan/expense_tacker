from django.contrib import admin
from django.urls import path
from expenses.views import add_expense, expense_list, user_login, user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add-expense/', add_expense, name='add_expense'),
    path('expense-list/', expense_list, name='expense_list'),
]

# Add the following lines to serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# expense_tacker
<h2>#Set up the Django project:<br> </h2>
1. Install Django using pip: pip install django<br>
2. Create a new Django project: django-admin startproject expense_tracker<br>
3. Create a new Django app within the project: cd expense_tracker && python manage.py startapp expenses<br>
4. Define the Expense model in expenses/models.py <br> 
5. Set up the database and user authentication in expense_tracker/settings.py, configure the database settings and enable authentication: <br> 
6. Create views and templates in expenses/views.py <br> 
7. Define URLs and routing in expense_tracker/urls.py <br>
8. Create templates and static files:<br>
  8.1. Create the add_expense.html, expense_list.html, login.html, and base.html templates in the expenses/templates directory.<br> 
  8.2. Create a static directory in the project root and add necessary CSS and JS files<br> 

<h2> Run the development server:<br></h2>
Run the following command: python manage.py runserver<br>
Visit http://localhost:8000/expense-list/ in your web browser to see the expense list.<br>
Visit http://localhost:8000/add-expense/ to add new expenses.<br>
Visit http://localhost:8000/login/ to access the login page.<br>
Please make sure to properly configure the static file handling and adjust the database settings according to your needs.<br>

# This projects is demonstration of Qnline Quiz

# Walk through the Application
--> The user login through loginpage and will enter the following:
	Name - First letter should be capital
	email - email id
	Services: Select the choice between Handyman and Home Cleaning

--> Next he will land up to the Quiz page where he will get 5 questions each having 4 options
--> User will see the score

# Admin has lot of privileges like:
	localhost/admin/search - to get api view of all the questions
	localhost/admin/create - can create questions through api view
	localhost/admin/update - can update the questions
	localhost/admin/delete - can delete the questions

	localhost/admin/leader - can view the leaders of the quiz
	localhost/userresult - can view the questions and answer of each user


# Setup
 1. Download the project
 2. Go to the Handy_Project/Handy_Project folder
 3. Create django superuser 
	cmd - python manage.py migrate
	cmd - python manage.py createsuperuser
 4. Run the django server
	cmd - python django runserver
 5. Use localhost:8000 to see the Application
 
## Note
 python version - 3.6
 django version - 2.1
 	
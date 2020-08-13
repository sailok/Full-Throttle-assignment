# Full-Throttle-assignment

This is a Backend assignment based on creating a GET API and giving JSON as a response.

Live demo:
1. Restful GET API: http://sailokchinta.pythonanywhere.com/get_user_activity/

Tech Stack:
1. Django framework
2. SQLite

Models:
1. User
2. ActivityPeriod

User has a many-to-many relationship with ActivityPeriod.


Dummy data is populated in database by making a custom command. Can be accessed from Full-Throttle-assignment/FullThrottle_app/backend_test/management/commands/create_data.py

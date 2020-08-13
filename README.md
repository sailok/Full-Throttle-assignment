# Full-Throttle-assignment

This is a Backend assignment based on creating a GET API and giving JSON as a response.

Live demo:
1. Restful GET API: http://sailokchinta.pythonanywhere.com/get_user_activity/

Tech Stack:
1. Django framework
2. SQLite
3. djangorestframwork 

Models:
1. User
2. ActivityPeriod

User has a many-to-many relationship with ActivityPeriod.

Rest Api is implemented using djangorestframwork. Made serializer.py file which has classes related to these files and converts fetched data to OrderedDict with each activityperiod to its corresponding member. 

Dummy data is populated in database by making a custom command. Made method which will randomly generate ActivityPeriod objects and associate them to User objects.  

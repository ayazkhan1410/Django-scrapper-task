# Functional requrinments - Functional requirements define what a system must do

# Authentication related API's
# 1- User must register/login
# 2- Only authenticated users can access APIs
# 3- Each user can only manage their own profiles

# User Profile
# 4- User submits profile URL
# 5- System validates URL format
# 6- Detect platform automatically (Facebook, LinkedIn)
# 7- Save the profile with status of (Pending)
# 8 - We need to implement the state machine as well
# 9 - Suppose our internet got down or the website which we are targeting did not accept the request or we can say celery worker got crashed database somehow did not saved the data correctly
# 10 - also one more thing we can add more status like pending, completed, worker is retrying, failed and etc
# 11- we also need to check the celery timeout as well becuase and we need to implement the retry machnism in celery as well
# 12 - we also need to implement the logs so we can search logs according to the status like when the task is successfull we can add log after running the success, also we can add log in case of failuer (The logs must be clear it doesn't reveal the actual system code. Only the important information which is requried.)
# 13 - If the target website is unresponsive or blocking our requests, the Celery task will hit a timeout.
# 14- to prevent duplication we have 2 methods First one is that we can add unique=True in the url field and second we can use the unique_together in the model's meta class to prevent duplication of the records in the database but we also need to handle the exception in case of duplication as well because if the user try to add the same URL again then it will throw an exception so we need to handle that exception as well and return the response like (Profile with this URL already exists) and also we can return the status code like (400) as well.
# 15 - After that since we are creating the profile so it might be possible due to some issues database did not saved the data correctly and cause error so in that case we must wrap the code into try and except and we should use the transaction.atomic so the database must be created successfully or did not create any other records
# 16 - Currently we are parsing the URL based upon the person now if the user send URL like this URL/groups/betacodes since we are not parsing it so our code will throw an expcetion now to fix this we must need to check the URL path strcuture as well (we can use the regex).
# 17 - okay now the URL has been parsed and saved into the db the scrapper will start working but what if user added the URL ID which does not exist?
# 18 - We also need to implement the pagination for the API's as well because if the user have 1000 records then it will be hard to fetch all the records at once so we can implement the pagination for that as well
# 19 - We also need to implement the filteration for the API's as well because if the user have 1000 records then it will be hard to fetch all the records at once so we can implement the filteration for that as well (filteration based upon the status, platform and etc)
# 20 - We also need to implement the sorting for the API's as well because if the user have 1000 records then it will be hard to fetch all the records at once so we can implement the sorting for that as well (sorting based upon the created_at, updated_at and etc)
# 21 - We also need to implement the search for the API's as well because if the user have 1000 records then it will be hard to fetch all the records at once so we can implement the search for that as well (search based upon the URL, platform and etc)
# 22 - We also need to implement the rate limiting for the API's as well because if the user have 1000 records then it will be hard to fetch all the records at once so we can implement the rate limiting for that as well.
# 23 - We also need to implement the cache for the API's so user can get the response faster and also it will reduce the load on the database as well.
# 24 - We also need to implement the documentation like (swagger) for the API's so user can understand how to use the API's and also it will help us to maintain the API's as well.
# 25 - We also need to implement the testing for the API's so we can ensure that our API's are working fine and also it will help us to maintain the API's as well.
# 26 - now suppose if the user wants to fetch the profile data which does not exist in the database then we can return the response like (Profile not found) and also we can return the status code like (404) as well.
# 27 - now suppose if the user wants to delete the profile based upon the ID's and some ids are not exist in the database so we will show the response like (Profile with ID 1, 2, 3 not found) and also we will display the status code like (404) as well and also we can delete the records which are exist in the database as well.
# 28 - Now if the user delete the records in bulk and then try to fetch the records which are deleted then we can return the response like (Profile not found) and also we can return the status code like (404) as well.
# 29 - Now if the user delete the records in bulk and then try to delete the records which are already deleted then we can return the response like (Profile with ID 1, 2, 3 not found) and also we can return the status code like (404) as well.
# 30 - Now if the user wants to update the profile based upon the ID's and some ids are not exist in the database so we will show the response like (Profile with ID 1, 2, 3 not found) and also we will display the status code like (404) as well and also we can update the records which are exist in the database as well.

# 31 - How i am going to Create the models.py?
# - We will use the Django built in User model which will be used for authentication and also it will be used for managing the profiles as well.
# - After that we need to create the Profile model which will be used for storing the profile data and also it will be used for managing the profiles as well.
# - Possible fields for the Profile model are:
# -  (ForeignKey to User model)
# - url (CharField)
# - platform (CharField)
# - status (CharField)
# - data (JSONField)
# - task_status (CharField)
# - last_executed_at (DateTimeField)
# - is_active (BooleanField)
# - created_at (DateTimeField)
# - updated_at (DateTimeField)

# 32 - We also need to create Profile logging model which will be used for storing the logs of the profile data and also it will be used for managing the logs as well.
# - Possible fields for the Profile logging model are:
# - profile (ForeignKey to Profile model)
# - log_message (CharField)
# - created_at (DateTimeField)
# - updated_at (DateTimeField)

# 33 - We also need to create the serializers for the API's so we can convert the data into JSON format and also it will help us to validate the data as well.
# 34 - Now if the user delete 500 records in bulk delete accidently then we can implement the soft delete for the records as well so we can keep the data in the database and also we can restore the data if the user want to restore the data as well.
# 35 - We also need to implement the permissions for the API's so only authenticated users can access the API's and also only the owner of the profile can manage the profile as well.
# 36 - We also need to use the django-debug-toolbar for debugging the API's so we can easily debug the API's and also it will help us to optimize the API's as well.
# 37 - We also need to register the models in the admin panel so we can easily manage the data in the database and also it will help us to debug the API's as well.

# How i am going to desing the DB --> Updated
# First - Since we can have multiple users which can search the same records so what i am planning to do is that i will create seperate Table like ScrapTarget which will store 

# Table name: ScrapTarget
# - URL (Unique Field)
# - Platform (CharField)
# - Created_at 
# - Updated_at

# Now Next Table will be related to the Profile which will looks this
# Table name: Profile
# - ScrapTarget (ForeignKey to ScrapTarget model)
# - User (ForeignKey to User model)
# - Task Status (CharField)
# - Last Executed At (DateTimeField)
# - Is Active (BooleanField)
# - Created_at 
# - Updated_at

# Next table will be the scrapping data against that user
# Next table will be the scrapping data against that user
# Table name: Youtube Channel
# - channel_name
# - subscriber_count
# - videos_count
# - views
# - country
# - join_date
# - url
# - description
# - Profile (FK)

# Table name: Youtube Video
# Youtube Channel (FK)
# title
# upload_date
# image
# video_duration
# description
# views_count
# like_count
# comment_count
# link
# transcript_language
# transcript

# Class Web

# Next table will be for logs
# Table name: ScrapLogs
# - Profile (ForeignKey to Profile model)
# - Log type (Info, Debug, Error, Warning)
# - Log (CharField)
# - Created_at
# - Updated_at

## Manual Testing
______________________________
Back to *[Readme](https://github.com/Deepak9912/django-travel-blog)*

* I tested continuously throughout the development of the project.Each view was tested regularly. When i did not get the desired outcome, i did debugging the fixed the issues.

### Python Validation - PEP8
Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files were entered into the online checker and no errors were found in any of the custom codes.

**Django-travel-blog Blog**
1. Admin.py
![admin](https://user-images.githubusercontent.com/93731898/180001414-83f91a1f-d8a4-47f6-8b06-2d1c88c5da60.PNG)

2. Apps.py
![app](https://user-images.githubusercontent.com/93731898/180001498-5e0dcb16-4b3b-4872-bd01-f2d8f8ad1c69.PNG)

3. models.py
![models](https://user-images.githubusercontent.com/93731898/180001542-f035308e-a722-4915-b5d5-c2c539208267.PNG)

4. forms.py
![forms](https://user-images.githubusercontent.com/93731898/180001603-4469dd52-c7f8-4c6c-b33d-a4c1d8b3f177.PNG)

5. urls.py
![url](https://user-images.githubusercontent.com/93731898/180001665-8ed65077-15b4-4ccf-9f38-184129a17745.PNG)

6. views.py
![View](https://user-images.githubusercontent.com/93731898/180001710-ad6451aa-a77c-4ccb-867c-9157cb321e57.PNG)

**Django-travel-blog Contact**
1. Admin.py
![admin](https://user-images.githubusercontent.com/93731898/180001760-3bc0a277-1489-496b-8ae6-69ce45124482.PNG)

2. Apps.py
![app](https://user-images.githubusercontent.com/93731898/180001792-6d72345e-af3e-4126-a269-663e785de0d9.PNG)

3. models.py
 ![models](https://user-images.githubusercontent.com/93731898/180001854-de3a9b8c-b682-47f0-adde-7a8c37459d7b.PNG)

4. forms.py
![forms](https://user-images.githubusercontent.com/93731898/180001904-1c8432db-0c96-4908-a89f-a44d685ba429.PNG)

5. urls.py
![url](https://user-images.githubusercontent.com/93731898/180001947-7db85685-5ea4-48b8-a3c1-cb691af5150c.PNG)

6. views.py
![view](https://user-images.githubusercontent.com/93731898/180001997-c5ab272e-85bd-438f-ab87-8b25106d187e.PNG)


**Django-travel-blog Main-app**
1. asgi.py
![asgi](https://user-images.githubusercontent.com/93731898/180003644-5a496043-3153-46ab-a9f1-7513b52fba1c.PNG)

2. settings.py
![settings](https://user-images.githubusercontent.com/93731898/180003715-a53d78e5-dd7f-4567-b0f0-b8e723280039.PNG)

A few errors were raised in the settings.py file, however these were related to default django authorisation code and could not be changed to remove the errors.

3. urls.py
![url](https://user-images.githubusercontent.com/93731898/180003761-ca4b6d2e-3a22-4802-9444-4be3074581f1.PNG)

4. wsgi.py
![wsgi](https://user-images.githubusercontent.com/93731898/180003803-d60784d6-39cf-4bd6-92df-8f75bc6cfe26.PNG)


### HTML Validation 


### CSS Validation


### Javascript Validation
![jsHint](https://user-images.githubusercontent.com/93731898/180004804-9863f864-3617-4780-b897-efb1dbc9d369.PNG)

### Lighthouse
![lighthouse](https://user-images.githubusercontent.com/93731898/180081848-fe265411-3880-4a93-a49f-4b0efb2f4b44.PNG)


### Manual Testing

1. Frontend

- The Signup, Login and Logout system has no issues and is working accordingly. It shows correct interactive message to the users.
- The Navbar works fine on different screens and when the user is logged in, User name appears on the navbar with user icon.
- All the internal links are working and bring the user to the right page on the website.
- All the external links are working and bring the user to the right social media page by opening a new browser tab.
- The contact form on the contact page is working and when the user sends an email, it appears on the admin panel.
- The pagination system is working. Any posts after the sixth post appears on the next page and the user will get next or prev button to navigate.
- On the Post Details Page, the Like/unlike functionality is working without issues and shows the right interactive message to the user when the heart icon is clicked.
- The comment form has no issues and it submits a new comment once the form is completed by a registered user. Once the user submits a comment, they receive a message that their comment is waiting for approval. Once the comment is approved, user can see their message under the blog.
- The functionality to delete a message, previously sent by the user or by the superuser, is working without issues. The Bootstrap model is open to asking the user if they want to delete the message. Once the action is complete, the interactive message is displayed at the top of the page.
- The functionality to update a message, previously sent by the user or by the superuser, is working without issues. A new page is open, to update the comment when the button edit is pressed. And when the user clicks submit and new comment is updated in the comment section.
- Over all, the CRUD functionality is working without issues. Logged in users can create a new post such as update or delete their own posts, also any post can be updated or deleted on this page by the Superuser.


2. Backend

- I have tested the Admin Panel repeatedly since the start of the project development. All the models are working without issues.
- I have created, deleted, and updated data in all models without errors. The models have the behavior expected for what they were built for.
- Whenever a user comments on a post or submits a book post the Superuser has to approve it before it will be displayed on the website. This functionality is working without issues.


3. Fixed bug

- I continuously had issues with cloudinary and static files and could not deploy my project on heroku, i contacted tutors support team several times for the same issue and evenutally i created a new cloudinary account and new heroku app for the project and after that i was able to deploy my project.

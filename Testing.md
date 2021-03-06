## Manual Testing
______________________________
Back to **[Readme](https://github.com/Deepak9912/django-travel-blog)**

* I continually tested throughout the project. Each view was tested regularly. When the desired outcome was not achieved, I perfomred a debugging exercise to correct the issues.

### Python Validation - PEP8
Python testing was completed using PEP8 Online to ensure there were no syntax errors in the project. All python files were entered into the online checker and no errors were identified in any of the custom codes.

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

A few errors were detected in the settings.py file, however these were related to the default django authorisation code and could not be altered to remove the errors.

3. urls.py

![url](https://user-images.githubusercontent.com/93731898/180003761-ca4b6d2e-3a22-4802-9444-4be3074581f1.PNG)

4. wsgi.py

![wsgi](https://user-images.githubusercontent.com/93731898/180003803-d60784d6-39cf-4bd6-92df-8f75bc6cfe26.PNG)


### HTML Validation 

![html](https://user-images.githubusercontent.com/93731898/180420528-b7c68888-019a-484a-87f3-e8cd5dc10797.PNG)


### CSS Validation

![CSS](https://user-images.githubusercontent.com/93731898/180420560-8099287b-9c32-45d7-a082-2eb44c6ff693.PNG)


### Javascript Validation

![jsHint](https://user-images.githubusercontent.com/93731898/180004804-9863f864-3617-4780-b897-efb1dbc9d369.PNG)


### Lighthouse

![lighthouse](https://user-images.githubusercontent.com/93731898/180081848-fe265411-3880-4a93-a49f-4b0efb2f4b44.PNG)


### Manual Testing

1. Frontend

- The Signup, Login and Logout system has no issues and is operating accordingly. It displays correct interactive messages to the users.
- The Navbar functions correctly on different screens and when the user is logged in, the Username appears on the navbar alongside the user icon.
- All the internal links are mapping and operating correctly and bring the user to the right page on the website.
- All the external links are mapping and operating correctly and bring the user to the right social media page by opening a new browser tab.
- The contact form on the contact page is working and when the user sends an email, it appears on the admin panel.
- The pagination system is functioning correctly. Any subsequent posts, after the sixth post, will appear on the next page, and the user will be promted to click on the next or prev button to access the next set of posts.
- On the Post Details Page, the Like/unlike icon functionality is running without issues. A solid heart icon appears once the Like button is clicked and if clicked a second time, the post is unliked.
- The comment form has no issues and a new comment is submitted once the form is completed by a user. Once the user submits a comment, they receive a message that their comment is waiting for approval. Once the comment is approved, the user can see their message under the blog.
- The functionality to delete a message previously sent by the user, or by the superuser, is performing without issues. The Bootstrap model appears and asks the user if they want to delete the message. 
- The functionality to update a message previously sent by the user, or by the superuser, is operatating without issues. A new page opens when the user clicks on edit,  allowing them to update the comment. When the user clicks submit, the new comment is updated in the comment section.
- Over all, the CRUD functionality is working without issues. Logged in users can edit or delete their own posts. Also, any post can be updated or deleted on this page by the Superuser.


2. Backend

- I have tested the Admin Panel regularly since the start of the project. All the models are working without issues.
- I have created, deleted, and updated data in all models without errors. The models behaved as expected according to their function.
- Whenever a user comments on a post, the Superuser must approve the comment before it will be displayed on the website. This functionality is working without issues.


3. Fixed bug

- I continuously had issues with cloudinary and static files and could not deploy my project on heroku. I contacted tutors support team several times for the same issue and evenutally I created a new cloudinary account and new heroku app for the project and following those changes I was able to deploy my project.

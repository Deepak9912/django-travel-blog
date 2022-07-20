# Django-Travel-Blog

Project milestone 4 for Code Institute Full-stack development program with Django framework:

A travel blog website, where a user can post their travel related blogs. When the user posts their blogs, it will be displayed in reverse chronological order, so that the most recent post appears first, at the top of the web page.

The site is fully responsive and was built using the Django framework in Python.

![Screenshot_20220720_205821](https://user-images.githubusercontent.com/93731898/180079448-64f7e362-3c8c-4719-bac2-9055d4ad23ff.png)

The live site has been deployed [here](https://travelblog2022.herokuapp.com/).

## User Experience (UX)

- As a website user I can:
1. Navigate around the site and easily view the desired content.
2. View a list of travel blogs and read them.
3. Click on a blog to read the article on that blog.
4. Register for an account to avail of the services offered to members.
5. View comments on blogs so that I can read other users’ opinions.

- As logged in website user, I can:
1. Comment on blogs and give my opinion about the posts.
2. Update my comments from the blog.
3. Delete my previous comments.
4. Logout from the website.

- As a website Admin account holder, I can:
1. Create and publish a new travel blog.
2. Create draft blog posts that can be reviewed and finalised later.
3. Create a new user, blogs and categories.
4. Delete user, recipes, author, categories and comments.
5. Approve user's comments.
6. Delete a blog post.
7. Delete a user and their posts.
8. Change the website permissions for a user.

## Agile Methodology
All functionality and development of this project were managed using GitHub which Projects can be found [here](https://github.com/Deepak9912).

### The Scope

Main Site goals:
1. To provide users with a good experience when using the travel blog website.
2. To provide users with a website that is easy to navigate.
3. To provide a website with a clear purpose.
4. To provide role-based permissions that allows user to interact with the website.

### Design
The color scheme chosen for this project is mainly black and white using bootstrap colors. The text color on the navbar and footer is text-light, text-muted and text-wraning using bootstrap against a black background. The carousel section has white bold text color against a faded background image. 

![color](https://user-images.githubusercontent.com/93731898/179424976-df48c8b6-63a0-425d-a2bb-c95a3ddf7cbf.PNG)

### Typography
There was no special typography used in this project. I have only used in-built p, h1 & h2 typography to keep the website simple.

### Imagery
All the imagees used in the project is related to the cities related to the blog. Only 4 images are static which are in carousel section and about section. The remaining images will be uploaded by the author to the database.


## Features

### Navbar
![navbar](https://user-images.githubusercontent.com/93731898/179614193-006bcdde-a93f-4978-b1aa-217ea0468e96.PNG)

![logged-in](https://user-images.githubusercontent.com/93731898/179614202-23841874-f1de-443f-8549-e2f324817557.PNG)

![mobile](https://user-images.githubusercontent.com/93731898/179614222-588f2c11-23bb-43a5-a690-36790e4bd3d6.PNG)

![mobilenav](https://user-images.githubusercontent.com/93731898/179614232-c177eb52-ba12-4570-8a84-4e45edd0fc26.PNG)

- The navigation bar is at the top of every page and consists of links to the other page such as login, logout, register and contact.
- The options to Register or Log in will change to the option to log out once a user has logged in.
- Once a user has signed in, more options such as username and the profile icon will be visible to them.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

### User Profile Icon
![user](https://user-images.githubusercontent.com/93731898/179613273-bf933e49-6079-4729-b184-e30f56b291d1.PNG)

User will be a profile icon and their name on the navbar when they are logged in.


### Homepage
![homepage](https://user-images.githubusercontent.com/93731898/179603514-4c07c310-29c8-46d3-aa8c-7dbfc1d10941.PNG)

The main landing section welcomes user with a short message advertising what the website is about. There are three carousel images with a yellow button to navigate to blogs. When the user clicks on the button, they will be directed to the blog section where they read the blogs.

### Homepage -About
![About](https://user-images.githubusercontent.com/93731898/179605542-b64ca535-d16f-4b48-82e0-adcaf6d57a71.PNG)

The about section gives a brief introduction about the website and the travel blogs. This section has a yellow button similar to homepage where a used can click and they will be directed to the blog section.

### Homepage -Blog posts
![blogs](https://user-images.githubusercontent.com/93731898/179605558-67a1b94e-a827-497a-b11c-53a23fc115da.PNG)

The blog posts section consists of all the travel blogs which user can read. There are six blog posts and all the blog posts are written by the site admin.

### Detail blog page
![detail-image](https://user-images.githubusercontent.com/93731898/179606732-fc822dbf-479c-48b4-a2b9-d1d99411a865.PNG)
![detail-text](https://user-images.githubusercontent.com/93731898/179606752-c33c75cf-68d8-4ecf-b6a1-d7a3cee324b4.PNG)

At the top of the detail blog page, users can see a button to navigte back to orginal page, title of the blog post which is name of the blog city and the image of the city. Below that users can read the blog about that city. It will also show the number of comments the post has received.

### Detail blog page- Comments
![comments](https://user-images.githubusercontent.com/93731898/179607174-bc8896aa-4610-4eb4-a2e7-535143347b2a.PNG)
![edit](https://user-images.githubusercontent.com/93731898/179611668-47bf9c7e-aeac-493d-adb9-1c96278a7083.PNG)

At the bottom of the detail blog, users can read the comments posted by other users. If the user is logged in or is a superuser they have access to the buttons to edit or delete the comments.

### Edit comments page
![edit comment](https://user-images.githubusercontent.com/93731898/179607779-f17d3c65-a60e-42dd-b080-d6fb643cae2b.PNG)

The user must be logged in, in order to edit the comments otherwise they will not see the edit button. Once the user is logged in, they can comment on a post, edit it or delete it too.

### Contact page
![contact](https://user-images.githubusercontent.com/93731898/179608441-8b3dcc8c-7eba-46f8-a9f2-51a19c68c4c0.PNG)

The Contact Page allows users to contact the admin using the contact form provided on the website, once the user clicks send button, the contact form will be submitted to the admin site which the admin has access to read.

### Signup page
![signup](https://user-images.githubusercontent.com/93731898/179612483-d71511ca-a3b8-4be9-bdfb-30fcf76ced82.PNG)

On the Signup Page, a new user can sign up for the website by filling out and then submitting the form. Users are not require to provide an email address for signup, it is optional.

### Login page
![signup](https://user-images.githubusercontent.com/93731898/179612497-5d1f3b20-a80a-4213-a192-ab5093464abc.PNG)

On the Login Page, users can log in to the website by entering their username and password and have access to website services for a user registered.

### Logout page
![logout](https://user-images.githubusercontent.com/93731898/179612973-07d1e27c-6c5e-4c65-85a9-cfc7c5aa534e.PNG)

On the Logout Page, users can confirm that they wish to exit the website, when the user clicks on logout, they will get a pop up window, asking them if they want to logout.

### Footer
![footer](https://user-images.githubusercontent.com/93731898/179614820-a5cb13a8-a87e-4590-aaff-fdd7d3707c6e.PNG)

![mobile footer](https://user-images.githubusercontent.com/93731898/179614849-e46ea401-8f41-4737-b770-6c6071c81226.PNG)

On the website footer, users can see basic information about the blog such as contact details, address, social media links, and a quote about travel.


## User Interaction
I have added an some interactive message to make the website more user friendly and improve user experience.

- Comment on a post

![commentbox](https://user-images.githubusercontent.com/93731898/179616293-f1cfef34-0d67-4a08-9968-fe045e504d48.PNG)

![postcomment](https://user-images.githubusercontent.com/93731898/179616302-54967124-54af-4b75-b659-42c1fe96f99d.PNG)

  When users are logged in to the website they can comment on a post and after they submit the comment they will see a message at the top of the page saying "Thank you (username)! Your comment is awaiting approval".

- Like/Unlike a post
  Logged in users can like or unlike the post
  
![Capture](https://user-images.githubusercontent.com/93731898/180083003-468b5669-9caa-49fa-8bb7-d1d816b87f8b.PNG)

- Edit a comment

![edit box](https://user-images.githubusercontent.com/93731898/179616956-3e7482c0-8e4f-4d1d-abfc-7c56e1f178f4.PNG)

![commentbox](https://user-images.githubusercontent.com/93731898/179616973-276e1a3c-02c2-4141-9eed-97fc994242b9.PNG)

  User can click on an edit button to edit their comment. User can only edit or delete their comments, they cannot update or remove someone else's comment.

- Delete a comment

![delete](https://user-images.githubusercontent.com/93731898/179617049-12977779-ddd4-40a9-be5c-cd5e64ea1564.PNG)

  Similiar to edit a comment, user can click on a delete button and if they click on delete button, they will get a pop up window asking them if they wish to delete      the comment. User can only delete their own comment.


### Admin Panel/ Superuser

![admin](https://user-images.githubusercontent.com/93731898/179617976-ef120f41-4943-4b7f-ba5d-2b541b351a6d.PNG)

On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and delete the following ones:
1. Posts
2. Comments
3. Contact emails

As admin/superuser I can also approve comments, approve posts and change the status and give other permissions to the users to post a blog.


## Technologies used

* Languages Used
1. [HTML5](https://www.w3schools.com/html/html_intro.asp)
2. [CSS3](https://www.w3schools.com/css/default.asp)
3. [JavaScript](https://www.w3schools.com/js/default.asp)
4. [Python](https://www.w3schools.com/python/default.asp)
5. [Django](https://www.djangoproject.com/)

* Django Packages
1. [Gunicorn](https://gunicorn.org/) - As the server for Heroku
2. [Cloudinary](https://cloudinary.com/) - To host the static and media files
3. [dj-database-url](https://pypi.org/project/dj-database-url/) - To parse the database URL from the environment variables in Heroku
4. [psycopg2](https://pypi.org/project/psycopg2/) - As an adaptor for Python and PostgreSQL databases
5. [Summernote](https://summernote.org/) - As a text editer
6. [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - For authentication, registration, account management
7. [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) - To style the forms


* Frameworks - Libraries - Programs Used

1 [Bootstrap](https://getbootstrap.com/)
  Was used to style the website, add responsiveness and interactivity
  
2 [Git](https://git-scm.com/)
  Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
  
3 [GitHub](https://github.com/)
  GitHub is used to store the project's code after being pushed from Git
  
4 [PostgreSQL](https://www.postgresql.org/)
  Database used through heroku.
  
5 [VSCode](https://code.visualstudio.com/)
  VSCode was used to create and edit the website
  
6 [PEP8](http://pep8online.com/)
  PEP8 was used to validate all the Python code
  
7 [W3C- HTML](https://validator.w3.org/)
  W3C- HTML was used to validate all the HTML code
  
8 [W3C- CSS](https://jigsaw.w3.org/css-validator/)
  W3C - CSS was used to validate the CSS code
  
9 [Fontawesome](https://fontawesome.com/)
  To add icons to the website
  
10 [Google chrome Dev tool](https://developer.chrome.com/docs/devtools/)
  To check App responsiveness and debugging
  
11 [Pexels](https://www.pexels.com/)
  To download the pictures
  
12 [Heroku](https://dashboard.heroku.com/)
  Heroku was used to deploy the live project
  
  
## Testing

[Testing results](https://github.com/Deepak9912/django-travel-blog/blob/main/Testind.md)


## Creating the Django app

1. Go to the Code Institute Gitpod Full Template Template
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: pip3 install django gunicorn
6. Install supporting database libraries dj_database_url and psycopg2 library: pip3 install dj_database_url psycopg2
7. Create file for requirements: in the terminal window type pip freeze --local > requirements.txt
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!


## Deployment of This Project

*This site was deployed by completing the following steps:

1. Log in to Heroku or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the CLOUDINARY_URL
9. Click Reveal Config Vars and add a new record with the DISABLE_COLLECTSTATIC = 1
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github


## Final Deployment

1. Create a runtime.txt python-3.8.13
2. Create a Procfile web: gunicorn your_project_name.wsgi
3. When development is complete change the debug setting to: DEBUG = False in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: X_FRAME_OPTIONS = SAMEORIGIN to settings.py.
5. In Heroku settings, delete the config vars for DISABLE_COLLECTSTATIC = 1

## Credits

### Content

* All the travel blog content was taken from [Travel borg](https://www.travelblog.org/} and [Wikipedia]{https://www.wikipedia.org/)
* All the images were taken from [Pexels](https://www.pexels.com/)
* The webiste logo and design was build by me.

### Information Sources / Resources

* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack overflow](https://stackoverflow.com/)
* [Code Institute django blog](https://codeinstitute.net/ie/)
* [Net ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
* [Django Central](https://djangocentral.com/building-a-blog-application-with-django/)

### Special Thanks

Special thanks to my mentor Spencer Barriball, my colleagues and tutor support team at Code Institute and Kasia Bogucka for their assistance throughout this project.

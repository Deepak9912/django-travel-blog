# Django-Travel-Blog

Project milestone 4 for Code Institute Full-stack development program with Django framework:

A travel blog website, where a user can post their travel related blogs. When the user posts their blogs, it will be displayed in reverse chronological order, so that the most recent post appears first, at the top of the web page.

The site is fully responsive and was built using the Django framework in Python.

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

At the bottom of the detail blog, users can read the comments posted by other users. If the user is logged in or is a superuser they have access to the buttons to edit or delete the comments.

### Edit comments page
![edit comment](https://user-images.githubusercontent.com/93731898/179607779-f17d3c65-a60e-42dd-b080-d6fb643cae2b.PNG)

The user must be logged in, in order to edit the comments otherwise they will not see the edit button. Once the user is logged in, they can comment on a post, edit it or delete it too.

### Contact page
![contact](https://user-images.githubusercontent.com/93731898/179608441-8b3dcc8c-7eba-46f8-a9f2-51a19c68c4c0.PNG)

The Contact Page allows users to contact the admin using the contact form provided on the website, once the user clicks send button, the contact form will be submitted to the admin site which the admin has access to read.

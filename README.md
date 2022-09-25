# A fully operational and responsive blog.

This blog is a fully operational and responsive CRUD web application. It makes use of
Django Framework, HTML5, CSS3, and Boostrap. The database engine is the 
default sqlite3.

Take note that, while this product is ready for deployment, the settings.py
file has NOT been modified to reflect use for production.

Blog's features include:

1. Various Views with their corresponding urls,

2. A homepave View in which users can also "subscribe". After "subscription", the user 
receives an email which informs them that they have subscribed to a newsletter,

3. A functioning contact page. Users can fill a form and provide feedback. 
The administrator receives an email with the filled out form,

4. Users can view Posts and leave comments. Comment section is scrollable by itself, 
and embedded in the same page as the Post,

5. Users can also use a "search" functionality. The search queries the database and
shows the results that associate the search terms with anything that exists in the posts'
title, body, or author,

6. Fully functioning Authentication system with its own page. Since it is a personal blog, only one person
has the need to login (admin). However, there is a possibility of creating groups and permissions 
through admin page,

7. Only logged in users can Create, Update, Delete posts. They also have the choice to create a post and not 
publish it (create draft). The unpublished posts have a separate page dedicated to drafts, that
is only accessible by logged in users. Drafts can also by updated, deleted, or published,

NOTE: This is a personal project intended for self education purposes.
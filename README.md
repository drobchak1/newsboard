# Newsboard

To start project type:
```sh
python manage.py runserver
```

## Main endpoints:  
**/admin/** - django administration  
**/posts/** - post-list and post-creation  
**/posts/<int:pk>** - CRUD operations on post`s instance  
**/posts/<int:pk>/upvote/** - Like post  
**/posts/<int:pk>/unupvote/** - Unlike post  
**/comments/** - post-list and post-creation  
**/comments/<int:pk>** - CRUD operations on comment`s instance  
**/token/** - JWT token acquiring  
**/token/refresh/** - JWT token refresh  

## Postman:  
There is a Postman collection available for testing purposes:  

## Tests:  
There are tests that check post_creation with JWT-token, post-list view and comment-list view.  

To run them type:
```sh
python manage.py test
```
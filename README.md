# Newsboard

To start project type:
```sh
python manage.py runserver
```

## Main endpoints:  
**/admin/** - django administration  
**/posts/** - post-list and post-creation  
**/posts/<int:pk>** - CRUD operations on posts instance  
**/posts/<int:pk>/upvote/** - Like post  
**/posts/<int:pk>/unupvote/** - Unlike post  
**/comments/** - post-list and post-creation  
**/comments/<int:pk>** - CRUD operations on comments instance  
**/token/** - JWT token acquiring  
**/token/refresh/** - JWT token refresh  

## Heroku: 
Link to heroku development server: https://newsboard-developstoday.herokuapp.com/  

## Postman:  
There is a Postman collection available for testing purposes: https://www.getpostman.com/collections/4e2c5e8b54718f4f57f9  

## Tests:  
There are tests that check post_creation with JWT-token, post-list view and comment-list view.  

To run them type:
```sh
python manage.py test
```

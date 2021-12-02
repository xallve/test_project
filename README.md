# test_project

Usage:

- POST localhost:8000/api/users/ for registration; provide JSON, example: 
```JSON
{
    "user": {
        "username": "yourusername",
        "email": "user@user.user",
        "password": "yourpassword"
    }
}
```
You will get JSON:
```JSON
{
    "user": {
        "email": "user@user.user",
        "username": "yourusername",
        "token": "<your_token>"
    }
}
```
- POST localhost:8000/api/users/login/ is simple; use email and password that you've created before to get the same JSON response as earlier
- GET localhost:8000/api/posts/ you will be redirected to the page with posts where you can login and leave a post(if you are authenticated)
- GET localhost:8000/api/posts/<int> you will be redirected to the page containing post with this specific id(can change if you are authenticated as owner of the post)
- POST localhost:8000/api/user with header: Authorisation: Token <your_token_here> (could be some issues)

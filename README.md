
### Description:
Create a multi-user application that caters to various types of users, each with their own set of roles and permissions. 
The application will serve as a platform for users to interact with image galleries, but with different levels of access and capabilities based on their roles.

Firstly, users will have the ability to sign up and log in with different roles. 
We'll have three main roles: beta players, company users, and growth plan subscribers. 
Beta players are individuals who are testing out new features, while company users represent organizations utilizing the platform, and growth plan subscribers are users with special access due to subscription plans.

Once logged in, users will be able to access the image gallery feature. However, the level of interaction they have with the gallery will vary depending on their role. Beta players,
for instance, will have full control over the gallery. They can upload new images, delete existing ones, and update image descriptions. On the other hand, company users and growth plan subscribers will have view-only access to the gallery.

### Objective: 
The objective of this project is to create a multi-user application with role-based access control using a RESTful API architecture.

### Instruction:
- [x] Build a RESTful API to handle CRUD operations (Create, Read, Update, Delete) for users, roles, images, and asset approval.
- [x] Use standard HTTP methods (GET, POST, PUT, DELETE) for each operation.
- [ ] Ensure proper validation and error handling at the API endpoints.
- [x] Use a relational database PostgreSQL.
- [x] Implement user signup, login, and token generation using JWT.
- [x] Implement user authentication using JWT (JSON Web Tokens).
- [ ] Create a system to manage subscription plans for growth plan subscribers.
- [ ] Define the features and benefits associated with each subscription plan.

### Technologies:
For this project, we will use:
- Django [link](https://docs.djangoproject.com/en/5.0/)
- Django Rest Framework (DRF) [link](https://www.django-rest-framework.org/topics/documenting-your-api/)
- PostgreSQL
- JWT authentication
- Subscription management tools are free to choose.

### Designs:
The user interface for interacting with API is optional.
 
---

### Overview:
- users types/roles:
    1. company users
    1. beta players
    1. subscribers
- Tables Schema
    1. users
        - `id`: _int auto increment (unique)_
        - `username`: _string (unique)_
        - `password`: _string_
        - `is_beta_player`: boolean (false)
        - `is_company_user`: boolean (false)
        - `is_growth_user`: boolean (false)

    1. images:
        - `description` : _string_
        - `image`: _string (path to img in sever)_
        - `uploaded_by` : _foreignKey(users.id)_
        - `uploaded_at` : _date_

### TODO:
- [x] setup dockerized env running _Django Rest Framework + PostgreSQL_
- [x] install djangorestframework_simplejwt + config
- [x] run basic login/register
- [x] add protected route
- [x] add roles fields to model
- [x] init `imgService` app
- [x] CURD images
    - [x] UPLOAD image protected for auth users
        - [x] save image + meta data in DB
        - [x] allow `beta players` only to upload imgs
    - [x] VIEW ONE images (by all)
    - [x] VIEW ALL image (by all)
        - [ ] ~~pagination~~
    - [x] UPDATE image description (by `beta players`)
    - [x] DELETE image (by `beta players`)
- [ ] ~~input validation~~
- [x] setup postman testing collection for the workflow
    - [x] setup postman built script to auto load auth tokens
    - [x] create req for each service
    - [x] test all reqs for `betaPlayer` vs `others`
- [ ] ~~handle subscription plans~~
- [x] review code & remove redundent code
    - [x] refact users app
    - [x] refact img service
    - [x] refact path formats
- [x] document APIs
- [x] move secrets to env at the end

### Note:
- i used admin panel to set roles for users (can be more dynamic. It was the easy way x) )

### Installation:

```
git clone https://github.com/aallali/technical-test-c3/
cd technical-test-c3/
docker-compose up
```
- service up and running at `0.0.0.0:8000`
### API enpoints:
- #### register
    <details>
    <summary>Click me</summary>

    - create a beta player user:
        `POST: http://0.0.0.0:8000/api/v1/auth/register`
        body:
        ```json
        {
            "username": "betaPlayer",
            "password": "12345"
        }
        ```
        response (200):
        ```json
        {
            "id": 1,
            "username": "betaPlayer",
            "is_beta_player": false,
            "is_company_user": false,
            "is_growth_user": false
        }
        ```
    - create a company user:
        `POST: http://0.0.0.0:8000/api/v1/auth/register`
        body:
        ```json
        {
            "username": "companyUser",
            "password": "12345"
        }
        ```
        response (200):
        ```json
        {
            "id": 2,
            "username": "companyUser",
            "is_beta_player": false,
            "is_company_user": false,
            "is_growth_user": false
        }
        ```
    - duplicated username:
        `POST: http://0.0.0.0:8000/api/v1/auth/register`
        body:
        ```json
        {
            "username": "companyUser",
            "password": "12345"
        }
        ```
        response (400):
        ```json
        {
            "username": [
                "A user with that username already exists."
            ]
        }
        ```
    
    - by default all newly created users doesnt have any role assigned to them, we update that in admin panel
- #### login
    <details>
    <summary>Click me</summary>

    - authenticate as betaPlayer
        `POST: http://0.0.0.0:8000/api/v1/auth/login`
        body:
        ```json
        {
            "username": "betaPlayer",
            "password": "12345"
        }
        ```
        response (200):
        ```json
        {
            "username": "betaPlayer",
            "tokens": {
                "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMDQzMTY5NywiaWF0IjoxNzEwMzQ1Mjk3LCJqdGkiOiJkYzIxYTZhMzNjYTA0MjU2YWZiMzI5OGVjMGY3YjZkZCIsInVzZXJfaWQiOjF9.2TKze2kE9SiODFOZxxG0-wzAnUk06sYhEq2D6HBX_30",
                "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwNDMxNjk3LCJpYXQiOjE3MTAzNDUyOTcsImp0aSI6ImU0MjEzYTkzYzljMjRlZDg4MDE2NGY3ZTdlNjliNGM5IiwidXNlcl9pZCI6MX0.viZqtZyTWbkIxVvoT8vncQCf2_xRST6MbwPZIsDk3yI"
            }
        }
        ```
        or 
        response (401)
        ```json
        {
            "detail": "Invalid credentials"
        }
        ```
    </details>
- #### upload image
    <details>
    <summary>Click me</summary>

    - upload image as beta player:
        `POST: http://0.0.0.0:8000/api/v1/images/`
        form-data:
        ```json
        image: 1709557015176.jpeg
        description: hhh lmghrb mab9a lih walu, nice
        ```
        response (200):
        ```json
        {
            "id": 1,
            "description": "hhh lmghrb mab9a lih walu, nice",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_RDfn0ag.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:02:35.104697Z"
        }
        ```
        or 
        response (401) if user doesn't have betaPlayer role
        ```json
        {
            "detail": "You do not have permission to perform this action."
        }
        ```
    </details>
- #### update image description
    <details>
    <summary>Click me</summary>

    - update descrition as betaPlayer
        `PATCH: http://0.0.0.0:8000/api/v1/images/1/description`
        form-data:
        ```json
        image: 1709557015176.jpeg
        description: hhh lmghrb mab9a lih walu, nice
        ```
        response (200):
        ```json
        {
            "id": 1,
            "description": "[JUST GOT UPDATED]",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_9bFjiY6.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:02:35.104697Z"
        }
        ```
        or 
        response (404) if image id not valid
        ```json
        {
            "detail": "Not found."
        }
        ```
        or
        response (400) invalid body
        ```json
        {
            "error": "Description is required"
        }
        ```
    </details>
- #### get single image 
    <details>
    <summary>Click me</summary>

    `GET: http://0.0.0.0:8000/api/v1/images/2`

    response (200):
    ```json
    {
        "id": 2,
        "description": "this is a second upload :) :) (:)",
        "image": "http://0.0.0.0:8000/media/images/1709557015176_igYVQOk.jpeg",
        "uploaded_by": 1,
        "uploaded_at": "2024-03-13T16:03:31.838862Z"
    }
    ```
    or 
    response (404) if image id not valid
    ```json
    {
        "detail": "Not found."
    }
    ```
    </details>
- #### get all images
    <details>
    <summary>Click me</summary>

    `GET: http://0.0.0.0:8000/api/v1/images/`

    response (200):
    ```json
    [
        {
            "id": 2,
            "description": "this is a second upload :) :) (:)",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_igYVQOk.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:03:31.838862Z"
        },
        {
            "id": 3,
            "description": "and the third (:",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_aCA6gwu.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:03:43.365172Z"
        },
        {
            "id": 4,
            "description": "ok last one xD",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_OkXKYjk.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:03:56.878422Z"
        },
        {
            "id": 1,
            "description": "[JUST GOT UPDATED]",
            "image": "http://0.0.0.0:8000/media/images/1709557015176_9bFjiY6.jpeg",
            "uploaded_by": 1,
            "uploaded_at": "2024-03-13T16:02:35.104697Z"
        }
    ]
    ```
    </details>
- #### delete image
    <details>
    <summary>Click me</summary>

    - delete single image by id by betaPlayer users only
    `DELETE: http://0.0.0.0:8000/api/v1/images/3/`
        - query : 3 (the img id)
        - response (204 No Content) in case of success
        - response (404 Not found) in case of invalid id
            ```json
            {
                "detail": "Not found."
            }
            ```
        - response (403 Forbidden) in case non betaPlayer users:
            ```json
            {
                "detail": "You do not have permission to perform this action."
            }
            ```
    </details>
### Cheat sheets:

- run the docker container:
    - `docker-compose up` : build containers first time.
    - `docker-compose up --no-deps --build web` re-build the web service.

- init django app:
    - `django-admin startproject server .` : init project called `server` in current directory,
    - `django-admin startapp users`: add app called `users`.
    - `django-admin startapp imgService`: add app called `imgService`.

    - `python manage.py runserver 0.0.0.0:8000`: run the web service.
- migrate DB:
    - `python manage.py makemigrations && python manage.py migrate`
    
- create super user:
    - `python manage.py createsuperuser`
        ```bash
        (djang-env) ➜  technical-test-c3 git:(main) ✗ python manage.py createsuperuser
        Username: admin
        Email address: hi@allali.me
        Password: admin
        Password (again): admin
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
        (djang-env) ➜  technical-test-c3 git:(main) ✗ 
        ```

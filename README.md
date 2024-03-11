
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
- [ ] Build a RESTful API to handle CRUD operations (Create, Read, Update, Delete) for users, roles, images, and asset approval.
- [ ] Use standard HTTP methods (GET, POST, PUT, DELETE) for each operation.
- [ ] Ensure proper validation and error handling at the API endpoints.
- [ ] Use a relational database PostgreSQL.
- [ ] Implement user signup, login, and token generation using JWT.
- [ ] Implement user authentication using JWT (JSON Web Tokens).
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

### Plan:
- users types/roles:
    1. company users
    1. beta players
    1. subscribers
- Tables Schema
    1. users
        - `id`: _int auto increment (unique)_
        - `username`: _string (unique)_
        - `password`: _string_
    1. images:
        - `description` : _string_
        - `image`: _string (path to img in sever)_
        - `uploaded_by` : _foreignKey(users.id)_
        - `uploaded_at` : _date_

### TODO:
- [x] setup dockerized env running _Django Rest Framework + PostgreSQL_
- [x] install djangorestframework_simplejwt + config
- [x] run basic login/register
- [ ] add protected route
- [ ] add roles fields to model
- [x] init `imgService` app
- [ ] CURD images
    - [x] UPLOAD image protected for auth users
        - [x] save image + meta data in DB
        - [ ] allow `beta players` only to upload imgs
    - [x] VIEW ONE images (by all)
    - [x] VIEW ALL image (by all)
    - [ ] UPDATE image description (by `beta players`)
    - [ ] DELETE image (by `beta players`)

- [ ] move secrets to env at the end


### Guide:
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
    
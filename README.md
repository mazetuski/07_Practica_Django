# Práctica Django Miguel Ángel Zamora Blanco

## Installation

- Create VirtualEnv

```
virtualenv -p python3 envname
```

- Activate VirtualEnv

```
source envname/bin/activate
```

- Install Requirements

```
pip install -r requirements.txt
```

- Update database

```
python manage.py migrate
```

- Create super user

```
python manage.py createsuperuser --username=admin --email=admin@example.com
```

## Deploy dev

```
python manage.py runserver
```

## Admin Page

- Url: /admin

## API

### Blog

#### Get all blogs
- Method: GET
- Url: api/1.0/blogs/

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| Search     | String  |  Search by first_name and last_name |
| Ordering  | String  |  Can be first_name or last_name |


#### Get all posts of one blog
- Method: GET
- Url: api/1.0/blog/:ID_USER/

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| Search     | String  |  Search by title and description_short|
| Category  | Integer  |  Filter by category id |
| Ordering  | String  |  Can be title or pub_date |

#### Create post
- Method: POST
- Url: api/1.0/posts/
- Need authentication

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| title  | String  | Title of the post |
| description_short  | String | A short description of the post |
| description_long  | String | Description of the post |
| url_assert | String(Url) | Url of image for post header |
| category  | Integer  | Define category of the post, can be an array of categories |

#### Get post by id
- Method: GET
- Url: api/1.0/posts/:ID/
- No authentication is required, only the owners and admins will be able to see the unpublished post

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| id | integer | Id of the post |

#### Update post
- Method: PUT
- Url: api/1.0/posts/:ID/
- Need authentication, only owners and admins will be able to update posts

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| id | integer | Id of the post |
| title  | String  | Title of the post |
| description_short  | String | A short description of the post |
| description_long  | String | Description of the post |
| url_assert | String(Url) | Url of image for post header |
| category  | Integer  | Define category of the post, can be an array of categories |

#### Remove post
- Method: DELETE
- Url: api/1.0/posts/:ID/
- Need authentication, only owners and admins will be able to remove posts

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| id | integer | Id of the post |

### Users

#### Create new User
- Method: POST
- Url: api/1.0/users/

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| first_name  | String  |  |
| last_name  | String  |  |
| email  | String(Email)  | |
| username  | String  |  |
| password  | String  |  |

#### Get one user detail
- Method: GET
- Url: api/1.0/users/:ID
- Need authentication, only the same user or an admin can be their details

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| id  | Integer | id of the user |

#### Update User
- Method: PUT
- Url: api/1.0/users/
- Need authentication, only the same user or an admin can see their details

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| first_name  | String  |  |
| last_name  | String  |  |
| email  | String(Email)  | |
| username  | String  |  |
| password  | String  |  |

#### Remove user
- Method: DELETE
- Url: api/1.0/users/:ID
- Need authentication, only the user or an admin can delete them

| Param     | Type    | Help  |
| :-------: |:-------:| ----- |
| id  | Integer | id of the user |

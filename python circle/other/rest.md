# REST

Representational State transfer

`www.example.com/api/circle/.`

## Get

### Get a list of users

`www.example.com/api/users/page=2`

Json response
- respose code  200

```
{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data":{
        "id": 2
        "name":magnus
        "email": magnusgilje@kubrickgroup.com
    }
    
}
```
### Get a single user
`/api/user/2`

```
"data":{
        "id": 2
        "name":magnus
        "email": magnusgilje@kubrickgroup.com
    }
```
### User not found
- Request
`api/users/23`
- Response 404
```
{

}
```

## POST

similar to a get, but with a post we pass a json object inside the html for the user

### POST CREATE 

- Request

`api/users`

```json
{
    "name": "morpheus",
    "job": "leader"
}
```
- Response [201] {created}

```json
{
    "name": "morpheus",
    "job": "leader",
    "id": "433",
    "createdAt": "2021-12-20T07:49:48:4482" 
}
```
### POST UPDATE

- Request

`api/users/433`

```json
{
    "name": "morpheus",
    "job": "Zion Resident",
}
```

- Response [204]

```json
{
    "name": "morpheus",
    "job": "Zion Resident",
    "createdAt": "2021-12-20T07:51:10:0442
}
```
## PATCH
### PATCH UPDATE


- Request

`api/users/433`

-Response [204]

```json
{

}
```

---
# User Creation.
- Request

`/api/register`
```json
{
    "email":"magnusgilje@kubrickgroup.com",
    "password": "8 characters and numbers"
}
```

-Response [200]

```json
{
    "id": 4,
    "token" : "QnbuibjkfeQ7"
}
```

### POST REGISTER UNSUCCESSFUL

- Request

```json
{
    "email":"magnusgilje@kubrickgroup.com"
}
```
- Response [400]

```json
{
    "error": "Missing password"
}
```
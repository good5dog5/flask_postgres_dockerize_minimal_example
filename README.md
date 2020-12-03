# Flask on Docker with external PostgreSQL database

# Testing

* list all users
```
curl -X GET "http://localhost:5000/user/" -H "accept: application/json"
```

* list user by id
```
curl -X GET "http://localhost:5000/user/1" -H "accept: application/json"
```

* create new user
```
curl -X POST "http://localhost:5000/user/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"first_name\": \"jordan\", \"last_name\": \"huang\", \"job_title\": \"SRE\", \"communication\": { \"email\": \"jordan.huang.happy@gmail.com\", \"mobile\": \"093231231\" }}"
```

* update a user by id
```
curl -X PUT "http://localhost:5000/user/1" -H "accept: application/json" -H "Content-Type:
application/json" -d "{ \"first_name\": \"a_first_name\", \"last_name\": \"a_last_name\",
\"job_title\": \"SRE\", \"communication\": { \"email\": \"a_email\", \"mobile\": \"a_mobile\" }}""
```

* delete a user by id
```
curl -X DELETE "http://localhost:5000/user/2" -H "accept: application/json"
```

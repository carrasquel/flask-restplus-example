# flask-restplus-example

This project is a Flask API interface for front-end development and practice, it supports auth, events and todos.

# Requirements

In order to execute this web application install the Python requirements.

```
>>> pip install -r requirements.txt
```

# Setup

This application uses *Flask_Migrate* to perform database migrations. export the *FLASK_APP* environment variable with the value, *run.py*, then initialize your database.

```
>>> flask db init
```

After you need to migrate your models

```
>>> flask db migrate
```

and finally to upgrade your model schemas to the database.

```
>>> flask db upgrade
```

# Execution

After you have setup correctly your database, the only thing to do next, is tu run your application.

```
>>> flask run
```

# API Documentation

You will find the api documentation in a Swagger UI in the following url

```
http://localhost:5000/api/docs
```

### Support development

If you liked this, donate to the cause.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/carrasquel)

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2020-present, Nelson Carrasquel
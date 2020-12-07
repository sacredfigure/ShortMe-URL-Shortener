![screenshot](https://user-images.githubusercontent.com/10364402/101261831-93161800-3742-11eb-9b31-7f4106df238e.png) 


### [ShortMe](http://shortme.biz/) - URL shortner app

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About The Project](#About-The-Project)
    + [Built With](#built-with)
    + [Extensions](#Extensions)
* [API](#API)
    + [Shorten a Link](#Shorten-a-Link)
    + [Get total URL clicks](#Get-total-URL-clicks)
* [Getting Started](#Getting-Started)
* [Architecture](#Architecture)
* [Contributing](#Contributing)
* [Project Structure](#project-structure)
* [License](#license)

<!-- about -->
## About The Project

### ShortMe

A Flask web app and API used to shorten long URLs.

[Hosted version](http://shortme.biz/)

#### Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Backend
* [Bootstrap](https://getbootstrap.com) - Frontend
* CSS for styling

#### Extensions
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - API
* [Flask-SQLalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - SQL ORM
* [Flask-Testing](https://flask.palletsprojects.com/en/0.12.x/testing/) - API testing
* [Selenium WebDriver](https://www.selenium.dev/projects/) - UI Automation
* [unittest](https://docs.python.org/3/library/unittest.html) - Testing


## API
ShortMe's API lets you interact with ShortMe's URL shortening capabilities.

### Shorten a Link
Given a full URL, returns a ShortMe short URL. 
Currently, the API only supports shortening a single URL per API call.

* URL: `/api/shorten`
* Method: `POST`
* Request Params: Json containing the long URL `{"url": "www.longurl.com/long"}`
* Response: Returns short url data on success

Example call:

    POST: http://shortme.biz/shorten?url=http://www.longurl.com

Example Response:
 
```
{
    'short_url': shortme.biz/f3Jds, 
    'original_url': 'http://www.longurl.com', 
    'success':True
}
```

### Get total URL clicks
Given a short URL, returns the number of times it has been clicked.  
Currently, the API only supports shortening a single URL per API call.

* URL: `/api/total_clicks`
* Method: `GET`
* Request Params: Json containing the short URL `{"url": "shortme.biz/f3Jds"}`
* Response: Returns total short url visit count

Example call:

    GET http://shortme.biz/api/total_clicks?url=shortme.biz/f3Jds

Example Response:

```
{
    'total': 2,
    'short_url': 'shortme.biz/f3Jds',
    'original_url': 'http://www.longurl.com',
    'success': True
}
```

<!-- GETTING STARTED -->
## Getting Started
Clone using 

    $ git clone https://github.com/AcrobaticPanicc/ShortMe-URL-Shortener.git 

Create a virtual environment for the project and activate it:

    $ virtualenv venv
    $ source venv/bin/activate

Install the required packages:

    $ pip install -r requirements.txt

Run the app using:

    $ flask run


## Architecture
* The framework selected for the operation is Flask because of the ease of its setup readability of the code.
* The Database selected is SQLite, although there is no relationship to maintain among the tables and thus going with NoSql DB would have worked too.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what makes the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Project Structure
```
    .
    - app
    |   - api
    |   |   - __init__.py
    |   |   - api.py
    |   - db
    |   |   - __init__.py
    |   |   - db.py
    |   |   - models.py
    |   - static
    |   |   - CSS
    |   |   |   - styles.css
    |   |   - JS
    |   |   |   - main.js
    |   |   - favicon.ico
    |   - templates
    |   |   - base.html
    |   - tests
    |   |   - api_testing
    |   |   |   - __init__.py
    |   |   |   - settings.py
    |   |   |   - test.db
    |   |   |   - test_api.py
    |   |   - front_end_testing
    |   |   |   - index
    |   |   |   |   - __init__.py
    |   |   |   |   - index.py
    |   |   |   - result
    |   |   |   |   - __init__.py
    |   |   |   |   - result.py
    |   |   |   - total_clicks
    |   |   |   |   - __init__.py
    |   |   |   |   - total_clicks.py
    |   |   |   - SeleniumUtility.log
    |   |   |   - __init__.py
    |   |   |   - test_front_end.py
    |   |   - utilities
    |   |       - __init__.py
    |   |       - logger.py
    |   |       - selenium_utility.py
    |   - views
    |   |   - error
    |   |   |   - templates
    |   |   |   |   - error.html
    |   |   |   - __init__.py
    |   |   |   - error.py
    |   |   - index
    |   |   |   - templates
    |   |   |   |   - index.html
    |   |   |   - __init__.py
    |   |   |   - index.py
    |   |   - internal
    |   |   |   - __init__.py
    |   |   |   - routes.py
    |   |   - result
    |   |   |   - templates
    |   |   |   |   - result.html
    |   |   |   - __init__.py
    |   |   |   - result.py
    |   |   - total_clicks
    |   |   |   - templates
    |   |   |   |   - total-clicks.html
    |   |   |   - __init__.py
    |   |   |   - total_clicks.py
    |   |   - __init__.py
    |   - __init__.py
    |   - settings.py
    - LICENSE
    - Procfile
    - requirements.txt
    - run.py

```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
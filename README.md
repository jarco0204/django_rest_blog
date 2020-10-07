# Django REST API Blogs

## Cross Origin Resource Sharing (CORS)

This allows your client-side application to connect with your RESTful API

1. install CORS
   - `python3 -m pip install django-cors-headers`
   - make sure it is installed `pip list`
2. Go to your project's `settings.py`
3. Under `INSTALLED_APPS` add `corsheaders`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog_api_app',
    'corsheaders',
]
```

4. Go to `MIDDLEWARE` and add the CORS middleware `'corsheaders.middleware.CorsMiddleware'`

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

<b>Make sure that the middleware is at the top of the `MIDDLEWARE` or else Django will not be able to ad the CORS headers to the responses </b>

5. Configure Your Origin Path
   - add the URL of your client-side server
     - Example: React.js

```python
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]
```

Make sure your url path does not have a `/` at the end for example http://localhost:3000/ will not work as the error will read as:

```red
ERRORS:
?: (corsheaders.E014) Origin 'http://localhost:3000/' in CORS_ORIGIN_WHITELIST should not have path
```

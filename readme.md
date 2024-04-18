# ISSUE: Middlewares are executed altough url doesnt exist in openapi spec


## install requirements

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Reproduce error with ASGI Middlewares

the asgi middleware raise "Working outside of operation context" exception in all request since
context object is a localproxy object that doesnt have a value.
i suppose the context object should be accesible since this custom middleware is invoked after connexion context middleware has been executed

```
enable this line in main.py -> # connexion_app.add_middleware(CustomConnexionMiddleware)
python3 main.py
curl http://localhost:8080/health/ping
```

## Reproduce error with Flask Hooks

the flask hook raise an "Working outside of operation context" exception if the invoked url doesnt exist,
i suppose the expected behaviour is connexion routing middleware stop the excecution returning 404

```
enable this line in main.py -> # flask_app.before_request(custom_flask_hook)
python3 main.py
curl http://localhost:8080/health/pong # this urls doesnt exist, 404 is the expected valur
```
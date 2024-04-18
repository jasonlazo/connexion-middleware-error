from connexion.context import context, request
from starlette.middleware.base import BaseHTTPMiddleware


class CustomConnexionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        """
        this middleware raise "Working outside of operation context" exception in all request since
        context object is a localproxy object that doesnt have a value.
        i suppose the context object should be accesible since this custom middleware is invoked after connexion context middleware
        """
        context["foo"] = "bar"
        response = await call_next(request)
        return response


def custom_flask_hook():
    print(request.url.path)
    """
    this flask hook raise an "Working outside of operation context" exception if the invoked url doesnt exist,
    i suppose the expected behaviour is connexion routing middleware stop the excecution returning 404
    """

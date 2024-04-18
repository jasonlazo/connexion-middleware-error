from connexion import FlaskApp

from middlewares import CustomConnexionMiddleware, custom_flask_hook  # noqa

connexion_app: FlaskApp = FlaskApp(__name__, specification_dir='.')
connexion_app.add_api('api.yaml',
                      arguments={'title': 'conas'},
                      # base_path=API_BASE_PATH,
                      pythonic_params=True,
                      strict_validation=True,
                      validate_responses=True)

flask_app = connexion_app.app

"""
Remove comments to test each case, there is an explantation inside each middleware definition
"""

# connexion_app.add_middleware(CustomConnexionMiddleware)
# flask_app.before_request(custom_flask_hook)

if __name__ == '__main__':
    connexion_app.run(port=8080)

import os

import uvicorn
from quart import Quart, jsonify, redirect, request

import config

app = Quart(__name__)


@app.errorhandler(Exception)
async def error_handler(error):
    print(error)
    status = error.args[1] if len(error.args) > 1 else 400
    return (
        jsonify(
            {
                'error': f'{status}: Bad Request',
                'message': (
                    error.args[0]
                    if len(error.args) > 0
                    else 'An unknown error occurred.'
                ),
            }
        ),
        status,
    )


@app.errorhandler(404)
async def not_found(error):
    return (
        jsonify(
            {
                'error': '404: Not Found',
                'message': 'The requested resource could not be found.',
            }
        ),
        404,
    )


@app.errorhandler(405)
async def invalid_method(error):
    return (
        jsonify(
            {
                'error': '405: Invalid method',
                'message': f"The requested resource doesn't support the {request.method} method.",
            }
        ),
        405,
    )


@app.errorhandler(500)
async def internal_server_error(error):
    return (
        jsonify(
            {
                'error': '500: Internal Server Error',
                'message': 'An internal server error occurred.',
            }
        ),
        500,
    )


@app.route('/')
async def index():
    return redirect('https://discord.gg/wock')


if __name__ == '__main__':
    for route in os.listdir('routes'):
        if route.endswith('.py'):
            router = __import__(f'routes.{route[:-3]}', fromlist=['*']).router
            router.app = app
            app.register_blueprint(router)
    uvicorn.run(app, host=config.Webserver.host, port=config.Webserver.port)

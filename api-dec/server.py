from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from core.controllers import detection_controller
from core.repository.calango_db import CalangoDatabase


def routers(request):
    rotas = []
    endpoints = ['login', 'logout', 'register', 'detectar']

    [rotas.append(f"http://{request['server'][0]}:{request['server'][1]}/{endpoint}") for endpoint in endpoints]

    return JSONResponse({'Rotas': rotas})


db = CalangoDatabase()
db.create_tables()

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(
    debug=True,
    routes=[
        Route('/', routers, methods=['GET']),
        Route('/detectar', detection_controller.detectar, methods=['POST']),
    ],
    middleware=middleware
)

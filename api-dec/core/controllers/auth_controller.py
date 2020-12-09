import json

from starlette.responses import JSONResponse

from core.repository.calango_db import CalangoDatabase, USERS


def get_query(query: str) -> dict:
    query = query.replace('=', '":"').replace('?', '","')
    query = '{"' + f'{query}' + '"}'

    query = json.loads(query)

    return dict(query)


async def login(request):
    print(dict(request).keys())

    query = get_query(request['query_string'].decode('utf-8'))
    username = query["username"]
    password = query["password"]

    db = CalangoDatabase()

    data = db.execute_query(f"SELECT * FROM '{USERS}' WHERE username='{username}' AND password='{password}';")

    print(data)

    return JSONResponse({'Metodo': request['method']})


async def logout(request):
    print(dict(request).keys())
    return JSONResponse({'Metodo': request['method']})


async def register(request):
    print(dict(request).keys())
    return JSONResponse({'Metodo': request['method']})

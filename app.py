from fastapi import FastAPI

from route import router, processing_resultats


def get_app():
    app = FastAPI()
    app.include_router(router=router)

    return app

app = get_app()
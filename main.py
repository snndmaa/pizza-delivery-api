from fastapi import FastAPI;
# from fastapi_jwt_auth import AuthJWT;
from routes import auth_router, order_router;
# from schema import Settings;

app = FastAPI();

# @AuthJWT.load_config
# def get_config():
#     return Settings();

app.include_router(auth_router);
app.include_router(order_router);
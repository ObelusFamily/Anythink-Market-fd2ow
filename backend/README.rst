Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.


Project structure
-----------------

Project dependencies are managed by poetry `(https://python-poetry.org)`, using venv `(https://docs.python.org/3/library/venv.html)`.


Deployment
----------

Using Heroku Buildpacks:
1. Install heroku CLI.
2. Use these set of commands:
   - heroku login
   - git init
   - heroku git:remote -a anythink-market-fd2ow-api
   - git add .
   - git commit -am "Production Deployment"
   - heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
   - heroku buildpacks:add heroku/python
   - heroku config:set PROJECT_PATH=backend/
   - git push heroku main

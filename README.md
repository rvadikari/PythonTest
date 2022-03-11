# PythonTest
TestProject

Python
-------
create a python file
to test  py <filename>.py
to test fastapi through server: Uvicorn <filename>:app --reload

heroku
----------
To create an app on Heroku
Heroku create -a <appname>

To push changes on Heroku
git push heroku main

To reset the DB credentials
heroku pg:credentials:rotate

to restart the heroku app
heroku rs:restart

PyTest
------
To install py test
pip install pytest

To execute test
pytest -v

to discard warnings
pytest --disable-warnings

CI/CD pipeline
------------
create a .github/workflows folder
create build-deploy.yml file to configure CI pipelline



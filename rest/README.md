## Setup
You need to have an activated virtual environment in order for the package imports to work properly, without messing with sys.path syntax.
  
For the Playlist API to function, you need to setup the environment variables (dotenv, /controllers/.env), with the YOUTUBE_DATA_V3_API_KEY=your_key field.  
See the console output logs for success/failure information.

  
FastAPI needs to be installed with the `python -m pip install 'fastapi[standard]'` directive, for the documentation to work (why wouldn't you want documentation?). Do not compile packages with any interpreter optimizations (`-O`, `-OO`, etc.), else API documentation may break and become unusable.
  
### Docs
See http://localhost:8000/docs for Swagger documentation, or http://localhost:8000/redoc for the Redoc documentation.



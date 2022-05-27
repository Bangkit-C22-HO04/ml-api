import uvicorn
import sys

from recommenders import app


if __name__ == '__main__':
    args = sys.argv
    if args[1] == "run":
        uvicorn.run("recommenders:app", reload=True, debug=True, workers=3)

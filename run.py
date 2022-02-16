from distutils.log import debug
from fur_converter import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from app import create_app

app = create_app()

if __name__ == '__main__':
    # set on fast version
    # app.run(port=5001, host='0.0.0.0', debug=False, access_log=False, fast=True)
    # set normal version
    app.run(port=5001, host='0.0.0.0', debug=True, access_log=True)

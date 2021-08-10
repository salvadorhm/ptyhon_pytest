from webtest import TestApp as ta
from app import app as application

class TestIndex():
    def test_get(self):
        file = open('templates/index.html', 'r')
        middleware = []
        app = ta(application.wsgifunc(*middleware))
        resp = app.get('/index')
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text ==  file.read() + "\n"

class TestDato():

    def test_get(self):
        file = open('templates/index.html', 'r')
        middleware = []
        app = ta(application.wsgifunc(*middleware))
        resp = app.get('/dato')
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text ==  file.read() + "\n"


    def test_post(self):
        middleware = []
        app = ta(application.wsgifunc(*middleware))
        resp = app.post('/dato',{'name':'John Doe'})
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text == 'Hello, John Doe!'

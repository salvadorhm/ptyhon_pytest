from webtest import TestApp
from app import app

class TestIndex():
    def test_get(self):
        middleware = []
        a = TestApp(app.wsgifunc(*middleware))
        resp = a.get('/index')
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text == 'Hello, world!'

class TestDato():

    def test_get(self):
        middleware = []
        a = TestApp(app.wsgifunc(*middleware))
        resp = a.get('/dato')
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text == 'Hello, world!'


    def test_post(self):
        middleware = []
        a = TestApp(app.wsgifunc(*middleware))
        resp = a.post('/dato',{'name':'John Doe'})
        print(resp)
        assert resp.status == '200 OK'
        assert resp.text == 'Hello, John Doe!'

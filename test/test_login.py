from webtest import TestApp as ta
from app import app as application


class TestLogin():

    def test_get(self):
        file = open('templates/login.html')
        middleware = []
        app = ta(application.wsgifunc(*middleware))
        resp = app.get('/login')
        assert resp.status == '200 OK'
        assert resp.content_type == 'text/html'
        assert resp.text == file.read() + "\n"


    def test_post(self):
        index = open('templates/index.html')
        login  = open('templates/login.html')
        middleware = []
        app = ta(application.wsgifunc(*middleware))

        # Login email y password correctos
        resp = app.post('/login',{'email':'hola@email.com','password':'123456'})
        assert resp.status == '200 OK'
        assert resp.text == index.read() + "\n"

        # Login email y password incorrectos
        resp = app.post('/login',{'email':'hola@email.com','password':'12345'})
        assert resp.status == '200 OK'
        assert resp.text == login.read() + "\n"

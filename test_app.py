from webtest import TestApp
from app import app

def test_index():
    middleware = []
    a = TestApp(app.wsgifunc(*middleware))
    resp = a.get('/index')
    print(resp)
    assert resp.status == '200 OK'
    assert resp.text == 'Hello, world!'

def test_dato():
    middleware = []
    a = TestApp(app.wsgifunc(*middleware))
    resp = a.get('/dato',{'name':'John Doe'})
    print(resp)
    assert resp.status == '200 OK'
    assert resp.text == 'Hello, John Doe!'
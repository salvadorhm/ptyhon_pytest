import web

urls = (
    '/index', 'Index',
    '/dato','Dato'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hello, world!'

class Dato:
    def GET(self):
        form = web.input()
        print(form.name)
        return 'Hello, ' +  form.name + '!'

if __name__ == "__main__":
    app.run()

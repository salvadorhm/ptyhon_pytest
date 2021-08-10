import web
import login

urls = (
    '/index', 'Index',
    '/dato','Dato',
    '/login','login.Login',
)
app = web.application(urls, globals())

render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Dato:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        print(form.name)
        return 'Hello, ' +  form.name + '!'

if __name__ == "__main__":
    app.run()

import web

render = web.template.render('templates')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        form = web.input()
        email = form.email
        password = form.password

        if email == "hola@email.com" and password == "123456":
            return render.index()
        else:
            return render.login()

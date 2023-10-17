from jinja2 import Environment, PackageLoader, select_autoescape
from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    layout_main = env.get_template("layout.html")
    page = layout_main.render(name=name, go="here")

    # return web.Response(text=text)
    return web.Response(body=page, content_type='text/html')

env = Environment(
    loader=PackageLoader("AioHttpJinja"),
    autoescape=select_autoescape()
)
app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, port=8085)
# if __name__ == '__main__':

#     layout_main = env.get_template("layout.html")
#
#     print(layout_main.render(the="variables", go="here"))

from flask import Flask, render_template, send_from_directory, request
import mvc.mvc as mvc
from mvc.lib import *

app = Flask(__name__)
app.jinja_env.filters['embed'] = lambda u: get_embed_html_object(u)
app.jinja_env.filters['embed_cover'] = lambda u: get_ebbed_object_cover(u)

@app.route("/")
def main_page():
    items = mvc.read_items(30)
    return render_template('index.html', items=items)

@app.route('/robots.txt')
@app.route('/yandex_521dd2dc8230be44.html')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/news/<slug>', methods=["POST", "GET"])
def news(slug):
    item = mvc.read_item(slug)
    return render_template('news.html', item=item)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)

links = [
{"link": "https://rars888.github.io/RARS-tutor/", "dis": "RARS-tutor"}
]

@app.route('/')
def index():
    return redirect('/links')

@app.route('/links')
def linksi():
    return render_template('links.html', links=links)

@app.route('/links/<int:link_id>/del')
def del_cati(link_id):
    try:
        del links[link_id]
    except:
        abort(404)
    return redirect('/links')



@app.route('/links/add')
def add_link():
    return render_template('link-add.html')


@app.route('/links/add', methods=['post'])
def add_link_p():
    link = request.form.get('link')
    dis = request.form.get('dis')
    
    if link and dis:
        try:
            links.append({"link": link, "dis": dis})
        except:
            abort(404)
    else:
        pass
#        return render_template('link-add.html')
    return redirect('/links')




'''@app.route('/category/<int:link_id>/add')
def add_link(link_id):
    if category_id < 0 or category_id >= len(fanfics):
        abort(404)
        
    return render_template('cat-edit.html', idn = category_id)


@app.route('/category/<int:category_id>/add', methods=['post'])
def add_link_p(category_id):
    name = request.form.get('name')
    
    if name:
        fanfics[category_id]['name'] = name

    return redirect('/')
'''


app.run(debug=True)

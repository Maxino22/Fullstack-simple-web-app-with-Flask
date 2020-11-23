from myproject import app, db
from myproject.forms import SubForm
from myproject.models import InfoTAble
from flask import redirect, render_template, url_for, flash


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # add new message to database
        new_message = InfoTAble(name, message)
        db.session.add(new_message)
        db.session.commit()

        flash("Thanks we'll get back to you")
        return redirect(url_for("index"))

    return render_template('index.html', form=form)


@app.route('/admin')
def admin():
    messages = InfoTAble.query.all()
    return render_template('admin.html', messages=messages)


if __name__ == "__main__":
    app.run(debug=True)

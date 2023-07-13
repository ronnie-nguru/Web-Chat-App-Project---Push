from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
        jsonify, current_app, make_response
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditProfileForm, EmptyForm, MessageForm
from app.models import User, Message, Notification
from app.main import bp


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/select_user/<int:user_id>')
@login_required
def select_user(user_id):
    response = make_response(redirect(url_for('main.index')))
    response.set_cookie('selected_user_id', str(user_id), max_age = 60 * 60)
    return response

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    users = User.query.filter(User.id != current_user.id).order_by(
            User.username.asc()).all()
    selected_user_id = 0
    if request.cookies.get('selected_user_id') is not None:
        selected_user_id = int(request.cookies.get('selected_user_id'))

    messages = None
    selected_user = None
    if selected_user_id != 0:
        selected_user = User.query.filter_by(id=selected_user_id).first_or_404()
        from sqlalchemy import or_

        messages = Message.query.filter(
            or_(
                (Message.sender_id == current_user.id) & (Message.recipient_id == selected_user_id),
                (Message.sender_id == selected_user_id) & (Message.recipient_id == current_user.id)
            )
        ).order_by(Message.timestamp.asc())
    return render_template('index.html', users = users, selected_user_id = selected_user_id,
            selected_user = selected_user, messages = messages)


@bp.route('/user/<username>')
@login_required
def user(username):
    return render_template('user.html')


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
            form=form)


@bp.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
    message = request.form.get('message-input')
    selected_user_id = 0

    if message == '':
        return

    if request.cookies.get('selected_user_id') is not None:
        selected_user_id = int(request.cookies.get('selected_user_id'))
    user = User.query.filter_by(id = selected_user_id).first_or_404()
    msg = Message(author=current_user, recipient=user, body=message)
    db.session.add(msg)
    user.add_notification('unread_message_count', user.new_messages())
    db.session.commit()
    flash('Your message has been sent.')
    return redirect(url_for('main.index'))


@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
            Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
        } for n in notifications])

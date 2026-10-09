from flask import Blueprint, render_template, request, redirect, url_for, flash,session
auth_bp=Blueprint('auth',__name__)
@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        USER_CREDENTIALS={
            'username':'admin',
            'password':'admin123'
        }
        if username==USER_CREDENTIALS['username'] and password==USER_CREDENTIALS['password']:
            session['user']=username
            flash('Login Sucessful','success')
        else:
            flash('Invalid Credentials','danger')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('You have been logged out','info')
    return redirect(url_for('auth.login'))
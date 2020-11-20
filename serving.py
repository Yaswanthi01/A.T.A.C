from flask import Flask
from flask import render_template, request, url_for, redirect, session, make_response, flash





@app.route('/menu_for_forms_positive', methods=['GET', 'POST'])
def menu_for_forms_positive():
	return render_template('menu_for_forms_positive.html')


@app.route('/menu_for_forms_negative', methods=['GET', 'POST'])
def menu_for_forms_negative():
	return render_template('menu_for_forms_negative.html')


@app.route('/general_details_positive', methods=['GET', 'POST'])
def general_details_positive():
	return render_template('general_details_positive.html')


@app.route('/general_details_negative', methods=['GET', 'POST'])
def general_details_negative():
	return render_template('general_details_negative.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
	return render_template('output.html')


@app.route('/unique_code_positive', methods=['GET', 'POST'])
def unique_code_positive():

	return render_template('unique_code_positive.html')


@app.route('/unique_code_negative', methods=['GET', 'POST'])
def unique_code_negative():

	return render_template('unique_code_negative.html')


@app.route('/medical_details', methods=['GET', 'POST'])
def medical_details():
	return render_template('medical_details.html')


@app.route('/xray_upload', methods=['GET', 'POST'])
def xray_upload():

	return render_template('xray_upload.html')


@app.route('/')
def index():

	return render_template('coronacare.html')


@app.route('/symptoms')
def symptoms():
	return render_template('symptoms.html')


@app.route('/preventions')
def prevent():

	return render_template('preventions.html')


@app.route('/treatments')
def treatments():

	return render_template('treatments.html')


@app.route('/coping')
def cope():

	return render_template('coping.html')


@app.route('/contact')
def contact():

	return render_template('contact.html')


@app.route('/login')
def login():

	return render_template('login.html')


@app.route('/signin')
def signin():

	return render_template('signin.html')


@app.route('/thankyou')
def thankyou():

	return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404



if __name__ == '__main__':
	app.run(debug=True)

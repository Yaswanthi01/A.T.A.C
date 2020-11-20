from flask import Flask
from flask import render_template, request, url_for, redirect, session, make_response, flash
import sqlite3 as lite
import os

from patient_form_details.general_details_positive import GeneralDetailsPositive
from patient_form_details.general_details_negative import GeneralDetailsNegative
from patient_form_details.medical_details import MedicalDetails
from patient_form_details.code_generation import CodeGeneration
from patient_form_details.xray_details import XrayDetails
from patient_form_details.output_generation import OutputGeneration
# from patient_form_details.session_for_unique_code import SessionForUniqueCode
app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))

db_path = r"C:\Users\anjuv\Documents\A.T.A.C\database\patient.db"

con = lite.connect(db_path, check_same_thread=False)
print("db connection successful")

app.secret_key = os.urandom(25)

@app.route('/menu_for_forms_positive', methods=['GET', 'POST'])
def menu_for_forms_positive():
	return render_template('menu_for_forms_positive.html')


@app.route('/menu_for_forms_negative', methods=['GET', 'POST'])
def menu_for_forms_negative():
	return render_template('menu_for_forms_negative.html')


@app.route('/general_details_positive', methods=['GET', 'POST'])
def general_details_positive():
	if request.method == "POST":
		Code_Generation = CodeGeneration()
		General_Details_Positive = GeneralDetailsPositive(con)
		positive_code = Code_Generation.positive_code()
		General_Details_Positive.general_details_positive_input(positive_code)

		return redirect(url_for('menu_for_forms_positive'))

	if request.method == "GET":
		return render_template('general_details_positive.html')

@app.route('/general_details_negative', methods=['GET', 'POST'])
def general_details_negative():
	if request.method == "POST":
		Code_Generation = CodeGeneration()
		General_Details_Negative = GeneralDetailsNegative(con)
		negative_code = Code_Generation.negative_code()
		General_Details_Negative.general_details_negative_input(negative_code)
		return redirect(url_for('menu_for_forms_positive'))

	if request.method == "GET":
		return render_template('general_details_negative.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
	Calculations_output = OutputGeneration(con)
	Calculations_output.get_data_from_medical_details()

	# return redirect(url_for('output'))
	cur = con.cursor()
	# if request.method == "GET":
	var = cur.execute("SELECT * FROM general_details WHERE ID = ?", (session['data'],))
	for row in cur.fetchall():
		gen_det = row
	print(gen_det)
	var = cur.execute("SELECT * FROM medical_details WHERE  unique_code= ?", (session['unique'],))
	for row in cur.fetchall():
		med_det = row
	print(med_det)
	path_to_photo =session['photo_path']
	print(path_to_photo)



	return render_template('user_report.html',gen_det=gen_det,med_det=med_det, path_to_photo=path_to_photo)


@app.route('/unique_code_positive', methods=['GET', 'POST'])
def unique_code_positive():
	# session_for_unique_code = SessionForUniqueCode(con)
	# code_unique = session['self.code_unique']
	return render_template('unique_code_positive.html',code_unique=code_unique)


@app.route('/unique_code_negative', methods=['GET', 'POST'])
def unique_code_negative():

	return render_template('unique_code_negative.html')


@app.route('/medical_details', methods=['GET', 'POST'])
def medical_details():
	if request.method == "POST":
		Medical_Details_Negative = MedicalDetails(con)
		Medical_Details_Negative.medical_details_input()
		return redirect(url_for('menu_for_forms_positive'))

	if request.method == "GET":
		return render_template('medical_details.html')


@app.route('/xray_upload', methods=['GET', 'POST'])
def xray_upload():
	if request.method == "POST":
		Xray_Details = XrayDetails(con)
		Xray_Details.xray_input("unique_code", app_root)

		return redirect(url_for('menu_for_forms_positive'))

	if request.method == "GET":
		return render_template('xray_upload.html')


@app.route('/')
def index():

	return render_template('atac_home.html')


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


@app.route('/signup')
def signup():

	return render_template('signup.html')


@app.route('/thankyou')
def thankyou():

	fname = request.args.get('fname')
	lname = request.args.get('lname')
	return render_template('thankyou.html', fname=fname, lname=lname)



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404



if __name__ == '__main__':
	app.run(debug=True)

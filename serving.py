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


app = Flask(__name__)
app_root = os.path.abspath(os.path.dirname(__file__))

db_path = r"C:\Users\anjuv\Documents\A.T.A.C\database\patient.db"

con = lite.connect(db_path, check_same_thread=False)
print("db connection successful")


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
    Calculations_output = OutputGeneration(con)
    Calculations_output.get_data_from_medical_details()

    # return redirect(url_for('output'))
    cur = con.cursor()
    # if request.method == "GET":
    var = cur.execute(
        "SELECT * FROM general_details WHERE ID = ?", (session['data'],))
    for row in cur.fetchall():
        gen_det = row
    print(gen_det)

    cursor = cur.execute('SELECT max(id) FROM general_details')
    max_id = cursor.fetchone()[0]
    print(max_id)
    str_id = str(max_id)

    var = cur.execute(
        "SELECT unique_code FROM general_details WHERE ID = ? ", (str_id,))
    for row in cur.fetchone():
        session['code_unique'] = row
    code_unique_new = session['code_unique']
    print(code_unique_new)

    var = cur.execute(
        "SELECT * FROM medical_details WHERE  unique_code= ?", (code_unique_new,))
    for row in cur.fetchall():
        med_det = row

    print(med_det)
    path_to_photo = session['photo_path']
    print(path_to_photo)

    var = cur.execute(
        "SELECT * FROM output WHERE unique_code = ?", (code_unique_new,))
    for row in cur.fetchall():
        output_det = row
    print(output_det)

    return render_template('user_report.html', gen_det=gen_det, med_det=med_det, path_to_photo=path_to_photo, output_det=output_det)


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

    return render_template('thankyou.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

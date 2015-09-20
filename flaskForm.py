from flask import Flask, request, render_template
from models import OnboardingInfo

app = Flask(__name__)

@app.route('/')
def form_content():
    return render_template('index1.html')

@app.route('/userdata/', methods=['POST'])
def userdata():
    onboarding_info = OnboardingInfo(request.form)
    # import pdb; pdb.set_trace()
    return render_template(
        'index.html',
        firstname=onboarding_info.firstname,
        lastname=onboarding_info.lastname,
    )


if __name__ == "__main__":
    app.debug = True
    #host= "0.0.0.0", port= 8000
    app.run(host= "0.0.0.0", port= 7000)

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# with this flask variables now our code is running dynamically and it is super efficient
@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


# creating a function to store data in database.txt

def write_to_file(data):
	with open('database.txt', mode='a') as database: # mode a means to append
		# now in the below three var we are acccesing data for the database from submit_form data variable
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email}, {subject}, {message}')


# CREATING CSV MODULE DB


def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # delimeter , means each item will be separated by a comma
		# quotechar means do we want any quotes now since we do not want any so it will just be an empty string
		# and that is all the text we need now rest we can read in documentation of csv
		csv_writer.writerow([email, subject, message])


# now using the code for contact

@app.route('/submit_form', methods=['POST', 'GET'])
# POST simply means that the browser wants us to save information
# GET means the browser wants us to send information
def submit_form():
    if request.method == 'POST':
    # here we are saying if the method is equal to post which in this case we have already added method as post in form tag in conatct.html. So if the method if post then we have to grab the data by doing this.
        try:
            data = request.form.to_dict()
            # here we are requesting the data from  the form and then converting it to dict. we are grabbing the values as shown
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'data not saved in database'

    else:
        return 'something went wrong try again'
    	# upon submitting we can see the response in dict form in cmd 


# this is just the general syntax as shown above
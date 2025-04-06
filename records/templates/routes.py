from records import records

data = [
    {
        'recordID': '000001',
        'recordCreationDateTime': 'Mon, April 5, 2025',
        'recordAuthor': ' Danny Dang',
        'market': 'NSW H&C',
        'VenueName': 'Bankstown Sports Club',
        'machineType': 'Dynasty Vue',
        'machineSerial': 'XEV2000000'
    },
    {
        'recordID': '000002',
        'recordCreationDateTime': 'Mon, April 6, 2025',
        'recordAuthor': ' Danny Dang',
        'market': 'NSW H&C',
        'VenueName': 'Bankstown Sports Club',
        'machineType': 'Dynasty Vue',
        'machineSerial': 'XEV2000001'
    },
    {
        'recordID': '000003',
        'recordCreationDateTime': 'Mon, April 5, 2025',
        'recordAuthor': ' Danny Dang',
        'market': 'NSW H&C',
        'VenueName': 'Bankstown Sports Club',
        'machineType': 'Dynasty Vue',
        'machineSerial': 'XEV2000003'
    }
]

@app.route("/")
@app.route("/index")
def index():
    # return render_template('home.html', records=records)
    return "Hello World!"

'''
@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
'''
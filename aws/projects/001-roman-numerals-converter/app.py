from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':    
        number_input = request.form["number"]
        romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
        if (not number_input.isdigit()) or ((int(number_input) > 3999) or (int(number_input) < 1)):
            return render_template("index.html", developer_name = "Mehmet", not_valid= True)
        number_decimal = int(number_input)   
        number_roman = ""
        for key, value in romandict.items():
            while number_decimal >= value:
                quotient = number_decimal // value 
                number_roman += key * quotient
                number_decimal %= value
        return render_template("result.html", developer_name = "E2012-Murat", number_decimal = int(number_input), number_roman=number_roman)
    
    else:
        return render_template("index.html", developer_name = "E2012-Murat")
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

import requests

url = 'https://api.futureme.org/letters'
data = {
    #'authenticity_token': 'BNcLVRFHgsHjgY4LubdRX4ipgqgbeqeJv9CQiMr62FvWnlzDthJp6b0G1_cvzX0KnlOcPphZoSb6c0Zc3qGARg',
    'letter[subject]': 'A letter from Jun 17th, 2021',
    'letter[body]': 'letter to mo r ro w',
    'letter[send_date(2i)]': '6',
    'letter[send_date(3i)]': '16',
    'letter[send_date(1i)]': '2022',
    'letter[pick_date]': '1',
    'letter[public]': 'true',
    'letter[comments]': '',
    'letter[email]': 'usapplestore1234@gmail.com'
}

res = requests.post(url, data=data)
print(res.text)

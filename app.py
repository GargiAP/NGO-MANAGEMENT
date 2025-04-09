from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    ngos = [
        {'name': 'HungerHope', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAiUn7zarjh91rmn-bbEDmb3FD2BhU4Ab_-w&s'},
        {'name': 'ElderNest', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSVqMISB0NdZkjRWqLrPJph5BP74O2lg10D7l9bKAXNzFcIl9MVxXXF3UfGKPiGOrNtRg&usqp=CAU'},
        {'name': 'SheRise', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoszObMs9cof_vqH-xMtlyXWQUVxQ01zgaTw&s'},
        {'name': 'PawSafe', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8SJzfyz7l9DuVF_h1YHQ1EVhO5lgkHaZrEA&s'},
        {'name': 'BrightSteps', 'image': 'https://www.sharanalayam.org/wp-content/uploads/2024/01/banner1.jpg'}
    ]
    return render_template('home.html', ngos=ngos)

@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')

@app.route('/volunteer')
def volunteer():
    blog_posts = [
        {
            'id': 1,
            'title': 'HungerHope',
            'description': 'HungerHope is a dedicated NGO committed to eradicating hunger...',
            'venue': 'Pune',
            'date': 'April 24, 2025',
            'time': '11:00 a.m',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAiUn7zarjh91rmn-bbEDmb3FD2BhU4Ab_-w&s',
        },
        {
            'id': 2,
            'title': 'PawSafe',
            'description': 'EduBridge focuses on bridging the education gap...',
            'venue': 'Pune',
            'date': 'May 3, 2025',
            'time': '10:00 a.m',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8SJzfyz7l9DuVF_h1YHQ1EVhO5lgkHaZrEA&s',
        },
        {
            'id': 3,
            'title': 'Fly high',
            'description': 'GreenFuture is an environmental NGO working on reforestation...',
            'venue': 'Bangalore',
            'date': 'June 15, 2025',
            'time': '9:30 a.m',
            'image': 'https://www.aahwahan.com/Ngo-for-education-aahwahan.jpg',
        },
        {
            'id': 4,
            'title': 'BrightSteps',
            'description': 'HealthFirst provides essential medical support...',
            'venue': 'Hyderabad',
            'date': 'July 10, 2025',
            'time': '2:00 p.m',
            'image': 'https://www.sharanalayam.org/wp-content/uploads/2024/01/banner1.jpg',
        },
        {
            'id': 5,
            'title': 'SheRise',
            'description': 'ShelterAid supports homeless families...',
            'venue': 'Mumbai',
            'date': 'August 20, 2025',
            'time': '4:00 p.m',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoszObMs9cof_vqH-xMtlyXWQUVxQ01zgaTw&s',
        },
        {
            'id': 6,
            'title': 'ElderNest',
            'description': 'HealthFirst provides essential medical support...',
            'venue': 'Hyderabad',
            'date': 'July 10, 2025',
            'time': '2:00 p.m',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSVqMISB0NdZkjRWqLrPJph5BP74O2lg10D7l9bKAXNzFcIl9MVxXXF3UfGKPiGOrNtRg&usqp=CAU',
        },
    ]
    return render_template('volunteerpg.html', blog_posts=blog_posts)

@app.route('/volunteerform')
def volunteer_form():
    return render_template("volunteerform.html")

@app.route('/donation')
def donation():
    return "<h1>Donation page under construction</h1>"

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/ngosignup')
def ngosignup():
    return render_template('ngosignin.html')
if __name__ == '__main__':
    app.run(debug=True)

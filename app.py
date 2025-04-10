from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime, date
from flask import session

app = Flask(__name__)
app.secret_key = 'ngoproject'

# --- MySQL Connection ---
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gargee",     # Replace with your MySQL password
    database="ngo"      # Replace with your database name
)
cursor = db.cursor()

# --- Home Page ---
@app.route('/')
def home():
    ngos = [
        {'name': 'HungerHope', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAiUn7zarjh91rmn-bbEDmb3FD2BhU4Ab_-w&s'},
        {'name': 'ElderNest', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSVqMISB0NdZkjRWqLrPJph5BP74O2lg10D7l9bKAXNzFcIl9MVxXXF3UfGKPiGOrNtRg&usqp=CAU'},
        {'name': 'SheRise', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoszObMs9cof_vqH-xMtlyXWQUVxQ01zgaTw&s'},
        {'name': 'PawSafe', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8SJzfyz7l9DuVF_h1YHQ1EVhO5lgkHaZrEA&s'},
        {'name': 'BrightSteps', 'image': 'https://www.sharanalayam.org/wp-content/uploads/2024/01/banner1.jpg'}
    ]
    initials = None
    if 'username' in session:
        initials = session['username'][0].upper()
    elif 'ngo_name' in session:
        initials = session['ngo_name'][0].upper()

    return render_template('home.html', ngos=ngos, initials=initials)

# --- Login Page ---
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check for volunteer login
    cursor.execute("SELECT * FROM volunteer_signup WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        session['username'] = user[1]  # username is in 2nd column

        # Check if user already exists in `users`
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()

        if not existing_user:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()

        return redirect(url_for('home'))

    # Check for NGO login
    cursor.execute("SELECT * FROM ngo_signup WHERE ngo_name=%s AND password=%s", (username, password))
    ngo = cursor.fetchone()

    if ngo:
        session['ngo_name'] = ngo[1]  # ngo_name is in 2nd column

        # Check if NGO already exists in `users`
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()

        if not existing_user:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()

        return redirect(url_for('home'))

    flash("⚠️ Invalid login credentials", "error")
    return redirect(url_for('home'))

    
# --- Volunteer Page ---
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

    initials = None
    if 'username' in session:
        initials = session['username'][0].upper()
    elif 'ngo_name' in session:
        initials = session['ngo_name'][0].upper()

    return render_template('volunteerpg.html', blog_posts=blog_posts, initials=initials)


# --- Volunteer Form Page ---
@app.route('/volunteerform')
def volunteer_form():
    return render_template("volunteerform.html")

@app.route('/eventregister')
def event_register():
    return render_template('eventregister.html')

# --- Register Volunteer (form action) ---
@app.route('/register_volunteer', methods=['POST'])
def register_volunteer():
    data = request.form
    cursor.execute("""
        INSERT INTO volunteer_register (username, email, age, contact_no, gender, address, medical_conditions)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['username'], data['email'], data['age'], data['contact'],
        data['gender'], data['address'], data['medical_conditions']
    ))
    db.commit()
    return redirect(url_for('home'))

# --- Register Event ---
@app.route('/register_event', methods=['POST'])
def register_event():
    data = request.form
    event_date_str = data['event_date']
    event_date = datetime.strptime(event_date_str, '%Y-%m-%d').date()
    today = date.today()

    if event_date < today:
        flash('⚠️ Event date cannot be before today!', 'error')
        return redirect(url_for('event_register'))  # Redirect back to the form

    try:
        cursor = db.cursor()
        cursor.callproc('RegisterEvent', [
            data['ngo_name'],
            data['description'],
            data['venue'],
            data['contact_no'],
            event_date_str,
            data['event_time']
        ])
        db.commit()
        flash('🎉 Event registered successfully!', 'success')
    except Exception as e:
        db.rollback()
        flash(f'❌ Error: {str(e)}', 'error')

    return redirect(url_for('volunteer'))


# --- NGO Signup ---
@app.route('/register_ngo', methods=['POST'])
def register_ngo():
    data = request.form
    cursor.execute("""
        INSERT INTO ngo_signup (ngo_name, email, contact_no, address, password, confirm_password)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data['ngo_name'], data['email'], data['contact_no'],
        data['address'], data['password'], data['confirm_password']
    ))
    db.commit()
    return redirect(url_for('home'))

# --- Volunteer Signup ---
@app.route('/signup_volunteer', methods=['POST'])
def signup_volunteer():
    data = request.form
    cursor.execute("""
        INSERT INTO volunteer_signup (username, email, age, contact_no, gender, address, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['username'], data['email'], data['age'], data['contact_no'],
        data['gender'], data['address'], data['password']
    ))
    db.commit()
    return redirect(url_for('home'))

# --- Donation Page ---
@app.route('/donation')
def donation():
    return "<h1>Donation page under construction</h1>"

# --- Sign In Page ---
@app.route('/signin')
def signin():
    return render_template('signin.html')

# --- NGO Signup Page ---
@app.route('/ngosignup')
def ngosignup():
    return render_template('ngosignin.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))


# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)

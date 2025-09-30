from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Main route to render the index.html template
@app.route('/')
def home():
    # In a larger application, data would come from a database. 
    # Here, we pass the key resume data as a dictionary to the template.
    portfolio_data = {
        'name': "BANDARU AKHIL", # 
        'tagline': "Motivated and detail-oriented Computer Science and Engineering student specializing in Data Science.", # [cite: 6]
        'email': "akhilbandaru326@gmail.com", # [cite: 4]
        'phone': "91-7093659842", # [cite: 2]
        'linkedin': "Linkedin Profile Link (Not provided in text)", # [cite: 5]
        'github': "Github Profile Link (Not provided in text)", # [cite: 4]
        'skills': [
            "Python", "Java", "C", "HTML", "CSS", "JavaScript", "React.js", "Node.js", # [cite: 43, 44]
            "MySQL", "MongoDB", "Pandas", "NumPy", "Power BI" # [cite: 45, 50]
        ],
        'projects': [
            {"title": "Fake News Detection using Computer Vision", "tech": "PYTHON | ML | GEMINI API", "desc": "Developed a system to detect fake news by analyzing images for manipulation and cross-referencing with headline and content data using CNN and NLP techniques."}, # [cite: 10, 11, 13]
            {"title": "Talk Wise Circles", "tech": "REACT | NEXT.JS | TAILWIND CSS | NODE.JS", "desc": "Developed a web application for structured group discussions using a talking-circle format. Implemented real-time messaging with WebSockets."}, # [cite: 14, 15, 16, 17]
            {"title": "Smart Data Analyzer", "tech": "PYTHON | PANDAS | STREAMLIT", "desc": "Built a Python-based tool that automatically reads, cleans, analyzes, and visualizes datasets. Implemented smart insights and interactive dashboards."}, # [cite: 18, 19, 20, 21]
        ],
        'education': "HOLY MARY INSTITUTE OF SCIENCE & TECHNOLOGY - B.Tech in Computer Science and Engineering (Data Science) | CGPA: 8.30 (2026)" # [cite: 53, 54, 55]
    }
    return render_template('index.html', data=portfolio_data)

# Route to handle form submission (part of the Task 6 objective)
@app.route('/contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # --- Deliverable action (e.g., send email or log data) ---
        print(f"--- NEW CONTACT MESSAGE ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}\n")
        # In a production environment, you would use an email library or database here.
        
        # Flash a success message and redirect to prevent form resubmission
        # For simplicity, we just redirect home.
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
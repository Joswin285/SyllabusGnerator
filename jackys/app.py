from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_syllabus', methods=['POST'])
def generate_syllabus():
    topic = request.form.get('topic')
    educational_level = request.form.get('educational-level')

    # Mock data for demonstration
    description = f"This course will cover the essential topics of {topic}."
    course_outcomes = [
        "Understand the basics of the topic.",
        "Apply the knowledge in real-world scenarios.",
        "Analyze and evaluate the concepts."
    ]
    course_outline = [
        {"unit": 1, "title": "Introduction to Topic", "content": "Overview and basic concepts."},
        {"unit": 2, "title": "Intermediate Concepts", "content": "In-depth analysis and examples."},
        {"unit": 3, "title": "Advanced Techniques", "content": "Complex topics and applications."}
    ]
    roadmap = [
        {"week": 1, "activity": "Introduction and overview."},
        {"week": 2, "activity": "Intermediate lessons and exercises."},
        {"week": 3, "activity": "Advanced projects and presentations."}
    ]

    # Different templates for responses
    templates = [
        lambda: {
            "title": f"Syllabus for {topic} ({educational_level})",
            "description": description,
            "sections": [
                {"title": "Course Outcomes", "content": "\n".join([f"- {outcome}" for outcome in course_outcomes])},
                {"title": "Course Outline", "content": "\n".join([f"Unit {unit['unit']}: {unit['title']} - {unit['content']}" for unit in course_outline])},
                {"title": "Roadmap", "content": "\n".join([f"Week {week['week']}: {week['activity']}" for week in roadmap])}
            ]
        },
        lambda: {
            "title": f"{educational_level} Level {topic} Syllabus",
            "description": f"Here's what you'll learn in this {topic} course:",
            "sections": [
                {"title": "Learning Objectives", "content": "\n".join([f"* {outcome}" for outcome in course_outcomes])},
                {"title": "Modules", "content": "\n".join([f"Module {unit['unit']}: {unit['title']} - {unit['content']}" for unit in course_outline])},
                {"title": "Weekly Plan", "content": "\n".join([f"Week {week['week']}: {week['activity']}" for week in roadmap])}
            ]
        }
    ]

    selected_template = random.choice(templates)()
    
    return jsonify(selected_template)

if __name__ == '__main__':
    app.run(debug=True)

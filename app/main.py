from flask import Flask, request, jsonify
from app.github_api import fetch_repo_files
from app.code_analysis import analyze_code
from app.models.review_model import suggest_improvements

app = Flask(__name__)

@app.route('/review', methods=['POST'])
def review():
    data = request.json
    code = data.get('code')
    analysis = analyze_code(code)
    suggestions = suggest_improvements(code)
    return jsonify({"analysis": analysis, "suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
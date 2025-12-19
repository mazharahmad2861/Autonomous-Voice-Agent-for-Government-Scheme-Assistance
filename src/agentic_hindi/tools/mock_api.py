from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory application store
applications = []

@app.route('/apply', methods=['POST'])
def apply():
    data = request.json
    if not data or 'scheme_id' not in data or 'applicant' not in data:
        return jsonify({'status':'error','message':'Invalid request'}), 400
    application_id = f"app_{len(applications)+1}"
    applications.append({'id': application_id, 'scheme_id': data['scheme_id'], 'applicant': data['applicant'], 'status': 'submitted'})
    return jsonify({'status': 'ok', 'application_id': application_id})

@app.route('/applications', methods=['GET'])
def list_apps():
    return jsonify(applications)

@app.route('/')
def index():
    return "<h3>Mock API running — endpoints: /applications (GET), /apply (POST)</h3>"

@app.route('/favicon.ico')
def favicon():
    # Return no content to avoid browser 404 noise
    return ('', 204)

if __name__ == '__main__':
    import os
    port = int(os.getenv('MOCK_API_PORT', os.getenv('PORT', 5002)))
    host = os.getenv('MOCK_API_HOST', '127.0.0.1')
    print(f"Starting mock API on http://{host}:{port}")
    app.run(host=host, port=port)

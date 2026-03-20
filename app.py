from flask import Flask, jsonify
from flask_cors import CORS
import random
import time
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to call API

start_time = time.time()

# Pipeline stages
stages = ["Clone", "Test", "Build", "Deploy", "Verify"]
current_stage_index = 2

@app.route('/')
def home():
    return jsonify({"message": "DevOps Pipeline API is running!"})

@app.route('/api/pipeline')
def pipeline():
    elapsed = time.time() - start_time
    progress = (current_stage_index / len(stages)) * 100
    
    return jsonify({
        "stages": stages,
        "current_stage": stages[current_stage_index],
        "progress": round(progress, 1),
        "elapsed_time": round(elapsed, 1),
        "status": "running" if current_stage_index < len(stages) - 1 else "completed"
    })

@app.route('/api/metrics')
def metrics():
    return jsonify({
        "containers": random.randint(3, 8),
        "cpu": random.randint(20, 80),
        "memory": random.randint(30, 70),
        "deployments": random.randint(100, 500),
        "success_rate": random.randint(85, 99)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
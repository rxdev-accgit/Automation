from flask import Flask as FLS, jsonify as js, request
import requests

app = FLS("AutomationServer.FLS")

WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "http://localhost:5678/webhook-test/roblox-events")
@app.route("/AutomationRequest", methods=["POST"])
def roblox_webhook():
    data = request.get_json()
    
    if not data:
        return js({
            "error": "No JSON Data received"
        }), 400
        
    print("Received from roblox: ", data)

    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        print(True, f"Forwarded to n8n. Status {response.status_code}")
    
    except requests.exceptions.RequestException as e:  
        print(f"Failed to forward to n8n: {e}")
        return js({
            "Status": f"failed, reason: {e}"  
        }), 500  
        
    return js({
        "Status": "Ok"
    }), 200
   
@app.route("/", methods=["GET"])
def health_check():
    return "Server is alive", 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask as FLS, jsonify as js, request

app = FLS("AutomationServer.FLS")

@app.route("/AutomationRequest", Methods=["POST"])
def roblox_webhook():
    data = request.get_json()
    
    if not data:
        return js({
            "error": "No JSON Data received"
        }), 400
        
    print("Received from roblox: ", data)
    
    return js({
        "Status": "Ok"
    }), 200
    

@app.route("/", methods=["GET"])
def health_check():
    return "Server is alive", 200
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
    

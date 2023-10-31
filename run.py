from flask import Flask, render_template, request, jsonify
from web3 import Web3
from waitress import serve

app = Flask(__name__)
app.debug = True

# Connect to an Ethereum node (for example, Infura)
w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/2e4963a9ddb34baf87e34ad158572c37"))

# Replace with your contract address and ABI
contract_address = '0xa8EFD0BA4b676dAe0586aD00A7C9F29fD8C3D4D6'
contract_abi = [
    {
        "inputs": [],
        "name": "message",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_message", methods=["GET"])
def get_message():
    try:
        message = contract.functions.message().call()
        output = contract_address

        print("Message retrieved:", message)
        # print("contract address:", contract_address)
        return jsonify({"message": message})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)
    serve(app, host="0.0.0.0", port=8080)

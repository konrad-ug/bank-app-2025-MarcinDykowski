from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_acount import PersonalAccount

app = Flask(__name__)

registry = AccountRegistry()
@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["first_name"], data["last_name"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.every_account()
    accounts_data = [{"first_name": account.first_name, "last_name": account.last_name, "pesel":account.pesel, "balance": account.balance} for account in accounts]
    return jsonify(accounts_data), 200
@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = registry.number_of_accounts()
    return jsonify({"count": count}), 200
@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    found_account = registry.search_pesel(pesel)

    if found_account is False:
        return jsonify({"error": "404"}), 404
    else:
        return jsonify({
            "first_name": found_account[0],
            "last_name": found_account[1],
            "pesel": found_account[2]
        }), 201
@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    new_first_name = data.get("first_name")
    new_last_name = data.get("last_name")

    info = registry.update_account(pesel, new_first_name, new_last_name)
    if (info == False):
        return jsonify({"error": "404"}), 404
    else:
        return jsonify({"message": info}), 201
@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    info = registry.delete_account(pesel)
    if (info == False):
        return jsonify({"error": "404"}), 404
    else:
        return jsonify({"message": info}), 201


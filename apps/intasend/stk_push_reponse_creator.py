def entangle_stk_push_response(data):
    return {
        "transaction_id": data.get("id"),
        "invoice_id": data["invoice"].get("invoice_id"),
        "state": data["invoice"].get("state"),
        "charges": data["invoice"].get("charges"),
        "provider": data["invoice"].get("provider"),
        "currency": data["invoice"].get("currency"),
        "amount_transacted": data["invoice"].get("net_amount"),
        "amount": data["invoice"].get("value"),
        "phone_number": data["invoice"].get("account"),
        "mpesa_reference": data["invoice"].get("mpesa_reference"),
        "api_ref": data["invoice"].get("api_ref"),
        "customer": data.get("customer"),
        "transaction_timestamp": data.get("created_at"),
    }

import json
from flask import jsonify, request, Response

from settings import app
from DbModel import Inventory


@app.route("/inventory/<int:inventory_id>")
def get_inventory(inventory_id):
    """Get inventory by id"""
    return jsonify({"tickets": Inventory.get_inventory(inventory_id)})


# TODO: Validate event_id in request to avoid 500 status
@app.route("/inventory/event/<int:event_id>")
def get_ticket_by_event(event_id):
    """Get available tickets for an event"""
    return jsonify({"tickets": Inventory.get_available_tickets(event_id)})


@app.route("/inventory/best-ticket/<int:event_id>")
def get_best_ticket(event_id):
    """Get 'best'/cheapest ticket for an event"""
    return jsonify({"tickets": Inventory.get_lowest_price_ticket(event_id)})


@app.route("/inventory", methods=['POST'])
def post_new_ticket():
    """Post a new ticket from a seller

    Args:
        request: json POST request

    Returns:
        response object - 201 status w/ location header or 400 w/ error

    """
    def is_valid_record(request_data):
        """Checks whether a request to post new ticket from seller
           has all required fields and no null string values.
        Args:
            request_data: request data as json

        Returns: boolean.
        """
        required_fields = ['inventoryId', 'sellerId', 'eventId',
                           'row', 'section', 'price', 'quantity']
        missing_fields = [field for field in required_fields
                          if field not in request_data.keys()]
        null_values = [k for k, v in request_data.items() if v == '']
        if missing_fields or null_values:
            return False
        else:
            return True

    request_data = request.get_json()
    if is_valid_record(request_data):
        Inventory.insert_ticket(
            request_data['inventoryId'],
            request_data['sellerId'],
            request_data['eventId'],
            request_data['row'],
            request_data['section'],
            float(request_data['price']),
            request_data['quantity']
        )
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/inventory/" + str(request_data['inventoryId'])
        return response
    else:
        invalidInventoryErrorMsg = {
            "error": "Invalid inventory data passed in request",
            "helpString": "Missing required field or data element"
        }
        return Response(json.dumps(invalidInventoryErrorMsg),
                        status=400, mimetype='application/json')


# TODO: Add request validation
@app.route("/inventory/sold/<int:inventory_id>", methods=['PUT'])
def put_ticket_to_sold(inventory_id):
    """Update a ticket to sold"""
    request_data = request.get_json()
    Inventory.update_ticket(request_data["inventoryId"])
    response = Response("", 204, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

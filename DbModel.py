import datetime
from flask_sqlalchemy import SQLAlchemy

from settings import app


db = SQLAlchemy(app)


class Inventory(db.Model):
    """Represents the quantity and price of tickets available per
       seller and event by seating (section and row)
    """
    inventory_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'), nullable=False)
    section = db.Column(db.Integer, nullable=False)
    row = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def json(self):
        """Helper function to convert from SQLAlchemy objects to JSON"""
        return {
            "inventoryId": self.inventory_id,
            "eventId": self.event_id,
            "section": self.section,
            "row": self.row,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status
        }

    def get_inventory(inventory_id):
        """Get inventory entry"""
        inventory = (Inventory.query
                     .filter_by(inventory_id=inventory_id)
                     .all())
        return [Inventory.json(i) for i in inventory]

    def get_available_tickets(event_id):
        """Get all available tickets for an event
        Args:
            event_id: integer event

        Return: list of tickets formatted as json
        """
        tickets = (Inventory.query
                   .filter_by(event_id=event_id)
                   .filter_by(status='AVAILABLE')
                   .all())
        return [Inventory.json(ticket) for ticket in tickets]

    def get_lowest_price_ticket(event_id):
        cheapest_ticket = (Inventory.query
                           .filter_by(event_id=event_id)
                           .order_by(Inventory.price)
                           .first())
        return Inventory.json(cheapest_ticket)

    def insert_ticket(inventory_id, event_id, seller_id, section, row, quantity, price):
        """Inserts a new ticket from a seller"""
        new_ticket = Inventory(
            inventory_id=int(inventory_id),
            event_id=int(event_id),
            seller_id=int(seller_id),
            section=int(section),
            row=str(row),
            quantity=int(quantity),
            price=float(price),
            status="AVAILABLE",
            created=datetime.datetime.now(),
            updated=datetime.datetime.now())
        db.session.add(new_ticket)
        db.session.commit()

    def update_ticket(inventory_id):
        """Update ticket(s) to sold"""
        ticket_to_update = Inventory.query.filter_by(inventory_id=inventory_id).first()
        ticket_to_update.status = "SOLD"
        ticket_to_update.updated = datetime.datetime.now()
        db.session.commit()


class Event(db.Model):
    """Dimension table describing an event"""
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    type = db.Column(db.String(20))
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    venue = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)


class Seller(db.Model):
    """Dimension table describing a ticket vendor"""
    seller_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    street1 = db.Column(db.String(40))
    street2 = db.Column(db.String(40))
    city = db.Column(db.String(40))
    state = db.Column(db.String(4))
    postal = db.Column(db.String(10))
    country_code = db.Column(db.String(3))


class Customer(db.Model):
    """Dimension table describing a ticket purchaser"""
    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    prefix = db.Column(db.String(10))
    first = db.Column(db.String(40), nullable=False)
    middle = db.Column(db.String(40))
    last = db.Column(db.String(40), nullable=False)
    suffix = db.Column(db.String(10))
    email = db.Column(db.String(36), unique=True, nullable=False)
    phone = db.Column(db.String(36))
    street1 = db.Column(db.String(40))
    street2 = db.Column(db.String(40))
    city = db.Column(db.String(20))
    state_code = db.Column(db.String(2))
    postal_code = db.Column(db.String(10))
    country_code = db.Column(db.String(4))


class Purchase(db.Model):
    """Transactional table describing tickets purchased
       by a customer from a seller for a given event
    """
    purchase_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.seller_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)
    section = db.Column(db.Integer, nullable=False)
    row = db.Column(db.String(3), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    referral = db.Column(db.String, nullable=False)  # direct, ESPN, Google
    delivery_method = db.Column(db.String, nullable=False)  # mobile, email, mail
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

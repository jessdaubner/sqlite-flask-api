"""Create database tables and populate with sample and fake data"""
import datetime
import csv
import random
from DbModel import db, Inventory, Seller, Event
from data.fake_data import SELLERS, EVENTS


def insert_events():
    for event in EVENTS:
        db.session.add(Event(name=event["Name"], type=event["Type"],
                             start_date=event["StartDate"], end_date=event["EndDate"],
                             venue=event["Venue"], city=event["City"],
                             state=event["State"], postal_code=event["PostalCode"],
                             country_code=event["CountryCode"]))
        db.session.commit()


def insert_sellers():
    for seller in SELLERS:
        db.session.add(Seller(name=seller["Name"], email=seller["Email"]))
        db.session.commit()


def populate_inventory_table():
    """Reads sample CSV data and inserts it into the inventory table
       after adding seller_id, status, created and updated timestamps
    """
    with open('data/sampleTickets.csv') as data:
        sample_tickets = csv.reader(data, delimiter=',')
        next(sample_tickets, None)  # skip file header
        for row in sample_tickets:
            record = Inventory(
                event_id=int(row[0]),
                seller_id=random.choice([1, 2, 3]),
                section=str(row[1]),
                row=str(row[4]),
                quantity=int(row[2]),
                price=float(row[3]),
                status="AVAILABLE",
                created=datetime.datetime.now(),
                updated=datetime.datetime.now())
            db.session.add(record)
            db.session.commit()


if __name__ == "__main__":
    db.create_all()
    insert_sellers()
    insert_events()
    populate_inventory_table()

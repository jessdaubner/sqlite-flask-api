import datetime


SELLERS = [
    {
        "Name": "ABC Media Inc.",
        "Email": "support@ABCMedia.inc"
    },
    {
        "Name": "BuyTickets.com",
        "Email": "john@buytickets.com"
    },
    {
        "Name": "TicketHub LLC",
        "Email": "general@tickethub.com"
    }
]

EVENTS = [
    {
        "EventId": 162,
        "Name": "Taylor Swift reputation",
        "Type": "concert",
        "StartDate": datetime.datetime(2018, 11, 13, 20, 0, 0, 0),
        "EndDate": datetime.datetime(2018, 11, 13, 22, 30, 0, 0),
        "Venue": "Staples Center",
        "Street": "1111 South Figueroa Street",
        "City": "Los Angeles",
        "State": "CA",
        "PostalCode": "90015",
        "CountryCode": "USA",
    },
    {
        "EventId": 164,
        "Name": "Foo Fighters",
        "Type": "concert",
        "StartDate": datetime.datetime(2018, 7, 29, 18, 0, 0, 0),
        "EndDate": datetime.datetime(2018, 7, 29, 23, 30, 0, 0),
        "Venue": "Wrigley Field",
        "Street": "1060 W Addison St",
        "City": "Chicago",
        "State": "IL",
        "PostalCode": "60613",
        "CountryCode": "USA",
    },
    {
        "EventId": 107,
        "Name": "Hamilton",
        "Type": "muscial",
        "StartDate": datetime.datetime(2018, 10, 9, 18, 0, 0, 0),
        "EndDate": datetime.datetime(2018, 10, 9, 22, 0, 0, 0),
        "Venue": "CIBC Theatre",
        "Street": "18 W Monroe St",
        "City": "Chicago",
        "State": "IL",
        "PostalCode": "60603",
        "CountryCode": "USA",
    }
]

# SQLite Flask API
This repo establishes a relational data model, populates a SQLite database from a sample CSV file and fake data, and builds a REST API using Flask to communicate to the database.

## Setup
### Clone the project repo
`git clone git@github.com:jessdaubner/sqlite-flask-api.git`

### Docker
Download and install [Docker](https://www.docker.com/get-started). Build the app locally `docker build -t sqlite-flask-api .`.

### Postman
Download and install [Postman](https://www.getpostman.com/apps) which will be used to send API requests to the service for testing.

## Running the App
Run the app, mapping your machine's port 5000 to the container's published port 80.
`docker run -p 5000:80 sqlite-flask-api`

It will take a few seconds for the database to populate and the API service to start. The app will run on `http://localhost:5000`.

### Endpoints
| Method | Endpoint | Purpose |
| ------ | -------- | ------- |
| GET | `/inventory/{inventory-id}` | Get ticket by inventoryId, for testing |
| GET | `/inventory/event/{event-id}`  | Get available tickets for an event |
| GET | `/inventory/best-ticket/{event-id}` | Get "best"/cheapest tickt for an event |
| POST | `/inventory` | Add ticket to inventory |
| PUT | `/inventory/sold/{inventory-id}` | Update a ticket to sold |

## Testing the API
The files in `postman/` contain sample requests to test the API calls that update or add records to the database. Note that only 164, 107, and 162 are valid values for `event-id` while `inventory-id` created from the imported sample data will range from 1 to 1533.

### Testing GET
With the method set to GET (the default option), enter the request URL of the route you'd like to test, hit "Send" and view the response. For example, request URLs include `http://localhost:5000/inventory/event/164`, `http://localhost:5000/inventory/best-ticket/107`, and `http://localhost:5000/inventory/12`.

### Testing POST
1. In the "Headers" tab add a new key-value pair of `Content-Type` and `application/json` in order to set the content-type header to JSON.
2. In the "Body" tab, select the "raw" radio button and copy-and-paste an entry from `/postman/put_test.json` or create your own (`inventoryId` must be unique).
3. Change the method to POST in the drop-down menu, fill-in the request URL (e.g, `http://localhost:5000/inventory`) and hit "Send".

### Testing PUT
1. In the "Headers" tab, add a new key-value pair of `Content-Type` and `application/json` in order to set the content-type header to JSON.
2. In the "Body" tab, select the "raw" radio button and add an entry in the format of `{"inventoryId": 56}`.
3. Change the method to PUT in the drop-down menu and enter a valid request URL (e.g, `http://localhost:5000/inventory/sold/56`) corresponding to the `inventoryId` value in the request body.
4. Hit "Send" and view the 204 response. You can also send a GET request before and after the PUT request for the same `inventoryId` to see the status change from "AVAILABLE" to "SOLD".

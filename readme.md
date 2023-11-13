 
# Flask MongoDB Dockerized App

This is a simple Flask app connected to a MongoDB database, everything is dockerized.

---

## Setup:

1. Clone the repository:
    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Build and run the Docker containers:
    ```
    docker-compose up --build
    ```

3. Access the Flask app at `http://localhost:5000` and the MongoDB database at `mongodb://root:pass@docker_host:27017/mongo_database`.

---

## API Endpoints:

### GET /api/mongo_table
* Retrieve all objects from the MongoDB collection.

### POST /api/mongo_table
* Add a new object to the MongoDB collection. Send a JSON payload.

### PUT /api/mongo_table?id=\<object_id>
* Update an existing object in the MongoDB collection. Provide the object ID as a query parameter and send a JSON payload.

---

## Project Structure:

### app.py
* The `app.py` file contains the Flask application code, defining routes and interacting with the MongoDB database.

### mongo-init.js
* The `mongo-init.js` file initializes the MongoDB database with sample data and creates a user for authentication.

### requirements.txt
* The requirements.txt file lists the Python dependencies required for the Flask app.

### Dockerfile
* The Dockerfile specifies the configuration for building the Flask app Docker image.

### docker-compose.yml
* The `docker-compose.yml` file defines two services: `flask` and `mongodb`.
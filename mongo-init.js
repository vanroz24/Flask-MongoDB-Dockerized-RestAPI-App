db = db.getSiblingDB("mongo_database");

db.createUser({
    user: "root",
    pwd: "pass",
    roles: [{ role: "root", db: "admin" }]
});
db.auth("root", "pass");

db.mongo_table.insertMany([
    {
        "id": 0,
        "name": "test_name",
        "type": "test_type",
        "value": "test_value"
    },
    {
        "id": 1,
        "name": "greeting_msg",
        "type": "string",
        "value": "Hello!"
    },
    {
        "id": 2,
        "name": "num",
        "type": "int",
        "value": 123
    }
]);

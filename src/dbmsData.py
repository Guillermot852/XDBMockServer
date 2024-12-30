dbms_data = [
    {
        "id": "1",
        "hostName": "localhost",
        "dbPort": 3306,
        "dbName": "exampleDB",
        "dbType": "MySQL",
        "dbUser": "user",
        "dbPassword": "password",
        "dbRootUser": "root",
        "dbRootPassword": "rootPassword",
        "isConnected": False,
        "tables": [
            {"name": "users", "columns": ["id", "name", "email"]},
            {"name": "orders", "columns": ["id", "userId", "amount"]}
        ]
    },
    {
        "id": "2",
        "hostName": "localhost",
        "dbPort": 5432,
        "dbName": "storeDB",
        "dbType": "PostgreSQL",
        "dbUser": "postgresUser",
        "dbPassword": "postgresPassword",
        "dbRootUser": "postgres",
        "dbRootPassword": "postgresRootPassword",
        "isConnected": True,
        "tables": [
            {"name": "products", "columns": ["id", "name", "price"]},
            {"name": "customers", "columns": ["id", "name", "email", "phone"]}
        ]
    },
    {
        "id": "3",
        "hostName": "192.168.1.100",
        "dbPort": 1521,
        "dbName": "oracleDB",
        "dbType": "Oracle",
        "dbUser": "oracleUser",
        "dbPassword": "oraclePassword",
        "dbRootUser": "sys",
        "dbRootPassword": "sysPassword",
        "isConnected": True,
        "tables": [
            {"name": "employees", "columns": ["id", "name", "department"]},
            {"name": "projects", "columns": ["id", "name", "budget"]}
        ]
    },
    {
        "id": "4",
        "hostName": "localhost",
        "dbPort": 27017,
        "dbName": "mongoDB",
        "dbType": "MongoDB",
        "dbUser": "mongoUser",
        "dbPassword": "mongoPassword",
        "dbRootUser": "root",
        "dbRootPassword": "rootPassword",
        "isConnected": False,
        "tables": [
            {"name": "customers", "columns": ["_id", "name", "email", "address"]},
            {"name": "invoices", "columns": ["_id", "customerId", "amount", "status"]}
        ]
    },
    {
        "id": "5",
        "hostName": "localhost",
        "dbPort": 6379,
        "dbName": "redisDB",
        "dbType": "Redis",
        "dbUser": "redisUser",
        "dbPassword": "redisPassword",
        "dbRootUser": "root",
        "dbRootPassword": "rootPassword",
        "isConnected": True,
        "tables": [
            {"name": "sessions", "columns": ["sessionId", "data", "expiry"]},
            {"name": "caches", "columns": ["cacheKey", "cacheValue", "expiration"]}
        ]
    }
]

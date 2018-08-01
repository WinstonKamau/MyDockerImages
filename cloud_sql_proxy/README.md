Cloud SQL Proxy adopted from [here](https://github.com/veltra/docker-cloudsql-proxy)

### Step 1

Get your GCP json credentials that has the right of being a cloud sql proxy client.
Convert the json credentials using base64 and save it in a file called **credentials.txt** (Dont't commit this file to github)
e.g.
```
base64 sample.json > credentials.txt
```

### Step 2

Edit the .env file to include the instance connection name and then source the file.

```
source .env
```

### Step 3
Build the client. (You should run the command under the folder for clous_sql_proxy)

```
make build
```

To view the built image run `docker images` and you should see and image called `database` with the tag `v1`

### Step 4
Run the client.
```
make run
```
This should run the client in the background. You can run the command `docker ps` and look for a container called **database**.

### Step 5
Test access to the database. Remember port 3300 is the one that has been exposed.

```
psql "host=127.0.0.1 port=3300 sslmode=disable dbname=<DB_NAME> user=<USER_NAME>"
```

### Step 6

Destroy the images, network and containers
```
make destroy
```



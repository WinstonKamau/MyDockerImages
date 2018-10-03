## Versions
Docker Version
```
Client:
 Version:      18.03.1-ce
 API version:  1.37
 Go version:   go1.9.5
 Git commit:   9ee9f40
 Built:        Thu Apr 26 07:13:02 2018
 OS/Arch:      darwin/amd64
 Experimental: false
 Orchestrator: swarm
Server:
 Engine:
  Version:      18.03.1-ce
  API version:  1.37 (minimum version 1.12)
  Go version:   go1.9.5
  Git commit:   9ee9f40
  Built:        Thu Apr 26 07:22:38 2018
  OS/Arch:      linux/amd64
  Experimental: true
```


**Note:** This docker image was tested using the docker version above. This image uses `host.docker.internal` to connect to services on the host. This Special DNS may not be accessible to versions lower than *Version 18.0.3*. You can read more about the changelog for Version  [here](https://docs.docker.com/docker-for-mac/release-notes/#docker-community-edition-18030-ce-mac60-2018-03-30)


## Running the image
You can jump Step 1 by simply pulling an already built docker image and replacing the image name on step 2 with `winstonkamau/nginx:proxy`

```
docker pull winstonkamau/nginx:proxy
```

### Step 1 Build the docker image

Clone the repository to your preferred directory

```
git clone https://github.com/WinstonKamau/MyDockerImages.git
```

Change directory to the nginx folder

```
cd MyDockerImages/nginx
```

Run the docker command below to build the image and tag it with the name `nginx:test` You can replace the two names still separated by a colon. `<name>:<tag>`

```
docker build . -t nginx:test
```

### Step 2 Run the docker image

* The docker image allows you to specify whether to use HTTP or HTTPS but uses HTTP by default. This is made possible by specifying the environment variable `NGINX_PROTOCOL`
* The docker image allows you to specify the port, that the application running on your host machine, is running on. This is specified by the `NGINX_PORT` environment variable. By default it uses port 5000.

To run the image and proxy requests to an application running on port 7000 using HTTPS, run the command below
```
docker run -p 8000:80 -e NGINX_PROTOCOL=https -e NNGINX_PORT=7000 nginx:test
```
To run the image and proxy requests to an application running on port 7000 using HTTP, run the command below
```
docker run -p 8000:80 -e NGINX_PORT=4023 nginx:test
```
If your application runs on port 5000 and you want to access it via HTTP simply run the command below

```
docker run nginx:test
```

* Visit the browser on http://localhost:8000 to access your application.




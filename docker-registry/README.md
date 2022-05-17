# Docker Registry
Docker Registry is an application that manages storing and delivering Docker container images. Registries centralize container images and reduce build times for developers. Docker images guarantee the same runtime environment through virtualization, but building an image can involve a significant time investment. For example, rather than installing dependencies and packages separately to use Docker, developers can download a compressed image from a registry that contains all of the necessary components. 

##  Installing and Configuring the Docker Registry
store the configuration in a directory called docker-registry on the main server. Create it by running:

```
mkdir ~/docker-registry
```
Navigate to it:

```
cd ~/docker-registry
```
Then, create a subdirectory called data, where your registry will store its images:

```
mkdir data
```
Create and open a file called docker-compose.yml by running:

```
nano docker-compose.yml
```
Add the following lines, which define a basic instance of a Docker Registry:

```
version: '3'

services:
  registry:
    image: registry:2
    ports:
    - "5000:5000"
    environment:
      REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY: /data
    volumes:
      - ./data:/data
```

First, you name the first service registry, and set its image to registry, version 2. Then, under ports, you map the port 5000 on the host to the port 5000 of the container. This allows you to send a request to port 5000 on the server, and have the request forwarded to the registry.
Save and close the file.

***

## Setting Up Nginx Port Forwarding
As part of the prerequisites, you’ve enabled HTTPS at your domain. To expose your secured Docker Registry there, you’ll only need to configure Nginx to forward traffic from your domain to the registry container.

```
sudo nano /etc/nginx/sites-available/your_domain
```

need to forward traffic to port 5000, where your registry will be listening for traffic:

```
...
location / {
    # Do not allow connections from docker 1.5 and earlier
    # docker pre-1.6.0 did not properly set the user agent on ping, catch "Go *" user agents
    if ($http_user_agent ~ "^(docker\/1\.(3|4|5(?!\.[0-9]-dev))|Go ).*$" ) {
      return 404;
    }

    proxy_pass                          http://localhost:5000;
    proxy_set_header  Host              $http_host;   # required for docker client's sake
    proxy_set_header  X-Real-IP         $remote_addr; # pass on real client's IP
    proxy_set_header  X-Forwarded-For   $proxy_add_x_forwarded_for;
    proxy_set_header  X-Forwarded-Proto $scheme;
    proxy_read_timeout                  900;
}
...
```
Save and close the file when you’re done. Apply the changes by restarting Nginx:

```
sudo systemctl restart nginx
```
To confirm that Nginx is properly forwarding traffic to your registry container on port 5000, run it:

```
docker-compose up
```

***

## Setting Up Authentication
 can obtain the htpasswd utility by installing the apache2-utils package. Do so by running:
 
 ```
 sudo apt install apache2-utils -y
 ```
 store the authentication file with credentials under ~/docker-registry/auth. Create it by running:
 
 ```
 mkdir ~/docker-registry/auth
 ```
 Navigate to it:
 
 ```
 cd ~/docker-registry/auth
 ```
 
 Create the first user, replacing username with the username you want to use. The -B flag orders the use of the bcrypt algorithm, which Docker requires

```
htpasswd -Bc registry.password username
nano ~/docker-registry/docker-compose.yml
```
Add the highlighted lines:

```
version: '3'

services:
  registry:
    image: registry:2
    ports:
    - "5000:5000"
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/registry.password
      REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY: /data
    volumes:
      - ./auth:/auth
      - ./data:/data
 ```
 
 



# NGINX Exercise
Deploying an application behind an NGINX reverse proxy that has a front end and backend service.

## Prerequisites
- 3 VMs on the same network/subnet with the host names as follows:
  - nginx
  - web-app
  - api
- The nginx VM will need a public IP address and have port 80 accessible for incoming traffic over the internet.

## Configuration
1. On the `api` and `web-app` VMs, run each relative `./setup.bash` to configure those VMs.
2. On the `nginx` VM, run `./setup.bash` to configure the NGINX server.

# Deploying Raspberry Pi cluster with Docker Swarm

To achieve this tutorial, you will need at least two Raspberry Pi , their power supplies , as well as micro-SD card(8GB is sufficient).



### Step 1 - Install Docker on Raspberry Pi
fisrt, Connect Pi in SSH, then execute the following command:

```
$ curl -sSL https://get.docker.com | sh
```

### Step 2 - Setting up the Raspberry Pi cluster with Docker Swarm
Initializing the cluster

First, we started with initializing the cluster. For this we executed the command docker swarm init on the Raspberry Pi Manager.
After the command is issued, the terminal will send you a note to add the staff to the cluster.

```
$sudo docker swarm init
```
As you can see, Docker Swarm just initialized. To add your Raspberry Pi to the Docker cluster, we only need to connect to the second Pi (raspWorker01) in SSH and paste the command to us, here docker swarm join -token SWMTKN-1-0fomfa1ogeibc67p3fdxn4ea17g8jsvbtip52qptky3h7w5th4-8efjokb38uhtdqgvg3df874l 192.168. 1.100: 2377

```
$sudo docker swarm join --token SWMTKN-1-0fomfa1ogeibc67p3fdxn4ea17g8jsvbtip52qptky3h7w5th4-8efjokb38uhtdqgvg3idf874l 192.168.1.100:2377
```
Warning, the mark given by the manager will never be the same. Please copy the command given by Raspberry Manager.
After confirming the worker's order, the terminal will inform you of the success of the addition.

```
This node joined a swarm as a worker.
```


### Step 3 - Check the status of the cluster
You can use the docker node ls command at any time to check the status of the cluster and run this command on the Manager machine.
```sh
$ sudo docker node ls
```

# Reference
This tutorial is followed from https://howtoraspberrypi.com/how-to-raspberry-pi-cluster-docker-swarm/

# Classification of different periods of time based on the Measurements of electric power consumption using REST service and Docker packaged service

>Lin, Qingyun

# keywords
hid-sp18-515 classification REST


# Abstract
This dataset is about a sampling rate of nearly 4 years to measure the power consumption of a household.
We want to classify this dataset into four groups to see if the electric company can give some advises or discount to consumers.
Here, we use the dataset file household_power_consumption.txt to do this machine learning classification. The result will be displayed in REST service, and the whole project will be run in docker service.

# Introduction
What is docker?
Docker is a computer program that performs operating system level virtualization, also known as containerization. It was developed by Docker, Inc. Docker is primarily developed for Linux. It uses the Linux kernel resource isolation features (such as cgroups and kernel namespaces) and support for federated file systems (such as OverlayFS, etc.) to allow independent "containers" to run in a single Linux instance, avoiding startup. And maintain the overhead of the virtual machine (VM). The Linux kernel's support for namespaces usually isolates the application's view of the operating environment, including the process tree, network, user ID, and mounted file systems, while the kernel's cgroups provide memory and CPU resource limits. Since version 0.9, in addition to using the abstracted virtualization interface through libvirt, LXC, and systemd-nspawn, Docker also uses the libcontainer library as its own method to directly use the virtualization tools provided by the Linux kernel.[1]
Therefore, project running in docker file can be apply to other environment easly.
REST is an architectural style that defines a set of constraints and attributes based on HTTP. A REST-conformant Web service or RESTful Web service provides interoperability between computer systems on the Internet. RESTful web services allow the requesting system to access and manipulate textual representations of web resources by using a uniform and predefined set of stateless operations.[2]
Therefore, deploying the project both in docker and REST, helps the project easy to transfer and the result of the project easy to be accessed.
And electric consuming problem is a heated issue both for the goverments and consumers. Therefore, get more understanding of the features of electric measurement is useful for the environment.
To sum up, this project is meaningful. 

# Scope of work
* Download the necessary data set household_power_consumption.txt from https://archive.ics.uci.edu/ml/datasets.html
* Clean the data to be complete to train.
* Analyze the data, and generate a suitable classification.
* Generate suitable graph to discribe the classification.
* Draw conclusion of the project.

# Technology Stack
* Python will be used to analyze and generate graph
* The result will be displayed in REST
* The project will be deployed in docker
* Certain machine learning algorithm will be applied 

# References
[1] https://en.wikipedia.org/wiki/Docker_(software)
[2] https://en.wikipedia.org/wiki/Representational_state_transfer

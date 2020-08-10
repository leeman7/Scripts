# Utility Scripts

These scripts are a collection of utility and network tools variously used throughout my Linux usage. These scripts range from DNS poison attacks to basic network scanning. The vast majority of these are meant to work out of the box on any Linux system with BASH and Python 2.7 installed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to use the scripts on a live system.

### Prerequisites

To use these scripts please ensure you have BASH and Python 2.7 installed.

```
# refreshing the repositories
sudo apt-get update
sudo apt-get install libreadline-dev
sudo apt-get install libsqlite3-dev
sudo apt-get install libbz2-dev
sudo apt-get install libssl-dev
# you can skip the following line if you not
# want to update all your software
sudo apt upgrade
# installing python 2.7 and pip for it
sudo apt install python2.7 python-pip
```

### Installing

A step by step series of examples that tell you how to get a development env running

Git:
```
git clone https://github.com/leeman7/Scripts.git
```

Makefile:
Refer to the makefile for some of the programs/scripts.

Making files executable:
```
chmod +x netcat.py
```

### Usage

Using the scripts may or may not be intuitive upon first examination. Some require parameters to be passed to them, typically an IP address in most cases. Some will provide acceptable commands to pass to the scripts.

```
./netcat.py 8.8.8.8
```

## Deployment

Deploying these scripts will entail making the script executable as well as invoking the script correctly. A script in most cases on Linux can be invoked using the following method:

```
./netcat.py <args>
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

For details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Lee Nardo** - *Initial work* - [Leeman7](https://github.com/leeman7)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

None.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


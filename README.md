# ETL Project (template)
[![deploy to heroku](https://img.shields.io/badge/Deploy%20to-heroku-7056bf.svg)](https://heroku.com/deploy)

Batch data processing (template) with pyinvoke and heroku

## Settings
key|value schema|description
-|-|-
PORT|<int:80>|TCP Port to listen on
ENV|<str:"Production"|"Development">|Flask environment

## Installation

Installation is done by clicking the 'deploy to heroku' shield at the top of
this Readme.

For other environments see below:

### Building from scratch

#### Dependancies

* docker, docker-machine
* [pack](https://buildpacks.io/docs/tools/pack)

#### Steps

1. if needed create a docker vm for builds and tests: `docker-machine create runner && eval $(docker-machine env runner)`
2. For easy of maintence we use cloud native buildpacks: `pack build $(whoami)/$(basename $(pwd)) --default-process worker`
3. Release: `docker login && docker push $(whoami)/$(basename $(pwd))`
4. Clean up (as needed): `docker-machine rm -y -f runner`

#### Deployment

* ansible: `ansible -i localhost, -c local -m docker\_container -a "image=denzuko/etl:latest state=started interactive=yes auto_remove=yes tty=yes"`
* docker-engine: `docker run --rm -ti $(whoami)/$(basename $(pwd))`
* docker-swarm: `docker stack deploy -c docker-compose $(basename $(pwd))`
* kubernetes: `helm install $(basename $(pwd)) ./helm/


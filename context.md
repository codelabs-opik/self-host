Local deployment

Copy page

Describes how to run Opik locally using Docker Compose
Important: If you’re using or looking to use Opik or Comet enterprise version please reach out to Sales@comet.com to gain access to the correct deployment documentation.

To run Opik locally we recommend using Docker Compose. It’s easy to setup and allows you to get started in a couple of minutes but is not meant for production deployments. If you would like to run Opik in a production environment, we recommend using our Kubernetes Helm chart.

Before running the installation, make sure you have Docker and Docker Compose installed:

Docker
Docker Compose
If you are using Mac or Windows, both docker and docker compose are included in the Docker Desktop installation.

Installation
To install Opik, you will need to clone the Opik repository and run the following commands:

Linux / Mac
Windows
# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git
# Navigate to the opik folder
cd opik
# Start the Opik platform
./opik.sh


Opik will now be available at http://localhost:5173

In order to use the Opik Python SDK with your local Opik instance, you will need to run:

pip install opik
opik configure --use_local


or in python:

import opik
opik.configure(use_local=True)


This will create a ~/.opik.config file that will store the URL of your local Opik instance.

All the data logged to the Opik platform will be stored in the ~/opik directory, which means that you can start and stop the Opik platform without losing any data.

Installation script options
The opik.sh and opik.ps1 scripts support the following options:

Option	Description
--infra	Start only the infrastructure services (MySQL, Redis, ClickHouse, ZooKeeper, MinIO etc.)
--backend	Start the infrastructure and backend services
--guardrails	Enable guardrails, can be combined with the other start options
--build	Build the containers from source before starting
--verify	Check that all containers are healthy
--stop	Stop all containers
--clean	Stop all containers and remove all Opik data volumes
--help	Show all available options
The --clean option removes all Opik data volumes. All data stored in the Opik platform will be lost and cannot be recovered.

Run ./opik.sh --help (or powershell -ExecutionPolicy ByPass -c ".\opik.ps1 --help" on Windows) to see the full list of options.

Stopping the Opik platform
You can stop the Opik server by running the following commands:

Linux / Mac
Windows
# Ensure you are running this command for the root of the Opik repository you cloned
./opik.sh --stop


Note: You can safely stop the Opik platform without losing any data.

Upgrading and restarting the Opik platform
To upgrade or restart the Opik platform, you can simply run the opik script again:

Linux / Mac
Windows
# Ensure you are running this command for the root of the Opik repository you cloned
./opik.sh


Since the Docker Compose deployment is using mounted volumes, your data will not be lost when you upgrade Opik. You can also safely start and stop the Opik platform without losing any data.

Advanced configuration - Docker compose
Using Docker Compose directly instead of using the opik.sh or opik.ps1 scripts provides you with some additional options.

Starting Opik with Docker Compose
Instead of using the opik.sh or opik.ps1 scripts, you can also run the docker compose command directly with service profiles:

# Navigate to the opik/deployment/docker-compose directory
cd opik/deployment/docker-compose
# Start full Opik platform (equivalent to ./opik.sh)
docker compose --profile opik up --detach
# Start only infrastructure services (equivalent to ./opik.sh --infra)
docker compose up --detach
# Start infrastructure + backend services (equivalent to ./opik.sh --backend)
docker compose --profile backend up --detach


Uninstalling Opik
To remove Opik, you can use the script or remove containers and volumes manually:

# Using the script (recommended)
./opik.sh --stop
# Or manually remove containers and volumes
cd deployment/docker-compose
docker compose --profile opik down --volumes


Removing the volumes will delete all the data stored in the Opik platform and cannot be recovered. We do not recommend this option unless you are sure that you will not need any of the data stored in the Opik platform.

Running a specific version of Opik
You can run a specific version of Opik by setting the OPIK_VERSION environment variable:

OPIK_VERSION=latest
./opik.sh


Building the Opik platform from source
You can also build the Opik platform from source using the provided script:

# Clone the Opik repository
git clone https://github.com/comet-ml/opik.git
# Navigate to the opik directory
cd opik
# Build the Opik platform from source
./opik.sh --build
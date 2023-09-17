## Getting Started


Getting the source code and initializing the submodules:

		git clone git@github.com:amlstation/tensorflow-object-detection.git
		git submodule update --init --recursive --progress


## Building The Container

1. [Building on AMD64 (no GPU)](#AMD64-CPU)
2. [Building on AMD64 (nVIDIA GPU)](#AMD64-nVIDIA-GPU)

<h3 id="AMD64-CPU">AMD64 CPUs (Intel chips)</h3>

You should use the default `docker-compose.yml` and `Dockerfile`.

Creating the necessary services:

		docker compose up -d --build --force-recreate

You may skip the `--build` and `--force-recreate` flags if there are no changes to your container since you last built it.

<h3 id="AMD64-nVIDIA-GPU">AMD64 with nVIDIA GPU</h3>

You should extend the default `docker-compose.yml` file with `docker-compose.gpu.yml`, which uses the nvidia gpu as a resource and reads from `Dockerfile.gpu`.

		docker compose -f docker-compose.yml -f docker-compose.gpu.yml up -d --build --force-recreate

You may skip the `--build` and `--force-recreate` flags depending if there are no changes to your container since you last built it.


## Running The Container and the Jupyter Notebook

		docker exec -it tf_object_detection /bin/bash
		jupyter lab --allow-root --ip 0.0.0.0
		## From this ponit forward you can follow the instruction in TensorFlow-Object-Detection.ipynb

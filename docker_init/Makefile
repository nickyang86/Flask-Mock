image:
	docker build -f Dockerfile \
	--cache-from matthewfeickert/docker-python3-ubuntu:latest \
	--build-arg PYTHON_VERSION_TAG=3.7.3 \
	--build-arg LINK_PYTHON_TO_PYTHON3=1 \
	-t python3-ubuntu:3.7.3 \
	--compress .
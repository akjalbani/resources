import docker

# Create a Docker client
client = docker.from_env()

# Define the Dockerfile contents
dockerfile = '''
FROM openjdk:8-jdk-alpine

RUN apk update && apk add --no-cache curl \
    && apk add --no-cache eclipse

WORKDIR /app
COPY . /app

CMD ["eclipse"]
''`

# Build an image from the Dockerfile
image, build_logs = client.images.build(
    fileobj=dockerfile,
    tag='java-lab-eclipse:latest',
    rm=True
)

# Run a container from the image
container = client.containers.run(
    'java-lab-eclipse:latest',
    name='java-lab-eclipse',
    ports={'8080/tcp': 8080},
    volumes={'/app': {'bind': '/app', 'mode': 'rw'}}
)

# Print the container ID
print(container.id)

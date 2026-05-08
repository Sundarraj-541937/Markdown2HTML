# Docker Beginner Guide

Docker helps developers package applications and run them consistently across environments.

## What is Docker?

Docker is a containerization platform that allows applications to run in isolated environments called containers.

## Why Use Docker?

- Consistent environments
- Easy deployment
- Lightweight compared to virtual machines
- Simplifies dependency management

## Install Docker

### Ubuntu

```bash
sudo apt update
sudo apt install docker.io
```

### Verify Installation

```bash
docker --version
```

## Basic Docker Commands

### Pull an Image

```bash
docker pull nginx
```

### Run a Container

```bash
docker run -d -p 8080:80 nginx
```

### List Running Containers

```bash
docker ps
```

### Stop a Container

```bash
docker stop <container-id>
```

## Example Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

## Benefits of Containers

| Feature | Benefit |
|--------|---------|
| Isolation | Prevents dependency conflicts |
| Portability | Runs anywhere |
| Fast Startup | Lightweight execution |

## Conclusion

Docker is an essential tool for modern DevOps development.
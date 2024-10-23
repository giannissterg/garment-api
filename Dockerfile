# syntax=docker/dockerfile:1.9

# Use the official Python 3.12 image as the base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /server

# Install system dependencies and uv in one RUN command
RUN apt-get update && apt-get install -y \
    build-essential \
    libuv1-dev \
    && rm -rf /var/lib/apt/lists/* 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set environment variables for uv
ENV UV_COMPILE_BYTECODE=1 \
    PATH="/server/.venv/bin:$PATH"

# Copy only the uv.lock file first to utilize Docker's cache
COPY ./uv.lock ./
COPY ./pyproject.toml ./

# Initialize the virtual environment and sync dependencies
RUN uv sync --frozen

COPY ./src ./src
COPY ./.env ./.env

RUN uv sync --frozen

# Run the application using uv (adjust based on your application entry point)
CMD ["uv", "run", "src/router.py"]

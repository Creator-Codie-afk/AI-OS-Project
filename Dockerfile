# Use the official Ubuntu base image
FROM ubuntu:latest

# Update package index and install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    make \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the kernel source code into the container
COPY Kernel/ /app/Kernel/

# Compile the kernel
RUN gcc /app/Kernel/main.c -o /app/Kernel/kernel

# Set the entrypoint to run the kernel
ENTRYPOINT ["/app/Kernel/kernel"]

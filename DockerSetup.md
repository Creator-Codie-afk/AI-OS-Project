# Docker Setup Instructions for AI-OS

## Introduction
This document provides instructions for setting up Docker on Ubuntu using the apt repository. Docker is essential for creating a containerized development environment for the AI-OS project.

## Prerequisites
- A system running Ubuntu.
- Sudo privileges for installing packages.

## Steps

### 1. Update the package index
```sh
sudo apt-get update
```

### 2. Install packages to allow apt to use a repository over HTTPS
```sh
sudo apt-get install ca-certificates curl
```

### 3. Add Docker's official GPG key
```sh
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### 4. Set up the Docker apt repository
```sh
echo \
  "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 5. Install Docker Engine
```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Conclusion
Follow these steps to set up Docker on your Ubuntu system. Once Docker is installed, you can use it to create and manage containers for the AI-OS project.

# Fetch ubuntu image
FROM ubuntu:22.04

# Install build tools and other dependencies
RUN apt update && \
    apt install -y wget build-essential autoconf automake libtool

# Download CppUTest
RUN mkdir -p /project/tools/ && \
    cd /project/ && \
    wget https://github.com/cpputest/cpputest/releases/download/v4.0/cpputest-4.0.tar.gz
y
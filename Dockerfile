# Fetch ubuntu image
# FROM ubuntu:22.04
# Use the base image
FROM cpp_test_base



# Copy project into image
RUN mkdir /project -p
COPY src /project/src
COPY tests /project/tests
COPY Makefile /project/Makefile

# Download and build CppUTest
RUN cd /project/ && \
    if [ -f "cpputest-4.0.tar.gz" ]; then \
        tar xf cpputest-4.0.tar.gz && \
        mv cpputest-4.0/ tools/cpputest/ && \
        cd tools/cpputest/ && \
        autoreconf -i && \
        ./configure && \
        make; \
    else \
        echo "CppUTest tarball not found."; \
        exit 1; \
    fi

# Execute script
ENTRYPOINT ["make", "test", "-C", "/project/"]
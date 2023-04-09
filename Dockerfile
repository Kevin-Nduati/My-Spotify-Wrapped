# Use the official Ubuntu 20.04 image as the base image
FROM ubuntu:20.04

# Install Apache 2.2.0 and other necessary packages
RUN apt-get update && apt-get install -y apache2=2.2.0-9ubuntu1.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy your website files to the appropriate directory
COPY ./website/ /var/www/html/

# Expose port 80 to the outside world
EXPOSE 80

# Start Apache when the container launches
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

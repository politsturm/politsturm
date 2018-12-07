FROM mysql:8.0.13

RUN apt-get update \
 && apt-get install --no-install-recommends -y tzdata \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

# Copy starting scripts file
COPY copy_conf.sh /root/copy_conf.sh

# Run necessary services
CMD ["/bin/bash", "/root/copy_conf.sh"]
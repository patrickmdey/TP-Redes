FROM --platform=linux/amd64 mailserver/docker-mailserver

# Install necessary dependencies
RUN apt-get update && apt-get install -y curl
RUN apt-get install -y git

# Download and install Go
RUN curl -O https://dl.google.com/go/go1.17.linux-amd64.tar.gz
RUN tar -xvf go1.17.linux-amd64.tar.gz
RUN mv go /usr/local

# Set Go environment variables
ENV GOPATH=/go
ENV PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

# Set the working directory inside the container
WORKDIR /app

RUN git clone https://github.com/cherti/mailexporter.git
WORKDIR /app/mailexporter

RUN go build

# Expose the necessary port (adjust if needed)
EXPOSE 8025

# Set the command to run the mailexporter binary
CMD ["./mailexporter"]

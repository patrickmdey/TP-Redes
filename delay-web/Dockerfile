FROM node

# Create app directory
COPY ./app /usr/src/app

# Install app dependencies
WORKDIR /usr/src/app
RUN npm install

# Expose port
EXPOSE 3002

# Start app
CMD [ "npm", "start" ]



# Use Node.js official image as the base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

COPY package.json ./

# Install dependencies using Yarn
RUN yarn install

# Copy the rest of your application
COPY . .

# Expose the port for the React app
EXPOSE 3000

# Command to run the React application
CMD ["yarn", "start"]
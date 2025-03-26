# Use Node.js official image as the base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app


# Install dependencies using Yarn
RUN yarn install

# Copy the rest of your application
COPY . .

# Expose the port (adjust as needed)
EXPOSE 3000

# Command to run the application (adjust as needed)
CMD ["yarn", "start"]

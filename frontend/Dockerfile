FROM docker.arvancloud.ir/node:25-alpine as builder 

WORKDIR /app

# Set npm registry BEFORE installing
RUN npm config set registry "https://archive.ito.gov.ir/npm/"

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Install Python for build scripts if needed
RUN apk add --no-cache python3

# Copy source code
COPY . .

# Build the application
RUN npm run build:prod

# Production stage with Nginx
FROM docker.arvancloud.ir/nginx:alpine

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built files from builder
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

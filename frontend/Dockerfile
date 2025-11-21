FROM docker.arvancloud.ir/node:20-alpine as builder 

WORKDIR /app

# Copy package files first
COPY package*.json ./

# Install dependencies with fallback registry
# Try Iranian registry first, if fails use official npm registry
RUN npm config set registry "https://archive.ito.gov.ir/npm/" && \
    npm install || ( \
        echo "Iranian registry failed, trying official npm registry..." && \
        npm config set registry "https://registry.npmjs.org/" && \
        npm install \
    )

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

# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Accept build arguments
ARG VITE_ZONOS_API_URL
ARG VITE_MEMO_API_URL

# Set environment variables for build
ENV VITE_ZONOS_API_URL=$VITE_ZONOS_API_URL
ENV VITE_MEMO_API_URL=$VITE_MEMO_API_URL

# Build the application
RUN npm run build

# Production stage
FROM docker.io/nginx:alpine

# Copy built files from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
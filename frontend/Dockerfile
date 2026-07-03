###################### Build stage ######################
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm install --legacy-peer-deps

COPY . .

RUN npm run build:prod


###################### Runtime stage ######################
FROM nginx:alpine

RUN apk add --no-cache openssl

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY start-nginx.sh /usr/local/bin/start-nginx.sh

COPY --from=builder /app/dist /usr/share/nginx/html
COPY public/Content /usr/share/nginx/html/Content

RUN mkdir -p /usr/share/nginx/html/assets /usr/share/nginx/html/img
RUN chmod +x /usr/local/bin/start-nginx.sh

EXPOSE 80
EXPOSE 443

CMD ["/usr/local/bin/start-nginx.sh"]

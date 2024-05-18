FROM nginx:latest

# Del default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy nginx conf to image
COPY nginx.conf /etc/nginx/conf.d
COPY proxy_params /etc/nginx
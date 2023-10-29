server {
    listen 80;
    listen [::]:80;

    server_name lineage2hiro.com www.lineage2hiro.com;
    server_tokens off;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://lineage2hiro.com$request_uri;
    }
}

server {
    listen 443 default_server ssl http2;
    listen [::]:443 ssl http2;

    server_name lineage2hiro.com;

    ssl_certificate /etc/nginx/ssl/live/lineage2hiro.com/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/live/lineage2hiro.com/privkey.pem;
    
    location / {
    	proxy_pass http://web:8000;
    }
}

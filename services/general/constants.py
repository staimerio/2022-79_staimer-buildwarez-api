NGINX_TEMPLATE = """
server {
    listen      $HOST:$PORT;
    server_name $DOMAIN www.$DOMAIN;
    root        /home/admin/web/$DOMAIN/public_html;
    index       index.php index.html index.htm;
    access_log  /var/log/nginx/domains/$DOMAIN.log combined;
    access_log  /var/log/nginx/domains/$DOMAIN.bytes bytes;
    error_log   /var/log/nginx/domains/$DOMAIN.error.log error;

    location = /favicon.ico {
        log_not_found off;
        access_log off;
    }

    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }
    
    set $cache_uri $request_uri;

    if ($request_method = POST) {
        set $cache_uri 'null cache';
    }

    if ($query_string != "") {
        set $cache_uri 'null cache';
    }   

    if ($request_uri ~* "(/wp-admin/|/xmlrpc.php|/wp-(app|cron|login|register|mail).php
                        |wp-.*.php|/feed/|index.php|wp-comments-popup.php
                        |wp-links-opml.php|wp-locations.php |sitemap(_index)?.xml
                        |[a-z0-9_-]+-sitemap([0-9]+)?.xml)") {
        set $cache_uri 'null cache';
    }  

    if ($http_cookie ~* "comment_author|wordpress_[a-f0-9]+
                        |wp-postpass|wordpress_logged_in|woocommerce_cart_hash|woocommerce_items_in_cart|wp_woocommerce_session_") {
        set $cache_uri 'null cache';
    }

    location / {
        try_files /wp-content/cache/supercache/$http_host/$cache_uri/index.html $uri $uri/ /index.php?$args;

        location ~* ^.+\.(jpeg|jpg|png|gif|bmp|ico|svg|css|js)$ {
            expires     max;
        }

        location ~ [^/]\.php(/|$) {
            fastcgi_param HTTPS 1;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            if (!-f $document_root$fastcgi_script_name) {
                return  404;
            }

            fastcgi_pass    127.0.0.1:9018;
            fastcgi_index   index.php;
            include         /etc/nginx/fastcgi_params;
        }
    }

    error_page  403 /error/404.html;
    error_page  404 /error/404.html;
    error_page  500 502 503 504 /error/50x.html;

    location /error/ {
        alias   /home/admin/web/$DOMAIN/document_errors/;
    }

    location ~* "/\.(htaccess|htpasswd)$" {
        deny    all;
        return  404;
    }

    location /vstats/ {
        alias   /home/admin/web/$DOMAIN/stats/;
        include /home/admin/conf/web/$DOMAIN.auth*;
    }

    include     /etc/nginx/conf.d/phpmyadmin.inc*;
    include     /etc/nginx/conf.d/phppgadmin.inc*;
    include     /etc/nginx/conf.d/webmail.inc*;

    include     /home/admin/conf/web/nginx.$DOMAIN.conf*;
}
"""

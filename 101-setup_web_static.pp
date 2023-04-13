#!/usr/bin/pup
# puppet code to setup my remote servers for deployment
# create /data/web_static/released/ and /data/web_static/shared/ directories

file { '/data/web_static/released':
  ensure => 'directory',
  recurse => true,
  force => true,
}

file { '/data/web_static/shared':
  ensure => 'directory',
  recurse => true,
  force => true,
}

# write "hola mate" to /data/web_static/released/test/index.html

file { '/data/web_static/released/test/index.html':
  ensure => 'present',
  recurse => true,
  force => true,
  content => 'hola mate'
}

# create a link ln -sf /data/web_static/releases/test/ /data/web_static/current

file { '/data/web_static/current':
  link => true,
  target => '/data/web_static/releases/test/'
}
# exec chown -R ubuntu:ubuntu /data/

file { '/data/':
  ensure => 'directory',
  owner => 'ubuntu',
  group => 'ubuntu',
  recurse => true,
}

# file_line location /hbnb { /data/web_static/current; }

file_line { hhhhh:
  path => '/etc/nginx/sites-available/default'
  ensure => 'present',
  after => 'server_name _;',
  line => 'location /hbnn_static { /data/web_static/current; }'
}

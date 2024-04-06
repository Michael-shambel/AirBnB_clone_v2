# 101-setup_web_static.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}


file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Change ownership
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Modify Nginx configuration
file_line { 'nginx_hbnb_static_location':
  path    => '/etc/nginx/sites-available/default',
  line    => '  location /hbnb_static/ {',
  match   => '^.*root.*;$',
  after   => '^.*root.*;$',
  notify  => Service['nginx'],
}

file_line { 'nginx_alias_config':
  path    => '/etc/nginx/sites-available/default',
  line    => '        alias /data/web_static/current/;',
  match   => '^\s*location /hbnb_static/ {$',
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
}


# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create web_static directory structure
file { '/data':
  ensure => directory,
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
  ensure  => present,
  content => '<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
  </html>',
}

# Create symbolic link to current release
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}


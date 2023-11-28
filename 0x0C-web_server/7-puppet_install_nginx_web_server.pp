# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

# Check 404 file
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Check index file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
package { 'nginx':
  ensure => installed,
}

# Web server directory
file { 'Website directory':
  ensure  => directory,
  path    => '/var/www/html',
  require => Package['nginx'],
}

# Ensure index file is present and contains 'Hello World!'
file { 'Website index file':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}

# Ensure 404 file is present and contains 'Ceci n'est pas une page'
file { 'Website 404 file':
  ensure  => present,
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page",
}

# Ensure nginx redirects to a custom page when accessing /redirect_me
file_line { 'nginx redirect':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure nginx is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}

# Puppet script ot increase nginx 

$nginx_ulimit = 4096

package { 'nginx':
  ensure => installed,
}

file { '/etc/default/nginx':
  ensure  => present,
  content => 'ULIMIT="-n 65535"',
  notify  => Service['nginx']
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

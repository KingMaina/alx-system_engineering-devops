# Kills a process named killmenow

exec { 'Kills a process named killmenow':
  command => 'pkill killmenow',
  path    => '/bin',
}

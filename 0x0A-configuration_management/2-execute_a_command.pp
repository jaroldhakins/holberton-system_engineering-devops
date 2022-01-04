# Executing this script, kill a process killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}

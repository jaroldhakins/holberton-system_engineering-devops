# Fix the issue, (why is returning Internal server error 500) 
exec { 'fix_settings_error':
    command => 'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}

# configurate some things in the cofig file

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/config':
        path    => '/bin/'
}

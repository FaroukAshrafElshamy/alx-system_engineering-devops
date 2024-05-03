# Create a manifest that kills a process named killmenow

exec { 'pkill killmenow':
    command => 'pkill -x killmenow',
    path    => 'usr/bin/'
}
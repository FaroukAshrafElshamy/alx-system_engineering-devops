# Use pip3 to install flask with a specific version

package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
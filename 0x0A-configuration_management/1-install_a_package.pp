# Use pip3 to install flask with a specific version

# Ensure python is installed
class { 'python': }

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
# Using Puppet, install puppet-lint

package { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0'
}
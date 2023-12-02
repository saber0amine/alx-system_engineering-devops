# 1-install_a_package.pp

# Define package resource to install Flask with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify the user about the installation
notify { 'Flask installation completed':
  require => Package['Flask'],
}


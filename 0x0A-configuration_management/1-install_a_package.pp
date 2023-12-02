# 1-install_a_package.pp

# Define package resources to install Flask and Werkzeug with specific versions
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1', # Use the correct version compatible with Flask 2.1.0
  provider => 'pip3',
}

# Notify the user about the installation
notify { 'Flask installation completed':
  require => [Package['Flask'], Package['Werkzeug']],
}


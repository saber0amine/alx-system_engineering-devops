exec { "kill process test" :
  command => "/usr/bin/pkill killmenow || true" ,
  provider => "shell",
}

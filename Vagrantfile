# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "geerlingguy/ubuntu1604"

  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 80, host: 8081

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  # config.vm.synced_folder ".", "/vagrant/"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
    config.vm.provider "virtualbox" do |vb|
       # name machine
       # vb.name = "time_tracker"
       vb.memory = 512
    end 
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get -y install software-properties-common python-software-properties
      
      sudo apt-get install -y virtualbox-guest-utils
      
      # DOCKER
      curl -sSL https://get.docker.com/ | sh
      
      curl -L https://github.com/docker/machine/releases/download/v0.7.0/docker-machine-`uname -s`-`uname -m` > sudo /usr/local/bin/docker-machine
      sudo chmod +x /usr/local/bin/docker-machine
  
      set -e
      
      if [ -x /usr/local/bin/python3.5 ]; then
        echo 'Skipping Python installation since Python 3.5 is already installed.'
      else
        echo 'Install required libraries...'
        apt-get update -yq
        apt-get install -yq libreadline-dev libsqlite3-dev libssl-dev build-essential libtool
  
        echo 'Install Python 3.5...'
        cd /tmp
        wget -O- https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz | tar xz
        cd Python-3.5.1
        ./configure
        make
        make altinstall
  
        echo 'Clean up...'
        cd && rm -rf /tmp/Python-3.5.1
  
        echo 'Done!'
      fi
      
      # REDIS
      cd /home/vagrant
      wget http://download.redis.io/redis-stable.tar.gz
      tar xvzf redis-stable.tar.gz
      cd redis-stable
      make
      sudo make install
      cd utils
      sudo ./install_server.sh
          
      # POSTGRES
      sudo apt-get -y install postgresql libpq-dev
      sudo -u postgres createuser vagrant
      sudo -u postgres createdb vagrant
      sudo -u postgres createdb -O vagrant time_tracker
      sudo -u postgres psql -c "ALTER ROLE vagrant SUPERUSER"
  
      cd /vagrant
      # python libs dependencies
      sudo apt-get -y install libjpeg-dev
      sudo python3.5 -m pip install -r requirements.txt
      ln -sf time_tracker/settings/vagrant.py time_tracker/settings/local.py
  SHELL
end

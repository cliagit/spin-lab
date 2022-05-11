#!/bin/bash
cd /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/
make clean
make
sudo make install
make clean

cmd_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/sys/modules.order := {   echo /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/sys/gpib_common.ko; :; } | awk '!x[$$0]++' - > /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/sys/modules.order
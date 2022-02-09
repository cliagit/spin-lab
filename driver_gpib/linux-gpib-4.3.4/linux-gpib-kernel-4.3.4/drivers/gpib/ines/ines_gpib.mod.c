#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x4e79ba4a, "module_layout" },
	{ 0x4a899fbf, "nec7210_serial_poll_response" },
	{ 0x85bd1608, "__request_region" },
	{ 0x7c8cd159, "kmalloc_caches" },
	{ 0x40ccc6f5, "nec7210_command" },
	{ 0xe5fa6ebd, "nec7210_remote_enable" },
	{ 0xd8627e58, "nec7210_set_reg_bits" },
	{ 0x9d5a9c57, "nec7210_set_handshake_mode" },
	{ 0x78d85ade, "nec7210_serial_poll_status" },
	{ 0xb34ff1e, "nec7210_enable_eos" },
	{ 0xc29957c3, "__x86_indirect_thunk_rcx" },
	{ 0xd2c385b4, "nec7210_update_status" },
	{ 0x246dd6f, "pci_release_regions" },
	{ 0xe1e3818, "gpib_unregister_driver" },
	{ 0x4bf817a3, "nec7210_return_to_local" },
	{ 0xc40225b2, "nec7210_parallel_poll_configure" },
	{ 0x8f4c2520, "push_gpib_event" },
	{ 0xdbdf6c92, "ioport_resource" },
	{ 0x986f0922, "pci_get_subsys" },
	{ 0xd2220676, "nec7210_parallel_poll" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x6e6f4b85, "current_task" },
	{ 0xc5850110, "printk" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0x1da52834, "nec7210_interface_clear" },
	{ 0xd596bf5f, "nec7210_go_to_standby" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0xfd1f0525, "nec7210_ioport_read_byte" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0xeb99bae1, "nec7210_read_data_in" },
	{ 0x69e8458d, "nec7210_board_online" },
	{ 0xc044f019, "nec7210_ioport_write_byte" },
	{ 0x20613149, "nec7210_interrupt" },
	{ 0x3cd91623, "nec7210_take_control" },
	{ 0x5e218491, "nec7210_secondary_address" },
	{ 0x58f9f6f1, "nec7210_disable_eos" },
	{ 0x808333a4, "nec7210_write" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0x1000e51, "schedule" },
	{ 0x9a7239f3, "gpib_register_driver" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x1035c7c2, "__release_region" },
	{ 0xa3670410, "kmem_cache_alloc_trace" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xced18dfa, "nec7210_board_reset" },
	{ 0xc6f680a5, "nec7210_request_system_control" },
	{ 0xc4b0eab1, "nec7210_primary_address" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x37a0cba, "kfree" },
	{ 0x9fedddaf, "pci_request_regions" },
	{ 0xcdfd3731, "pci_get_device" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x873db1f6, "pci_dev_put" },
	{ 0x6e6c4187, "nec7210_t1_delay" },
	{ 0x9a2fa82, "nec7210_parallel_poll_response" },
	{ 0xd92da600, "pci_enable_device" },
	{ 0x4290dd9e, "nec7210_read" },
	{ 0xc1514a3b, "free_irq" },
};

MODULE_INFO(depends, "nec7210,gpib_common");

MODULE_ALIAS("pci:v000010B5d00009050sv000010B5sd00001072bc*sc*i*");
MODULE_ALIAS("pci:v000010E8d00008507sv000010E8sd00001072bc*sc*i*");
MODULE_ALIAS("pci:v000016DAd00000011sv000016DAsd00000011bc*sc*i*");
MODULE_ALIAS("pci:v00008008d00003302sv*sd*bc*sc*i*");

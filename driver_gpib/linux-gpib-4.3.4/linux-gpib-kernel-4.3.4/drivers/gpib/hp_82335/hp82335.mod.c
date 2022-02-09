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
	{ 0xdaddf74d, "tms9914_request_system_control" },
	{ 0x85bd1608, "__request_region" },
	{ 0x7c8cd159, "kmalloc_caches" },
	{ 0x77358855, "iomem_resource" },
	{ 0xbdf086a2, "tms9914_disable_eos" },
	{ 0xc0f07e19, "tms9914_online" },
	{ 0x2365c5d3, "tms9914_enable_eos" },
	{ 0xef5e34f5, "tms9914_read" },
	{ 0x5f4365f3, "tms9914_primary_address" },
	{ 0x4124bad7, "tms9914_parallel_poll_response" },
	{ 0xe1e3818, "gpib_unregister_driver" },
	{ 0xafee9c59, "tms9914_t1_delay" },
	{ 0x9da6fdee, "tms9914_parallel_poll" },
	{ 0x350d469e, "tms9914_iomem_read_byte" },
	{ 0x76aac7b0, "tms9914_parallel_poll_configure" },
	{ 0xd220f33a, "tms9914_write" },
	{ 0xb4197a0b, "tms9914_update_status" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0xc5850110, "printk" },
	{ 0x5e78e4b6, "tms9914_serial_poll_status" },
	{ 0xde80cd09, "ioremap" },
	{ 0x9fef51c3, "tms9914_board_reset" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x2f102aca, "tms9914_secondary_address" },
	{ 0xb492bf25, "tms9914_remote_enable" },
	{ 0x216467a3, "tms9914_serial_poll_response" },
	{ 0xb8ccc3a8, "tms9914_command" },
	{ 0x9a7239f3, "gpib_register_driver" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0xba5081c8, "tms9914_interface_clear" },
	{ 0xc8201e97, "tms9914_take_control" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x1035c7c2, "__release_region" },
	{ 0xa3670410, "kmem_cache_alloc_trace" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xdb6263f6, "tms9914_go_to_standby" },
	{ 0x37a0cba, "kfree" },
	{ 0xedc03953, "iounmap" },
	{ 0x58476804, "tms9914_interrupt_have_status" },
	{ 0x56d3f3ad, "tms9914_return_to_local" },
	{ 0xec119222, "tms9914_iomem_write_byte" },
	{ 0x2cc71ef9, "tms9914_line_status" },
	{ 0xc1514a3b, "free_irq" },
};

MODULE_INFO(depends, "tms9914,gpib_common");


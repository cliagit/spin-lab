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
	{ 0x27a2ca93, "param_ops_int" },
	{ 0x318d6fec, "mutex_is_locked" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x1000e51, "schedule" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0xe1e3818, "gpib_unregister_driver" },
	{ 0xb0d1656c, "gpio_free_array" },
	{ 0xe7d655e4, "gpiod_set_raw_value" },
	{ 0x9a7239f3, "gpib_register_driver" },
	{ 0x9ba2bb2b, "gpio_request_array" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0xa394b749, "gpiod_direction_input" },
	{ 0x7e6de84d, "gpiod_to_irq" },
	{ 0xa3670410, "kmem_cache_alloc_trace" },
	{ 0x7c8cd159, "kmalloc_caches" },
	{ 0x222aa7ad, "gpiod_direction_output_raw" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x5e515be6, "ktime_get_ts64" },
	{ 0x37a0cba, "kfree" },
	{ 0x9e7d6bd0, "__udelay" },
	{ 0x54185222, "gpiod_get_raw_value" },
	{ 0xfc2a03c, "gpio_to_desc" },
	{ 0xc5850110, "printk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "gpib_common");


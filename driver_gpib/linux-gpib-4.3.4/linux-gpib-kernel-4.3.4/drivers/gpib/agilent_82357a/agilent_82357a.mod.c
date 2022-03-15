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
	{ 0xcea15aad, "module_layout" },
	{ 0xcf40ddb1, "usb_deregister" },
	{ 0xe1e3818, "gpib_unregister_driver" },
	{ 0x9a7239f3, "gpib_register_driver" },
	{ 0x25bcba4c, "usb_register_driver" },
	{ 0xc6f46339, "init_timer_key" },
	{  0xf16aa, "_dev_info" },
	{ 0xe2d5255a, "strcmp" },
	{ 0x4af4ac6d, "gpib_match_device_path" },
	{ 0x977f511b, "__mutex_init" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0x6e6f4b85, "current_task" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x1000e51, "schedule" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0xf21017d9, "mutex_trylock" },
	{ 0x37befc70, "jiffies_to_msecs" },
	{ 0x69acdf38, "memcpy" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xd793188f, "usb_control_msg" },
	{ 0xc38c83b8, "mod_timer" },
	{ 0x15ba50a6, "jiffies" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0x6138a907, "usb_free_urb" },
	{ 0x97934ecf, "del_timer_sync" },
	{ 0x6bd0e573, "down_interruptible" },
	{ 0xf583b885, "usb_alloc_urb" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0xd31af05d, "usb_submit_urb" },
	{ 0x1163987c, "usb_kill_urb" },
	{ 0x2ab7989d, "mutex_lock" },
	{ 0x37a0cba, "kfree" },
	{ 0x656e4a6e, "snprintf" },
	{ 0x409bcb62, "mutex_unlock" },
	{ 0x5eadc959, "usb_put_dev" },
	{ 0xa3670410, "kmem_cache_alloc_trace" },
	{ 0xe04b26ea, "kmalloc_caches" },
	{ 0xe3e1cd69, "usb_get_dev" },
	{ 0xb5136dc7, "mutex_lock_interruptible" },
	{ 0xcf2a6966, "up" },
	{ 0xc5850110, "printk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "usbcore,gpib_common");

MODULE_ALIAS("usb:v0957p0107d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0957p0718d*dc*dsc*dp*ic*isc*ip*in*");

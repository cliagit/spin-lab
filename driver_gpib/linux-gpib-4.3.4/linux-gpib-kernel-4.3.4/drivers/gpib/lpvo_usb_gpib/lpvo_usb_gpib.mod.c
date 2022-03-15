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
	{ 0x27a2ca93, "param_ops_int" },
	{ 0x461fb2a4, "noop_llseek" },
	{ 0xcf40ddb1, "usb_deregister" },
	{ 0x25bcba4c, "usb_register_driver" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x4af4ac6d, "gpib_match_device_path" },
	{ 0x6e6f4b85, "current_task" },
	{ 0x754d539c, "strlen" },
	{ 0x263ed23b, "__x86_indirect_thunk_r12" },
	{ 0xf9a482f9, "msleep" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x709f62ed, "usb_unanchor_urb" },
	{ 0xd75ff0df, "usb_anchor_urb" },
	{ 0x19e7ae0c, "usb_alloc_coherent" },
	{ 0x6bd0e573, "down_interruptible" },
	{ 0x2ea2c95c, "__x86_indirect_thunk_rax" },
	{ 0x593c1bac, "__x86_indirect_thunk_rbx" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0xa916b694, "strnlen" },
	{ 0x656e4a6e, "snprintf" },
	{ 0xfd1e1c8f, "get_current_tty" },
	{ 0x9ec6ca96, "ktime_get_real_ts64" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x69acdf38, "memcpy" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x1000e51, "schedule" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0xa1c76e0a, "_cond_resched" },
	{ 0xd31af05d, "usb_submit_urb" },
	{ 0xfb7799f, "pv_ops" },
	{ 0x8427cc7b, "_raw_spin_lock_irq" },
	{ 0x9a7239f3, "gpib_register_driver" },
	{ 0xb5136dc7, "mutex_lock_interruptible" },
	{ 0xd793188f, "usb_control_msg" },
	{ 0x9819224, "usb_register_dev" },
	{ 0xa35c08e2, "kobject_get_path" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0xf583b885, "usb_alloc_urb" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0x93c7edeb, "usb_find_common_endpoints" },
	{ 0xe3e1cd69, "usb_get_dev" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0xa3670410, "kmem_cache_alloc_trace" },
	{ 0xe04b26ea, "kmalloc_caches" },
	{ 0x977f511b, "__mutex_init" },
	{ 0xe1e3818, "gpib_unregister_driver" },
	{  0xf16aa, "_dev_info" },
	{ 0x28edca2b, "usb_deregister_dev" },
	{ 0x37a0cba, "kfree" },
	{ 0x5eadc959, "usb_put_dev" },
	{ 0x6138a907, "usb_free_urb" },
	{ 0xa19625ee, "usb_autopm_put_interface" },
	{ 0x962c8ae1, "usb_kill_anchored_urbs" },
	{ 0x1163987c, "usb_kill_urb" },
	{ 0x407af304, "usb_wait_anchor_empty_timeout" },
	{ 0x2ab7989d, "mutex_lock" },
	{ 0x296695f, "refcount_warn_saturate" },
	{ 0x9e1f503a, "usb_autopm_get_interface" },
	{ 0x8910dbc2, "usb_find_interface" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0xc5850110, "printk" },
	{ 0xe29879e3, "_dev_err" },
	{ 0xcf2a6966, "up" },
	{ 0x46083b0a, "usb_free_coherent" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0x409bcb62, "mutex_unlock" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "usbcore,gpib_common");

MODULE_ALIAS("usb:v0403p6001d*dc*dsc*dp*ic*isc*ip*in*");

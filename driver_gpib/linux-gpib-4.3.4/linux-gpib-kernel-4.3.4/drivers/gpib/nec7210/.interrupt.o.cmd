cmd_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o :=  gcc-10 -Wp,-MMD,/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/.interrupt.o.d -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/10/include -I/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include -I/usr/src/linux-headers-5.10.0-11-common/arch/x86/include -I./arch/x86/include/generated -I/usr/src/linux-headers-5.10.0-11-common/include -I./include -I/usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I/usr/src/linux-headers-5.10.0-11-common/include/uapi -I./include/generated/uapi -include /usr/src/linux-headers-5.10.0-11-common/include/linux/kconfig.h -include /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler_types.h -D__KERNEL__ -fmacro-prefix-map=/usr/src/linux-headers-5.10.0-11-common/= -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -std=gnu89 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -DCONFIG_X86_X32_ABI -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -fno-jump-tables -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 -fno-allow-store-data-races -Wframe-larger-than=2048 -fstack-protector-strong -Wimplicit-fallthrough -Wno-unused-but-set-variable -Wno-unused-const-variable -g -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wno-stringop-truncation -Wno-zero-length-bounds -Wno-array-bounds -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -fno-strict-overflow -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -Wno-packed-not-aligned -I/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include -DHAVE_DEV_OF_NODE= -DGPIB_CONFIG_PCMCIA=0 -DGPIB_CONFIG_KERNEL_DEBUG=0  -DMODULE  -DKBUILD_BASENAME='"interrupt"' -DKBUILD_MODNAME='"nec7210"' -c -o /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.c

source_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o := /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.c

deps_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o := \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kconfig.h \
    $(wildcard include/config/cc/version/text.h) \
    $(wildcard include/config/cpu/big/endian.h) \
    $(wildcard include/config/booger.h) \
    $(wildcard include/config/foo.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler_types.h \
    $(wildcard include/config/have/arch/compiler/h.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/cc/has/asm/inline.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler_attributes.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler-gcc.h \
    $(wildcard include/config/arm64.h) \
    $(wildcard include/config/retpoline.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
    $(wildcard include/config/kcov.h) \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/board.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpibP.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/types.h \
    $(wildcard include/config/have/uid16.h) \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/types.h \
  arch/x86/include/generated/uapi/asm/types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/int-ll64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/int-ll64.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/posix_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/stddef.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/stddef.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler_types.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/x86/32.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/posix_types_64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/posix_types.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpib_user.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpib_types.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/atomic.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/atomic.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/atomic.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/compiler.h \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/stack/validation.h) \
  arch/x86/include/generated/asm/rwonce.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/rwonce.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kasan-checks.h \
    $(wildcard include/config/kasan.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kcsan-checks.h \
    $(wildcard include/config/kcsan.h) \
    $(wildcard include/config/kcsan/ignore/atomics.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/alternative.h \
    $(wildcard include/config/smp.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/stringify.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/asm.h \
    $(wildcard include/config/kprobes.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cmpxchg.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cpufeatures.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/required-features.h \
    $(wildcard include/config/x86/minimum/cpu/family.h) \
    $(wildcard include/config/math/emulation.h) \
    $(wildcard include/config/x86/pae.h) \
    $(wildcard include/config/x86/64.h) \
    $(wildcard include/config/x86/cmpxchg64.h) \
    $(wildcard include/config/x86/cmov.h) \
    $(wildcard include/config/x86/use/3dnow.h) \
    $(wildcard include/config/x86/p6/nop.h) \
    $(wildcard include/config/matom.h) \
    $(wildcard include/config/paravirt/xxl.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/disabled-features.h \
    $(wildcard include/config/x86/smap.h) \
    $(wildcard include/config/x86/umip.h) \
    $(wildcard include/config/x86/intel/memory/protection/keys.h) \
    $(wildcard include/config/x86/5level.h) \
    $(wildcard include/config/page/table/isolation.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cmpxchg_64.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/rmwcc.h \
    $(wildcard include/config/cc/has/asm/goto.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/barrier.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/nops.h \
    $(wildcard include/config/mk7.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/barrier.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/atomic64_64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/atomic-arch-fallback.h \
    $(wildcard include/config/generic/atomic64.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/atomic-instrumented.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/build_bug.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/instrumented.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/atomic-long.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/device.h \
  include/generated/uapi/linux/version.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/device.h \
    $(wildcard include/config/debug/devres.h) \
    $(wildcard include/config/prove/locking.h) \
    $(wildcard include/config/energy/model.h) \
    $(wildcard include/config/generic/msi/irq/domain.h) \
    $(wildcard include/config/pinctrl.h) \
    $(wildcard include/config/generic/msi/irq.h) \
    $(wildcard include/config/dma/ops.h) \
    $(wildcard include/config/dma/declare/coherent.h) \
    $(wildcard include/config/dma/cma.h) \
    $(wildcard include/config/numa.h) \
    $(wildcard include/config/arch/has/sync/dma/for/device.h) \
    $(wildcard include/config/arch/has/sync/dma/for/cpu.h) \
    $(wildcard include/config/arch/has/sync/dma/for/cpu/all.h) \
    $(wildcard include/config/dma/ops/bypass.h) \
    $(wildcard include/config/pm/sleep.h) \
    $(wildcard include/config/of.h) \
    $(wildcard include/config/devtmpfs.h) \
    $(wildcard include/config/sysfs/deprecated.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dev_printk.h \
    $(wildcard include/config/printk.h) \
    $(wildcard include/config/dynamic/debug.h) \
    $(wildcard include/config/dynamic/debug/core.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ratelimit.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ratelimit_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bits.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/const.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/const.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/const.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/bits.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/param.h \
  arch/x86/include/generated/uapi/asm/param.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/param.h \
    $(wildcard include/config/hz.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/param.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/spinlock_types.h \
    $(wildcard include/config/debug/spinlock.h) \
    $(wildcard include/config/debug/lock/alloc.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/spinlock_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/qspinlock_types.h \
    $(wildcard include/config/nr/cpus.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/qrwlock_types.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/byteorder.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/byteorder/little_endian.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/byteorder/little_endian.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/swab.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/swab.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/swab.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/byteorder/generic.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/lockdep_types.h \
    $(wildcard include/config/prove/raw/lock/nesting.h) \
    $(wildcard include/config/preempt/lock.h) \
    $(wildcard include/config/lockdep.h) \
    $(wildcard include/config/lock/stat.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rwlock_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched.h \
    $(wildcard include/config/debug/atomic/sleep.h) \
    $(wildcard include/config/virt/cpu/accounting/native.h) \
    $(wildcard include/config/sched/info.h) \
    $(wildcard include/config/schedstats.h) \
    $(wildcard include/config/fair/group/sched.h) \
    $(wildcard include/config/rt/group/sched.h) \
    $(wildcard include/config/rt/mutexes.h) \
    $(wildcard include/config/uclamp/task.h) \
    $(wildcard include/config/uclamp/buckets/count.h) \
    $(wildcard include/config/thread/info/in/task.h) \
    $(wildcard include/config/cgroup/sched.h) \
    $(wildcard include/config/preempt/notifiers.h) \
    $(wildcard include/config/blk/dev/io/trace.h) \
    $(wildcard include/config/preempt/rcu.h) \
    $(wildcard include/config/tasks/rcu.h) \
    $(wildcard include/config/tasks/trace/rcu.h) \
    $(wildcard include/config/psi.h) \
    $(wildcard include/config/memcg.h) \
    $(wildcard include/config/compat/brk.h) \
    $(wildcard include/config/cgroups.h) \
    $(wildcard include/config/blk/cgroup.h) \
    $(wildcard include/config/stackprotector.h) \
    $(wildcard include/config/arch/has/scaled/cputime.h) \
    $(wildcard include/config/virt/cpu/accounting/gen.h) \
    $(wildcard include/config/no/hz/full.h) \
    $(wildcard include/config/posix/cputimers.h) \
    $(wildcard include/config/posix/cpu/timers/task/work.h) \
    $(wildcard include/config/keys.h) \
    $(wildcard include/config/sysvipc.h) \
    $(wildcard include/config/detect/hung/task.h) \
    $(wildcard include/config/io/uring.h) \
    $(wildcard include/config/audit.h) \
    $(wildcard include/config/auditsyscall.h) \
    $(wildcard include/config/debug/mutexes.h) \
    $(wildcard include/config/trace/irqflags.h) \
    $(wildcard include/config/ubsan.h) \
    $(wildcard include/config/ubsan/trap.h) \
    $(wildcard include/config/block.h) \
    $(wildcard include/config/compaction.h) \
    $(wildcard include/config/task/xacct.h) \
    $(wildcard include/config/cpusets.h) \
    $(wildcard include/config/x86/cpu/resctrl.h) \
    $(wildcard include/config/futex.h) \
    $(wildcard include/config/compat.h) \
    $(wildcard include/config/perf/events.h) \
    $(wildcard include/config/debug/preempt.h) \
    $(wildcard include/config/numa/balancing.h) \
    $(wildcard include/config/rseq.h) \
    $(wildcard include/config/task/delay/acct.h) \
    $(wildcard include/config/fault/injection.h) \
    $(wildcard include/config/latencytop.h) \
    $(wildcard include/config/kunit.h) \
    $(wildcard include/config/function/graph/tracer.h) \
    $(wildcard include/config/tracing.h) \
    $(wildcard include/config/uprobes.h) \
    $(wildcard include/config/bcache.h) \
    $(wildcard include/config/mmu.h) \
    $(wildcard include/config/vmap/stack.h) \
    $(wildcard include/config/livepatch.h) \
    $(wildcard include/config/security.h) \
    $(wildcard include/config/gcc/plugin/stackleak.h) \
    $(wildcard include/config/x86/mce.h) \
    $(wildcard include/config/arch/task/struct/on/stack.h) \
    $(wildcard include/config/preemption.h) \
    $(wildcard include/config/debug/rseq.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/sched.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/current.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/percpu.h \
    $(wildcard include/config/x86/64/smp.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kernel.h \
    $(wildcard include/config/preempt/voluntary.h) \
    $(wildcard include/config/preempt/rt.h) \
    $(wildcard include/config/panic/timeout.h) \
    $(wildcard include/config/ftrace/mcount/record.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/limits.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/limits.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/limits.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/linkage.h \
    $(wildcard include/config/arch/use/sym/annotations.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/export.h \
    $(wildcard include/config/modversions.h) \
    $(wildcard include/config/module/rel/crcs.h) \
    $(wildcard include/config/have/arch/prel32/relocations.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/trim/unused/ksyms.h) \
    $(wildcard include/config/unused/symbols.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/linkage.h \
    $(wildcard include/config/x86/alignment/16.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bitops.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/bitops.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/find.h \
    $(wildcard include/config/generic/find/first/bit.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/sched.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/arch_hweight.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/const_hweight.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/instrumented-atomic.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/instrumented-non-atomic.h \
    $(wildcard include/config/kcsan/assume/plain/writes/atomic.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/instrumented-lock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/le.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bitops/ext2-atomic-setbit.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/log2.h \
    $(wildcard include/config/arch/has/ilog2/u32.h) \
    $(wildcard include/config/arch/has/ilog2/u64.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/minmax.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/typecheck.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/printk.h \
    $(wildcard include/config/message/loglevel/default.h) \
    $(wildcard include/config/console/loglevel/default.h) \
    $(wildcard include/config/console/loglevel/quiet.h) \
    $(wildcard include/config/early/printk.h) \
    $(wildcard include/config/printk/nmi.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/init.h \
    $(wildcard include/config/strict/kernel/rwx.h) \
    $(wildcard include/config/strict/module/rwx.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kern_levels.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/cache.h \
    $(wildcard include/config/arch/has/cache/line/size.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/kernel.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/sysinfo.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cache.h \
    $(wildcard include/config/x86/l1/cache/shift.h) \
    $(wildcard include/config/x86/internode/cache/shift.h) \
    $(wildcard include/config/x86/vsmp.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dynamic_debug.h \
    $(wildcard include/config/jump/label.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/jump_label.h \
    $(wildcard include/config/have/arch/jump/label/relative.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/jump_label.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/div64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/div64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/percpu.h \
    $(wildcard include/config/have/setup/per/cpu/area.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/threads.h \
    $(wildcard include/config/base/small.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/percpu-defs.h \
    $(wildcard include/config/debug/force/weak/per/cpu.h) \
    $(wildcard include/config/amd/mem/encrypt.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/pid.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rculist.h \
    $(wildcard include/config/prove/rcu/list.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/list.h \
    $(wildcard include/config/debug/list.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/poison.h \
    $(wildcard include/config/illegal/pointer/value.h) \
    $(wildcard include/config/page/poisoning/zero.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcupdate.h \
    $(wildcard include/config/tiny/rcu.h) \
    $(wildcard include/config/tasks/rcu/generic.h) \
    $(wildcard include/config/rcu/stall/common.h) \
    $(wildcard include/config/rcu/nocb/cpu.h) \
    $(wildcard include/config/tasks/rude/rcu.h) \
    $(wildcard include/config/tree/rcu.h) \
    $(wildcard include/config/debug/objects/rcu/head.h) \
    $(wildcard include/config/hotplug/cpu.h) \
    $(wildcard include/config/prove/rcu.h) \
    $(wildcard include/config/rcu/boost.h) \
    $(wildcard include/config/arch/weak/release/acquire.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/irqflags.h \
    $(wildcard include/config/irqsoff/tracer.h) \
    $(wildcard include/config/preempt/tracer.h) \
    $(wildcard include/config/trace/irqflags/support.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/irqflags.h \
    $(wildcard include/config/debug/entry.h) \
    $(wildcard include/config/xen/pv.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/processor-flags.h \
    $(wildcard include/config/vm86.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/processor-flags.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mem_encrypt.h \
    $(wildcard include/config/arch/has/mem/encrypt.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mem_encrypt.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/cc_platform.h \
    $(wildcard include/config/arch/has/cc/platform.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/bootparam.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/screen_info.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/screen_info.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/apm_bios.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/apm_bios.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/ioctl.h \
  arch/x86/include/generated/uapi/asm/ioctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/ioctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/ioctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/edd.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/edd.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/ist.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/ist.h \
  /usr/src/linux-headers-5.10.0-11-common/include/video/edid.h \
    $(wildcard include/config/x86.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/video/edid.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/nospec-branch.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/static_key.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/objtool.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/alternative-asm.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/msr-index.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/unwind_hints.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/orc_types.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/segment.h \
    $(wildcard include/config/x86/32/lazy/gs.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/paravirt.h \
    $(wildcard include/config/paravirt.h) \
    $(wildcard include/config/x86/iopl/ioperm.h) \
    $(wildcard include/config/pgtable/levels.h) \
    $(wildcard include/config/paravirt/spinlocks.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/pgtable_types.h \
    $(wildcard include/config/mem/soft/dirty.h) \
    $(wildcard include/config/have/arch/userfaultfd/wp.h) \
    $(wildcard include/config/proc/fs.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/page_types.h \
    $(wildcard include/config/physical/start.h) \
    $(wildcard include/config/physical/align.h) \
    $(wildcard include/config/dynamic/physical/mask.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/page_64_types.h \
    $(wildcard include/config/dynamic/memory/layout.h) \
    $(wildcard include/config/randomize/base.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/kaslr.h \
    $(wildcard include/config/randomize/memory.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/pgtable_64_types.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/sparsemem.h \
    $(wildcard include/config/sparsemem.h) \
    $(wildcard include/config/numa/keep/meminfo.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/pgtable-nop4d.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/paravirt_types.h \
    $(wildcard include/config/paravirt/debug.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/desc_defs.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/kmap_types.h \
    $(wildcard include/config/debug/highmem.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/kmap_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bug.h \
    $(wildcard include/config/generic/bug.h) \
    $(wildcard include/config/bug/on/data/corruption.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/bug.h \
    $(wildcard include/config/debug/bugverbose.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/instrumentation.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/bug.h \
    $(wildcard include/config/bug.h) \
    $(wildcard include/config/generic/bug/relative/pointers.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/cpumask.h \
    $(wildcard include/config/cpumask/offstack.h) \
    $(wildcard include/config/debug/per/cpu/maps.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bitmap.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/string.h \
    $(wildcard include/config/binary/printf.h) \
    $(wildcard include/config/fortify/source.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/string.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/string.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/string_64.h \
    $(wildcard include/config/arch/has/uaccess/flushcache.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/frame.h \
    $(wildcard include/config/frame/pointer.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/preempt.h \
    $(wildcard include/config/preempt/count.h) \
    $(wildcard include/config/trace/preempt/toggle.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/preempt.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/thread_info.h \
    $(wildcard include/config/have/arch/within/stack/frames.h) \
    $(wildcard include/config/hardened/usercopy.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/restart_block.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/time64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/math64.h \
    $(wildcard include/config/arch/supports/int128.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/math64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/time64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/time.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/time_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/errno.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/errno.h \
  arch/x86/include/generated/uapi/asm/errno.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/errno.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/errno-base.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/thread_info.h \
    $(wildcard include/config/ia32/emulation.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/page.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/page_64.h \
    $(wildcard include/config/debug/virtual.h) \
    $(wildcard include/config/flatmem.h) \
    $(wildcard include/config/x86/vsyscall/emulation.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/range.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/memory_model.h \
    $(wildcard include/config/discontigmem.h) \
    $(wildcard include/config/sparsemem/vmemmap.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/pfn.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/getorder.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cpufeature.h \
    $(wildcard include/config/x86/feature/names.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/processor.h \
    $(wildcard include/config/x86/vmx/feature/names.h) \
    $(wildcard include/config/x86/debugctlmsr.h) \
    $(wildcard include/config/cpu/sup/amd.h) \
    $(wildcard include/config/xen.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/math_emu.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/ptrace.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/ptrace.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/ptrace-abi.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/proto.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/ldt.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/sigcontext.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/msr.h \
    $(wildcard include/config/tracepoints.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/msr-index.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/cpumask.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/msr.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/tracepoint-defs.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/special_insns.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/fpu/types.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/vmxfeatures.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/vdso/processor.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/personality.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/personality.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/err.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bottom_half.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/lockdep.h \
    $(wildcard include/config/debug/locking/api/selftests.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/smp.h \
    $(wildcard include/config/up/late/init.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/smp_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/llist.h \
    $(wildcard include/config/arch/have/nmi/safe/cmpxchg.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/smp.h \
    $(wildcard include/config/x86/local/apic.h) \
    $(wildcard include/config/debug/nmi/selftest.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcutree.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/wait.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/spinlock.h \
  arch/x86/include/generated/asm/mmiowb.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/mmiowb.h \
    $(wildcard include/config/mmiowb.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/spinlock.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/qspinlock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/qspinlock.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/qrwlock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/qrwlock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rwlock.h \
    $(wildcard include/config/preempt.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/spinlock_api_smp.h \
    $(wildcard include/config/inline/spin/lock.h) \
    $(wildcard include/config/inline/spin/lock/bh.h) \
    $(wildcard include/config/inline/spin/lock/irq.h) \
    $(wildcard include/config/inline/spin/lock/irqsave.h) \
    $(wildcard include/config/inline/spin/trylock.h) \
    $(wildcard include/config/inline/spin/trylock/bh.h) \
    $(wildcard include/config/uninline/spin/unlock.h) \
    $(wildcard include/config/inline/spin/unlock/bh.h) \
    $(wildcard include/config/inline/spin/unlock/irq.h) \
    $(wildcard include/config/inline/spin/unlock/irqrestore.h) \
    $(wildcard include/config/generic/lockbreak.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rwlock_api_smp.h \
    $(wildcard include/config/inline/read/lock.h) \
    $(wildcard include/config/inline/write/lock.h) \
    $(wildcard include/config/inline/read/lock/bh.h) \
    $(wildcard include/config/inline/write/lock/bh.h) \
    $(wildcard include/config/inline/read/lock/irq.h) \
    $(wildcard include/config/inline/write/lock/irq.h) \
    $(wildcard include/config/inline/read/lock/irqsave.h) \
    $(wildcard include/config/inline/write/lock/irqsave.h) \
    $(wildcard include/config/inline/read/trylock.h) \
    $(wildcard include/config/inline/write/trylock.h) \
    $(wildcard include/config/inline/read/unlock.h) \
    $(wildcard include/config/inline/write/unlock.h) \
    $(wildcard include/config/inline/read/unlock/bh.h) \
    $(wildcard include/config/inline/write/unlock/bh.h) \
    $(wildcard include/config/inline/read/unlock/irq.h) \
    $(wildcard include/config/inline/write/unlock/irq.h) \
    $(wildcard include/config/inline/read/unlock/irqrestore.h) \
    $(wildcard include/config/inline/write/unlock/irqrestore.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/wait.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/refcount.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sem.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/sem.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ipc.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/uidgid.h \
    $(wildcard include/config/multiuser.h) \
    $(wildcard include/config/user/ns.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/highuid.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rhashtable-types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mutex.h \
    $(wildcard include/config/mutex/spin/on/owner.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/osq_lock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/debug_locks.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/workqueue.h \
    $(wildcard include/config/debug/objects/work.h) \
    $(wildcard include/config/freezer.h) \
    $(wildcard include/config/sysfs.h) \
    $(wildcard include/config/wq/watchdog.h) \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/timer.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/timer.h \
    $(wildcard include/config/debug/objects/timers.h) \
    $(wildcard include/config/no/hz/common.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ktime.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/time.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/time.h \
    $(wildcard include/config/arch/uses/gettimeoffset.h) \
    $(wildcard include/config/posix/timers.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/time32.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/timex.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/timex.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/timex.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/tsc.h \
    $(wildcard include/config/x86/tsc.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/time32.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/time.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/jiffies.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/jiffies.h \
  include/generated/timeconst.h \
  /usr/src/linux-headers-5.10.0-11-common/include/vdso/ktime.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/timekeeping.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/timekeeping32.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/debugobjects.h \
    $(wildcard include/config/debug/objects.h) \
    $(wildcard include/config/debug/objects/free.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/ipc.h \
  arch/x86/include/generated/uapi/asm/ipcbuf.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/ipcbuf.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/sembuf.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/shm.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/shm.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/hugetlb_encode.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/shmbuf.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/shmbuf.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/shmparam.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kcov.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/kcov.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/plist.h \
    $(wildcard include/config/debug/plist.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/hrtimer.h \
    $(wildcard include/config/high/res/timers.h) \
    $(wildcard include/config/time/low/res.h) \
    $(wildcard include/config/timerfd.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/hrtimer_defs.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rbtree.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/percpu.h \
    $(wildcard include/config/need/per/cpu/embed/first/chunk.h) \
    $(wildcard include/config/need/per/cpu/page/first/chunk.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mmdebug.h \
    $(wildcard include/config/debug/vm.h) \
    $(wildcard include/config/debug/vm/pgflags.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/seqlock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ww_mutex.h \
    $(wildcard include/config/debug/ww/mutex/slowpath.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/timerqueue.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/seccomp.h \
    $(wildcard include/config/seccomp.h) \
    $(wildcard include/config/have/arch/seccomp/filter.h) \
    $(wildcard include/config/seccomp/filter.h) \
    $(wildcard include/config/checkpoint/restore.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/seccomp.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/seccomp.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/unistd.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/unistd.h \
  arch/x86/include/generated/uapi/asm/unistd_64.h \
  arch/x86/include/generated/asm/unistd_64_x32.h \
  arch/x86/include/generated/asm/unistd_32_ia32.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/ia32_unistd.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/seccomp.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/unistd.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/nodemask.h \
    $(wildcard include/config/highmem.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/numa.h \
    $(wildcard include/config/nodes/shift.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/resource.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/resource.h \
  arch/x86/include/generated/uapi/asm/resource.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/resource.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/resource.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/latencytop.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/prio.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/signal_types.h \
    $(wildcard include/config/old/sigaction.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/signal.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/signal.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/signal.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/signal-defs.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/siginfo.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/siginfo.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mm_types_task.h \
    $(wildcard include/config/arch/want/batched/unmap/tlb/flush.h) \
    $(wildcard include/config/split/ptlock/cpus.h) \
    $(wildcard include/config/arch/enable/split/pmd/ptlock.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/tlbbatch.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/task_io_accounting.h \
    $(wildcard include/config/task/io/accounting.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/posix-timers.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/alarmtimer.h \
    $(wildcard include/config/rtc/class.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/task_work.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/rseq.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kcsan.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/energy_model.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kobject.h \
    $(wildcard include/config/uevent/helper.h) \
    $(wildcard include/config/debug/kobject/release.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sysfs.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kernfs.h \
    $(wildcard include/config/kernfs.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/idr.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/radix-tree.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/xarray.h \
    $(wildcard include/config/xarray/multi.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/gfp.h \
    $(wildcard include/config/zone/dma.h) \
    $(wildcard include/config/zone/dma32.h) \
    $(wildcard include/config/zone/device.h) \
    $(wildcard include/config/contig/alloc.h) \
    $(wildcard include/config/cma.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mmzone.h \
    $(wildcard include/config/force/max/zoneorder.h) \
    $(wildcard include/config/memory/isolation.h) \
    $(wildcard include/config/zsmalloc.h) \
    $(wildcard include/config/shadow/call/stack.h) \
    $(wildcard include/config/need/multiple/nodes.h) \
    $(wildcard include/config/memory/hotplug.h) \
    $(wildcard include/config/transparent/hugepage.h) \
    $(wildcard include/config/flat/node/mem/map.h) \
    $(wildcard include/config/page/extension.h) \
    $(wildcard include/config/deferred/struct/page/init.h) \
    $(wildcard include/config/have/memoryless/nodes.h) \
    $(wildcard include/config/sparsemem/extreme.h) \
    $(wildcard include/config/memory/hotremove.h) \
    $(wildcard include/config/have/arch/pfn/valid.h) \
    $(wildcard include/config/holes/in/zone.h) \
    $(wildcard include/config/arch/has/holes/memorymodel.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/pageblock-flags.h \
    $(wildcard include/config/hugetlb/page.h) \
    $(wildcard include/config/hugetlb/page/size/variable.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/page-flags-layout.h \
    $(wildcard include/config/kasan/sw/tags.h) \
  include/generated/bounds.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/mm_types.h \
    $(wildcard include/config/have/aligned/struct/page.h) \
    $(wildcard include/config/userfaultfd.h) \
    $(wildcard include/config/swap.h) \
    $(wildcard include/config/have/arch/compat/mmap/bases.h) \
    $(wildcard include/config/membarrier.h) \
    $(wildcard include/config/aio.h) \
    $(wildcard include/config/mmu/notifier.h) \
    $(wildcard include/config/iommu/support.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/auxvec.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/auxvec.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/auxvec.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rwsem.h \
    $(wildcard include/config/rwsem/spin/on/owner.h) \
    $(wildcard include/config/debug/rwsems.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/completion.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/swait.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/uprobes.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/uprobes.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/notifier.h \
    $(wildcard include/config/tree/srcu.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/srcu.h \
    $(wildcard include/config/tiny/srcu.h) \
    $(wildcard include/config/srcu.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcu_segcblist.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/srcutree.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcu_node_tree.h \
    $(wildcard include/config/rcu/fanout.h) \
    $(wildcard include/config/rcu/fanout/leaf.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mmu.h \
    $(wildcard include/config/modify/ldt/syscall.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/page-flags.h \
    $(wildcard include/config/arch/uses/pg/uncached.h) \
    $(wildcard include/config/memory/failure.h) \
    $(wildcard include/config/idle/page/tracking.h) \
    $(wildcard include/config/thp/swap.h) \
    $(wildcard include/config/ksm.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/memory_hotplug.h \
    $(wildcard include/config/arch/has/add/pages.h) \
    $(wildcard include/config/have/arch/nodedata/extension.h) \
    $(wildcard include/config/have/bootmem/info/node.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mmzone.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mmzone_64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/topology.h \
    $(wildcard include/config/use/percpu/numa/node/id.h) \
    $(wildcard include/config/sched/smt.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/arch_topology.h \
    $(wildcard include/config/generic/arch/topology.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/topology.h \
    $(wildcard include/config/sched/mc/prio.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mpspec.h \
    $(wildcard include/config/eisa.h) \
    $(wildcard include/config/x86/mpparse.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/mpspec_def.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/x86_init.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/apicdef.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/topology.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kconfig.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/local_lock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/local_lock_internal.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kobject_ns.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/stat.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/uapi/asm/stat.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/stat.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kref.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/cpufreq.h \
    $(wildcard include/config/cpu/freq.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/topology.h \
    $(wildcard include/config/sched/debug.h) \
    $(wildcard include/config/sched/mc.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/idle.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/sd_flags.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ioport.h \
    $(wildcard include/config/io/strict/devmem.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/klist.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/pm.h \
    $(wildcard include/config/vt/console/sleep.h) \
    $(wildcard include/config/pm.h) \
    $(wildcard include/config/pm/clk.h) \
    $(wildcard include/config/pm/generic/domains.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/overflow.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/device/bus.h \
    $(wildcard include/config/acpi.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/device/class.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/device/driver.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/device.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/pm_wakeup.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/interrupt.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/interrupt.h \
    $(wildcard include/config/irq/forced/threading.h) \
    $(wildcard include/config/generic/irq/probe.h) \
    $(wildcard include/config/irq/timings.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/irqreturn.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/irqnr.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/irqnr.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/hardirq.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/context_tracking_state.h \
    $(wildcard include/config/context/tracking.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ftrace_irq.h \
    $(wildcard include/config/hwlat/tracer.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/vtime.h \
    $(wildcard include/config/virt/cpu/accounting.h) \
    $(wildcard include/config/irq/time/accounting.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/hardirq.h \
    $(wildcard include/config/kvm/intel.h) \
    $(wildcard include/config/have/kvm.h) \
    $(wildcard include/config/x86/thermal/vector.h) \
    $(wildcard include/config/x86/mce/threshold.h) \
    $(wildcard include/config/x86/mce/amd.h) \
    $(wildcard include/config/x86/hv/callback/vector.h) \
    $(wildcard include/config/hyperv.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/irq.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/irq_vectors.h \
    $(wildcard include/config/x86/io/apic.h) \
    $(wildcard include/config/pci/msi.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/sections.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/sections.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/extable.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpib_proto.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/fs.h \
    $(wildcard include/config/read/only/thp/for/fs.h) \
    $(wildcard include/config/fs/posix/acl.h) \
    $(wildcard include/config/cgroup/writeback.h) \
    $(wildcard include/config/ima.h) \
    $(wildcard include/config/file/locking.h) \
    $(wildcard include/config/fsnotify.h) \
    $(wildcard include/config/fs/encryption.h) \
    $(wildcard include/config/fs/verity.h) \
    $(wildcard include/config/epoll.h) \
    $(wildcard include/config/unicode.h) \
    $(wildcard include/config/quota.h) \
    $(wildcard include/config/fs/dax.h) \
    $(wildcard include/config/mandatory/file/locking.h) \
    $(wildcard include/config/migration.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/wait_bit.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kdev_t.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/kdev_t.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dcache.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rculist_bl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/list_bl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/bit_spinlock.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/lockref.h \
    $(wildcard include/config/arch/use/cmpxchg/lockref.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/stringhash.h \
    $(wildcard include/config/dcache/word/access.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/hash.h \
    $(wildcard include/config/have/arch/hash.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/path.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/list_lru.h \
    $(wildcard include/config/memcg/kmem.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/shrinker.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/capability.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/capability.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/semaphore.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/semaphore.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/fcntl.h \
    $(wildcard include/config/arch/32bit/off/t.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/fcntl.h \
  arch/x86/include/generated/uapi/asm/fcntl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/asm-generic/fcntl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/openat2.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/migrate_mode.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/percpu-rwsem.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcuwait.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/sched/signal.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/signal.h \
    $(wildcard include/config/sched/autogroup.h) \
    $(wildcard include/config/bsd/process/acct.h) \
    $(wildcard include/config/taskstats.h) \
    $(wildcard include/config/stack/growsup.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/signal.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/jobctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/task.h \
    $(wildcard include/config/have/exit/thread.h) \
    $(wildcard include/config/arch/wants/dynamic/task/struct.h) \
    $(wildcard include/config/have/arch/thread/struct/whitelist.h) \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/uaccess.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/uaccess.h \
    $(wildcard include/config/set/fs.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/fault-inject-usercopy.h \
    $(wildcard include/config/fault/injection/usercopy.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/uaccess.h \
    $(wildcard include/config/cc/has/asm/goto/output.h) \
    $(wildcard include/config/cc/asm/goto/output.h) \
    $(wildcard include/config/arch/has/copy/mc.h) \
    $(wildcard include/config/x86/intel/usercopy.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/smap.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/uaccess_64.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/cred.h \
    $(wildcard include/config/debug/credentials.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/key.h \
    $(wildcard include/config/key/notifications.h) \
    $(wildcard include/config/net.h) \
    $(wildcard include/config/sysctl.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sysctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/sysctl.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/assoc_array.h \
    $(wildcard include/config/associative/array.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/user.h \
    $(wildcard include/config/fanotify.h) \
    $(wildcard include/config/posix/mqueue.h) \
    $(wildcard include/config/bpf/syscall.h) \
    $(wildcard include/config/watch/queue.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rcu_sync.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/delayed_call.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/uuid.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/uuid.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/errseq.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/ioprio.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/sched/rt.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/iocontext.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/fs_types.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/fs.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/quota.h \
    $(wildcard include/config/quota/netlink/interface.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/percpu_counter.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/dqblk_xfs.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dqblk_v1.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dqblk_v2.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/dqblk_qtree.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/projid.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/quota.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/nfs_fs_i.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpib_ioctl.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/version.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/io.h \
    $(wildcard include/config/mtrr.h) \
    $(wildcard include/config/x86/pat.h) \
  arch/x86/include/generated/asm/early_ioremap.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/early_ioremap.h \
    $(wildcard include/config/generic/early/ioremap.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/iomap.h \
    $(wildcard include/config/has/ioport/map.h) \
    $(wildcard include/config/pci.h) \
    $(wildcard include/config/generic/iomap.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/pci_iomap.h \
    $(wildcard include/config/no/generic/pci/ioport/map.h) \
    $(wildcard include/config/generic/pci/iomap.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/io.h \
    $(wildcard include/config/generic/ioremap.h) \
    $(wildcard include/config/virt/to/bus.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/logic_pio.h \
    $(wildcard include/config/indirect/pio.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/fwnode.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/vmalloc.h \
    $(wildcard include/config/kasan/vmalloc.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/vmalloc.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/pgtable_areas.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/module.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/module.h \
    $(wildcard include/config/modules/tree/lookup.h) \
    $(wildcard include/config/module/sig.h) \
    $(wildcard include/config/kallsyms.h) \
    $(wildcard include/config/bpf/events.h) \
    $(wildcard include/config/event/tracing.h) \
    $(wildcard include/config/have/static/call/inline.h) \
    $(wildcard include/config/module/unload.h) \
    $(wildcard include/config/constructors.h) \
    $(wildcard include/config/function/error/injection.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/kmod.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/umh.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/elf.h \
    $(wildcard include/config/arch/use/gnu/property.h) \
    $(wildcard include/config/arch/have/elf/prot.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/elf.h \
    $(wildcard include/config/x86/x32/abi.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/user.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/user_64.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/fsgsbase.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/syscall.h \
    $(wildcard include/config/x86/x32/disabled.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/audit.h \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/elf-em.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/vdso.h \
    $(wildcard include/config/x86/x32.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/uapi/linux/elf.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/moduleparam.h \
    $(wildcard include/config/alpha.h) \
    $(wildcard include/config/ia64.h) \
    $(wildcard include/config/ppc64.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/rbtree_latch.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/error-injection.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/error-injection.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/static_call_types.h \
    $(wildcard include/config/have/static/call.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/module.h \
    $(wildcard include/config/unwinder/orc.h) \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/module.h \
    $(wildcard include/config/have/mod/arch/specific.h) \
    $(wildcard include/config/modules/use/elf/rel.h) \
    $(wildcard include/config/modules/use/elf/rela.h) \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/orc_types.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/compat/include/linux/delay.h \
  /usr/src/linux-headers-5.10.0-11-common/include/linux/delay.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/delay.h \
  /usr/src/linux-headers-5.10.0-11-common/include/asm-generic/delay.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/nec7210.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/gpib_state_machines.h \
  /home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/include/nec7210_registers.h \
  /usr/src/linux-headers-5.10.0-11-common/arch/x86/include/asm/dma.h \
    $(wildcard include/config/isa/dma/api.h) \
    $(wildcard include/config/generic/isa/dma.h) \

/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o: $(deps_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o)

$(deps_/home/spin/driver_gpib/linux-gpib-4.3.4/linux-gpib-kernel-4.3.4/drivers/gpib/nec7210/interrupt.o):

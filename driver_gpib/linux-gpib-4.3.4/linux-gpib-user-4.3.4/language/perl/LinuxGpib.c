/*
 * This file was generated automatically by ExtUtils::ParseXS version 3.40 from the
 * contents of LinuxGpib.xs. Do not edit this file, edit LinuxGpib.xs instead.
 *
 *    ANY CHANGES MADE HERE WILL BE LOST!
 *
 */

#line 1 "LinuxGpib.xs"
#include <gpib/ib.h>
#include "EXTERN.h"
#include "perl.h"
#include "XSUB.h"
#include <stdlib.h>

static int
not_here(char *s)
{
    croak("%s not implemented on this architecture", s);
    return -1;
}

static double
constant(char *name, int len, int arg)
{
    errno = EINVAL;
    return 0;
}

#line 31 "LinuxGpib.c"
#ifndef PERL_UNUSED_VAR
#  define PERL_UNUSED_VAR(var) if (0) var = var
#endif

#ifndef dVAR
#  define dVAR		dNOOP
#endif


/* This stuff is not part of the API! You have been warned. */
#ifndef PERL_VERSION_DECIMAL
#  define PERL_VERSION_DECIMAL(r,v,s) (r*1000000 + v*1000 + s)
#endif
#ifndef PERL_DECIMAL_VERSION
#  define PERL_DECIMAL_VERSION \
	  PERL_VERSION_DECIMAL(PERL_REVISION,PERL_VERSION,PERL_SUBVERSION)
#endif
#ifndef PERL_VERSION_GE
#  define PERL_VERSION_GE(r,v,s) \
	  (PERL_DECIMAL_VERSION >= PERL_VERSION_DECIMAL(r,v,s))
#endif
#ifndef PERL_VERSION_LE
#  define PERL_VERSION_LE(r,v,s) \
	  (PERL_DECIMAL_VERSION <= PERL_VERSION_DECIMAL(r,v,s))
#endif

/* XS_INTERNAL is the explicit static-linkage variant of the default
 * XS macro.
 *
 * XS_EXTERNAL is the same as XS_INTERNAL except it does not include
 * "STATIC", ie. it exports XSUB symbols. You probably don't want that
 * for anything but the BOOT XSUB.
 *
 * See XSUB.h in core!
 */


/* TODO: This might be compatible further back than 5.10.0. */
#if PERL_VERSION_GE(5, 10, 0) && PERL_VERSION_LE(5, 15, 1)
#  undef XS_EXTERNAL
#  undef XS_INTERNAL
#  if defined(__CYGWIN__) && defined(USE_DYNAMIC_LOADING)
#    define XS_EXTERNAL(name) __declspec(dllexport) XSPROTO(name)
#    define XS_INTERNAL(name) STATIC XSPROTO(name)
#  endif
#  if defined(__SYMBIAN32__)
#    define XS_EXTERNAL(name) EXPORT_C XSPROTO(name)
#    define XS_INTERNAL(name) EXPORT_C STATIC XSPROTO(name)
#  endif
#  ifndef XS_EXTERNAL
#    if defined(HASATTRIBUTE_UNUSED) && !defined(__cplusplus)
#      define XS_EXTERNAL(name) void name(pTHX_ CV* cv __attribute__unused__)
#      define XS_INTERNAL(name) STATIC void name(pTHX_ CV* cv __attribute__unused__)
#    else
#      ifdef __cplusplus
#        define XS_EXTERNAL(name) extern "C" XSPROTO(name)
#        define XS_INTERNAL(name) static XSPROTO(name)
#      else
#        define XS_EXTERNAL(name) XSPROTO(name)
#        define XS_INTERNAL(name) STATIC XSPROTO(name)
#      endif
#    endif
#  endif
#endif

/* perl >= 5.10.0 && perl <= 5.15.1 */


/* The XS_EXTERNAL macro is used for functions that must not be static
 * like the boot XSUB of a module. If perl didn't have an XS_EXTERNAL
 * macro defined, the best we can do is assume XS is the same.
 * Dito for XS_INTERNAL.
 */
#ifndef XS_EXTERNAL
#  define XS_EXTERNAL(name) XS(name)
#endif
#ifndef XS_INTERNAL
#  define XS_INTERNAL(name) XS(name)
#endif

/* Now, finally, after all this mess, we want an ExtUtils::ParseXS
 * internal macro that we're free to redefine for varying linkage due
 * to the EXPORT_XSUB_SYMBOLS XS keyword. This is internal, use
 * XS_EXTERNAL(name) or XS_INTERNAL(name) in your code if you need to!
 */

#undef XS_EUPXS
#if defined(PERL_EUPXS_ALWAYS_EXPORT)
#  define XS_EUPXS(name) XS_EXTERNAL(name)
#else
   /* default to internal */
#  define XS_EUPXS(name) XS_INTERNAL(name)
#endif

#ifndef PERL_ARGS_ASSERT_CROAK_XS_USAGE
#define PERL_ARGS_ASSERT_CROAK_XS_USAGE assert(cv); assert(params)

/* prototype to pass -Wmissing-prototypes */
STATIC void
S_croak_xs_usage(const CV *const cv, const char *const params);

STATIC void
S_croak_xs_usage(const CV *const cv, const char *const params)
{
    const GV *const gv = CvGV(cv);

    PERL_ARGS_ASSERT_CROAK_XS_USAGE;

    if (gv) {
        const char *const gvname = GvNAME(gv);
        const HV *const stash = GvSTASH(gv);
        const char *const hvname = stash ? HvNAME(stash) : NULL;

        if (hvname)
	    Perl_croak_nocontext("Usage: %s::%s(%s)", hvname, gvname, params);
        else
	    Perl_croak_nocontext("Usage: %s(%s)", gvname, params);
    } else {
        /* Pants. I don't think that it should be possible to get here. */
	Perl_croak_nocontext("Usage: CODE(0x%" UVxf ")(%s)", PTR2UV(cv), params);
    }
}
#undef  PERL_ARGS_ASSERT_CROAK_XS_USAGE

#define croak_xs_usage        S_croak_xs_usage

#endif

/* NOTE: the prototype of newXSproto() is different in versions of perls,
 * so we define a portable version of newXSproto()
 */
#ifdef newXS_flags
#define newXSproto_portable(name, c_impl, file, proto) newXS_flags(name, c_impl, file, proto, 0)
#else
#define newXSproto_portable(name, c_impl, file, proto) (PL_Sv=(SV*)newXS(name, c_impl, file), sv_setpv(PL_Sv, proto), (CV*)PL_Sv)
#endif /* !defined(newXS_flags) */

#if PERL_VERSION_LE(5, 21, 5)
#  define newXS_deffile(a,b) Perl_newXS(aTHX_ a,b,file)
#else
#  define newXS_deffile(a,b) Perl_newXS_deffile(aTHX_ a,b)
#endif

#line 175 "LinuxGpib.c"

XS_EUPXS(XS_LinuxGpib_constant); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_constant)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "sv, arg");
    {
#line 27 "LinuxGpib.xs"
	STRLEN len;
#line 186 "LinuxGpib.c"
	SV *	sv = ST(0)
;
	char *	s = SvPV(sv, len);
	int	arg = (int)SvIV(ST(1))
;
	double	RETVAL;
	dXSTARG;
#line 33 "LinuxGpib.xs"
	RETVAL = constant(s,len,arg);
#line 196 "LinuxGpib.c"
	XSprePUSH; PUSHn((double)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibcac); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibcac)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibcac(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibclr); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibclr)
{
    dVAR; dXSARGS;
    if (items != 1)
       croak_xs_usage(cv,  "ud");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibclr(ud);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibcmd); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibcmd)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, cmd, cnt");
    {
	int	ud = (int)SvIV(ST(0))
;
	char *	cmd = (char *)SvPV_nolen(ST(1))
;
	unsigned long	cnt = (unsigned long)SvUV(ST(2))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibcmd(ud, cmd, cnt);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibconfig); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibconfig)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, option, value");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	option = (int)SvIV(ST(1))
;
	int	value = (int)SvIV(ST(2))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibconfig(ud, option, value);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibdev); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibdev)
{
    dVAR; dXSARGS;
    if (items != 6)
       croak_xs_usage(cv,  "minor, pad, sad, timo, eot, eos");
    {
	int	minor = (int)SvIV(ST(0))
;
	int	pad = (int)SvIV(ST(1))
;
	int	sad = (int)SvIV(ST(2))
;
	int	timo = (int)SvIV(ST(3))
;
	int	eot = (int)SvIV(ST(4))
;
	int	eos = (int)SvIV(ST(5))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibdev(minor, pad, sad, timo, eot, eos);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibdma); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibdma)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibdma(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibeot); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibeot)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibeot(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibevent); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibevent)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, event");
    {
	int	RETVAL;
	dXSTARG;
	int	ud = (int)SvIV(ST(0))
;
	short	event;

	RETVAL = ibevent(ud, &event);
	sv_setiv(ST(1), (IV)event);
	SvSETMAGIC(ST(1));
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibfind); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibfind)
{
    dVAR; dXSARGS;
    if (items != 1)
       croak_xs_usage(cv,  "dev");
    {
	char *	dev = (char *)SvPV_nolen(ST(0))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibfind(dev);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibgts); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibgts)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibgts(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_iblines); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_iblines)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, line_status");
    {
	int	RETVAL;
	dXSTARG;
	int	ud = (int)SvIV(ST(0))
;
	short	line_status;

	RETVAL = iblines(ud, &line_status);
	sv_setiv(ST(1), (IV)line_status);
	SvSETMAGIC(ST(1));
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibloc); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibloc)
{
    dVAR; dXSARGS;
    if (items != 1)
       croak_xs_usage(cv,  "ud");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibloc(ud);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibonl); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibonl)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, onl");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	onl = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibonl(ud, onl);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibpad); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibpad)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibpad(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibrd); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibrd)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, rd, cnt");
    {
	int	ud = (int)SvIV(ST(0))
;
	SV *	rd = ST(1)
;
	unsigned long	cnt = (unsigned long)SvUV(ST(2))
;
#line 113 "LinuxGpib.xs"
	int i;
	char *buf;
#line 521 "LinuxGpib.c"
	int	RETVAL;
	dXSTARG;
#line 116 "LinuxGpib.xs"
	buf = malloc( cnt + 1 );
	if( buf == NULL )
		croak( "malloc() returned NULL in ibrd()\n" );

	RETVAL = ibrd(ud, buf, cnt);
	sv_setpvn(rd, buf, ThreadIbcntl());
	free( buf );
#line 532 "LinuxGpib.c"
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibrdi); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibrdi)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, array, cnt");
    {
	int	ud = (int)SvIV(ST(0))
;
	AV *	array;
	unsigned long	cnt = (unsigned long)SvUV(ST(2))
;
#line 132 "LinuxGpib.xs"
	int i;
	char *buf;
#line 554 "LinuxGpib.c"
	int	RETVAL;
	dXSTARG;

	STMT_START {
		SV* const xsub_tmp_sv = ST(1);
		SvGETMAGIC(xsub_tmp_sv);
		if (SvROK(xsub_tmp_sv) && SvTYPE(SvRV(xsub_tmp_sv)) == SVt_PVAV){
		    array = (AV*)SvRV(xsub_tmp_sv);
		}
		else{
		    Perl_croak_nocontext("%s: %s is not an ARRAY reference",
				"LinuxGpib::ibrdi",
				"array");
		}
	} STMT_END
;
#line 135 "LinuxGpib.xs"
	av_clear( array );
	buf = malloc( cnt );
	if( buf == NULL )
		croak( "malloc() returned NULL in ibrdi()\n" );
	RETVAL = ibrd(ud, buf, cnt);
	if( ( RETVAL & ERR ) == 0 )
	{
		for( i = 0; i < ThreadIbcntl(); i++ )
		{
			av_push( array, newSViv( buf[ i ] & 0xff ) );
		}
	}
	free( buf );
#line 585 "LinuxGpib.c"
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibrpp); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibrpp)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, ppr");
    {
	int	ud = (int)SvIV(ST(0))
;
	SV *	ppr = ST(1)
;
	int	RETVAL;
	dXSTARG;
#line 156 "LinuxGpib.xs"
	char response;

	RETVAL = ibrsp( ud, &response );
	if( ( RETVAL & ERR ) == 0 )
		sv_setiv( ppr, response );
#line 611 "LinuxGpib.c"
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibrsp); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibrsp)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, result");
    {
	int	ud = (int)SvIV(ST(0))
;
	SV *	result = ST(1)
;
	int	RETVAL;
	dXSTARG;
#line 169 "LinuxGpib.xs"
	char status;

	RETVAL = ibrsp( ud, &status );
	if( ( RETVAL & ERR ) == 0 )
		sv_setiv( result, status );
#line 637 "LinuxGpib.c"
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibrsv); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibrsv)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibrsv(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibsad); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibsad)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibsad(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibsic); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibsic)
{
    dVAR; dXSARGS;
    if (items != 1)
       croak_xs_usage(cv,  "ud");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibsic(ud);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibsre); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibsre)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibsre(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibtmo); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibtmo)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, v");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	v = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibtmo(ud, v);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibtrg); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibtrg)
{
    dVAR; dXSARGS;
    if (items != 1)
       croak_xs_usage(cv,  "ud");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibtrg(ud);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibwait); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibwait)
{
    dVAR; dXSARGS;
    if (items != 2)
       croak_xs_usage(cv,  "ud, mask");
    {
	int	ud = (int)SvIV(ST(0))
;
	int	mask = (int)SvIV(ST(1))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibwait(ud, mask);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibwrt); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibwrt)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, rd, cnt");
    {
	int	ud = (int)SvIV(ST(0))
;
	char *	rd = (char *)SvPV_nolen(ST(1))
;
	unsigned long	cnt = (unsigned long)SvUV(ST(2))
;
	int	RETVAL;
	dXSTARG;

	RETVAL = ibwrt(ud, rd, cnt);
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ibwrti); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ibwrti)
{
    dVAR; dXSARGS;
    if (items != 3)
       croak_xs_usage(cv,  "ud, array, cnt");
    {
	int	ud = (int)SvIV(ST(0))
;
	AV *	array;
	unsigned long	cnt = (unsigned long)SvUV(ST(2))
;
#line 222 "LinuxGpib.xs"
	int i;
	char *buf;
	SV **sv_ptr;
#line 826 "LinuxGpib.c"
	int	RETVAL;
	dXSTARG;

	STMT_START {
		SV* const xsub_tmp_sv = ST(1);
		SvGETMAGIC(xsub_tmp_sv);
		if (SvROK(xsub_tmp_sv) && SvTYPE(SvRV(xsub_tmp_sv)) == SVt_PVAV){
		    array = (AV*)SvRV(xsub_tmp_sv);
		}
		else{
		    Perl_croak_nocontext("%s: %s is not an ARRAY reference",
				"LinuxGpib::ibwrti",
				"array");
		}
	} STMT_END
;
#line 226 "LinuxGpib.xs"
	buf = malloc( cnt );
	if( buf == NULL )
		croak( "malloc() returned NULL in ibwrti()\n" );
	for( i = 0; i < cnt; i++ )
	{
		sv_ptr = av_fetch( array, i, 0 );
		if( sv_ptr == NULL )
			croak( "av_fetch returned NULL in ibwrti()\nn" );
		buf[ i ] = SvIV(*sv_ptr);
	}
	RETVAL = ibwrt(ud, buf, cnt);
	free( buf );
#line 856 "LinuxGpib.c"
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ThreadIbsta); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ThreadIbsta)
{
    dVAR; dXSARGS;
    if (items != 0)
       croak_xs_usage(cv,  "");
    {
	int	RETVAL;
	dXSTARG;

	RETVAL = ThreadIbsta();
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ThreadIberr); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ThreadIberr)
{
    dVAR; dXSARGS;
    if (items != 0)
       croak_xs_usage(cv,  "");
    {
	int	RETVAL;
	dXSTARG;

	RETVAL = ThreadIberr();
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ThreadIbcnt); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ThreadIbcnt)
{
    dVAR; dXSARGS;
    if (items != 0)
       croak_xs_usage(cv,  "");
    {
	int	RETVAL;
	dXSTARG;

	RETVAL = ThreadIbcnt();
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}


XS_EUPXS(XS_LinuxGpib_ThreadIbcntl); /* prototype to pass -Wmissing-prototypes */
XS_EUPXS(XS_LinuxGpib_ThreadIbcntl)
{
    dVAR; dXSARGS;
    if (items != 0)
       croak_xs_usage(cv,  "");
    {
	long	RETVAL;
	dXSTARG;

	RETVAL = ThreadIbcntl();
	XSprePUSH; PUSHi((IV)RETVAL);
    }
    XSRETURN(1);
}

#ifdef __cplusplus
extern "C"
#endif
XS_EXTERNAL(boot_LinuxGpib); /* prototype to pass -Wmissing-prototypes */
XS_EXTERNAL(boot_LinuxGpib)
{
#if PERL_VERSION_LE(5, 21, 5)
    dVAR; dXSARGS;
#else
    dVAR; dXSBOOTARGSXSAPIVERCHK;
#endif
#if (PERL_REVISION == 5 && PERL_VERSION < 9)
    char* file = __FILE__;
#else
    const char* file = __FILE__;
#endif

    PERL_UNUSED_VAR(file);

    PERL_UNUSED_VAR(cv); /* -W */
    PERL_UNUSED_VAR(items); /* -W */
#if PERL_VERSION_LE(5, 21, 5)
    XS_VERSION_BOOTCHECK;
#  ifdef XS_APIVERSION_BOOTCHECK
    XS_APIVERSION_BOOTCHECK;
#  endif
#endif

        (void)newXSproto_portable("LinuxGpib::constant", XS_LinuxGpib_constant, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibcac", XS_LinuxGpib_ibcac, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibclr", XS_LinuxGpib_ibclr, file, "$");
        (void)newXSproto_portable("LinuxGpib::ibcmd", XS_LinuxGpib_ibcmd, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ibconfig", XS_LinuxGpib_ibconfig, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ibdev", XS_LinuxGpib_ibdev, file, "$$$$$$");
        (void)newXSproto_portable("LinuxGpib::ibdma", XS_LinuxGpib_ibdma, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibeot", XS_LinuxGpib_ibeot, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibevent", XS_LinuxGpib_ibevent, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibfind", XS_LinuxGpib_ibfind, file, "$");
        (void)newXSproto_portable("LinuxGpib::ibgts", XS_LinuxGpib_ibgts, file, "$$");
        (void)newXSproto_portable("LinuxGpib::iblines", XS_LinuxGpib_iblines, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibloc", XS_LinuxGpib_ibloc, file, "$");
        (void)newXSproto_portable("LinuxGpib::ibonl", XS_LinuxGpib_ibonl, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibpad", XS_LinuxGpib_ibpad, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibrd", XS_LinuxGpib_ibrd, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ibrdi", XS_LinuxGpib_ibrdi, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ibrpp", XS_LinuxGpib_ibrpp, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibrsp", XS_LinuxGpib_ibrsp, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibrsv", XS_LinuxGpib_ibrsv, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibsad", XS_LinuxGpib_ibsad, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibsic", XS_LinuxGpib_ibsic, file, "$");
        (void)newXSproto_portable("LinuxGpib::ibsre", XS_LinuxGpib_ibsre, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibtmo", XS_LinuxGpib_ibtmo, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibtrg", XS_LinuxGpib_ibtrg, file, "$");
        (void)newXSproto_portable("LinuxGpib::ibwait", XS_LinuxGpib_ibwait, file, "$$");
        (void)newXSproto_portable("LinuxGpib::ibwrt", XS_LinuxGpib_ibwrt, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ibwrti", XS_LinuxGpib_ibwrti, file, "$$$");
        (void)newXSproto_portable("LinuxGpib::ThreadIbsta", XS_LinuxGpib_ThreadIbsta, file, "");
        (void)newXSproto_portable("LinuxGpib::ThreadIberr", XS_LinuxGpib_ThreadIberr, file, "");
        (void)newXSproto_portable("LinuxGpib::ThreadIbcnt", XS_LinuxGpib_ThreadIbcnt, file, "");
        (void)newXSproto_portable("LinuxGpib::ThreadIbcntl", XS_LinuxGpib_ThreadIbcntl, file, "");
#if PERL_VERSION_LE(5, 21, 5)
#  if PERL_VERSION_GE(5, 9, 0)
    if (PL_unitcheckav)
        call_list(PL_scopestack_ix, PL_unitcheckav);
#  endif
    XSRETURN_YES;
#else
    Perl_xs_boot_epilog(aTHX_ ax);
#endif
}


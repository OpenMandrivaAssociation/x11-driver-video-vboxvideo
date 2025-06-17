%define _disable_ld_no_undefined 1

%ifarch aarch64
%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%endif

%define	upname xf86-video-vbox
%define date 20260617

Summary:	VirtualBox video driver for the Xorg X server
Name:		x11-driver-video-vboxvideo
Version:	1.0.2%{?date:~%{date}}
Release:	1
%if 0%{?date:1}
Source0:	https://github.com/X11Libre/xf86-video-vbox/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
%else
Source0:	https://xorg.freedesktop.org/releases/individual/driver/%{upname}-%{version}.tar.xz
%endif
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xextproto)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(fontsproto)
BuildRequires:	pkgconfig(pciaccess)
BuildSystem:	autotools

%description
VirtualBox video driver for the Xorg X server.

%prep -a
[ -e autogen.sh ] && NOCONFIGURE=1 ./autogen.sh

%files
%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
%{_mandir}/man4/vboxvideo.*

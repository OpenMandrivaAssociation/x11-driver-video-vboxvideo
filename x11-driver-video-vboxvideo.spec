%define	upname xf86-video-vboxvideo

Summary:	VirtualBox video driver for the Xorg X server
Name:		x11-driver-video-vboxvideo
Version:	1.0.0
Release:	3
Source0:	http://xorg.freedesktop.org/releases/individual/driver/%{upname}-%{version}.tar.bz2
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xextproto)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(fontsproto)
BuildRequires:	pkgconfig(pciaccess)

%description
VirtualBox video driver for the Xorg X server.

%prep
%autosetup -n %{upname}-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
%{_mandir}/man4/vboxvideo.*

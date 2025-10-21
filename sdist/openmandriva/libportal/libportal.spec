%global debug_package %{nil}

%define major 1
%define libname %mklibname portal
%define devname %mklibname portal -d

Name:		libportal
Version:	0.9.1
Release:	1
Source0:	https://github.com/flatpak/libportal/archive/%{version}/%{name}-%{version}.tar.gz
# Fixes Qt6 Build Error
Patch0:     https://github.com/flatpak/libportal/commit/796053d2eebe4532aad6bd3fd80cdf3b197806ec.patch
Summary:	Flatpak portal library
URL:		https://github.com/flatpak/libportal
License:	LGPLv3
Group:		System/Libraries

BuildSystem:	meson
# BuildOption:   -Dbackend-qt6=disabled

BuildRequires:	vala-tools
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(Qt5ServiceSupport)
BuildRequires:	gi-docgen
%description
libportal provides GIO-style async APIs for most Flatpak portals.

%package -n %{libname}
Summary:	Flatpak portal library
Group:		System/Libraries

%description -n %{libname}
libportal provides GIO-style async APIs for most Flatpak portals.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1

%files
%license COPYING

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*
%{_datadir}/vala/vapi/*
%{_docdir}/%{name}-1

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%global debug_package %{nil}

Name:		breeze-plus
Version:	6.17.0
Release:	1
Source0:	https://github.com/mjkim0727/breeze-plus/archive/refs/tags/%{version}.tar.gz
Summary:	Breeze theme with additional icons
URL:		https://github.com/mjkim0727/breeze-plus/
License:	LGPLv2.1
Group:		Desktop Environment/KDE/Icons


%description
%summary.

%prep
%autosetup -p1

%install
install -d %{buildroot}%{_iconsdir}
cp -r src/* %{buildroot}%{_iconsdir}/

%transfiletriggerin -- %{_iconsdir}/breeze-plus
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_iconsdir}/breeze-plus &>/dev/null || :
fi

%transfiletriggerin -- %{_iconsdir}/breeze-plus-dark
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache --force %{_iconsdir}/breeze-plus-dark &>/dev/null || :
fi


%files
%license LICENSE
%{_iconsdir}/breeze-plus*

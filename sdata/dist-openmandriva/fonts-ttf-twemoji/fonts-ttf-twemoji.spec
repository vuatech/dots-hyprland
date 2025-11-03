%global commit0 ac1703e9d7feebbf5443a986e08332b1e1c5afcf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global foundry twitter
%global fontname twemoji
%global Fontname Twemoji


Name:           %{foundry}-%{fontname}-fonts
Version:        14.0.2
Release:        1
Summary:        Twitter Emoji for everyone

# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In twemoji source
## Artwork is Creative Commons Attribution 4.0 International
## Non-artwork is MIT
# Automatically converted from old format: OFL and ASL 2.0 and CC-BY and MIT - review is highly recommended.
License:        LicenseRef-Callaway-OFL AND Apache-2.0 AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-MIT
URL:            https://twemoji.twitter.com/
Source0:        https://github.com/googlei18n/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
# Source2:        https://src.fedoraproject.org/rpms/twitter-twemoji-fonts/blob/rawhide/f/com.twitter.twemoji.metainfo.xml
Source4:        https://github.com/%{foundry}/%{fontname}/archive/v%{version}.tar.gz#/%{fontname}-%{version}.tar.gz

Patch0:         https://src.fedoraproject.org/rpms/twitter-twemoji-fonts/blob/rawhide/f/noto-emoji-build-all-flags.patch
#Patch1:         https://src.fedoraproject.org/rpms/twitter-twemoji-fonts/blob/rawhide/f/noto-emoji-use-gm.patch
#Patch2:         https://src.fedoraproject.org/rpms/twitter-twemoji-fonts/blob/rawhide/f/noto-emoji-use-system-pngquant.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  graphicsmagick
BuildRequires:  pkgconfig(cairo)
BuildRequires:  fontpackages-devel
BuildRequires:  python%{pyver}dist(fonttools)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  python%{pyver}dist(notofonttools)
BuildRequires:  pngquant
BuildRequires:  python3-devel
BuildRequires:  zopfli
BuildRequires:	fonttools
BuildRequires:	appstream-util

Requires:       fontpackages-filesystem


%description
A color emoji font with a flat visual style, designed and used by Twitter.


%prep
%autosetup -p1 -n noto-emoji-%{commit0}
mv LICENSE LICENSE-BUILD

tar -xf %{SOURCE4}
sed 's/Noto Color Emoji/Twemoji/; s/NotoColorEmoji/Twemoji/; s/Copyright .* Google Inc\./Twitter, Inc and other contributors./; s/ Version .*/ %{version}/; s/.*is a trademark.*//; s/Google, Inc\./Twitter, Inc and other contributors/; s,http://www.google.com/get/noto/,https://github.com/twitter/twemoji/,; s/.*is licensed under.*/      Creative Commons Attribution 4.0 International/; s,http://scripts.sil.org/OFL,http://creativecommons.org/licenses/by/4.0/,' NotoColorEmoji.tmpl.ttx.tmpl > Twemoji.tmpl.ttx.tmpl
pushd %{fontname}-%{version}/assets/72x72/
for png in *.png; do
    mv $png emoji_u${png//-/_}
done
popd


%build
%make_build %{?_smp_mflags} OPT_CFLAGS="$RPM_OPT_FLAGS" EMOJI=%{Fontname} EMOJI_SRC_DIR=%{fontname}-%{version}/assets/72x72 FLAGS= BODY_DIMENSIONS=76x72


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{Fontname}.ttf %{buildroot}%{_fontdir}

# mkdir -p %{buildroot}%{_datadir}/metainfo
# install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/metainfo


%check
# appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.%{foundry}.%{fontname}.metainfo.xml


%_font_pkg %{Fontname}.ttf
%license LICENSE-BUILD
%license %{fontname}-%{version}/LICENSE
%license %{fontname}-%{version}/LICENSE-GRAPHICS
%doc %{fontname}-%{version}/CONTRIBUTING.md
%doc %{fontname}-%{version}/README.md
%{_datadir}/metainfo/com.%{foundry}.%{fontname}.metainfo.xml

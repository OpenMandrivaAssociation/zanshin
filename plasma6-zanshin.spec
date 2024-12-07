#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:           plasma6-zanshin
Version:        24.08.3
Release:        %{?git:0.%{git}.}2
Summary:        Getting Things Done application
Group:          Graphical desktop/KDE
License:        GPLv2+ and LGPLv2+
URL:            https://zanshin.kde.org
%if 0%{?git}
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/zanshin/-/archive/%{gitbranch}/zanshin-%{gitbranchd}.tar.bz2#/zanshin-%{git}.tar.bz2
%else
Source0:	https://invent.kde.org/plasma-mobile/plasma-angelfish/-/archive/v%{version}/plasma-angelfish-v%{version}.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/zanshin/-/archive/%{gitbranch}/zanshin-%{gitbranchd}.tar.bz2#/zanshin-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/zanshin-%{version}.tar.xz
%endif
%endif

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6AkonadiSearch)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KPim6LdapCore)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qtmultimedia-gstreamer

%description
A Getting Things Done application which aims at getting your mind like water.

%files -f zanshin.lang
%{_bindir}/zanshin
%{_bindir}/zanshin-migrator
%{_libdir}/qt6/plugins/kf6/krunner/org.kde.zanshin.so
%{_libdir}/qt6/plugins/pim6/kontact/kontact_zanshinplugin.so
%{_libdir}/qt6/plugins/zanshin_part.so
%{_datadir}/applications/org.kde.zanshin.desktop
%{_datadir}/icons/hicolor/*/apps/zanshin.*
%{_datadir}/metainfo/org.kde.zanshin.metainfo.xml

#---------------------------------------------------------------


%prep
%autosetup -p1 -n zanshin-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang zanshin

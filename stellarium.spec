
%define title	Stellarium

Name:		stellarium 
Version:	0.14.3
Release:	1
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2+
URL:		http://www.stellarium.org
Source0:	http://sourceforge.net/projects/stellarium/files/Stellarium-sources/0.14.2/%{name}-%{version}.tar.gz
Buildrequires:	pkgconfig(glu) 
Buildrequires:	pkgconfig(sdl)
Buildrequires:	pkgconfig(SDL_mixer)
Buildrequires:	pkgconfig(libpng)
Buildrequires:	jpeg-devel
Buildrequires:	pkgconfig(freetype2)
Buildrequires:	qt5-devel
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	gettext-devel
Buildrequires:	cmake
Buildrequires:	imagemagick

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q

%build 
%cmake_qt5
%make

%install
cd build
%makeinstall_std INSTALL="%{_bindir}/install -c -p"
cd -

mkdir -p %{buildroot}%{_datadir}/applications

install -d -m 755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[1] \
    %{buildroot}%{_liconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[2] \
    %{buildroot}%{_iconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[4] \
    %{buildroot}%{_miconsdir}/stellarium.png


%files
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/*.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/stellarium.xpm
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png


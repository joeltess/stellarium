%define name	stellarium
%define version	0.9.1
%define release	%mkrel 2
%define title	Stellarium

Name:		%{name} 
Version:	%{version} 
Release:	%{release} 
Summary:	Desktop planetarium 
Group:		Sciences/Astronomy
License:	GPLv2 
URL:		http://www.stellarium.org
Source:		http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
Patch0:		stellarium-0.8.2-manpage.diff
Buildrequires:	mesaglu-devel 
Buildrequires:	SDL-devel
Buildrequires:	SDL_mixer-devel
Buildrequires:	png-devel
Buildrequires:	jpeg-devel
Buildrequires:	freetype2-devel
Buildrequires:	qt4-devel
BuildRequires:	boost-devel
BuildRequires:	gettext-devel
Buildrequires:	cmake
Buildrequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Stellarium renders 3D photo-realistic skies in real time. 
With stellarium, you really see what you can see with your eyes,
binoculars or a small telescope.


%prep 
%setup -q
%patch0 -p1 -b .manpage 

%build 
export QTDIR=/usr/lib/qt4
export PATH=$QTDIR/bin:$PATH
%cmake
%make


%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -c -p"

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=Desktop planetarium
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Science;Astronomy;
EOF

install -d -m 755 %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[1] \
    %{buildroot}%{_liconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[2] \
    %{buildroot}%{_iconsdir}/stellarium.png
convert  %{buildroot}%{_datadir}/stellarium/data/stellarium.ico[4] \
    %{buildroot}%{_miconsdir}/stellarium.png
%find_lang %{name}

%clean 
rm -rf %{buildroot} 

%post
%{update_menus}

%postun
%{clean_menus}

%files -f build/%{name}.lang
%defattr(-,root,root,0755) 
%doc README COPYING AUTHORS 
%{_bindir}/%{name} 
%{_datadir}/%{name}/
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

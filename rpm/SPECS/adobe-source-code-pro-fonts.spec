%global fontname source-code-pro
%global fontconf 63-%{fontname}.conf

Name:           adobe-source-code-pro-fonts
Version:        1.009
Release:        1%{?dist}
Summary:        A set of OpenType fonts designed for user interfaces

License:        OFL
URL:            http://sourceforge.net/projects/sourcesans.adobe/

#unable to build from source : source format is unbuldable with free software
Source0:        https://github.com/downloads/adobe/Source-Code-Pro/SourceCodePro_FontsOnly-%{version}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Source Code Pro is a set of OpenType fonts that have been designed to work 
well in user interface (UI) environments, as well as in text setting for 
screen and print.

%prep
%setup -q -n SourceCodePro_FontsOnly-%{version}

sed -i "s|\r||" LICENSE.txt

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf

%doc *.txt SourceCodeProReadMe.html


%changelog
* Thu Sep 27 2012 Matt Rose <mattrose@folkwolf.net> - 1.009-1
- initial release


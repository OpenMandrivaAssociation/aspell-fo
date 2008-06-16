%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.2.16-1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageeng faroese
%define languageenglazy Faroese
%define languagecode fo

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.2.16.1
Release:       %mkrel 5
Epoch:         1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-fo

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright doc/contributors
%{_libdir}/aspell-%{aspell_ver}/*



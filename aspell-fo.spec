%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.2.16-1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageeng faroese
%define languageenglazy Faroese
%define languagecode fo

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	0.2.16.1
Release:	19
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-fo
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 README Copyright

%files
%doc README Copyright doc/contributors
%{_libdir}/aspell-%{aspell_ver}/*


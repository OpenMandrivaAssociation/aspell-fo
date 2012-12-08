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
Release:       %mkrel 11
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.16.1-10mdv2011.0
+ Revision: 662813
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.16.1-9mdv2011.0
+ Revision: 603208
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.16.1-8mdv2010.1
+ Revision: 518922
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.16.1-7mdv2010.0
+ Revision: 413065
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1:0.2.16.1-6mdv2009.1
+ Revision: 350023
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:0.2.16.1-5mdv2009.0
+ Revision: 220377
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1:0.2.16.1-4mdv2008.1
+ Revision: 182426
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:0.2.16.1-3mdv2008.1
+ Revision: 148765
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.16.1-2mdv2007.0
+ Revision: 123253
- Import aspell-fo

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.16.1-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.2.16.1-1mdk
- new release

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.51.0-1mdk
- updated to 0.51.0


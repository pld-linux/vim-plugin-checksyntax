%define		plugin	checksyntax
Summary:	Check a file's syntax when saving a file (PHP, Ruby, Tex ...) with Vim
Name:		vim-plugin-%{plugin}
Version:	2.03
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	https://github.com/tomtom/checksyntax_vim/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	235de7ae32b861262d74c4bf0212da90
URL:		https://github.com/tomtom/checksyntax_vim
Requires:	vim-rt >= 4:7.2.170
Requires(post,postun):	vim
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
The checksyntax plugin runs an external syntax checker for the current
buffer whenever the buffer is saved. Syntax errors are managed as
location or quickfix lists. If any syntax error occurs, the
location-list is opened. You can use any location-list related command
to navigate the list of syntax errors.

%prep
%setup -qn checksyntax_vim-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a autoload doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

gzip -9nf $RPM_BUILD_ROOT%{_vimdatadir}/doc/checksyntax.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
vim -c "helptags %{_vimdatadir}/doc" -c "q"

%postun
vim -c "helptags %{_vimdatadir}/doc" -c "q"

%files
%defattr(644,root,root,755)
%doc README CHANGES.TXT
%{_vimdatadir}/autoload/*.vim
%{_vimdatadir}/autoload/checksyntax
%{_vimdatadir}/doc/checksyntax.txt*
%{_vimdatadir}/plugin/checksyntax.vim

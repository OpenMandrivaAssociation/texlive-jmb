Name:		texlive-jmb
Version:	52718
Release:	2
Summary:	BibTeX style for the Journal of Theoretical Biology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jmb
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmb.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This BibTeX bibliography style is for the Journal of Molecular
Biology and Journal of Theoretical Biology; the accompanying
LaTeX (2.09) package is a close relative of apalike.sty in the
BibTeX distribution; it features author-date references. The
bibliography style has control over whether to print reference
titles; if your database contains an article with the cite key
"TitlesOn", and you invoke it by \nocite{TitlesOn}, titles will
be printed; otherwise titles will not be printed.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jmb
%{_texmfdistdir}/bibtex/bst/jmb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

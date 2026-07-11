%global tl_name jmb
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.21
Release:	%{tl_revision}.1
Summary:	BibTeX style for the Journal of Theoretical Biology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/jmb
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jmb.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This BibTeX bibliography style is for the Journal of Molecular Biology
and Journal of Theoretical Biology; the accompanying LaTeX (2.09)
package is a close relative of apalike.sty in the BibTeX distribution;
it features author-date references. The bibliography style has control
over whether to print reference titles; if your database contains an
article with the cite key "TitlesOn", and you invoke it by
\nocite{TitlesOn}, titles will be printed; otherwise titles will not be
printed.


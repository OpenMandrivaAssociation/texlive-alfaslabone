%global tl_name alfaslabone
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	The Alfa Slab One font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/alfaslabone
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alfaslabone.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The alfaslabone package supports the Alfa Slab One font face for LaTeX.
There is only a Regular font face. It's useful for book-chapter
headlines.


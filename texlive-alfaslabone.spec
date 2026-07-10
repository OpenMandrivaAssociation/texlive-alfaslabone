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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The alfaslabone package supports the Alfa Slab One font face for LaTeX.
There is only a Regular font face. It's useful for book-chapter
headlines.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/map/dvips/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/opentype/public/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/type1/public/alfaslabone
%dir %{_datadir}/texmf-dist/fonts/vf/public/alfaslabone
%doc %{_datadir}/texmf-dist/doc/fonts/alfaslabone/LICENSE.TXT
%doc %{_datadir}/texmf-dist/doc/fonts/alfaslabone/README
%doc %{_datadir}/texmf-dist/doc/fonts/alfaslabone/alfaslabone-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/alfaslabone/alfaslabone-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_5xld5w.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_adz5lu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_d2anrk.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_lzhlbi.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_rymxky.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_taosrr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/alfaslabone/a_vqpkf5.enc
%{_datadir}/texmf-dist/fonts/map/dvips/alfaslabone/AlphaSlabOne.map
%{_datadir}/texmf-dist/fonts/opentype/public/alfaslabone/AlphaSlabOne-Regular.otf
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/alfaslabone/AlphaSlabOne-Regular-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/type1/public/alfaslabone/AlphaSlabOne-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/public/alfaslabone/AlphaSlabOne-Regular-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/alfaslabone/AlphaSlabOne-Regular-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/alfaslabone/AlphaSlabOne-Regular-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/alfaslabone/AlphaSlabOne-Regular-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/alfaslabone/AlphaSlabOne-Regular-tlf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/alfaslabone/LY1AlphaSlabOne-Sup.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/LY1AlphaSlabOne-TLF.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/OT1AlphaSlabOne-Sup.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/OT1AlphaSlabOne-TLF.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/T1AlphaSlabOne-Sup.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/T1AlphaSlabOne-TLF.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/TS1AlphaSlabOne-TLF.fd
%{_datadir}/texmf-dist/tex/latex/alfaslabone/alfaslabone.sty

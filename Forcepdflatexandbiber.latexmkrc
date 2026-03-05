# --- Core Engine Settings ---
$pdf_mode = 1;          # Force pdflatex (use 1 for pdf, 4 for lualatex, 5 for xelatex)
$postscript_mode = 0;   # Disable PostScript
$dvi_mode = 0;          # Disable DVI

# --- Bibliography Tool ---
$bibtex_use = 2;        # Use biber (1 for bibtex, 2 for biber)

# --- Automation & Cleanup ---
$preview_continuous_mode = 0; # Don't start in 'watch' mode by default
$cleanup_mode = 0;            # Keep intermediate files for faster subsequent builds

# --- Tool Flags ---
# -shell-escape is optional; add it if you use packages like 'minted'
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
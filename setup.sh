mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"\"\n\
\n\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
maxUploadSize = 200\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
\n\
[theme]\n\
primaryColor = \"#FF6B35\"\n\
backgroundColor = \"#1e1e1e\"\n\
secondaryBackgroundColor = \"#2d2d2d\"\n\
textColor = \"#ffffff\"\n\
\n\
[runner]\n\
magicEnabled = false\n\
" > ~/.streamlit/config.toml

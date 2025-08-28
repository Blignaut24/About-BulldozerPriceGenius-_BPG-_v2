mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
maxUploadSize = 50\n\
enableStaticServing = true\n\
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
fastReruns = false\n\
\n\
[logger]\n\
level = \"error\"\n\
\n\
[client]\n\
showErrorDetails = false\n\
" > ~/.streamlit/config.toml

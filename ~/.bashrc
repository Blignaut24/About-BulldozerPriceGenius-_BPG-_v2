# Custom Git Bash configuration
# Set magenta color and cat symbol for prompt

# Color definitions
MAGENTA='\[\033[35m\]'
RESET='\[\033[0m\]'
BOLD='\[\033[1m\]'

# Cat symbol (you can change this to any cat emoji or symbol you prefer)
CAT_SYMBOL="🐱"

# Custom prompt with magenta color and cat symbol
# Format: 🐱 username@hostname:current_directory$ 
export PS1="${MAGENTA}${BOLD}${CAT_SYMBOL} \u@\h:\w\$ ${RESET}"

# Alternative simpler version (uncomment if you prefer this):
# export PS1="${MAGENTA}${CAT_SYMBOL} \w\$ ${RESET}"

# Optional: Add git branch information to prompt
# Uncomment the following lines if you want to see git branch in your prompt
# parse_git_branch() {
#     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
# }
# export PS1="${MAGENTA}${BOLD}${CAT_SYMBOL} \u@\h:\w\$(parse_git_branch)\$ ${RESET}"

# Make sure this file is sourced for new terminal sessions
echo "Custom Git Bash prompt loaded with magenta color and cat symbol! 🐱"

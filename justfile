set positional-arguments

# Show how to use this justfile
default:
    @echo "Usage: just search <term>"
    @echo "Example: just search AI-Frontend"

# Search blog posts by path/filename or by title in front matter
search term:
    @echo "=== Files matching '{{ term }}' in path ==="
    @find content/post -type f | rg -i -F {{ quote(term) }} || true
    @echo
    @echo "=== Posts with title matching '{{ term }}' ==="
    @rg -i -g '**/index.md' '^title:' content/post 2>/dev/null | rg -i -F {{ quote(term) }} || true

name: Auto-update SUMMARY.md

on:
  push:
    paths:
      - '**.md'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update-summary:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      
      - name: Update SUMMARY.md
        run: |
          #!/bin/bash
          set -e
          
          echo "🔍 Scanning repository for markdown files..."
          
          # Find all .md files except SUMMARY.md and README.md
          all_md_files=$(find . -type f -name "*.md" \
            ! -path "./SUMMARY.md" \
            ! -path "./README.md" \
            ! -path "*/node_modules/*" \
            ! -path "*/.git/*" \
            | sort)
          
          total_files=$(echo "$all_md_files" | wc -l)
          echo "📄 Found $total_files markdown file(s) to check"
          
          # Read SUMMARY.md content
          summary_content=$(cat SUMMARY.md)
          
          # Track missing files
          missing_files=()
          found_files=()
          
          # Check each .md file
          for file in $all_md_files; do
            clean_path="${file#./}"
            
            if echo "$summary_content" | grep -q "$clean_path"; then
              found_files+=("$clean_path")
            else
              missing_files+=("$clean_path")
            fi
          done
          
          echo "✅ Files already in SUMMARY.md: ${#found_files[@]}"
          echo "➕ Files to add: ${#missing_files[@]}"
          
          # Add missing files to SUMMARY.md
          if [ ${#missing_files[@]} -gt 0 ]; then
            echo ""
            echo "📝 Adding missing files to SUMMARY.md:"
            echo "" >> SUMMARY.md
            echo "## Auto-added pages" >> SUMMARY.md
            
            for file in "${missing_files[@]}"; do
              # Extract filename without extension for title
              filename=$(basename "$file" .md)
              # Convert hyphens/underscores to spaces and capitalize first letter of each word
              title=$(echo "$filename" | sed 's/[-_]/ /g' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
              
              echo "* [$title]($file)" >> SUMMARY.md
              echo "  ✓ Added: $file as '$title'"
            done
          fi
          
          # Fix capitalization in existing entries
          echo ""
          echo "🔤 Fixing capitalization in SUMMARY.md..."
          
          # Create a temporary file
          temp_file=$(mktemp)
          
          # Process SUMMARY.md line by line
          while IFS= read -r line; do
            # Check if line contains a markdown link with .md extension
            if echo "$line" | grep -q '\[.*\](.*\.md)'; then
              # Extract the title and path
              if [[ $line =~ \[([^\]]+)\]\(([^\)]+)\) ]]; then
                old_title="${BASH_REMATCH[1]}"
                path="${BASH_REMATCH[2]}"
                
                # Capitalize first letter of each word in title
                new_title=$(echo "$old_title" | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
                
                # Get the indentation/prefix (*, -, numbers, spaces)
                prefix=$(echo "$line" | sed 's/\[.*//')
                
                # Reconstruct the line with capitalized title
                new_line="${prefix}[$new_title]($path)"
                
                if [ "$old_title" != "$new_title" ]; then
                  echo "  ✓ Fixed: '$old_title' → '$new_title'"
                fi
                
                echo "$new_line" >> "$temp_file"
              else
                echo "$line" >> "$temp_file"
              fi
            else
              # Keep non-link lines as-is
              echo "$line" >> "$temp_file"
            fi
          done < SUMMARY.md
          
          # Replace original with fixed version
          mv "$temp_file" SUMMARY.md
          
          echo ""
          echo "✅ SUMMARY.md updated successfully!"
      
      - name: Commit changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          
          if git diff --quiet SUMMARY.md; then
            echo "✅ No changes needed - SUMMARY.md is up to date!"
          else
            git add SUMMARY.md
            git commit -m "chore: auto-update SUMMARY.md with new pages and fix capitalization"
            git push
            echo "✅ Changes committed and pushed!"
          fi
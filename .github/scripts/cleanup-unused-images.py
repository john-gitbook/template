#!/usr/bin/env python3
"""
Script to find and remove unused images from .gitbook/assets folder.
Scans all .md files to check if images are referenced.
"""

import os
import re
import sys
from pathlib import Path
from typing import Set, List

def find_all_assets(assets_dir: str = ".gitbook/assets") -> Set[str]:
    """Find all files in the assets directory."""
    assets_path = Path(assets_dir)
    if not assets_path.exists():
        print(f"❌ Assets directory '{assets_dir}' not found")
        return set()
    
    assets = set()
    for root, _, files in os.walk(assets_path):
        for file in files:
            # Get relative path from repo root
            rel_path = os.path.relpath(os.path.join(root, file))
            assets.add(rel_path)
    
    print(f"📁 Found {len(assets)} files in {assets_dir}")
    return assets

def find_all_markdown_files(root_dir: str = ".") -> List[str]:
    """Find all .md files in the repository."""
    md_files = []
    for root, _, files in os.walk(root_dir):
        # Skip .git directory and node_modules
        if '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"📝 Found {len(md_files)} markdown files")
    return md_files

def find_referenced_assets(md_files: List[str], assets: Set[str]) -> Set[str]:
    """
    Find which assets are referenced in markdown files.
    Checks for various markdown image patterns.
    """
    referenced = set()
    
    # Patterns to match image references
    # ![alt](.gitbook/assets/image.png)
    # ![alt](../.gitbook/assets/image.png)
    # <img src=".gitbook/assets/image.png">
    # Direct file references
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check each asset to see if it's referenced
                for asset in assets:
                    asset_name = os.path.basename(asset)
                    asset_path_variants = [
                        asset,  # Full path: .gitbook/assets/image.png
                        asset.replace('.gitbook/assets/', ''),  # Just filename
                        f"../{asset}",  # Relative path
                        f"../../{asset}",  # Deeper relative path
                        asset_path_variants_normalized(md_file, asset)
                    ]
                    
                    # Check if any variant is in the content
                    for variant in asset_path_variants:
                        if variant and variant in content:
                            referenced.add(asset)
                            break
                    
                    # Also check for the filename without path
                    if asset_name in content:
                        referenced.add(asset)
                        
        except Exception as e:
            print(f"⚠️  Warning: Could not read {md_file}: {e}")
    
    print(f"✅ Found {len(referenced)} referenced assets")
    return referenced

def asset_path_variants_normalized(md_file: str, asset: str) -> str:
    """Generate normalized relative path from md file to asset."""
    try:
        md_dir = os.path.dirname(os.path.abspath(md_file))
        asset_abs = os.path.abspath(asset)
        rel_path = os.path.relpath(asset_abs, md_dir)
        return rel_path
    except:
        return ""

def delete_unused_assets(unused_assets: Set[str], dry_run: bool = False) -> None:
    """Delete unused assets from the repository."""
    if not unused_assets:
        print("\n✨ No unused assets found! Your repository is clean.")
        return
    
    print(f"\n🗑️  Found {len(unused_assets)} unused assets:")
    for asset in sorted(unused_assets):
        print(f"   - {asset}")
    
    if dry_run:
        print("\n🔍 DRY RUN: No files were deleted.")
        print("   Remove the --dry-run flag to actually delete these files.")
        return
    
    print("\n🗑️  Deleting unused assets...")
    deleted_count = 0
    for asset in unused_assets:
        try:
            if os.path.exists(asset):
                os.remove(asset)
                deleted_count += 1
                print(f"   ✓ Deleted: {asset}")
        except Exception as e:
            print(f"   ✗ Error deleting {asset}: {e}")
    
    print(f"\n✅ Successfully deleted {deleted_count} unused assets")

def main():
    """Main function to orchestrate the cleanup process."""
    print("🧹 GitBook Assets Cleanup Tool")
    print("=" * 50)
    
    # Check for dry-run flag
    dry_run = "--dry-run" in sys.argv
    assets_dir = ".gitbook/assets"
    
    # Allow custom assets directory
    for arg in sys.argv[1:]:
        if arg.startswith("--assets-dir="):
            assets_dir = arg.split("=")[1]
    
    # Step 1: Find all assets
    all_assets = find_all_assets(assets_dir)
    if not all_assets:
        print("No assets found. Exiting.")
        return
    
    # Step 2: Find all markdown files
    md_files = find_all_markdown_files()
    if not md_files:
        print("⚠️  No markdown files found. This seems unusual.")
        return
    
    # Step 3: Find referenced assets
    referenced_assets = find_referenced_assets(md_files, all_assets)
    
    # Step 4: Calculate unused assets
    unused_assets = all_assets - referenced_assets
    
    # Step 5: Delete unused assets
    delete_unused_assets(unused_assets, dry_run)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Summary:")
    print(f"   Total assets: {len(all_assets)}")
    print(f"   Referenced: {len(referenced_assets)}")
    print(f"   Unused: {len(unused_assets)}")
    
    # Exit with status code 1 if unused assets were found (for CI)
    if unused_assets and not dry_run:
        sys.exit(0)  # Success - cleaned up
    elif unused_assets and dry_run:
        sys.exit(1)  # Found issues in dry-run mode

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Download and extract the full FORCE 2020 well-log benchmark dataset from Zenodo.

Source: https://zenodo.org/records/4351156
DOI: 10.5281/zenodo.4351156
MD5: da0d72d5783a780ac71779453d9fbfbf
"""
import hashlib
import sys
import urllib.request
import zipfile
from pathlib import Path

ZENODO_URL = "https://zenodo.org/records/4351156/files/FORCE2020_all_wells.zip?download=1"
EXPECTED_MD5 = "da0d72d5783a780ac71779453d9fbfbf"

def download_and_extract():
    root = Path(__file__).resolve().parent.parent
    data_dir = root / "data" / "force2020"
    data_dir.mkdir(parents=True, exist_ok=True)
    zip_path = data_dir / "FORCE2020_all_wells.zip"
    extract_dir = data_dir / "extracted"

    if extract_dir.exists() and any(extract_dir.rglob("*.las")):
        print(f"Dataset already extracted at {extract_dir}. {len(list(extract_dir.rglob('*.las')))} LAS wells found.")
        return

    if not zip_path.exists():
        print(f"Downloading FORCE 2020 dataset (~162 MB) from Zenodo...")
        urllib.request.urlretrieve(ZENODO_URL, zip_path)
        print("Download complete.")

    print("Verifying MD5 checksum...")
    h = hashlib.md5()
    with open(zip_path, "rb") as f:
        while chunk := f.read(8192 * 1024):
            h.update(chunk)
    actual_md5 = h.hexdigest()
    print(f"MD5: {actual_md5}")
    if actual_md5 != EXPECTED_MD5:
        print(f"Warning: MD5 mismatch (expected {EXPECTED_MD5}, got {actual_md5})")
    else:
        print("MD5 verified successfully!")

    print(f"Extracting to {extract_dir}...")
    extract_dir.mkdir(exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_dir)
    print(f"Extraction complete! {len(list(extract_dir.rglob('*.las')))} wells available.")

if __name__ == "__main__":
    download_and_extract()

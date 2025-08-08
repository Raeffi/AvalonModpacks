#!/usr/bin/env python3
import argparse
import urllib3.request
import shutil
import zipfile
import tempfile

def main():
  parser = argparse.ArgumentParser(description="Sync GTNH modpack files.")
  parser.add_argument("-s", "--source", type=str, required=True, default="https://downloads.gtnewhorizons.com/ClientPacks/GT_New_Horizons_2.7.4_Client_Java_8.zip")
  args = parser.parse_args()

if __name__ == "__main__":
  main()

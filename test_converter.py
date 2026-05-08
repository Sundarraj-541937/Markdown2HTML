from pathlib import Path

def test_docs_folder_exists():
    assert Path("docs").exists()

def test_converter_file_exists():
    assert Path("converter.py").exists()
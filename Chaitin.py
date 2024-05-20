# See https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin
import zlib

def read_task_from_file(file_path: str) -> str:
    """Read function from a specified python (or other code) file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def pseudo_chaitin_omega(data: str) -> int:
    """Theory from Chaitin: calculate an approximative Omega ."""
    compressed_data = zlib.compress(data.encode('utf-8'))
    return len(compressed_data) * 8 # bytes


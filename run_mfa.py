import subprocess

input_dir = 'sustained_vowels'
output_dir = 'sustained_vowels_aligned'

cmd = [
    'mfa', 'align',
    input_dir,
    'english_us_arpa',
    'english_us_arpa',
    output_dir,
    '--beam', '100',
    '--clean',
    '--overwrite'
]
subprocess.run(cmd, check=True, capture_output=True, text=True)
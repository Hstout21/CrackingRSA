PYTHON = python3
SCRIPT = rsaDecrypt.py
FILECIPHER = <FileNameForCipher>.input
FILEKEYS = <FileNameForKeys>.input

run:
	@(awk '{printf "%s\\n", $$0}' $(FILECIPHER); cat $(FILEKEYS)) | $(PYTHON) $(SCRIPT)
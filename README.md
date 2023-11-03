# link_scanner

This command-line tool is built to detect URL addresses within files located in a designated directory. It supports scanning various file types such as `.py`, `.yml`, `.yaml`, `.txt`, `.cfg`, `.ini`, and more. All discovered URL addresses are logged in a CSV file.

## Usage

To execute `link_scanner`, use the following command:

```bash
python main.py --dirpath path_to_dir_to_scan --output output.csv
```

If you want to customize it a bit you can use all args:

```bash
python main.py --dirpath your_directory --output output.csv --extensions .py,.yml,.yaml,.txt,.cfg,.ini --regex https?://\S+
```

## Output example

The resulting CSV file includes the discovered URLs and their respective file paths.

| URL                   | File                              | 
|-----------------------|-----------------------------------|
| http: //imnotscamlink | C://stable/and/secure/software.py |


### Command-Line Arguments:

- `--dirpath`: Directory where the scanning will take place.
- `--output`: The name of the CSV file for storing the scan results.
- `--extensions`: List of file extensions to be scanned, separated by commas.
- `--regex`: Regular expression for identifying URL addresses.

### Notes

- Use the command-line arguments to specify the scanning parameters.
- Ensure you have Python 3.x installed.
- Example command to execute the script is provided above.

# Public Domain Software
This software is released to the public domain without any license restrictions.

# Acknowledgments
This README was created with the assistance of OpenAI's ChatGPT, a large language model.
You can learn more about it [here](https://chat.openai.com/chat)

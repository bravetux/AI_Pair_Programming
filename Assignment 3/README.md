# Log Analyzer

This script analyzes a web server log file and counts the number of requests per IP address, saving the results to a CSV file.

## How to Use

1. **Ensure you have Python 3 installed.**

2. **Install Dependencies:**
   - You need the `kagglehub` package. Install it with:
     ```sh
     pip install kagglehub
     ```

3. **Run the Script:**
   - Open a terminal in the project directory.
   - Run the following command:
     ```sh
     python log_analyzer.py
     ```
   - The script will automatically download the latest web server access logs dataset from Kaggle and analyze the `access.log` file.

4. **Output:**
   - The results will be saved as `output.csv` in the `output` folder: `./output/output.csv`

## Example

```sh
python log_analyzer.py
```

After running, check the `output/output.csv` file for the results.

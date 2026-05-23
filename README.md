# High-Throughput Log Analytics Utility


A memory-efficient command-line interface (CLI) utility designed to stream, parse, and analyze large-scale system log files. This project demonstrates foundational software engineering principles including clean file I/O handling, string tokenization, and optimal data structure lookups.

##  Features 
- **Memory-Efficient Streaming:** Reads files line-by-line using a static $O(1)$ space complexity, ensuring the system safely processes gigabytes of logs without crashing RAM.
- **Blazing Fast Analytics:** Utilizes native hash mapping (dictionaries) to aggregate log levels and error frequencies in a single $O(N)$ pass.
- **Top-3 Error Isolation:** Automatically isolates and sorts high-frequency system failure messages.
- **Automated Reporting:** Generates a structured, clean `log_analysis_report.txt` file detailing execution metrics.

##  Performance Design
Unlike standard scripts that load entire datasets into memory using functions like `.readlines()`, this architecture maintains a constant memory footprint:

- **Time Complexity:** $O(N)$ where $N$ is the number of lines in the log file.
- **Space Complexity:** $O(1)$ constant auxiliary space for file reading.

##  How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/CYBER-CORE-DEV/log--analyzer.git](https://github.com/CYBER-CORE-DEV/log--analyzer.git)
2.Generate the dummy dataset:
python log_generator.py
  [[log generator.py](https://github.com/user-attachments/files/28171611/log.generator.py)]
3.Run the analytical engine:
python log_analyzer.py
  [log analyzer.py](https://github.com/user-attachments/files/28171648/log.analyzer.py)

	

   

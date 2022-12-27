# Justworks-Assignment

1. Install Python3 ( 3.10.x ) on mac/windows devices

   macOS devices -> https://docs.python-guide.org/starting/install3/osx/

   windows devices -> https://www.python.org/downloads/windows/
2. Adding python in windows / macOS after installing

   1. Windows -> https://realpython.com/add-python-to-path/
   2. macOS use this command in terminal

      1. if using zsh->

   ```
   echo "alias python=/usr/bin/python3" >> ~/.zshrc
   ```

   2. if using bash ->

   ```
   echo "alias python=/usr/bin/python3" >> ~/.bashrc
   ```

    restart the terminal after setting the environment variables in windows or entering the command in macOS

3. the csv file and ankit.py file location should be in the same directory.
4. csv file name should be "data_jw.csv"
5. Open the terminal at the location of the file.
6. Run Command: "pip3 install pandas"
7. Run command: "python3 ankit.py"
8. It will generate the output.csv in the same location.
9. In the output.csv, year is shown as MM/YY not as MM/YYYY.

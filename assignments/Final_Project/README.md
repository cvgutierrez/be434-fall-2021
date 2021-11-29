The program accepts either a file or a string, along with the language the file or string is in and the language you want to translate the file or string into, with an option to name the output directory.

If a neither a file or string is inputted, the program should stop after printing "There was nothing to translate. Please try again and input either a file or string." to the terminal

When run with the -h flag the following should appear:

$ ./project.py -h
usage: project.py [-h] [-l1 str] [-l2 str] [-i str] [-o DIR]

Translate a file or string into a different language with new files as an output in an output directory

optional arguments:
  -h, --help            show this help message and exit
  -l1 str, --language1 str
                        Input file's language (default: Korean)
  -l2 str, --language2 str
                        Language the file or string is being translated to (default: English)
  -i str, --input str   Input to translate (default: None)
  -o DIR, --outdir DIR  Output directory (default: sys.stdout)

  The output of the program should include an outputed directory containing three files: a file (1) with the original string/file, a file (2) with the translation of the original string/file into the desired output language, and a file (3) with the original string/file and the translated string/file.

  so if the program is run with the original string being Hello, the inputted language as English, and the outputted language as Spanish then in the outputted directory the three files should contain Hello in file (1), Hola in file (2), and english: Hello "\n" spanish: Hola in file (3).

  Unforunately with the translate package, some accents and special characters are not always used by the program and I am not sure why this is or how to fix it. I have also come to the realization that there is a limited amount of times you can use the translate package each day and so one might get something along the lines of:
  MYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY. NEXT AVAILABLE IN  17 HOURS 02 MINUTES 00 SECONDSVISIT HTTPS://MYMEMORY.TRANSLATED.NET/DOC/USAGELIMITS.PHP TO TRANSLATE MORE
as the output of the input being translated instead of the actual translation. Due to this, the test.py may not work correctly.
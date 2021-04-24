# Wage Calculator

The aim of this project was to write a program that tracks hours worked and wages earned.

## Project origins and overview
I chose this project as a way to track wages for free at my day job as the other programs I found online were either costly or lacking in features.

In this project, I have used multiple modules including datetime, xlsxwriter, re and tkinter. I used this combination as it allowed me to write the program I had originally envisaged - namely a program that could track chronological hours and export the resulting data to an Excel spreadsheet for further use.

## Usage instructions
The user is instructed to first input their hourly wage before being asked what time they started and finished working that day. An input of 'na' is required to indicate the user did not work on a particular day.

## Challenges faced
As this was my first full and more fleshed out project, I was not familiar with many of the modules and functions that would be required for the end product. 

After initially writing a lot of repetitive and inefficient code, I researched more concise ways of achieving what I wanted and ended up shortening an initial code of 6000+ chars to ~2000 chars. 

In the beginning I was calculating time differences as integers before that evolved into creating datetime objects. This was similar to my initial simple integer-check to check the correct format which eventually turned into using regex to ensure the user had used the correct HH:MM format. 

## Future project goals
As I have put this project temporarily on hold to pursue other projects that will use a wider array of techniques, I have written up a list of goals and evolutions I intend to implement here;
- Feature to allow user to add work breaks
- Date checking function so the program can be used across the working year and an eventual collation of working hours/wages in a database.
- Finishing and polishing of GUI

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License 
MIT License

Copyright (c) [2021] [Marco Macaluso]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


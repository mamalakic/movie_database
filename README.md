# SQL movie database
1. Run mySQL db creation
2. Run python script, add name, (optional) note
4. Repeat until bored

## Notes
Many parts of code were done with the help of ChatGPT

Genre column violates First Normal Form but it is not an important column to me

### How I found the columns I needed:
1. print(movie.\_\_dict\_\_)
2. Pass output to file
3. Open with notepad++:
4. Replace ", '" with ",\n'" so every new member goes into newline
5. Start of file contains members and contents of dictionary, end of file contains member names only

## TODO
- Add mass-imports (probably csv)
- Speed up querying to IMDb (if possible)




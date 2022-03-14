
Overview:

CS2CSV is a python GUI app designed to allow Kaart Team Leads to collect, investigate, analyse, and share changset statistics for ediotrs on thier team.




Usage:

CS2CSV holds team information in a pretty standard .Json file. The team file contains each editor's OSM UID and username, the editors full proper name, as well as their email address and their role on the team.

The user can import a team file, or create one from scratch, then edit it at any time and save the results.

Once a team file is created or imported, the user can select any number of editors from the team list for which to collect stats. An option titled "changeset report" in the menu bar will open a dialog allowing the user to select seacrh parmeters.

Within this dialog, the user can select the start and end dates of the serch timeframe they wish to gather. A number of built in methods are provided, i.e. Daily, Weekly & Monthly, which will search the last 24 hours, 7 days, and 30 days respectively.

A manual date selection section is also provided so the user can define a custom timeframe for the search.

Depending on how many editos are selected, the actual changeset query can take a substantial amount of time. folwing releases will see improvements to the background query function to try to speed this up, and at some point I will thread the Query function so it doesn't lock the UI, which isn't really terribly important but would be the decent thing to do.

Once the query is complete, the editor table will expand and populate each selected editor's table entry with detailed information on the number of changesets, specific stats on additions, modifications and deletions, as well as details on the number of mis-spelled comments & mis-spelled or missing hastags.

Under the menu bar, an option labeled "Changeset Comment Report" will open another dialog which will give deatils on changesets which contain mis-spellings or missing hashtags. Specifically, it will list any misspelled words or hashtags, and provide the changeset ID and date entered for each.

The User can also add new accepted words and hastags at any time, which will then be ignored by the comment & hashtag analyser.

Finally, the user can export the stats for the selected editors in the form of UID coded CSV file, which can be shared with their supervisors and team to help improve and maintain performance.

Future versions will feature an auto-email function and interactive charts to help the user visualize changes in statistics over time.





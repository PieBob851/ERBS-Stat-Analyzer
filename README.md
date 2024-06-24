# ERBS Stat Analyzer

To download games using the downloader, an API key is needed. To learn more about the API, visit https://developer.eternalreturn.io/.




# Analysis Methodology

Using the Eternal Return API, 2947 games were downloaded from top Camilo players in both North America and Korea (roughly 500 games were from North America, and about 2500 were from Korea).

Characters were then classified into the main role they may play in team compositions with Camilo. The list of all character classifications is as follows:

01 (Jackie): Diver
02 (Aya): Backline
03 (Fiora): Frontline
04 (Magnus): Frontline
05 (Zahir): Backline
06 (Nadine): Backline
07 (Hyunwoo): Frontline
08 (Hart): Backline
09 (Isol): Backline
10 (Li Dailin): Frontline
11 (Yuki): Frontline
12 (Hyejin): Backline
13 (Xiukai): Tank
14 (Chiara): Frontline
15 (Sissela): Backline
16 (Silvia): Diver
17 (Adriana): Backline
18 (Shoichi): Diver
19 (Emma): Backline
20 (Lenox): Tank
21 (Rozzi): Backline
22 (Luke): Frontline
23 (Cathy): Diver
24 (Adela): Backline
25 (Bernice): Backline
26 (Barbara): Frontline
27 (Alex): Frontline
28 (Sua): Frontline
29 (Leon): Frontline
30 (Eleven): Tank
31 (Rio): Backline
32 (William): Backline
33 (Nicky): Frontline
34 (Nathapon): Backline
35 (Jan): Frontline
36 (Eva): Backline
37 (Daniel): Diver
38 (Jenny): Backline
39 (Camilo): Frontline
40 (Chloe): Backline
41 (Johann): Support
42 (Bianca): Diver
43 (Celine): Backline
44 (Echion): Frontline
45 (Mai): Tank
46 (Aiden): Frontline
47 (Laura): Frontline
48 (Tia): Backline
49 (Felix): Frontline
50 (Elena): Frontline
51 (Priya): Backline
52 (Adina): Backline
53 (Markus): Frontline
54 (Karla): Backline
55 (Estelle): Tank
56 (Piolo): Frontline
57 (Martina): Backline
58 (Haze): Backline
59 (Isaac): Frontline
60 (Tazia): Frontline
61 (Irem): Backline
62 (Theodore): Backline
63 (Ly Anh): Frontline
64 (Vanya): Frontline
65 (DeMa): Frontline
66 (Arda): Backline
67 (Abigail): Frontline
68 (Alonso): Tank
69 (Leni): Support
70 (Tsubame): Backline
71 (Kenneth): Frontline
71 (Kenneth): Frontline
72 (Katja): Backline
73 (Charlotte): Support
74 (Darko): Frontline

Using this, criteria for different compositions were created. For example, when determining the efficacy of Camilo in team compositions with a dedicated Tank, only teams in the downloaded games with both Camilo and any of the characters classified as "Tank" were added to the stats.

Once all players meeting the criteria were added to the list of stats to consider, the average of various stats among all the players was output. The stats included were:
Average Game Rank
Average total MMR gain (entry cost not factored in)
Average total team kills
Average team eliminations
Average team downs
Average team Battle Zone downs
Average deaths
Average healing
Average shielding
Average damage dealt
Average damage taken

Additionally, ONLY stats from ranked matches in Season 4 were considered to ensure stats were most comparable.

# Analysis Results

Camilo stats across all team compositions in both regions:
Total number of games meeting criteria:  2152
Average game rank:  4.328996282527881
Average total MMR gain:  62.017657992565056
Average team kills:  8.897304832713754
Average team elims:  4.044144981412639
Average team downs:  4.044144981412639
Average team BZ downs:  0.8090148698884758
Average deaths:  2.4684014869888475
Average healing:  13258.940520446096
Average shielding:  7498.317843866171
Average damage:  15267.371282527882
Average damage taken:  16085.666356877324

Camilo stats in team compositions with a dedicated Support (Leni, Johann, or Charlotte):
Total number of games meeting criteria:  256
Average game rank:  4.1484375
Average total MMR gain:  68.84375
Average team kills:  9.8125
Average team elims:  4.40625
Average team downs:  4.40625
Average team BZ downs:  1.0
Average deaths:  2.390625
Average healing:  12779.01953125
Average shielding:  9610.85546875
Average damage:  19979.6171875
Average damage taken:  18622.92578125

As can be seen by these stats, dedicated supports offer a very significant benefit to Camilo performance, netting about a 6.8 increase in MMR gain on average, even with no other changes to the team composition considered. However, due to relatively low sample size, it is difficult to narrow team compositions further.

When further considering team compositions with support adjacent characters (Theodore, Priya, and Adina - characters who provide some shielding / healing utility, but not as the primary part of their kit), the stats drop noticably, however.

Total number of games meeting criteria:  459
Average game rank:  4.20479302832244
Average total MMR gain:  65.59477124183006
Average team kills:  9.24400871459695
Average team elims:  4.174291938997821
Average team downs:  4.174291938997821
Average team BZ downs:  0.8954248366013072
Average deaths:  2.411764705882353
Average healing:  12642.843137254902
Average shielding:  8754.333333333334
Average damage:  17824.57080610022
Average damage taken:  17405.9651416122

The stats drop off noticeably in this case, indicating that Camilo much prefers characters dedicated to supporting him over characters who may provide utility on the side.

Additionally, upon taking a further look at these stats, Priya has 51 games in the sample set with 62.96 average MMR gain, and Adina has 38 total games with Camilo with a 66.07 average MMR gain, while Theodore has 120 total games and only 58.34 average MMR gain.

Next, the stats for Camilo in team compositions with a dedicated Tank (see list in Methodology for specific characters) are as follows:
Total number of games meeting criteria:  331
Average game rank:  4.214501510574018
Average total MMR gain:  66.77643504531721
Average team kills:  9.622356495468278
Average team elims:  4.395770392749244
Average team downs:  4.395770392749244
Average team BZ downs:  0.8308157099697885
Average deaths:  2.2598187311178246
Average healing:  14042.70996978852
Average shielding:  7900.208459214501
Average damage:  16739.20241691843
Average damage taken:  16911.90332326284

There is again a sizable increase in stats over the baseline. Compare this to the stats when there are simply 2 other frontliners, but not a "Tank" dedicated to taking damage and CCing enemies:

Total number of games meeting criteria:  414
Average game rank:  4.282608695652174
Average total MMR gain:  63.57729468599034
Average team kills:  9.268115942028984
Average team elims:  4.234299516908212
Average team downs:  4.234299516908212
Average team BZ downs:  0.7995169082125604
Average deaths:  2.5096618357487923
Average healing:  13710.487922705313
Average shielding:  7297.586956521739
Average damage:  15465.154589371981
Average damage taken:  16070.084541062803

This indicates that Camilo also appreciates another character in the frontline taking the primary aggression from the enemy team, and setting up plays.

Furthermore, this relationship is mutually beneficial - the average stats for tanks across games (4769 total tanks counted in stats) has only 59.61 average MMR gain. 

Finally, to round out the different styles of compositions Camilo is played in, here are the stats for Camilo with 2 backliners:
Total number of games meeting criteria:  141
Average game rank:  4.276595744680851
Average total MMR gain:  63.11347517730496
Average team kills:  8.801418439716313
Average team elims:  3.9574468085106385
Average team downs:  3.9574468085106385
Average team BZ downs:  0.8865248226950354
Average deaths:  2.4468085106382977
Average healing:  13767.588652482269
Average shielding:  7307.702127659574
Average damage:  13841.425531914894
Average damage taken:  15587.241134751774

And here are the stats with 2 frontliners and a backliner:
Total number of games meeting criteria:  959
Average game rank:  4.3920750782064655
Average total MMR gain:  59.6089676746611
Average team kills:  8.533889468196037
Average team elims:  3.884254431699687
Average team downs:  3.884254431699687
Average team BZ downs:  0.7653806047966631
Average deaths:  2.553701772679875
Average healing:  13077.891553701773
Average shielding:  7097.281543274244
Average damage:  14257.66527632951
Average damage taken:  15570.332638164755

Surprisingly, the MMR gain is actually worse when Camilo is paired with a frontliner and a backliner as opposed to 2 backliners. This indicates that Camilo enables the average backliner more than the average other frontliner enables Camilo. This is supported by the average MMR gain for triple backline teams being only 55.62 (558 samples), which shows that having at least one frontliner to absorb damage helps most backliners in the ranked setting.


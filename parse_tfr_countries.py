import re
import json

data = """
1    Niger  6.6
2    Somalia    5.7
3    DR Congo   5.5
4    Mali   5.5
5    Chad   5.4
6    Angola 5.2
7    Burundi    5.1
8    Nigeria    5.1
9    Gambia 4.9
10   Burkina Faso   4.9
11   Tanzania   4.7
12   Mozambique 4.6
13   Benin  4.6
14   Uganda 4.5
15   Central African Republic   4.4
16   Guinea 4.4
17   South Sudan    4.4
18   Ivory Coast    4.4
19   Zambia 4.4
20   Senegal    4.4
21   Mauritania 4.3
22   Cameroon   4.3
23   Equatorial Guinea  4.2
24   Guinea-Bissau  4.2
25   Congo  4.2
26   Solomon Islands    4.2
27   Sudan  4.2
28   São Tomé and Príncipe  4.1
29   Togo   4.1
30   Liberia    4.1
31   Comoros    4.0
32   Afghanistan    3.9
33   Sierra Leone   3.9
34   Ethiopia   3.9
35   Malawi 3.9
36   Madagascar 3.9
37   Eritrea    3.8
38   Rwanda 3.8
39   Gabon  3.8
40   East Timor 3.7
41   Ghana  3.7
42   Vanuatu    3.6
43   Yemen  3.5
44   Iraq   3.5
45   Tajikistan 3.4
46   Palestine  3.4
47   Papua New Guinea   3.4
48   Tonga  3.4
49   Zimbabwe   3.3
50   Pakistan   3.3
51   Kenya  3.3
52   Namibia    3.2
53   Egypt  3.2
54 (1)   French Guiana (France) 3.2
55   Lesotho    3.0
56   Israel 3.0
57   Kyrgyzstan 2.8
58   Algeria    2.8
59   Mongolia   2.8
60   Eswatini   2.8
61   Haiti  2.8
62   Botswana   2.7
63   Guatemala  2.7
64   Syria  2.7
65   Fiji   2.7
66   Kazakhstan 2.6
67   Oman   2.6
68   Turkmenistan   2.6
69   Bolivia    2.6
70   Jordan 2.6
71   Djibouti   2.5
72   Laos   2.5
73   Philippines    2.4
74   Cambodia   2.4
75   Guyana 2.4
76   Panama 2.4
77   Seychelles 2.4
  World 2.4
78   Uzbekistan 2.3
79   Honduras   2.3
80   Paraguay   2.3
81   Ecuador    2.3
82   Suriname   2.3
83   South Africa   2.3
84   Morocco    2.3
85   Nicaragua  2.3
86   Western Sahara 2.3
87   Dominican Republic 2.2
88   Indonesia  2.2
89 (2)   Réunion (France)   2.2
90   Saudi Arabia   2.2
91   Belize 2.2
92   Venezuela  2.2
93   Argentina  2.2
94   Cape Verde 2.2
95   Peru   2.2
96   India  2.1
97   Libya  2.1
98   Sri Lanka  2.1
99   Tunisia    2.1
100  Iran   2.1
101  Myanmar (Burma)    2.1
102 (3)  Guadeloupe (France)    2.1
  Population replacement    2.1
103  Mexico 2.0
104  Kuwait 2.0
105  Lebanon    2.0
106  Georgia    2.0
107  Vietnam    2.0
108  Turkey 2.0
109  Grenada    2.0
110  El Salvador    2.0
111  Azerbaijan 2.0
112  Antigua and Barbuda    2.0
113 (4)  U.S. Virgin Islands (US)   2.0
114  Bangladesh 1.9
115  Malaysia   1.9
116  Jamaica    1.9
117  Uruguay    1.9
118  Bahrain    1.9
119  Bhutan 1.9
120 (5)  New Caledonia (France) 1.9
121 (6)  French Polynesia (France)  1.9
122 (7)  Aruba (Netherlands)    1.9
123  North Korea    1.9
124  Saint Vincent and the Grenadines   1.8
125  Nepal  1.8
126  France 1.8
127  Qatar  1.8
128  Maldives   1.8
129  Brunei 1.8
130  Armenia    1.8
131  Denmark    1.8
132  Sweden 1.8
133  United States  1.8
134  Ireland    1.8
135  New Zealand    1.8
136  Australia  1.8
137  Russia 1.8
138 (8)  Martinique (France)    1.8
139  Colombia   1.7
140  Montenegro 1.7
141  Bahamas    1.7
142  Iceland    1.7
143  Costa Rica 1.7
144  Czech Republic 1.7
145  Brazil 1.7
146  Trinidad and Tobago    1.7
147 (9)  Curaçao (Netherlands)  1.7
148  China  1.7
149  United Kingdom 1.7
150  Latvia 1.7
151  Netherlands    1.7
152  Belgium    1.7
153  Lithuania  1.7
154  Norway 1.7
155  Belarus    1.7
156  Chile  1.6
157  Romania    1.6
158  Slovenia   1.6
159  Cuba   1.6
160  Barbados   1.6
161  Estonia    1.6
162  Albania    1.6
163  Slovakia   1.6
164  Bulgaria   1.6
165  Germany    1.6
166  Switzerland    1.6
167  Austria    1.6
168  Hungary    1.5
169  Thailand   1.5
170  Canada 1.5
171  Poland 1.5
172  North Macedonia    1.5
173  Malta  1.5
174  Serbia 1.4
175  Croatia    1.4
176  Saint Lucia    1.4
177  Finland    1.4
178  Japan  1.4
179  Spain  1.4
180  Ukraine    1.4
181  Luxembourg 1.4
182 (10)     Hong Kong (China)  1.4
183  Mauritius  1.3
184  Portugal   1.3
185  United Arab Emirates   1.3
186  Greece 1.3
187  Cyprus 1.3
188  Moldova    1.3
189  Italy  1.3
190  Bosnia and Herzegovina 1.2
191  Singapore  1.2
192 (11)     Puerto Rico (US)   1.2
193  South Korea    1.1
"""

# https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate
# The pattern captures:
# 1. the rank (\d+),
# 2. the change in rank if it exists (\(\d+\))? (optional),
# 3. the country name ((?:[\w\s]+)?), and
# 4. the TFR value (\d+\.\d+).
pattern = r"(\d+)(?: \((\d+)\))?\s+((?:[\w\s\(\)]+))\s+(\d+\.\d+)"

matches = re.findall(pattern, data)

result = []

for match in matches:
    rank = int(match[0])
    change_in_rank = int(match[1]) if match[1] else None
    country = match[2].strip()
    tfr = float(match[3])

    entry = {
        "rank": rank,
        # "change_in_rank": change_in_rank,
        "country": country,
        "tfr": tfr
    }

    result.append(entry)

# Write result to JSON file, create if not exists, overwrite if exists
with open("tfr_data.json", "w+") as file:
    json.dump(result, file, indent=4)

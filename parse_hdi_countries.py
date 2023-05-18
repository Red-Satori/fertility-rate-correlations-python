import re
import json

data = """
Countries ranked from 1 to 66 in 2021 are designated "very high" HDI; those ranked from 67 to 115 are designated "high" HDI; those ranked from 116 to 159 are denoted "medium" HDI; and those ranked from 160 to 191 are designated "low" HDI.[19][13]

Table of countries by HDI
Rank	Nation	HDI
2021 data (2022 report)​[2]	Change since 2015​[20]	2021 data (2022 report)​[2]	Average annual growth (2010–2021)​[20]
1	Steady	 Switzerland	0.962	Increase 0.19%
2	Steady	 Norway	0.961	Increase 0.19%
3	Steady	 Iceland	0.959	Increase 0.56%
4	Increase (3)	 Hong Kong	0.952	Increase 0.44%
5	Increase (3)	 Australia	0.951	Increase 0.27%
6	Steady	 Denmark	0.948	Increase 0.34%
7	Decrease (2)	 Sweden	0.947	Increase 0.36%
8	Increase (6)	 Ireland	0.945	Increase 0.40%
9	Decrease (5)	 Germany	0.942	Increase 0.16%
10	Decrease (1)	 Netherlands	0.941	Increase 0.24%
11	Steady	 Finland	0.940	Increase 0.29%
12	Decrease (1)	 Singapore	0.939	Increase 0.29%
13	Increase (2)	 Belgium	0.937	Increase 0.25%
13	Decrease (3)	 New Zealand	0.937	Increase 0.15%
15	Decrease (2)	 Canada	0.936	Increase 0.25%
16	Decrease (1)	 Liechtenstein	0.935	Increase 0.22%
17	Increase (3)	 Luxembourg	0.930	Increase 0.18%
18	Decrease (3)	 United Kingdom	0.929	Increase 0.17%
19	Steady	 Japan	0.925	Increase 0.27%
19	Increase (3)	 South Korea	0.925	Increase 0.35%
21	Decrease (3)	 United States	0.921	Increase 0.10%
22	Steady	 Israel	0.919	Increase 0.25%
23	Increase (4)	 Malta	0.918	Increase 0.58%
23	Increase (1)	 Slovenia	0.918	Increase 0.28%
25	Decrease (4)	 Austria	0.916	Increase 0.14%
26	Increase (9)	 United Arab Emirates	0.911	Increase 0.80%
27	Steady	 Spain	0.905	Increase 0.38%
28	Decrease (3)	 France	0.903	Increase 0.27%
29	Increase (3)	 Cyprus	0.896	Increase 0.41%
30	Decrease (1)	 Italy	0.895	Increase 0.13%
31	Decrease (2)	 Estonia	0.890	Increase 0.30%
32	Decrease (6)	 Czech Republic	0.889	Increase 0.20%
33	Decrease (2)	 Greece	0.887	Increase 0.19%
34	Decrease (1)	 Poland	0.876	Increase 0.37%
35	Increase (3)	 Bahrain	0.875	Increase 0.73%
35	Increase (1)	 Lithuania	0.875	Increase 0.35%
35	Increase (2)	 Saudi Arabia	0.875	Increase 0.64%
38	Increase (2)	 Portugal	0.866	Increase 0.40%
39	Increase (1)	 Latvia	0.863	Increase 0.42%
40	Decrease (6)	 Andorra	0.858	Increase 0.11%
40	Increase (5)	 Croatia	0.858	Increase 0.40%
42	Increase (1)	 Chile	0.855	Increase 0.46%
42	Increase (1)	 Qatar	0.855	Increase 0.23%
44	NA[a]	 San Marino	0.853	NA[a]
45	Decrease (5)	 Slovakia	0.848	Increase 0.09%
46	Increase (1)	 Hungary	0.846	Increase 0.20%
47	Decrease (4)	 Argentina	0.842	Increase 0.09%
48	Increase (6)	 Turkey	0.838	Increase 1.03%
49	Increase (3)	 Montenegro	0.832	Increase 0.27%
50	Decrease (1)	 Kuwait	0.831	Increase 0.20%
51	Decrease (3)	 Brunei	0.829	Increase 0.01%
52	Decrease (2)	 Russia	0.822	Increase 0.29%
53	Decrease (4)	 Romania	0.821	Increase 0.16%
54	Decrease (3)	 Oman	0.816	Increase 0.32%
55	Decrease (2)	 Bahamas	0.812	Increase 0.00%
56	Increase (4)	 Kazakhstan	0.811	Increase 0.51%
57	Decrease (2)	 Trinidad and Tobago	0.810	Increase 0.23%
58	Increase (4)	 Costa Rica	0.809	Increase 0.43%
58	Steady	 Uruguay	0.809	Increase 0.25%
60	Decrease (3)	 Belarus	0.808	Increase 0.21%
61	Steady	 Panama	0.805	Increase 0.37%
62	Increase (1)	 Malaysia	0.803	Increase 0.39%
63	Increase (7)	 Georgia	0.802	Increase 0.50%
63	Increase (2)	 Mauritius	0.802	Increase 0.55%
63	Increase (4)	 Serbia	0.802	Increase 0.41%
66	Increase (6)	 Thailand	0.800	Increase 0.75%
67	Decrease (2)	 Albania	0.796	Increase 0.49%
68	Decrease (9)	 Bulgaria	0.795	Increase 0.06%
68	Increase (2)	 Grenada	0.795	Increase 0.15%
70	Decrease (2)	 Barbados	0.790	Increase 0.02%
71	Decrease (3)	 Antigua and Barbuda	0.788	Decrease 0.02%
72	Decrease (8)	 Seychelles	0.785	Increase 0.10%
73	Increase (9)	 Sri Lanka	0.782	Increase 0.54%
74	Increase (10)	 Bosnia and Herzegovina	0.780	Increase 0.67%
75	Increase (2)	 Saint Kitts and Nevis	0.777	Increase 0.21%
76	Decrease (2)	 Iran	0.774	Increase 0.35%
77	Decrease (2)	 Ukraine	0.773	Increase 0.11%
78	Increase (5)	 North Macedonia	0.770	Increase 0.39%
79	Increase (19)	 China	0.768	Increase 0.97%
80	Increase (16)	 Dominican Republic	0.767	Increase 0.73%
80	Increase (9)	 Moldova	0.767	Increase 0.45%
80	Decrease (7)	 Palau	0.767	Decrease 0.07%
83	Decrease (7)	 Cuba	0.764	Decrease 0.19%
84	Increase (1)	 Peru	0.762	Increase 0.45%
85	Decrease (5)	 Armenia	0.759	Increase 0.16%
86	Decrease (8)	 Mexico	0.758	Increase 0.15%
87	Increase (1)	 Brazil	0.754	Increase 0.38%
88	Decrease (1)	 Colombia	0.752	Increase 0.32%
89	Decrease (4)	 Saint Vincent and the Grenadines	0.751	Increase 0.21%
90	Increase (6)	 Maldives	0.747	Increase 0.75%
91	Increase (2)	 Algeria	0.745	Increase 0.30%
91	Decrease (1)	 Azerbaijan	0.745	Increase 0.22%
91	Increase (10)	 Tonga	0.745	Increase 0.40%
91	Increase (2)	 Turkmenistan	0.745	Increase 0.43%
95	Decrease (14)	 Ecuador	0.740	Increase 0.05%
96	Increase (4)	 Mongolia	0.739	Increase 0.48%
97	Increase (13)	 Egypt	0.731	Increase 0.73%
97	Increase (1)	 Tunisia	0.731	Increase 0.14%
99	Increase (3)	 Fiji	0.730	Increase 0.20%
99	Decrease (7)	 Suriname	0.730	Increase 0.09%
101	Increase (11)	 Uzbekistan	0.727	Increase 0.70%
102	Increase (11)	 Dominica	0.720	Increase 0.11%
102	Increase (2)	 Jordan	0.720	Decrease 0.06%
104	Increase (10)	 Libya	0.718	Decrease 0.26%
105	Decrease (2)	 Paraguay	0.717	Increase 0.42%
106	Increase (2)	 Palestine	0.715	Increase 0.36%
106	Decrease (11)	 Saint Lucia	0.715	Decrease 0.16%
108	Increase (12)	 Guyana	0.714	Increase 0.77%
109	Decrease (4)	 South Africa	0.713	Increase 0.50%
110	Decrease (3)	 Jamaica	0.709	Increase 0.06%
111	Decrease (6)	 Samoa	0.707	Decrease 0.08%
112	Increase (2)	 Gabon	0.706	Increase 0.56%
112	Decrease (21)	 Lebanon	0.706	Decrease 0.79%
114	Increase (3)	 Indonesia	0.705	Increase 0.55%
115	Increase (5)	 Vietnam	0.703	Increase 0.53%
116	Steady	 Philippines	0.699	Increase 0.33%
117	Decrease (6)	 Botswana	0.693	Increase 0.44%
118	Steady	 Bolivia	0.692	Increase 0.40%
118	Steady	 Kyrgyzstan	0.692	Increase 0.38%
120	Decrease (41)	 Venezuela	0.691	Decrease 0.80%
121	Increase (1)	 Iraq	0.686	Increase 0.63%
122	Increase (3)	 Tajikistan	0.685	Increase 0.68%
123	Decrease (14)	 Belize	0.683	Decrease 0.31%
123	Increase (3)	 Morocco	0.683	Increase 1.14%
125	Decrease (2)	 El Salvador	0.675	Increase 0.22%
126	Increase (1)	 Nicaragua	0.667	Increase 0.76%
127	Increase (6)	 Bhutan	0.666	Increase 1.25%
128	Decrease (4)	 Cape Verde	0.662	Increase 0.25%
129	Increase (11)	 Bangladesh	0.661	Increase 1.64%
130	Decrease (2)	 Tuvalu	0.641	Increase 0.36%
131	Decrease (1)	 Marshall Islands	0.639	NA[a]
132	Decrease (1)	 India	0.633	Increase 0.88%
133	Increase (5)	 Ghana	0.632	Increase 0.88%
134	Steady	 Micronesia	0.628	Increase 0.04%
135	Decrease (6)	 Guatemala	0.627	Increase 0.33%
136	Decrease (1)	 Kiribati	0.624	Increase 0.53%
137	Steady	 Honduras	0.621	Increase 0.36%
138	Increase (4)	 Sao Tome and Principe	0.618	Increase 1.00%
139	Decrease (7)	 Namibia	0.615	Increase 0.46%
140	Increase (1)	 Laos	0.607	Increase 0.88%
140	Decrease (4)	 East Timor	0.607	Decrease 0.18%
140	Increase (3)	 Vanuatu	0.607	Increase 0.24%
143	Increase (4)	   Nepal	0.602	Increase 0.94%
144	Increase (4)	 Eswatini	0.597	Increase 1.57%
145	Decrease (6)	 Equatorial Guinea	0.596	Increase 0.26%
146	Increase (3)	 Cambodia	0.593	Increase 0.85%
146	Decrease (1)	 Zimbabwe	0.593	Increase 1.34%
148	Decrease (3)	 Angola	0.586	Increase 1.27%
149	Increase (1)	 Myanmar	0.585	Increase 1.26%
150	Increase (5)	 Syria	0.577	Decrease 1.21%
151	Increase (2)	 Cameroon	0.576	Increase 1.06%
152	Steady	 Kenya	0.575	Increase 0.49%
153	Decrease (9)	 Republic of the Congo	0.571	Increase 0.16%
154	Decrease (4)	 Zambia	0.565	Increase 0.60%
155	Decrease (1)	 Solomon Islands	0.564	Increase 0.23%
156	Steady	 Comoros	0.558	Increase 0.64%
156	Increase (2)	 Papua New Guinea	0.558	Increase 1.02%
158	Decrease (2)	 Mauritania	0.556	Increase 0.79%
159	Increase (8)	 Ivory Coast	0.550	Increase 1.38%
160	Increase (2)	 Tanzania	0.549	Increase 0.98%
161	Decrease (2)	 Pakistan	0.544	Increase 0.68%
162	Increase (4)	 Togo	0.539	Increase 1.12%
163	Decrease (3)	 Haiti	0.535	Increase 1.94%
163	Increase (1)	 Nigeria	0.535	Increase 0.95%
165	Steady	 Rwanda	0.534	Increase 0.80%
166	Decrease (6)	 Benin	0.525	Increase 0.59%
166	Decrease (3)	 Uganda	0.525	Increase 0.41%
168	Increase (3)	 Lesotho	0.514	Increase 0.88%
169	Increase (4)	 Malawi	0.512	Increase 1.06%
170	Decrease (1)	 Senegal	0.511	Increase 0.80%
171	Increase (1)	 Djibouti	0.509	Increase 0.96%
172	Decrease (4)	 Sudan	0.508	Increase 0.40%
173	Decrease (3)	 Madagascar	0.501	Increase 0.16%
174	Increase (1)	 Gambia	0.500	Increase 0.76%
175	Increase (6)	 Ethiopia	0.498	Increase 1.74%
176	Decrease (2)	 Eritrea	0.492	Increase 0.55%
177	Increase (2)	 Guinea-Bissau	0.483	Increase 0.79%
178	Steady	 Liberia	0.481	Increase 0.41%
179	Increase (1)	 Democratic Republic of the Congo	0.479	Increase 1.01%
180	Decrease (5)	 Afghanistan	0.478	Increase 0.59%
181	Increase (1)	 Sierra Leone	0.477	Increase 1.01%
182	Increase (1)	 Guinea	0.465	Increase 1.04%
183	Decrease (6)	 Yemen	0.455	Decrease 1.03%
184	Increase (2)	 Burkina Faso	0.449	Increase 1.72%
185	Decrease (2)	 Mozambique	0.446	Increase 0.95%
186	Increase (1)	 Mali	0.428	Increase 0.53%
187	Decrease (2)	 Burundi	0.426	Increase 0.46%
188	Increase (2)	 Central African Republic	0.404	Increase 0.75%
189	Increase (2)	 Niger	0.400	Increase 1.54%
190	Decrease (1)	 Chad	0.394	Increase 0.77%
191	Decrease (3)	 South Sudan	0.385	Decrease 1.00%
"""

# https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index
# The pattern captures:
# 1. the rank (\d+),
# 2. the status with the change in rank if it exists (\w+( \(\d+\))?),
# 3. the country name ((?:[\w\s]+)?), and
# 4. the HDI value (\d+\.\d+).
pattern = r"(\d+)\s+(\w+(?: \(\d+\))?)\s+((?:[\w\s]+)?)\s+(\d+\.\d+)"

matches = re.findall(pattern, data)

result = []

for match in matches:
    rank = int(match[0])
    status = match[1].strip()
    country = match[2].strip()
    hdi = float(match[3])

    entry = {
        "rank": rank,
        "status": status,
        "country": country,
        "hdi": hdi
    }

    result.append(entry)


# Write result to JSON file, create if not exists, overwrite if exists
with open("hdi_data.json", "w+") as file:
    json.dump(result, file, indent=4)
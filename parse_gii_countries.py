import re
import json

data = """
GII Rank    HDI Rank    Country GII Value
1   2   Switzerland Switzerland 0.025
2   1   Norway Norway   0.038
3   11  Finland Finland 0.039
4   8   Netherlands Netherlands 0.043
4   10  Denmark Denmark 0.043
6   7   Sweden Sweden   0.045
6   14  Belgium Belgium 0.045
7   23  South Korea South Korea 0.047
8   26  France France   0.049
9   4   Iceland Iceland 0.058
10  22  Slovenia Slovenia   0.063
11  23  Taiwan Taiwan   0.064
12  11  Singapore Singapore 0.065
12  23  Luxembourg Luxembourg   0.065
14  18  Austria Austria 0.069
14  29  Italy Italy 0.069
16  25  Spain Spain 0.070
17  19  Japan Japan 0.075
18  38  Portugal Portugal   0.079
19  16  Canada Canada   0.080
20  6   Germany Germany 0.084
21  29  Estonia Estonia 0.086
21  33  Cyprus Cyprus   0.086
23  2   Republic of Ireland Ireland 0.093
24  14  New Zealand New Zealand 0.094
25  8   Australia Australia 0.097
26  19  United Kingdom United Kingdom   0.109
26  48  Montenegro Montenegro   0.109
28  35  Poland Poland   0.115
29  32  Greece Greece   0.116
29  43  Croatia Croatia 0.116
31  31  United Arab Emirates United Arab Emirates   0.118
31  53  Belarus Belarus 0.118
33  14  Israel Israel   0.123
34  34  Lithuania Lithuania 0.124
35  64  Serbia Serbia   0.132
36  27  Czech Republic Czech Republic   0.136
37  82  North Macedonia North Macedonia 0.143
38  73  Bosnia and Herzegovina Bosnia and Herzegovina   0.149
39  85  China China 0.168
40  28  Malta Malta 0.175
41  37  Latvia Latvia   0.176
42  69  Albania Albania 0.181
43  45  Qatar Qatar 0.185
44  51  Kazakhstan Kazakhstan   0.190
45  39  Slovakia Slovakia   0.191
46  17  United States United States 0.204
46  90  Moldova Moldova 0.204
48  56  Bulgaria Bulgaria   0.206
49  42  Bahrain 0.212
50  52  Russia  0.225
51  40  Hungary 0.233
52  74  Ukraine 0.234
53  64  Kuwait  0.242
54  81  Armenia 0.245
55  43  Chile   0.247
56  40  Saudi Arabia    0.252
56  58  Barbados    0.252
56  105 Libya   0.252
59  62  Malaysia    0.253
60  47  Brunei  0.255
61  49  Romania 0.276
62  55  Uruguay 0.288
62  62  Costa Rica  0.288
62  106 Uzbekistan  0.288
65  95  Tunisia 0.296
65  117 Vietnam 0.296
67  70  Cuba    0.304
68  54  Turkey  0.306
68  60  Oman    0.306
70  125 Tajikistan  0.314
71  74  Mexico  0.322
71  99  Mongolia    0.322
73  67  Trinidad and Tobago 0.323
73  88  Azerbaijan  0.323
75  46  Argentina   0.328
76  61  Georgia 0.331
77  58  Bahamas 0.341
78  66  Mauritius   0.347
79  104 Tonga   0.354
80  79  Thailand    0.359
81  111 Samoa   0.360
82  95  Maldives    0.369
82  120 Kyrgyzstan  0.369
84  93  Fiji    0.370
85  124 El Salvador 0.383
86  86  Ecuador 0.384
87  79  Peru    0.395
88  101 Jamaica 0.396
89  126 Cape Verde  0.397
90  72  Sri Lanka   0.401
90  86  Saint Lucia 0.401
92  160 Rwanda  0.402
93  114 South Africa    0.406
94  57  Panama  0.407
95  84  Brazil  0.408
96  92  Lebanon 0.411
97  110 Belize  0.415
98  107 Bolivia 0.417
99  129 Bhutan  0.421
100 132 Honduras    0.423
101 83  Colombia    0.428
101 128 Nicaragua   0.428
103 91  Algeria 0.429
104 107 Philippines 0.430
105 97  Suriname    0.436
106 130 Namibia 0.440
107 103 Paraguay    0.446
108 116 Egypt   0.449
109 102 Jordan  0.450
110 142 Nepal   0.452
111 121 Morocco 0.454
112 88  Dominican Republic  0.455
113 70  Iran    0.459
113 137 Laos    0.459
115 122 Guyana  0.462
116 100 Botswana    0.465
117 144 Cambodia    0.474
118 147 Myanmar 0.478
119 113 Venezuela   0.479
119 127 Guatemala   0.479
121 107 Indonesia   0.480
122 151 Syria   0.482
123 131 India   0.488
124 185 Burundi 0.504
125 173 Ethiopia    0.517
126 143 Kenya   0.518
127 181 Mozambique  0.523
128 119 Gabon   0.525
129 150 Zimbabwe    0.527
130 168 Senegal 0.533
131 159 Uganda  0.535
132 148 Angola  0.536
133 133 Bangladesh  0.537
133 135 Sao Tome and Principe   0.537
135 138 Ghana   0.538
135 154 Pakistan    0.538
137 146 Zambia  0.539
138 170 Sudan   0.545
139 165 Lesotho 0.553
140 163 Tanzania    0.556
141 153 Cameroon    0.560
142 174 Malawi  0.565
143 138 Eswatini    0.567
144 149 Republic of the Congo   0.570
145 167 Togo    0.573
146 123 Iraq    0.577
147 182 Burkina Faso    0.594
148 158 Benin   0.612
148 172 Gambia  0.612
150 175 Democratic Republic of the Congo    0.617
151 157 Mauritania  0.634
152 170 Haiti   0.636
153 162 Ivory Coast 0.638
154 189 Niger   0.642
155 182 Sierra Leone    0.644
156 175 Liberia 0.650
157 169 Afghanistan 0.655
158 184 Mali    0.671
159 188 Central African Republic    0.680
160 187 Chad    0.710
161 155 Papua New Guinea    0.725
162 179 Yemen   0.795
"""

# https://en.wikipedia.org/wiki/Gender_Inequality_Index
# The pattern captures:
# 1. the GII rank (\d+),
# 2. the HDI rank (\d+) (which we will ignore),
# 3. the country name (([\w\s]+)) (we take half of it as it's repeated), and
# 4. the GII value (\d+\.\d+).
pattern = r"(\d+)\s+\d+\s+([\w\s]+)\s+([\w\s]+)\s+(\d+\.\d+)"

matches = re.findall(pattern, data)

result = []

for match in matches:
    gii_rank = int(match[0])
    country = match[1].strip()  # taking only the first occurrence
    gii_value = float(match[3])

    entry = {
        "gii_rank": gii_rank,
        "country": country,
        "gii_value": gii_value
    }

    result.append(entry)

# Write result to JSON file, create if not exists, overwrite if exists
with open("gii_data.json", "w+") as file:
    json.dump(result, file, indent=4)
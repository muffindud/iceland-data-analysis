These are the explanations for common Eurostat dataset column codes used in this analysis:

| Column     | Meaning                                                         | Notes / Values                                                                                                                                   |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `coicop`   | **Classification of Individual Consumption by Purpose**         | Used mainly in HICP, consumption expenditure datasets. Codes group consumption spending (e.g., *01 Food*, *04 Housing*, etc.).                   |
| `isco08`   | **International Standard Classification of Occupations (2008)** | Occupational classification (e.g., *1 Managers*, *2 Professionals*, ... *9 Elementary occupations*).                                             |
| `isced11`  | **International Standard Classification of Education (2011)**   | Education level categories (e.g., *0 Pre-primary*, *3 Upper secondary*, *5 Short-cycle tertiary*, *8 Doctoral level*).                           |
| `citizen`  | **Citizenship / Population Group Code**                         | Used in labour & migration data. Examples: `EU27_2020_FOR` (foreign citizens from EU-27 countries), `FOR` (foreign citizens), `NRP` (nationals). |
| `nace_r2`  | **NACE Rev.2 Economic Activity Classification**                 | Industry / sector codes (e.g., *A Agriculture*, *C Manufacturing*, *G Wholesale/Retail*, *J Information & communication*).                       |
| `estruct`  | **Employment Structure / Age / Work Status Breakdown**          | Labour-force structure categories (e.g., *EMP* employed, *UNE* unemployed, age groups, FT/PT indicators depending on dataset).                   |
| `ecase`    | **Employment Case Category**                                    | Defines employment situation categories (e.g., permanent vs temporary contracts, type of job arrangement — dataset-dependent).                   |
| `s_adj`    | **Seasonal Adjustment Indicator**                               | `SA` = seasonally adjusted, `NSA` = not seasonally adjusted, `WDA` = working-day adjusted, `SA_WDA` combined.                                    |
| `indic_em` | **Employment Indicator Code**                                   | Identifies specific labour-market metric (e.g., unemployment rate, employment rate, hours worked — dataset-specific variable key).               |

Below is a **clean, ready-to-paste** explanation of the values for each Eurostat dimension you listed.

---

#### `s_adj` — Seasonal Adjustment

| Code  | Meaning                            |
| ----- | ---------------------------------- |
| `SCA` | Seasonal & calendar adjusted       |
| `NSA` | Not seasonally adjusted            |
| `SA`  | Seasonally adjusted                |
| `TC`  | Trend-cycle data (smoothed series) |

---

#### `na_item` — National Accounts Item

| Code   | Meaning                                                           |
| ------ | ----------------------------------------------------------------- |
| `B1GQ` | Gross Domestic Product (GDP), volume, chain-linked, market prices |

---

#### `coicop` — Consumption Purpose Categories

| Code             | Meaning                           |
| ---------------- | --------------------------------- |
| `TOTAL`          | Total consumption                 |
| `TOT_X_ALC_TBC`  | Total excluding alcohol & tobacco |
| `TOT_X_NRG_FOOD` | Total excluding energy & food     |
| `TOT_X_TBC`      | Total excluding tobacco           |

---

#### `isced11` — Education Levels (2011)

| Code      | Meaning                                                          |
| --------- | ---------------------------------------------------------------- |
| `ED0-2`   | Low education (primary & lower secondary)                        |
| `ED3_4`   | Medium education (upper secondary & post-secondary non-tertiary) |
| `ED5-8`   | High education (tertiary: bachelor → doctorate)                  |
| `ED34_44` | Specific combined middle-education groups (context-dependent)    |
| `ED35_45` | Specific mixed education groups (context-dependent)              |
| `TOTAL`   | All education levels                                             |
| `NRP`     | Not reported / Missing value category                            |

---

#### `citizen` — Citizenship Category

| Code             | Meaning                                      |
| ---------------- | -------------------------------------------- |
| `EU27_2020_FOR`  | Foreign citizens from EU-27 (post-Brexit EU) |
| `FOR`            | Foreign citizens (non-nationals)             |
| `NAT`            | Nationals of reporting country               |
| `NEU27_2020_FOR` | Foreign citizens not from EU-27 (non-EU)     |
| `NRP`            | Not reported / category not provided         |
| `TOTAL`          | All citizenship groups                       |
| `STLS`           | Stateless persons                            |

---

#### `isco08` — Occupation Group (2012 ISCO)

| Code    | Meaning                                          |
| ------- | ------------------------------------------------ |
| `OC1`   | Managers                                         |
| `OC2`   | Professionals                                    |
| `OC3`   | Technicians & associate professionals            |
| `OC4`   | Clerical support workers                         |
| `OC5`   | Service & sales workers                          |
| `OC6`   | Skilled agricultural, forestry & fishery workers |
| `OC7`   | Craft & related trades workers                   |
| `OC8`   | Plant & machine operators, assemblers            |
| `OC9`   | Elementary occupations                           |
| `TOTAL` | All occupations                                  |
| `NRP`   | Not reported                                     |

---

#### `indic_em` — Employment Indicators

> Codes combine Employment (E), Inactive (I), Unemployed (U) by origin/dest.
> Example: `U_E` = moved from unemployment to employment

| Code      | Meaning                               |
| --------- | ------------------------------------- |
| `E_E`     | Stayed employed                       |
| `E_I`     | Moved from employment → inactivity    |
| `E_U`     | Moved from employment → unemployment  |
| `I_E`     | Moved from inactivity → employment    |
| `I_I`     | Stayed inactive                       |
| `I_U`     | Moved from inactivity → unemployment  |
| `U_E`     | Moved from unemployment → employment  |
| `U_I`     | Moved from unemployment → inactivity  |
| `U_U`     | Stayed unemployed                     |
| `ACT`     | Activity rate indicator               |
| `EMP_LFS` | Employment rate (Labour Force Survey) |

---

#### `estruct` — Employment Structure Category

| Code  | Meaning                             |
| ----- | ----------------------------------- |
| `NET` | Net change / net employment balance |

---

#### `ecase` — Employment Case

| Code           | Meaning                                                                |
| -------------- | ---------------------------------------------------------------------- |
| `P1_NCH_AW100` | People not changing job, working 100% hours (full-time, no job change) |

> Very dataset-specific code:
> *P1 = same job; NCH = no change; AW100 = 100% working time*

---

#### `nace_r2` — Economic Activity (NACE Rev.2)

| Code  | Meaning                                                                                                                |
| ----- | ---------------------------------------------------------------------------------------------------------------------- |
| `B-S` | All industries from Mining (`B`) to Other Services (`S`) — basically whole economy except agriculture (A) & households |

---

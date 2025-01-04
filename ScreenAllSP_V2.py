sp500 = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'META', 'GOOGL', 'GOOG', 'BRK.B', 'LLY', 'JPM', 'AVGO', 'XOM', 'UNH', 'V', 'TSLA', 'PG', 'MA', 'JNJ', 'HD', 'MRK', 'COST', 'ABBV', 'CVX', 'CRM', 'BAC', 'WMT', 'NFLX', 'PEP', 'AMD', 'KO', 'WFC', 'LIN', 'TMO', 'ADBE', 'DIS', 'ACN', 'MCD', 'CSCO', 'ABT', 'ORCL', 'CAT', 'QCOM', 'INTU', 'GE', 'IBM', 'Other', 'VZ', 'CMCSA', 'DHR', 'AMAT', 'COP', 'TXN', 'PM', 'NOW', 'PFE', 'AMGN', 'INTC', 'UNP', 'UBER', 'LOW', 'GS', 'NEE', 'RTX', 'AXP', 'SPGI', 'ISRG', 'HON', 'PGR', 'ELV', 'MU', 'BKNG', 'ETN', 'C', 'T', 'MS', 'LRCX', 'NKE', 'SCHW', 'TJX', 'SYK', 'DE', 'MDT', 'UPS', 'BLK', 'VRTX', 'CB', 'LMT', 'BMY', 'CI', 'SBUX', 'ADP', 'BSX', 'MMC', 'PLD', 'BA', 'REGN', 'ADI', 'MDLZ', 'CVS', 'FI', 'BX', 'PANW', 'KLAC', 'GILD', 'TMUS', 'SNPS', 'AMT', 'CMG', 'SO', 'DUK', 'CME', 'TGT', 'ICE', 'MO', 'EOG', 'WM', 'CDNS', 'FCX', 'SLB', 'SHW', 'CL', 'MPC', 'EQIX', 'TT', 'ABNB', 'NOC', 'CSX', 'GD', 'MCK', 'TDG', 'PYPL', 'ITW', 'PSX', 'ZTS', 'APH', 'PH', 'BDX', 'EMR', 'FDX', 'HCA', 'ORLY', 'PNC', 'AON', 'ANET', 'USB', 'CTAS', 'ROP', 'PCAR', 'MAR', 'MCO', 'MSI', 'CEG', 'ECL', 'NXPI', 'VLO', 'NSC', 'COF', 'WELL', 'DXCM', 'APD', 'AJG', 'TRV', 'MMM', 'TFC', 'AZO', 'HLT', 'EW', 'GM', 'AIG', 'F', 'ALL', 'AEP', 'CPRT', 'ROST', 'NUE', 'ADSK', 'SPG', 'OKE', 'WMB', 'CARR', 'TEL', 'MCHP', 'SRE', 'AFL', 'O', 'KMB', 'DHI', 'PSA', 'CCI', 'NEM', 'FTNT', 'BK', 'GWW', 'CNC', 'MSCI', 'LULU', 'MET', 'D', 'HES', 'GIS', 'OXY', 'DLR', 'FIS', 'STZ', 'PRU', 'AMP', 'AME', 'JCI', 'URI', 'IQV', 'COR', 'IR', 'PCG', 'DOW', 'CMI', 'PAYX', 'GEV', 'LEN', 'FAST', 'A', 'FANG', 'LHX', 'IDXX', 'CTVA', 'MNST', 'EXC', 'RSG', 'SMCI', 'HUM', 'KR', 'OTIS', 'SYY', 'ODFL', 'MLM', 'YUM', 'KMI', 'KDP', 'CSGP', 'DVN', 'HAL', 'EL', 'GPN', 'PEG', 'ACGL', 'VRSK', 'VMC', 'ADM', 'BKR', 'CTSH', 'DFS', 'KVUE', 'CDW', 'PWR', 'IT', 'GEHC', 'DD', 'MRNA', 'ED', 'DG', 'ANSS', 'DAL', 'BIIB', 'PPG', 'FICO', 'XEL', 'HSY', 'FTV', 'HIG', 'KHC', 'ROK', 'XYL', 'WST', 'EA', 'MPWR', 'EXR', 'RCL', 'VICI', 'VST', 'TSCO', 'NVR', 'TRGP', 'CHTR', 'PHM', 'RJF', 'ON', 'KEYS', 'CAH', 'LYB', 'RMD', 'GLW', 'AVB', 'HWM', 'ZBH', 'FITB', 'WTW', 'DLTR', 'HPQ', 'EIX', 'MTD', 'EFX', 'WEC', 'CBRE', 'CHD', 'DOV', 'TROW', 'EBAY', 'NDAQ', 'MTB', 'WAB', 'FE', 'PTC', 'AWK', 'ALGN', 'WY', 'HPE', 'GRMN', 'CBOE', 'HBAN', 'ULTA', 'AEE', 'BRO', 'NTAP', 'STT', 'HUBB', 'IRM', 'STLD', 'TDY', 'ES', 'BR', 'TTWO', 'APTV', 'IFF', 'VLTO', 'CINF', 'EQR', 'ETR', 'PPL', 'AXON', 'GPC', 'STE', 'BAX', 'BALL', 'DECK', 'WDC', 'DTE', 'INVH', 'MOH', 'CPAY', 'CTRA', 'SBAC', 'BLDR', 'WBD', 'LUV', 'TSN', 'HOLX', 'LH', 'CLX', 'FSLR', 'CF', 'CMS', 'OMC', 'CAG', 'SWKS', 'PFG', 'DPZ', 'EXPE', 'RF', 'ATO', 'CNP', 'PKG', 'BG', 'TER', 'TXT', 'DRI', 'EG', 'MAS', 'ILMN', 'EQT', 'J', 'K', 'MAA', 'AVY', 'IEX', 'STX', 'LDOS', 'JBL', 'VRSN', 'ARE', 'MKC', 'EXPD', 'AKAM', 'UAL', 'WRB', 'MRO', 'CE', 'TYL', 'NRG', 'FDS', 'COO', 'VTR', 'ENPH', 'LVS', 'SYF', 'CFG', 'WAT', 'NTRS', 'ESS', 'POOL', 'EVRG', 'JBHT', 'PNR', 'ALB', 'SNA', 'ZBRA', 'SJM', 'EMN', 'IP', 'HST', 'HII', 'CCL', 'WRK', 'AMCR', 'FFIV', 'LKQ', 'GEN', 'UDR', 'DGX', 'LNT', 'JKHY', 'SWK', 'AES', 'VTRS', 'MGM', 'KEY', 'LYV', 'NDSN', 'PODD', 'TAP', 'EPAM', 'IPG', 'RVTY', 'KMX', 'ALLE', 'NI', 'WBA', 'DOC', 'TRMB', 'L', 'KIM', 'AOS', 'CRL', 'LW', 'BBY', 'ROL', 'JNPR', 'FMC', 'REG', 'PNW', 'AAL', 'HRL', 'RHI', 'APA', 'BBWI', 'FRT', 'CHRW', 'DVA', 'CTLT', 'IVZ', 'HAS', 'BWA', 'BEN', 'MTCH', 'CZR', 'SOLV', 'WYNN', 'DAY', 'NWSA', 'CPB', 'INCY', 'TPR', 'FOXA', 'BF.B', 'TFX', 'QRVO', 'BXP', 'CPT', 'AIZ', 'ETSY', 'CMA', 'RL', 'HSIC', 'MKTX', 'PAYC', 'MOS', 'TECH', 'NCLH', 'GNRC', 'UHS', 'NWS', 'PARA', 'FOX', 'GL', 'MHK', 'BIO']

sp400 = ['AA', 'AAON', 'ACHC', 'ACM', 'ADC', 'ADNT', 'AFG', 'AGCO', 'AIT', 'ALE', 'ALGM', 'ALLY', 'ALTM', 'ALTR', 'ALV', 'AM', 'AMED', 'AMG', 'AMH', 'AMKR', 'AN', 'APPF', 'AR', 'ARMK', 'ARW', 'ARWR', 'ASB', 'ASGN', 'ASH', 'ATR', 'AVNT', 'AVT', 'AXTA', 'AYI', 'AZPN', 'AZTA', 'BC', 'BCO', 'BDC', 'BERY', 'BHF', 'BJ', 'BKH', 'BLD', 'BLKB', 'BMRN', 'BRBR', 'BRKR', 'BRX', 'BURL', 'BWXT', 'BYD', 'CACI', 'CADE', 'CAR', 'CASY', 'CBSH', 'CBT', 'CC', 'CCK', 'CDP', 'CELH', 'CFR', 'CG', 'CGNX', 'CHDN', 'CHE', 'CHH', 'CHK', 'CHRD', 'CHX', 'CIEN', 'CIVI', 'CLF', 'CLH', 'CMC', 'CNM', 'CNO', 'CNX', 'CNXC', 'COHR', 'COKE', 'COLB', 'COLM', 'COTY', 'CPRI', 'CR', 'CRI', 'CROX', 'CRUS', 'CSL', 'CUBE', 'CUZ', 'CVLT', 'CW', 'CXT', 'CYTK', 'DAR', 'DBX', 'DCI', 'DINO', 'DKS', 'DLB', 'DOCS', 'DT', 'DTM', 'DUOL', 'EEFT', 'EGP', 'EHC', 'ELF', 'ELS', 'EME', 'ENOV', 'ENS', 'EPR', 'EQH', 'ERIE', 'ESAB', 'ESNT', 'ETRN', 'EVR', 'EWBC', 'EXEL', 'EXLS', 'EXP', 'EXPO', 'FAF', 'FBIN', 'FCFS', 'FCN', 'FFIN', 'FHI', 'FHN', 'FIVE', 'FIX', 'FLO', 'FLR', 'FLS', 'FNB', 'FND', 'FNF', 'FR', 'FYBR', 'G', 'GATX', 'GBCI', 'GEF', 'GGG', 'GHC', 'GLPI', 'GME', 'GMED', 'GNTX', 'GPK', 'GPS', 'GT', 'GTLS', 'GXO', 'H', 'HAE', 'HALO', 'HELE', 'HGV', 'HLI', 'HOG', 'HOMB', 'HQY', 'HR', 'HRB', 'HWC', 'HXL', 'IBKR', 'IBOC', 'IDA', 'ILMN', 'INGR', 'IPGP', 'IRDM', 'IRT', 'ITT', 'JAZZ', 'JEF', 'JHG', 'JLL', 'JWN', 'KBH', 'KBR', 'KD', 'KEX', 'KMPR', 'KNF', 'KNSL', 'KNX', 'KRC', 'KRG', 'LAD', 'LAMR', 'LANC', 'LEA', 'LECO', 'LFUS', 'LII', 'LITE', 'LIVN', 'LNTH', 'LNW', 'LOPE', 'LPX', 'LSCC', 'LSTR', 'M', 'MAN', 'MANH', 'MASI', 'MAT', 'MDU', 'MEDP', 'MIDD', 'MKSI', 'MMS', 'MORN', 'MP', 'MSA', 'MSM', 'MTDR', 'MTG', 'MTN', 'MTSI', 'MTZ', 'MUR', 'MUSA', 'NBIX', 'NEOG', 'NEU', 'NFG', 'NJR', 'NLY', 'NNN', 'NOV', 'NOVT', 'NSA', 'NSP', 'NVST', 'NVT', 'NWE', 'NXST', 'NXT', 'NYCB', 'NYT', 'OC', 'OGE', 'OGS', 'OHI', 'OLED', 'OLLI', 'OLN', 'ONB', 'ONTO', 'OPCH', 'ORA', 'ORI', 'OSK', 'OVV', 'OZK', 'PAG', 'PB', 'PBF', 'PCH', 'PCTY', 'PEN', 'PFGC', 'PGNY', 'PII', 'PK', 'PLNT', 'PNFP', 'PNM', 'POR', 'POST', 'POWI', 'PPC', 'PR', 'PRGO', 'PRI', 'PSTG', 'PVH', 'QDEL', 'QLYS', 'R', 'RBA', 'RBC', 'RCM', 'REXR', 'RGA', 'RGEN', 'RGLD', 'RH', 'RLI', 'RMBS', 'RNR', 'ROIV', 'RPM', 'RRC', 'RRX', 'RS', 'RYAN', 'RYN', 'SAIA', 'SAIC', 'SAM', 'SBRA', 'SCI', 'SEIC', 'SF', 'SFM', 'SHC', 'SIGI', 'SKX', 'SLAB', 'SLGN', 'SLM', 'SMG', 'SNV', 'SNX', 'SON', 'SR', 'SRCL', 'SRPT', 'SSB', 'SSD', 'ST', 'STAG', 'STWD', 'SWN', 'SWX', 'SYNA', 'TCBI', 'TDC', 'TEX', 'TGNA', 'THC', 'THG', 'THO', 'TKO', 'TKR', 'TMHC', 'TNL', 'TOL', 'TPL', 'TPX', 'TREX', 'TTC', 'TTEK', 'TXRH', 'UA', 'UAA', 'UBSI', 'UFPI', 'UGI', 'UMBF', 'UNM', 'USFD', 'UTHR', 'VAC', 'VAL', 'VC', 'VLY', 'VMI', 'VNO', 'VNT', 'VOYA', 'VSH', 'VVV', 'WBS', 'WCC', 'WEN', 'WEX', 'WFRD', 'WH', 'WHR', 'WING', 'WLK', 'WMG', 'WMS', 'WOLF', 'WPC', 'WSM', 'WSO', 'WTFC', 'WTRG', 'WTS', 'WU', 'WWD', 'X', 'XPO', 'XRAY', 'YETI', 'ZD', 'ZI', 'ZION']

sp600 = ['AAP', 'AAT', 'ABCB', 'ABG', 'ABM', 'ABR', 'ACA', 'ACIW', 'ACLS', 'ADEA', 'ADUS', 'AEIS', 'AEO', 'AGO', 'AGYS', 'AHCO', 'AHH', 'AIN', 'AIR', 'AKR', 'AL', 'ALEX', 'ALG', 'ALGT', 'ALK', 'ALKS', 'ALRM', 'AMBC', 'AMCX', 'AMN', 'AMPH', 'AMR', 'AMSF', 'AMWD', 'ANDE', 'ANF', 'ANIP', 'AORT', 'AOSL', 'APAM', 'APLE', 'APOG', 'ARCB', 'ARCH', 'ARI', 'ARLO', 'AROC', 'ARR', 'ASIX', 'ASO', 'ASTE', 'ASTH', 'ATEN', 'ATGE', 'ATI', 'AUB', 'AVA', 'AVAV', 'AVNS', 'AWI', 'AWR', 'AX', 'AXL', 'AZZ', 'B', 'BANC', 'BANF', 'BANR', 'BCC', 'BCPC', 'BDN', 'BFH', 'BFS', 'BGC', 'BGS', 'BHE', 'BHLB', 'BJRI', 'BKE', 'BKU', 'BL', 'BLFS', 'BLMN', 'BMI', 'BOH', 'BOOT', 'BOX', 'BRC', 'BRKL', 'BSIG', 'BTU', 'BXMT', 'CABO', 'CAKE', 'CAL', 'CALM', 'CALX', 'CARG', 'CARS', 'CASH', 'CATY', 'CBRL', 'CBU', 'CCOI', 'CCRN', 'CCS', 'CEIX', 'CENT', 'CENTA', 'CENX', 'CERT', 'CEVA', 'CFFN', 'CHCO', 'CHCT', 'CHEF', 'CHUY', 'CLB', 'CLW', 'CMA', 'CMP', 'CNK', 'CNMD', 'CNS', 'CNSL', 'CNXN', 'COHU', 'COLL', 'COOP', 'CORT', 'CPF', 'CPK', 'CPRX', 'CRC', 'CRK', 'CRS', 'CRSR', 'CRVL', 'CSGS', 'CSR', 'CTKB', 'CTRE', 'CTS', 'CUBI', 'CVBF', 'CVCO', 'CVGW', 'CVI', 'CWEN', 'CWEN.A', 'CWK', 'CWT', 'CXM', 'CXW', 'DAN', 'DBI', 'DCOM', 'DDD', 'DEA', 'DEI', 'DFIN', 'DGII', 'DIN', 'DIOD', 'DLX', 'DNOW', 'DOCN', 'DORM', 'DRH', 'DRQ', 'DV', 'DVAX', 'DXC', 'DXPE', 'DY', 'EAT', 'ECPG', 'EFC', 'EGBN', 'EHAB', 'EIG', 'ELME', 'EMBC', 'ENR', 'ENSG', 'ENV', 'ENVA', 'EPAC', 'EPC', 'EPRT', 'ESE', 'ETD', 'EVTC', 'EXPI', 'EXTR', 'EYE', 'EZPW', 'FBK', 'FBNC', 'FBP', 'FBRT', 'FCF', 'FCPT', 'FDP', 'FELE', 'FFBC', 'FHB', 'FIZZ', 'FL', 'FLGT', 'FN', 'FORM', 'FOXF', 'FSS', 'FTDR', 'FTRE', 'FUL', 'FULT', 'FWRD', 'GBX', 'GDEN', 'GDOT', 'GEO', 'GES', 'GFF', 'GIII', 'GKOS', 'GMS', 'GNL', 'GNW', 'GO', 'GOGO', 'GPI', 'GPRE', 'GRBK', 'GSHD', 'GTY', 'GVA', 'HAFC', 'HAIN', 'HASI', 'HAYN', 'HAYW', 'HBI', 'HCC', 'HCI', 'HCSG', 'HFWA', 'HI', 'HIBB', 'HIW', 'HLIT', 'HLX', 'HMN', 'HNI', 'HOPE', 'HP', 'HPP', 'HRMY', 'HSII', 'HSTM', 'HTH', 'HTLD', 'HTZ', 'HUBG', 'HVT', 'HWKN', 'HZO', 'IAC', 'IART', 'IBP', 'IBTX', 'ICHR', 'ICUI', 'IDCC', 'IIIN', 'IIPR', 'INDB', 'INN', 'INVA', 'IOSP', 'IPAR', 'IRWD', 'ITGR', 'ITRI', 'JACK', 'JBGS', 'JBLU', 'JBSS', 'JBT', 'JJSF', 'JOE', 'JXN', 'KALU', 'KAR', 'KELYA', 'KFY', 'KLG', 'KLIC', 'KMT', 'KN', 'KOP', 'KREF', 'KRYS', 'KSS', 'KTB', 'KW', 'KWR', 'LBRT', 'LCII', 'LEG', 'LESL', 'LGIH', 'LGND', 'LKFN', 'LMAT', 'LNC', 'LNN', 'LPG', 'LQDT', 'LRN', 'LTC', 'LUMN', 'LXP', 'LZB', 'MAC', 'MARA', 'MATV', 'MATW', 'MATX', 'MBC', 'MC', 'MCRI', 'MCW', 'MCY', 'MD', 'MERC', 'MGEE', 'MGPI', 'MGY', 'MHO', 'MLAB', 'MLKN', 'MLI', 'MMI', 'MMSI', 'MNRO', 'MODG', 'MOG.A', 'MOV', 'MPW', 'MRCY', 'MRTN', 'MSEX', 'MSGS', 'MTH', 'MTRN', 'MTUS', 'MTX', 'MXL', 'MYE', 'MYGN', 'MYRG', 'NABL', 'NARI', 'NATL', 'NAVI', 'NBHC', 'NBR', 'NBTB', 'NEO', 'NGVT', 'NHC', 'NMIH', 'NOG', 'NPK', 'NPO', 'NSIT', 'NTCT', 'NUS', 'NVEE', 'NVRI', 'NWBI', 'NWL', 'NWN', 'NX', 'NXRT', 'NYMT', 'ODP', 'OFG', 'OGN', 'OI', 'OII', 'OMCL', 'OMI', 'OSIS', 'OTTR', 'OUT', 'OXM', 'PAHC', 'PARR', 'PAYO', 'PATK', 'PBH', 'PBI', 'PCRX', 'PDCO', 'PDFS', 'PEB', 'PECO', 'PENN', 'PFBC', 'PFS', 'PHIN', 'PINC', 'PIPR', 'PJT', 'PLAB', 'PLAY', 'PLMR', 'PLUS', 'PLXS', 'PMT', 'POWL', 'PPBI', 'PRA', 'PRAA', 'PRDO', 'PRFT', 'PRG', 'PRGS', 'PRK', 'PRLB', 'PRVA', 'PSMT', 'PTEN', 'PTGX', 'PUMP', 'PZZA', 'QNST', 'RAMP', 'RC', 'RCUS', 'RDN', 'RDNT', 'RES', 'REX', 'REZI', 'RGNX', 'RGR', 'RHI', 'RILY', 'RNST', 'ROCK', 'ROG', 'ROIC', 'RUN', 'RUSHA', 'RWT', 'RXO', 'SAFE', 'SABR', 'SAFT', 'SAH', 'SANM', 'SATS', 'SBCF', 'SBH', 'SBSI', 'SCHL', 'SCL', 'SCSC', 'SCVL', 'SDGR', 'SEDG', 'SEE', 'SEM', 'SFBS', 'SFNC', 'SGH', 'SHAK', 'SHEN', 'SHO', 'SHOO', 'SIG', 'SITC', 'SITM', 'SJW', 'SKT', 'SKYW', 'SLCA', 'SLG', 'SLP', 'SLVM', 'SM', 'SMP', 'SMPL', 'SMTC', 'SNCY', 'SNEX', 'SONO', 'SPNT', 'SPSC', 'SPTN', 'SPWR', 'SPXC', 'SSTK', 'STAA', 'STBA', 'STC', 'STEL', 'STEP', 'STRA', 'SUPN', 'SVC', 'SXC', 'SXI', 'SXT', 'TALO', 'TBBK', 'TDS', 'TDW', 'TFIN', 'TGI', 'THRM', 'THRY', 'THS', 'TILE', 'TMP', 'TNC', 'TNDM', 'TPH', 'TR', 'TRIP', 'TRMK', 'TRN', 'TRST', 'TRUP', 'TTGT', 'TTMI', 'TWI', 'TWO', 'UCBI', 'UCTT', 'UE', 'UFCS', 'UFPT', 'UHT', 'UNF', 'UNFI', 'UNIT', 'UPBD', 'URBN', 'USNA', 'USPH', 'UTL', 'UVV', 'VBTX', 'VCEL', 'VECO', 'VFC', 'VGR', 'VIAV', 'VICR', 'VIR', 'VIRT', 'VRE', 'VREX', 'VRRM', 'VRTS', 'VSAT', 'VSCO', 'VSTO', 'VSTS', 'VTOL', 'VTLE', 'VVI', 'VYX', 'WABC', 'WAFD', 'WD', 'WDFC', 'WERN', 'WGO', 'WHD', 'WKC', 'WLY', 'WNC', 'WOR', 'WRLD', 'WS', 'WSFS', 'WSR', 'WT', 'WWW', 'XHR', 'XNCR', 'XPEL', 'XRX', 'YELP', 'ZEUS']


from technicalBuildout_V2 import technicalBuildout as tech
from Scraper import Scraper
import pandas as pd
import numpy as np
import csv
from datetime import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib


non_categorical_columns_first = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'emaFast', 'emaFastSlope',
'emaFastSecondDerivative', 'emaSlow', 'emaSlowSlope', 'emaSlowSecondDerivative', 'rawMACD', 'signalMACD', 'histogramMACD', 'slopeMACD', 'ADX', 
'slopeADX', 'posDI', 'negDI', 'fi13', 'fiSlope', 'stochK', 'stochD', 'slopeStoch', 'upperBollinger', 'lowerBollinger', 'deltaBollinger', "Return", "Return_Status", "Lowest_Value", "1.5 ATR Percent"]
non_categorical_columns_second = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'emaFast', 'emaFastSlope',
'emaFastSecondDerivative', 'emaSlow', 'emaSlowSlope', 'emaSlowSecondDerivative', 'rawMACD', 'signalMACD', 'histogramMACD', 'slopeMACD', 'ADX', 
'slopeADX', 'posDI', 'negDI', 'fi13', 'fiSlope', 'stochK', 'stochD', 'slopeStoch', 'upperBollinger', 'lowerBollinger', 'deltaBollinger', "Return_Status", "1.5 ATR Percent"]

# Input Current Positions:
positions = input("Please enter a comma and space separated list of the tickers that you currently own:  ")
if positions != "":
    position_list = positions.split(",")
    pos_returns = {}
    for pos in position_list:
        clean_pos = pos.strip()
        stock = Scraper.scrape_stock(clean_pos, return_df = True, start_date = "2019-01-02")
        if (type(stock) is not str) and (len(stock) > 1000):
            stockTech = tech(stock)
            df = stockTech.technical_buildout(stock)
            df.reset_index(inplace = True)
            df = df.iloc[-1250:]
            df = tech.add_return(df)
            df = df.dropna()
            returns = np.array(df["Return"])
            pos_returns[pos] = returns
else:
    pos_returns = False

results_df = pd.DataFrame(columns = ["Index", "Ticker", "Price", "Number", "Mean Return", "Median Return", "SD Return", "Percent < 1.5%", "Percent < 1%", "Risk Less 0", "Mean Low", "Median Lowest Value", "10th Percentile Low", "Correlation with Portfolio"])


dict_of_lists = {"SP500": sp500, "SP400": sp400, "SP600": sp600}

for sp in dict_of_lists:

    sp_index = []
    tickers = []
    price = []
    number = []
    mean_return = []
    median_return = []
    standard_deviation = []
    percent_less_onepointfive = []
    percent_less_one = []
    risk_less_zero = []
    mean_lowest_value = []
    median_lowest_value = []
    percentile_10_lowest_value = []
    atr = []
    correlation = []
    
    
    for ticker in dict_of_lists[sp]:
        stock = Scraper.scrape_stock(ticker, return_df = True, start_date = "2019-01-02", save = False)
        if (type(stock) is not str) and (len(stock) > 1000):
            stockTech = tech(stock)
            df = stockTech.technical_buildout(stock)
            df.reset_index(inplace = True)
            df = df.iloc[-1250:]
            df = tech.add_return(df)
            pr = df["Close"].iloc[-1]
            atr_curr = df["1.5 ATR Percent"].iloc[-1]
            df_copy = df.drop(non_categorical_columns_first, axis = 1)
            state = df_copy.iloc[-1]
            df = df.dropna()
            returns_for_corr = df["Return"]
            df = df.drop(non_categorical_columns_second, axis = 1)
            for idx in range(len(state)):
                df = df.loc[df[state.index[idx]] == state.iloc[idx]]
            if len(df) != 0:
                return_array = np.array(df["Return"])
                downside_array = np.array(df["Lowest_Value"])
                sp_index.append(sp)
                tickers.append(ticker)
                number.append(len(return_array))
                price.append(pr.round(4))
                mean_return.append(return_array.mean().round(4))
                median_return.append(np.median(return_array).round(4))
                standard_deviation.append(return_array.std().round(4))
                percent_less_onepointfive.append((sum(return_array < 1.5)/len(return_array)).round(4)*100)
                percent_less_one.append((sum(return_array < 1)/len(return_array)).round(4)*100)
                risk_less_zero.append(np.mean(return_array < 0).round(4))
                mean_lowest_value.append(downside_array.mean().round(4))
                median_lowest_value.append(np.median(downside_array).round(4))
                try:
                
                    percentile_10_lowest_value.append(np.quantile(downside_array, .10,  method= "closest_observation").round(4))
                except Exception as e:
                    percentile_10_lowest_value.append(None)

                atr.append(atr_curr * -1)
                
                correlation_dict = {}
                if pos_returns != False:
                    for holding in pos_returns:
                        if ticker == holding:
                            correlation_dict[holding] = 1
                        else:
                            pos_ret = pos_returns[holding]
                            if len(pos_ret) > len(returns_for_corr):
                                pos_ret = pos_ret[-len(returns_for_corr):]
                            else:
                                returns_for_corr = returns_for_corr.iloc[-len(pos_ret):]
                            
                            new_dict = {holding: pos_ret, ticker: returns_for_corr}
                            correlation_df = pd.DataFrame(new_dict)
                            correlation_dict[holding] = correlation_df.corr().iloc[1, 0].round(2)
                else:
                    correlation_dict = "No Holdings"
                    
                correlation.append(correlation_dict)
            else:
                continue
        else:
            continue


    dict = {"Index": sp_index, "Ticker": tickers, "Price": price, "Number": number, "Mean Return": mean_return, "Median Return": median_return, "SD Return": standard_deviation, "Percent < 1.5%": percent_less_onepointfive, "Percent < 1%": percent_less_one, "Risk Less 0": risk_less_zero, "Mean Low": mean_lowest_value, "Median Lowest Value": median_lowest_value, "10th Percentile Low": percentile_10_lowest_value, "1.5 ATR as % of Price": atr, "Correlation with Portfolio": correlation}
    df = pd.DataFrame(dict)
    curr_date = dt.now().strftime("%Y_%m_%d")
    df.to_csv(f"__SAVE PATH__\\results{sp}_{curr_date}.csv", index=False)
    
    slice = df[(df["Number"] > 10) & (df["Risk Less 0"] < .1) & (df["Percent < 1.5%"] < 20) & (df["Mean Low"] > -2) & ((df["Mean Return"] - df["SD Return"]) > 1)] 
    results_df = pd.concat([results_df, slice], ignore_index = True)


results_df.to_csv(f"__SAVE PATH__\\final_picks_{curr_date}.csv", index=False)

recipients = ["__LIST OF EMAIL RECIPIENTS__"]

msg = MIMEMultipart()
body_part = MIMEText("Here are the final stock selections for today", "plain")

msg["Subject"] = f"Runtime Results for {curr_date}"
msg["From"] = '__SENDER EMAIL__'
msg["To"] = ", ".join(recipients)
msg.attach(body_part)

blobfish = '__SENDER EMAIL__'
catfish = '__EMAIL AUTH TOKEN__'

with open(f"__SAVE PATH__\\final_picks_{curr_date}.csv", 'rb') as fp:
    csv_data = fp.read()
    msg.attach(MIMEApplication(csv_data, Name = f"final_picks_{curr_date}.csv"))

server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.login(blobfish, catfish)
server.sendmail(msg['From'], recipients , msg.as_string())
server.quit()

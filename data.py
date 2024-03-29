#First airport(s) should be the hub/depot!

MEMhub = ['MEM', 'ANC', 'SEA', 'GEG', 'GTF',
          'PDX', 'BIL', 'PWM', 'BOI', 'MSP',
          'MHT', 'RNO', 'SLC', 'CPR', 'FSD',
          'RST', 'ATW', 'FNT', 'BUR', 'ROC',
          'SYR', 'ALB', 'BOS', 'BDL', 'PVD',
          'OAK', 'SJC', 'SFO', 'SMF', 'DEN',
          'LAS', 'COS', 'ICT', 'MCI', 'OMA',
          'BUR', 'LAX', 'ONT', 'SNA', 'SAN',
          'PHX', 'ABQ', 'TUS', 'ELP', 'LBB',
          'LRD', 'HRL', 'IAH', 'SAT', 'AUS',
          'AFW', 'DFW', 'SHV', 'LFT', 'MSY',
          'BFM', 'MIA', 'FLL', 'RSW', 'PBI',
          'TPA', 'MCO', 'TLH', 'JAX', 'SAV',
          'CHS', 'CAE', 'ATL', 'BHM', 'HSV',
          'CHA', 'CLT', 'GSP', 'TYS', 'BNA',
          'GSO', 'RDU', 'ORF', 'RIC', 'ROA',
          'OKC', 'TUL', 'SGF', 'STL', 'DSM',
          'CID', 'PIA', 'MSN', 'MKE', 'ORD',
          'SBN', 'FNT', 'DTW', 'GRR', 'FWA',
          'CLE', 'PIT', 'SDF', 'CVG', 'DAY',
          'LCK', 'HTS', 'CRW', 'IAD', 'BWI',
          'MDT', 'PHL', 'ABE', 'JFK', 'EWR',
          'HNL', 'BQN', 'SJU']

MEMhub_s = ['MEM', 'SEA', 'GEG', 'GTF',
          'PDX', 'BIL', 'PWM', 'BOI', 'MSP',
          'MHT', 'RNO', 'SLC', 'CPR', 'FSD',
          'RST', 'ATW', 'FNT', 'BUR', 'ROC',
          'SYR', 'ALB', 'BOS', 'BDL', 'PVD',
          'OAK', 'SJC', 'SFO', 'SMF', 'DEN',
          'LAS', 'COS', 'ICT', 'MCI', 'OMA',
          'BUR', 'LAX', 'ONT', 'SNA', 'SAN',
          'PHX', 'ABQ', 'TUS', 'ELP', 'LBB',
          'LRD', 'HRL', 'IAH', 'SAT', 'AUS',
          'AFW', 'DFW', 'SHV', 'LFT', 'MSY',
          'BFM', 'MIA', 'FLL', 'RSW', 'PBI',
          'TPA', 'MCO', 'TLH', 'JAX', 'SAV',
          'CHS', 'CAE', 'ATL', 'BHM', 'HSV',
          'CHA', 'CLT', 'GSP', 'TYS', 'BNA',
          'GSO', 'RDU', 'ORF', 'RIC', 'ROA',
          'OKC', 'TUL', 'SGF', 'STL', 'DSM',
          'CID', 'PIA', 'MSN', 'MKE', 'ORD',
          'SBN', 'FNT', 'DTW', 'GRR', 'FWA',
          'CLE', 'PIT', 'SDF', 'CVG', 'DAY',
          'LCK', 'HTS', 'CRW', 'IAD', 'BWI',
          'MDT', 'PHL', 'ABE', 'JFK', 'EWR']


OAKhub = ['OAK', 'AFW', 'ANC', 'IND', 'EWR',
          'MEM', 'SEA', 'PDX', 'RNO', 'SLC',
          'MRY', 'FAT', 'VIS', 'LAS', 'LAX',
          'ONT', 'PHX', 'ATL', 'HNL'] 

AFWhub = ['AFW', 'OAK', 'PDX', 'MSP', 'ORD', 
          'MCI', 'ICT', 'TUL', 'LAX', 'DEN',
          'ONT', 'LBB', 'ATL', 'ELP', 'MAF',
          'SHV', 'AUS', 'IAH', 'MSY', 'SAT',
          'FLL', 'HRL']

AFWhub_s = ['AFW', 'OAK' ,'PDX', 'MSP',
            'ORD', 'MCI', 'ICT', 'LAX',
            'LBB', 'ATL', 'ELP', 'DEN',
            'SHV', 'IAH', 'MSY', 'SAT',
            'FLL', 'HRL']

AFWhub_mini = ['AFW', 'PDX', 'MSP', 'ORD', 'DEN',
          'OAK', 'MCI']

MEMDENhub_s = ['MEM', 'DEN', 'GEG', 'GTF',
          'PDX', 'BIL', 'PWM', 'BOI', 'MSP',
          'MHT', 'RNO', 'SLC', 'CPR', 'FSD',
          'RST', 'ATW', 'FNT', 'BUR', 'ROC',
          'SYR', 'ALB', 'BOS', 'BDL', 'PVD',
          'OAK', 'SJC', 'SFO', 'SMF', 'SEA',
          'LAS', 'COS', 'ICT', 'MCI', 'OMA',
          'BUR', 'LAX', 'ONT', 'SNA', 'SAN',
          'PHX', 'ABQ', 'TUS', 'ELP', 'LBB',
          'LRD', 'HRL', 'IAH', 'SAT', 'AUS',
          'AFW', 'DFW', 'SHV', 'LFT', 'MSY',
          'BFM', 'MIA', 'FLL', 'RSW', 'PBI',
          'TPA', 'MCO', 'TLH', 'JAX', 'SAV',
          'CHS', 'CAE', 'ATL', 'BHM', 'HSV',
          'CHA', 'CLT', 'GSP', 'TYS', 'BNA',
          'GSO', 'RDU', 'ORF', 'RIC', 'ROA',
          'OKC', 'TUL', 'SGF', 'STL', 'DSM',
          'CID', 'PIA', 'MSN', 'MKE', 'ORD',
          'SBN', 'FNT', 'DTW', 'GRR', 'FWA',
          'CLE', 'PIT', 'SDF', 'CVG', 'DAY',
          'LCK', 'HTS', 'CRW', 'IAD', 'BWI',
          'MDT', 'PHL', 'ABE', 'JFK', 'EWR']
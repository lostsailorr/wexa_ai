// ==========================================
// EMBEDDED REALISTIC DATASET (CLIENT-SIDE RESILIENCE)
// ==========================================
const DEFAULT_NODES = [
  {
    "id": "P-101",
    "label": "Person",
    "name": "Viktor Sterling",
    "nationality": "Russian",
    "is_pep": true,
    "base_risk": 0.94,
    "role": "Beneficial Owner / Politically Exposed"
  },
  {
    "id": "P-102",
    "label": "Person",
    "name": "Elena Sterling",
    "nationality": "Cypriot",
    "is_pep": true,
    "base_risk": 0.78,
    "role": "Nominee Director / Spouse"
  },
  {
    "id": "P-103",
    "label": "Person",
    "name": "Marcus Vance",
    "nationality": "British",
    "is_pep": false,
    "base_risk": 0.65,
    "role": "Corporate Lawyer & Escrow Agent"
  },
  {
    "id": "P-104",
    "label": "Person",
    "name": "Chloe Dubois",
    "nationality": "Swiss",
    "is_pep": false,
    "base_risk": 0.35,
    "role": "Private Wealth Manager"
  },
  {
    "id": "P-105",
    "label": "Person",
    "name": "Tariq Al-Mansoor",
    "nationality": "Emirati",
    "is_pep": false,
    "base_risk": 0.52,
    "role": "Trade Broker & Director"
  },
  {
    "id": "P-106",
    "label": "Person",
    "name": "Sergei Volkov",
    "nationality": "Russian",
    "is_pep": true,
    "base_risk": 0.99,
    "role": "Defense Contractor / Sanctioned Entity"
  },
  {
    "id": "P-107",
    "label": "Person",
    "name": "Lin Wei",
    "nationality": "Singaporean",
    "is_pep": false,
    "base_risk": 0.22,
    "role": "Logistics Managing Director"
  },
  {
    "id": "P-108",
    "label": "Person",
    "name": "Sofia Rossi",
    "nationality": "Italian",
    "is_pep": false,
    "base_risk": 0.28,
    "role": "Maritime Assets Broker"
  },
  {
    "id": "P-109",
    "label": "Person",
    "name": "Hans Gruber",
    "nationality": "German",
    "is_pep": false,
    "base_risk": 0.12,
    "role": "CleanTech Consultant"
  },
  {
    "id": "P-110",
    "label": "Person",
    "name": "Arthur Pendelton",
    "nationality": "Bermudian",
    "is_pep": false,
    "base_risk": 0.72,
    "role": "Offshore Trust Fiduciary"
  },
  {
    "id": "C-201",
    "label": "Company",
    "name": "Seashell Global Holdings Ltd",
    "jurisdiction": "BVI",
    "company_type": "Offshore Shell",
    "risk_score": 0.91,
    "status": "Active"
  },
  {
    "id": "C-202",
    "label": "Company",
    "name": "Apex Meridian Trading S.A.",
    "jurisdiction": "Cyprus",
    "company_type": "Intermediary Holding",
    "risk_score": 0.86,
    "status": "Active"
  },
  {
    "id": "C-203",
    "label": "Company",
    "name": "Golden Horizon Logistics Ltd",
    "jurisdiction": "United Kingdom",
    "company_type": "Front Operational",
    "risk_score": 0.62,
    "status": "Active"
  },
  {
    "id": "C-204",
    "label": "Company",
    "name": "Sovereign Blue Maritime Corp",
    "jurisdiction": "Panama",
    "company_type": "Vessel Special Purpose Vehicle",
    "risk_score": 0.88,
    "status": "Active"
  },
  {
    "id": "C-205",
    "label": "Company",
    "name": "Vostok Precision Dynamics",
    "jurisdiction": "Russia",
    "company_type": "Dual-Use Tech Manufacturing",
    "risk_score": 0.99,
    "status": "Sanctioned"
  },
  {
    "id": "C-206",
    "label": "Company",
    "name": "Silk Route Commodities FZE",
    "jurisdiction": "UAE",
    "company_type": "Freezone Trading Broker",
    "risk_score": 0.68,
    "status": "Active"
  },
  {
    "id": "C-207",
    "label": "Company",
    "name": "Alpine Crest Advisory AG",
    "jurisdiction": "Switzerland",
    "company_type": "Asset Management",
    "risk_score": 0.35,
    "status": "Active"
  },
  {
    "id": "C-208",
    "label": "Company",
    "name": "Lumina Capital Partners LP",
    "jurisdiction": "United States",
    "company_type": "Commercial Real Estate Fund",
    "risk_score": 0.48,
    "status": "Active"
  },
  {
    "id": "C-209",
    "label": "Company",
    "name": "Nordic CleanTech Solutions AB",
    "jurisdiction": "Sweden",
    "company_type": "Renewable Tech (Decoy)",
    "risk_score": 0.1,
    "status": "Active"
  },
  {
    "id": "C-210",
    "label": "Company",
    "name": "Pacific Rim Exports Pte",
    "jurisdiction": "Singapore",
    "company_type": "Import/Export Hub",
    "risk_score": 0.25,
    "status": "Active"
  },
  {
    "id": "C-211",
    "label": "Company",
    "name": "Blue Water Real Estate GmbH",
    "jurisdiction": "Germany",
    "company_type": "Luxury Property Holding",
    "risk_score": 0.5,
    "status": "Active"
  },
  {
    "id": "ACC-9001",
    "label": "BankAccount",
    "name": "CH93-Zurich-Private",
    "account_number": "ACC-9001",
    "bank_name": "Credit Suisse Private Banking",
    "country": "Switzerland",
    "balance": 4500000.0,
    "risk_level": "LOW"
  },
  {
    "id": "ACC-9002",
    "label": "BankAccount",
    "name": "CY21-Nicosia-Commercial",
    "account_number": "ACC-9002",
    "bank_name": "Bank of Cyprus Commercial",
    "country": "Cyprus",
    "balance": 1820000.0,
    "risk_level": "HIGH"
  },
  {
    "id": "ACC-9003",
    "label": "BankAccount",
    "name": "VG80-RoadTown-Offshore",
    "account_number": "ACC-9003",
    "bank_name": "BVI International Trust Bank",
    "country": "BVI",
    "balance": 8900000.0,
    "risk_level": "CRITICAL"
  },
  {
    "id": "ACC-9004",
    "label": "BankAccount",
    "name": "GB29-London-Metro",
    "account_number": "ACC-9004",
    "bank_name": "Barclays Commercial London",
    "country": "United Kingdom",
    "balance": 640000.0,
    "risk_level": "MEDIUM"
  },
  {
    "id": "ACC-9005",
    "label": "BankAccount",
    "name": "AE07-Dubai-Mashreq",
    "account_number": "ACC-9005",
    "bank_name": "Emirates NBD Freezone",
    "country": "UAE",
    "balance": 3100000.0,
    "risk_level": "HIGH"
  },
  {
    "id": "ACC-9006",
    "label": "BankAccount",
    "name": "PA15-Panama-Pacific",
    "account_number": "ACC-9006",
    "bank_name": "Banco General Panama",
    "country": "Panama",
    "balance": 2400000.0,
    "risk_level": "CRITICAL"
  },
  {
    "id": "ACC-9007",
    "label": "BankAccount",
    "name": "RU40-Moscow-Sber",
    "account_number": "ACC-9007",
    "bank_name": "Gazprombank Commercial",
    "country": "Russia",
    "balance": 12500000.0,
    "risk_level": "CRITICAL"
  },
  {
    "id": "ACC-9008",
    "label": "BankAccount",
    "name": "SG65-DBS-Singapore",
    "account_number": "ACC-9008",
    "bank_name": "DBS Corporate Singapore",
    "country": "Singapore",
    "balance": 1100000.0,
    "risk_level": "LOW"
  },
  {
    "id": "ACC-9009",
    "label": "BankAccount",
    "name": "US12-JPMorgan-NYC",
    "account_number": "ACC-9009",
    "bank_name": "JPMorgan Chase NYC",
    "country": "United States",
    "balance": 5200000.0,
    "risk_level": "MEDIUM"
  },
  {
    "id": "ACC-9010",
    "label": "BankAccount",
    "name": "DE89-Frankfurt-DB",
    "account_number": "ACC-9010",
    "bank_name": "Deutsche Bank Frankfurt",
    "country": "Germany",
    "balance": 980000.0,
    "risk_level": "LOW"
  },
  {
    "id": "ACC-9011",
    "label": "BankAccount",
    "name": "SE50-Stockholm-SEB",
    "account_number": "ACC-9011",
    "bank_name": "SEB Nordic Business",
    "country": "Sweden",
    "balance": 450000.0,
    "risk_level": "LOW"
  },
  {
    "id": "ACC-9012",
    "label": "BankAccount",
    "name": "KY11-Cayman-Mule-Transit",
    "account_number": "ACC-9012",
    "bank_name": "Cayman Grand Trust Bank",
    "country": "Cayman Islands",
    "balance": 120000.0,
    "risk_level": "CRITICAL"
  },
  {
    "id": "ACC-9013",
    "label": "BankAccount",
    "name": "MH22-Majuro-Escrow",
    "account_number": "ACC-9013",
    "bank_name": "Marshall Trust Depository",
    "country": "Marshall Islands",
    "balance": 85000.0,
    "risk_level": "CRITICAL"
  },
  {
    "id": "SANCT-OFAC-SDN",
    "label": "SanctionList",
    "name": "OFAC SDN List",
    "authority": "US Dept of Treasury",
    "program": "UKRAINE-EO14024 / DEFENSE_SECTOR",
    "date_listed": "2022-04-15",
    "reason": "Dual-use technology procurement & weapons proliferation funding"
  },
  {
    "id": "SANCT-EU-CFSP",
    "label": "SanctionList",
    "name": "EU Consolidated Sanctions",
    "authority": "European External Action Service",
    "program": "REG_269_2014",
    "date_listed": "2022-05-10",
    "reason": "Destabilizing actions & illicit financial asset concealment"
  },
  {
    "id": "JUR-BVI",
    "label": "Jurisdiction",
    "name": "British Virgin Islands",
    "code": "BVI",
    "risk_tier": "TIER_3_HIGH",
    "tax_haven": true
  },
  {
    "id": "JUR-CY",
    "label": "Jurisdiction",
    "name": "Cyprus",
    "code": "CY",
    "risk_tier": "TIER_2_MEDIUM",
    "tax_haven": true
  },
  {
    "id": "JUR-PA",
    "label": "Jurisdiction",
    "name": "Panama",
    "code": "PA",
    "risk_tier": "TIER_3_HIGH",
    "tax_haven": true
  },
  {
    "id": "JUR-RU",
    "label": "Jurisdiction",
    "name": "Russia",
    "code": "RU",
    "risk_tier": "TIER_3_HIGH",
    "tax_haven": false
  },
  {
    "id": "JUR-AE",
    "label": "Jurisdiction",
    "name": "United Arab Emirates",
    "code": "AE",
    "risk_tier": "TIER_2_MEDIUM",
    "tax_haven": true
  },
  {
    "id": "JUR-CH",
    "label": "Jurisdiction",
    "name": "Switzerland",
    "code": "CH",
    "risk_tier": "TIER_1_LOW",
    "tax_haven": false
  },
  {
    "id": "JUR-GB",
    "label": "Jurisdiction",
    "name": "United Kingdom",
    "code": "GB",
    "risk_tier": "TIER_1_LOW",
    "tax_haven": false
  },
  {
    "id": "JUR-US",
    "label": "Jurisdiction",
    "name": "United States",
    "code": "US",
    "risk_tier": "TIER_1_LOW",
    "tax_haven": false
  }
];
const DEFAULT_EDGES = [
  {
    "id": "E-101",
    "type": "OWNS",
    "source": "P-101",
    "target": "C-201",
    "properties": {
      "share_pct": 100.0,
      "since": "2020-03-15",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-102",
    "type": "OWNS",
    "source": "C-201",
    "target": "C-202",
    "properties": {
      "share_pct": 85.0,
      "since": "2020-08-01",
      "voting_rights": 85.0
    }
  },
  {
    "id": "E-103",
    "type": "OWNS",
    "source": "C-202",
    "target": "C-203",
    "properties": {
      "share_pct": 90.0,
      "since": "2021-02-14",
      "voting_rights": 90.0
    }
  },
  {
    "id": "E-104",
    "type": "OWNS",
    "source": "C-203",
    "target": "C-208",
    "properties": {
      "share_pct": 75.0,
      "since": "2021-11-20",
      "voting_rights": 75.0
    }
  },
  {
    "id": "E-105",
    "type": "OWNS",
    "source": "P-102",
    "target": "C-204",
    "properties": {
      "share_pct": 100.0,
      "since": "2019-06-10",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-106",
    "type": "OWNS",
    "source": "C-204",
    "target": "C-211",
    "properties": {
      "share_pct": 100.0,
      "since": "2021-04-05",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-107",
    "type": "OWNS",
    "source": "P-106",
    "target": "C-205",
    "properties": {
      "share_pct": 100.0,
      "since": "2018-01-01",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-108",
    "type": "OWNS",
    "source": "P-105",
    "target": "C-206",
    "properties": {
      "share_pct": 100.0,
      "since": "2020-09-12",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-109",
    "type": "OWNS",
    "source": "P-107",
    "target": "C-210",
    "properties": {
      "share_pct": 100.0,
      "since": "2019-12-01",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-110",
    "type": "OWNS",
    "source": "P-109",
    "target": "C-209",
    "properties": {
      "share_pct": 100.0,
      "since": "2022-01-15",
      "voting_rights": 100.0
    }
  },
  {
    "id": "E-201",
    "type": "DIRECTOR_OF",
    "source": "P-102",
    "target": "C-201",
    "properties": {
      "role": "Nominee Director",
      "appointed": "2020-03-15"
    }
  },
  {
    "id": "E-202",
    "type": "DIRECTOR_OF",
    "source": "P-103",
    "target": "C-203",
    "properties": {
      "role": "Corporate Secretary",
      "appointed": "2021-02-14"
    }
  },
  {
    "id": "E-203",
    "type": "DIRECTOR_OF",
    "source": "P-110",
    "target": "C-201",
    "properties": {
      "role": "Resident Agent",
      "appointed": "2020-03-15"
    }
  },
  {
    "id": "E-204",
    "type": "DIRECTOR_OF",
    "source": "P-104",
    "target": "C-207",
    "properties": {
      "role": "Managing Director",
      "appointed": "2017-05-01"
    }
  },
  {
    "id": "E-301",
    "type": "HOLDS_ACCOUNT",
    "source": "C-201",
    "target": "ACC-9003",
    "properties": {
      "opened": "2020-03-20"
    }
  },
  {
    "id": "E-302",
    "type": "HOLDS_ACCOUNT",
    "source": "C-202",
    "target": "ACC-9002",
    "properties": {
      "opened": "2020-08-10"
    }
  },
  {
    "id": "E-303",
    "type": "HOLDS_ACCOUNT",
    "source": "C-203",
    "target": "ACC-9004",
    "properties": {
      "opened": "2021-02-25"
    }
  },
  {
    "id": "E-304",
    "type": "HOLDS_ACCOUNT",
    "source": "C-204",
    "target": "ACC-9006",
    "properties": {
      "opened": "2019-06-20"
    }
  },
  {
    "id": "E-305",
    "type": "HOLDS_ACCOUNT",
    "source": "C-205",
    "target": "ACC-9007",
    "properties": {
      "opened": "2018-02-01"
    }
  },
  {
    "id": "E-306",
    "type": "HOLDS_ACCOUNT",
    "source": "C-206",
    "target": "ACC-9005",
    "properties": {
      "opened": "2020-09-25"
    }
  },
  {
    "id": "E-307",
    "type": "HOLDS_ACCOUNT",
    "source": "C-207",
    "target": "ACC-9001",
    "properties": {
      "opened": "2017-06-15"
    }
  },
  {
    "id": "E-308",
    "type": "HOLDS_ACCOUNT",
    "source": "C-208",
    "target": "ACC-9009",
    "properties": {
      "opened": "2021-12-01"
    }
  },
  {
    "id": "E-309",
    "type": "HOLDS_ACCOUNT",
    "source": "C-209",
    "target": "ACC-9011",
    "properties": {
      "opened": "2022-02-01"
    }
  },
  {
    "id": "E-310",
    "type": "HOLDS_ACCOUNT",
    "source": "C-210",
    "target": "ACC-9008",
    "properties": {
      "opened": "2019-12-10"
    }
  },
  {
    "id": "E-311",
    "type": "HOLDS_ACCOUNT",
    "source": "C-211",
    "target": "ACC-9010",
    "properties": {
      "opened": "2021-04-20"
    }
  },
  {
    "id": "E-401",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9003",
    "target": "ACC-9002",
    "properties": {
      "amount": 850000.0,
      "currency": "USD",
      "timestamp": "2023-11-01T09:15:00Z",
      "tx_id": "TX-SMURF-101",
      "risk_flag": true
    }
  },
  {
    "id": "E-402",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9002",
    "target": "ACC-9005",
    "properties": {
      "amount": 820000.0,
      "currency": "USD",
      "timestamp": "2023-11-02T11:30:00Z",
      "tx_id": "TX-SMURF-102",
      "risk_flag": true
    }
  },
  {
    "id": "E-403",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9005",
    "target": "ACC-9012",
    "properties": {
      "amount": 790000.0,
      "currency": "USD",
      "timestamp": "2023-11-03T14:45:00Z",
      "tx_id": "TX-SMURF-103",
      "risk_flag": true
    }
  },
  {
    "id": "E-404",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9012",
    "target": "ACC-9003",
    "properties": {
      "amount": 760000.0,
      "currency": "USD",
      "timestamp": "2023-11-04T16:20:00Z",
      "tx_id": "TX-SMURF-104",
      "risk_flag": true
    }
  },
  {
    "id": "E-405",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9006",
    "target": "ACC-9013",
    "properties": {
      "amount": 600000.0,
      "currency": "USD",
      "timestamp": "2023-12-10T10:00:00Z",
      "tx_id": "TX-LAYER-201",
      "risk_flag": true
    }
  },
  {
    "id": "E-406",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9013",
    "target": "ACC-9004",
    "properties": {
      "amount": 580000.0,
      "currency": "USD",
      "timestamp": "2023-12-11T13:10:00Z",
      "tx_id": "TX-LAYER-202",
      "risk_flag": true
    }
  },
  {
    "id": "E-407",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9004",
    "target": "ACC-9006",
    "properties": {
      "amount": 550000.0,
      "currency": "USD",
      "timestamp": "2023-12-12T15:40:00Z",
      "tx_id": "TX-LAYER-203",
      "risk_flag": true
    }
  },
  {
    "id": "E-408",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9007",
    "target": "ACC-9005",
    "properties": {
      "amount": 1450000.0,
      "currency": "USD",
      "timestamp": "2024-01-08T08:00:00Z",
      "tx_id": "TX-SANCT-301",
      "risk_flag": true
    }
  },
  {
    "id": "E-409",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9005",
    "target": "ACC-9004",
    "properties": {
      "amount": 1400000.0,
      "currency": "USD",
      "timestamp": "2024-01-10T11:20:00Z",
      "tx_id": "TX-SANCT-302",
      "risk_flag": true
    }
  },
  {
    "id": "E-410",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9004",
    "target": "ACC-9009",
    "properties": {
      "amount": 1350000.0,
      "currency": "USD",
      "timestamp": "2024-01-12T16:00:00Z",
      "tx_id": "TX-SANCT-303",
      "risk_flag": true
    }
  },
  {
    "id": "E-411",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9008",
    "target": "ACC-9011",
    "properties": {
      "amount": 180000.0,
      "currency": "EUR",
      "timestamp": "2024-02-01T10:00:00Z",
      "tx_id": "TX-LEGIT-401",
      "risk_flag": false
    }
  },
  {
    "id": "E-412",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9011",
    "target": "ACC-9010",
    "properties": {
      "amount": 95000.0,
      "currency": "EUR",
      "timestamp": "2024-02-05T14:30:00Z",
      "tx_id": "TX-LEGIT-402",
      "risk_flag": false
    }
  },
  {
    "id": "E-413",
    "type": "TRANSFERRED_TO",
    "source": "ACC-9001",
    "target": "ACC-9010",
    "properties": {
      "amount": 320000.0,
      "currency": "EUR",
      "timestamp": "2024-02-15T09:45:00Z",
      "tx_id": "TX-LEGIT-403",
      "risk_flag": false
    }
  },
  {
    "id": "E-501",
    "type": "SANCTIONED_UNDER",
    "source": "P-106",
    "target": "SANCT-OFAC-SDN",
    "properties": {
      "listed_date": "2022-04-15",
      "notice": "Executive Order 14024"
    }
  },
  {
    "id": "E-502",
    "type": "SANCTIONED_UNDER",
    "source": "C-205",
    "target": "SANCT-OFAC-SDN",
    "properties": {
      "listed_date": "2022-04-15",
      "notice": "Specially Designated Tech Entity"
    }
  },
  {
    "id": "E-503",
    "type": "SANCTIONED_UNDER",
    "source": "P-101",
    "target": "SANCT-EU-CFSP",
    "properties": {
      "listed_date": "2022-05-10",
      "notice": "EU High Net-Worth Oligarch Annex I"
    }
  },
  {
    "id": "E-601",
    "type": "REGISTERED_IN",
    "source": "C-201",
    "target": "JUR-BVI",
    "properties": {}
  },
  {
    "id": "E-602",
    "type": "REGISTERED_IN",
    "source": "C-202",
    "target": "JUR-CY",
    "properties": {}
  },
  {
    "id": "E-603",
    "type": "REGISTERED_IN",
    "source": "C-204",
    "target": "JUR-PA",
    "properties": {}
  },
  {
    "id": "E-604",
    "type": "REGISTERED_IN",
    "source": "C-205",
    "target": "JUR-RU",
    "properties": {}
  },
  {
    "id": "E-605",
    "type": "REGISTERED_IN",
    "source": "C-206",
    "target": "JUR-AE",
    "properties": {}
  },
  {
    "id": "E-606",
    "type": "REGISTERED_IN",
    "source": "C-207",
    "target": "JUR-CH",
    "properties": {}
  },
  {
    "id": "E-607",
    "type": "REGISTERED_IN",
    "source": "C-203",
    "target": "JUR-GB",
    "properties": {}
  },
  {
    "id": "E-608",
    "type": "REGISTERED_IN",
    "source": "C-208",
    "target": "JUR-US",
    "properties": {}
  }
];
const DEFAULT_RINGS = [
  {
    "origin_account": "ACC-9003",
    "origin_bank": "BVI International Trust Bank",
    "loop_length": 4,
    "total_volume": 3220000.0,
    "account_chain": [
      "ACC-9003",
      "ACC-9002",
      "ACC-9005",
      "ACC-9012",
      "ACC-9003"
    ],
    "transaction_chain": [
      "TX-SMURF-101",
      "TX-SMURF-102",
      "TX-SMURF-103",
      "TX-SMURF-104"
    ],
    "ring_nodes": [
      {
        "id": "ACC-9003",
        "label": "BankAccount",
        "account_number": "ACC-9003",
        "bank_name": "BVI International Trust Bank",
        "country": "BVI",
        "risk_level": "CRITICAL"
      },
      {
        "id": "ACC-9002",
        "label": "BankAccount",
        "account_number": "ACC-9002",
        "bank_name": "Bank of Cyprus Commercial",
        "country": "Cyprus",
        "risk_level": "HIGH"
      },
      {
        "id": "ACC-9005",
        "label": "BankAccount",
        "account_number": "ACC-9005",
        "bank_name": "Emirates NBD Freezone",
        "country": "UAE",
        "risk_level": "HIGH"
      },
      {
        "id": "ACC-9012",
        "label": "BankAccount",
        "account_number": "ACC-9012",
        "bank_name": "Cayman Grand Trust Bank",
        "country": "Cayman Islands",
        "risk_level": "CRITICAL"
      }
    ],
    "ring_edges": [
      {
        "tx_id": "TX-SMURF-101",
        "amount": 850000.0,
        "currency": "USD",
        "timestamp": "2023-11-01T09:15:00Z",
        "from_acc": "ACC-9003",
        "to_acc": "ACC-9002"
      },
      {
        "tx_id": "TX-SMURF-102",
        "amount": 820000.0,
        "currency": "USD",
        "timestamp": "2023-11-02T11:30:00Z",
        "from_acc": "ACC-9002",
        "to_acc": "ACC-9005"
      },
      {
        "tx_id": "TX-SMURF-103",
        "amount": 790000.0,
        "currency": "USD",
        "timestamp": "2023-11-03T14:45:00Z",
        "from_acc": "ACC-9005",
        "to_acc": "ACC-9012"
      },
      {
        "tx_id": "TX-SMURF-104",
        "amount": 760000.0,
        "currency": "USD",
        "timestamp": "2023-11-04T16:20:00Z",
        "from_acc": "ACC-9012",
        "to_acc": "ACC-9003"
      }
    ]
  },
  {
    "origin_account": "ACC-9006",
    "origin_bank": "Banco General Panama",
    "loop_length": 3,
    "total_volume": 1730000.0,
    "account_chain": [
      "ACC-9006",
      "ACC-9013",
      "ACC-9004",
      "ACC-9006"
    ],
    "transaction_chain": [
      "TX-LAYER-201",
      "TX-LAYER-202",
      "TX-LAYER-203"
    ],
    "ring_nodes": [
      {
        "id": "ACC-9006",
        "label": "BankAccount",
        "account_number": "ACC-9006",
        "bank_name": "Banco General Panama",
        "country": "Panama",
        "risk_level": "CRITICAL"
      },
      {
        "id": "ACC-9013",
        "label": "BankAccount",
        "account_number": "ACC-9013",
        "bank_name": "Marshall Trust Depository",
        "country": "Marshall Islands",
        "risk_level": "CRITICAL"
      },
      {
        "id": "ACC-9004",
        "label": "BankAccount",
        "account_number": "ACC-9004",
        "bank_name": "Barclays Commercial London",
        "country": "United Kingdom",
        "risk_level": "MEDIUM"
      }
    ],
    "ring_edges": [
      {
        "tx_id": "TX-LAYER-201",
        "amount": 600000.0,
        "currency": "USD",
        "timestamp": "2023-12-10T10:00:00Z",
        "from_acc": "ACC-9006",
        "to_acc": "ACC-9013"
      },
      {
        "tx_id": "TX-LAYER-202",
        "amount": 580000.0,
        "currency": "USD",
        "timestamp": "2023-12-11T13:10:00Z",
        "from_acc": "ACC-9013",
        "to_acc": "ACC-9004"
      },
      {
        "tx_id": "TX-LAYER-203",
        "amount": 550000.0,
        "currency": "USD",
        "timestamp": "2023-12-12T15:40:00Z",
        "from_acc": "ACC-9004",
        "to_acc": "ACC-9006"
      }
    ]
  }
];
const DEFAULT_UBO = {
  "C-208": [
    {
      "ubo_id": "P-101",
      "ubo_name": "Viktor Sterling",
      "nationality": "Russian",
      "is_pep": true,
      "person_risk": 0.94,
      "company_id": "C-208",
      "company_name": "Lumina Capital Partners LP",
      "effective_ownership_pct": 57.38,
      "ownership_depth": 4,
      "ownership_chain": [
        {
          "id": "P-101",
          "name": "Viktor Sterling",
          "type": "Person",
          "risk_score": 0.94,
          "jurisdiction": "Russian"
        },
        {
          "id": "C-201",
          "name": "Seashell Global Holdings Ltd",
          "type": "Company",
          "risk_score": 0.91,
          "jurisdiction": "BVI"
        },
        {
          "id": "C-202",
          "name": "Apex Meridian Trading S.A.",
          "type": "Company",
          "risk_score": 0.86,
          "jurisdiction": "Cyprus"
        },
        {
          "id": "C-203",
          "name": "Golden Horizon Logistics Ltd",
          "type": "Company",
          "risk_score": 0.62,
          "jurisdiction": "United Kingdom"
        },
        {
          "id": "C-208",
          "name": "Lumina Capital Partners LP",
          "type": "Company",
          "risk_score": 0.48,
          "jurisdiction": "United States"
        }
      ],
      "relationship_chain": [
        {
          "share_pct": 100.0,
          "since": "2020-03-15"
        },
        {
          "share_pct": 85.0,
          "since": "2020-08-01"
        },
        {
          "share_pct": 90.0,
          "since": "2021-02-14"
        },
        {
          "share_pct": 75.0,
          "since": "2021-11-20"
        }
      ]
    }
  ],
  "C-211": [
    {
      "ubo_id": "P-102",
      "ubo_name": "Elena Sterling",
      "nationality": "Cypriot",
      "is_pep": true,
      "person_risk": 0.78,
      "company_id": "C-211",
      "company_name": "Blue Water Real Estate GmbH",
      "effective_ownership_pct": 100.0,
      "ownership_depth": 2,
      "ownership_chain": [
        {
          "id": "P-102",
          "name": "Elena Sterling",
          "type": "Person",
          "risk_score": 0.78,
          "jurisdiction": "Cypriot"
        },
        {
          "id": "C-204",
          "name": "Sovereign Blue Maritime Corp",
          "type": "Company",
          "risk_score": 0.88,
          "jurisdiction": "Panama"
        },
        {
          "id": "C-211",
          "name": "Blue Water Real Estate GmbH",
          "type": "Company",
          "risk_score": 0.5,
          "jurisdiction": "Germany"
        }
      ],
      "relationship_chain": [
        {
          "share_pct": 100.0,
          "since": "2019-06-10"
        },
        {
          "share_pct": 100.0,
          "since": "2021-04-05"
        }
      ]
    }
  ]
};
const DEFAULT_SANCTIONS = {
  "C-208": {
    "found": true,
    "path": {
      "distance": 4,
      "sanction_id": "SANCT-OFAC-SDN",
      "sanctioning_body": "US Dept of Treasury",
      "sanction_program": "UKRAINE-EO14024 / DEFENSE_SECTOR",
      "sanction_reason": "Dual-use technology procurement & weapons proliferation funding",
      "path_nodes": [
        {
          "id": "C-208",
          "name": "Lumina Capital Partners LP",
          "label": "Company",
          "risk_score": 0.48,
          "country": "United States"
        },
        {
          "id": "ACC-9009",
          "name": "ACC-9009",
          "label": "BankAccount",
          "risk_score": 0.0,
          "country": "United States"
        },
        {
          "id": "ACC-9004",
          "name": "ACC-9004",
          "label": "BankAccount",
          "risk_score": 0.0,
          "country": "United Kingdom"
        },
        {
          "id": "ACC-9005",
          "name": "ACC-9005",
          "label": "BankAccount",
          "risk_score": 0.0,
          "country": "UAE"
        },
        {
          "id": "ACC-9007",
          "name": "ACC-9007",
          "label": "BankAccount",
          "risk_score": 0.0,
          "country": "Russia"
        },
        {
          "id": "C-205",
          "name": "Vostok Precision Dynamics",
          "label": "Company",
          "risk_score": 0.99,
          "country": "Russia"
        },
        {
          "id": "SANCT-OFAC-SDN",
          "name": "OFAC SDN List",
          "label": "SanctionList",
          "risk_score": 1.0,
          "country": "N/A"
        }
      ],
      "path_relationships": [
        {
          "type": "HOLDS_ACCOUNT",
          "from_id": "C-208",
          "to_id": "ACC-9009",
          "properties": {}
        },
        {
          "type": "TRANSFERRED_TO",
          "from_id": "ACC-9004",
          "to_id": "ACC-9009",
          "properties": {
            "amount": 1350000.0,
            "tx_id": "TX-SANCT-303"
          }
        },
        {
          "type": "TRANSFERRED_TO",
          "from_id": "ACC-9005",
          "to_id": "ACC-9004",
          "properties": {
            "amount": 1400000.0,
            "tx_id": "TX-SANCT-302"
          }
        },
        {
          "type": "TRANSFERRED_TO",
          "from_id": "ACC-9007",
          "to_id": "ACC-9005",
          "properties": {
            "amount": 1450000.0,
            "tx_id": "TX-SANCT-301"
          }
        },
        {
          "type": "HOLDS_ACCOUNT",
          "from_id": "C-205",
          "to_id": "ACC-9007",
          "properties": {}
        },
        {
          "type": "SANCTIONED_UNDER",
          "from_id": "C-205",
          "to_id": "SANCT-OFAC-SDN",
          "properties": {}
        }
      ]
    }
  },
  "P-101": {
    "found": true,
    "path": {
      "distance": 1,
      "sanction_id": "SANCT-EU-CFSP",
      "sanctioning_body": "European External Action Service",
      "sanction_program": "REG_269_2014",
      "sanction_reason": "Destabilizing actions & illicit financial asset concealment",
      "path_nodes": [
        {
          "id": "P-101",
          "name": "Viktor Sterling",
          "label": "Person",
          "risk_score": 0.94,
          "country": "Russian"
        },
        {
          "id": "SANCT-EU-CFSP",
          "name": "EU Consolidated Sanctions",
          "label": "SanctionList",
          "risk_score": 1.0,
          "country": "N/A"
        }
      ],
      "path_relationships": [
        {
          "type": "SANCTIONED_UNDER",
          "from_id": "P-101",
          "to_id": "SANCT-EU-CFSP",
          "properties": {
            "listed_date": "2022-05-10"
          }
        }
      ]
    }
  }
};
const DEFAULT_MULE_HUBS = [
  {
    "account_number": "ACC-9005",
    "bank_name": "Emirates NBD Freezone",
    "country": "UAE",
    "risk_level": "HIGH",
    "unique_senders": 2,
    "unique_recipients": 2,
    "total_inflow": 2270000.0,
    "total_outflow": 2190000.0,
    "net_retention": 80000.0,
    "centrality_index": 6.0
  },
  {
    "account_number": "ACC-9004",
    "bank_name": "Barclays Commercial London",
    "country": "United Kingdom",
    "risk_level": "MEDIUM",
    "unique_senders": 2,
    "unique_recipients": 2,
    "total_inflow": 1980000.0,
    "total_outflow": 1900000.0,
    "net_retention": 80000.0,
    "centrality_index": 6.0
  }
];

let networkInstance = null;
let graphData = { nodes: [], edges: [] };
let rawNodes = [];
let rawEdges = [];
let visNodesDataSet = null;
let visEdgesDataSet = null;

// Initialize when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  if (window.lucide) {
    lucide.createIcons();
  }
  checkDatabaseHealth();
  loadMetrics();
  loadInitialGraph();
  setupSearch();
  loadCircularRings();
  loadMuleHubs();
});

// ==========================================
// 1. HEALTH & METRICS
// ==========================================
async function checkDatabaseHealth() {
  const badge = document.getElementById("dbStatusBadge");
  const text = document.getElementById("dbStatusText");
  try {
    const res = await fetch("/api/admin/health");
    const data = await res.json();
    if (data.database.connected) {
      badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-400";
      text.innerText = "CognoDB Cloud (Connected)";
    } else {
      badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300";
      text.innerText = "Demo Simulation Mode";
    }
  } catch (err) {
    badge.className = "flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-amber-500/10 border border-amber-500/30 text-xs text-amber-300";
    text.innerText = "Demo Simulation Mode";
  }
}

async function loadMetrics() {
  let m = {
    person_count: DEFAULT_NODES.filter(n => n.label === 'Person').length,
    company_count: DEFAULT_NODES.filter(n => n.label === 'Company').length,
    account_count: DEFAULT_NODES.filter(n => n.label === 'BankAccount').length,
    transfer_count: DEFAULT_EDGES.filter(e => e.type === 'TRANSFERRED_TO').length,
    total_relationships: DEFAULT_EDGES.length
  };
  try {
    const res = await fetch("/api/graph/metrics");
    if (res.ok) {
      const data = await res.json();
      if (data.metrics) m = data.metrics;
    }
  } catch (e) {
    console.warn("Using fallback dataset metrics");
  }
  document.getElementById("statPersons").innerText = m.person_count || 0;
  document.getElementById("statCompanies").innerText = m.company_count || 0;
  document.getElementById("statAccounts").innerText = m.account_count || 0;
  document.getElementById("statTransfers").innerText = m.transfer_count || 0;
  document.getElementById("statEdges").innerText = m.total_relationships || 0;
}

// ==========================================
// 2. GRAPH CANVAS RENDERING (Vis.js)
// ==========================================
async function loadInitialGraph(nodeType = "", minRisk = 0.0) {
  const container = document.getElementById("graphCanvas");
  let url = `/api/graph/subgraph?`;
  if (nodeType) url += `node_type=${encodeURIComponent(nodeType)}&`;
  if (minRisk > 0) url += `min_risk=${minRisk}&`;

  try {
    try {
      const res = await fetch(url);
      if (res.ok) {
        const data = await res.json();
        rawNodes = data.nodes || [];
        rawEdges = data.edges || [];
      } else {
        rawNodes = DEFAULT_NODES;
        rawEdges = DEFAULT_EDGES;
      }
    } catch (fetchErr) {
      console.warn("Using resilient client dataset fallback");
      rawNodes = DEFAULT_NODES;
      rawEdges = DEFAULT_EDGES;
    }

    if (nodeType) {
      rawNodes = rawNodes.filter(n => n.label === nodeType);
      const validIds = new Set(rawNodes.map(n => n.id || n.account_number));
      rawEdges = rawEdges.filter(e => validIds.has(e.source) && validIds.has(e.target));
    }
    if (minRisk > 0) {
      rawNodes = rawNodes.filter(n => (n.risk_score || n.base_risk || 0.0) >= minRisk);
      const validIds = new Set(rawNodes.map(n => n.id || n.account_number));
      rawEdges = rawEdges.filter(e => validIds.has(e.source) && validIds.has(e.target));
    }

    const nodesArray = rawNodes.map((n) => {
      const label = n.label || "Entity";
      const name = n.name || n.id;
      const risk = n.risk_score || 0.0;
      
      let color = { background: "#1e293b", border: "#64748b", highlight: { background: "#334155", border: "#38bdf8" } };
      let shape = "dot";
      let size = 20;

      if (label === "Person") {
        color = { background: "#0891b2", border: "#22d3ee", highlight: { background: "#06b6d4", border: "#a5f3fc" } };
        shape = "dot";
        size = 22;
      } else if (label === "Company") {
        color = { background: "#d97706", border: "#fbbf24", highlight: { background: "#f59e0b", border: "#fde68a" } };
        shape = "box";
        size = 24;
      } else if (label === "BankAccount") {
        color = { background: "#059669", border: "#34d399", highlight: { background: "#10b981", border: "#a7f3d0" } };
        shape = "ellipse";
        size = 18;
      } else if (label === "SanctionList") {
        color = { background: "#b91c1c", border: "#f87171", highlight: { background: "#ef4444", border: "#fca5a5" } };
        shape = "hexagon";
        size = 28;
      } else if (label === "Jurisdiction") {
        color = { background: "#7c3aed", border: "#c084fc", highlight: { background: "#8b5cf6", border: "#e9d5ff" } };
        shape = "diamond";
        size = 20;
      }

      // High-risk halo
      if (risk >= 0.8) {
        color.border = "#ef4444";
      }

      return {
        id: n.id,
        label: name.length > 22 ? name.substring(0, 20) + "..." : name,
        title: `${label}: ${name}\nRisk Score: ${(risk * 100).toFixed(0)}%`,
        shape: shape,
        size: size,
        color: color,
        font: { color: "#f8fafc", face: "Plus Jakarta Sans", size: 11 },
        borderWidth: risk >= 0.8 ? 3 : 1.5,
        rawNode: n
      };
    });

    const edgesArray = rawEdges.map((e, idx) => {
      let color = "#475569";
      let arrows = "to";
      let labelText = e.type;

      if (e.type === "TRANSFERRED_TO") {
        color = e.properties && e.properties.risk_flag ? "#ef4444" : "#10b981";
        const amt = e.properties && e.properties.amount ? `$${(e.properties.amount / 1000).toFixed(0)}k` : "";
        labelText = amt ? `TX ${amt}` : "TRANSFERRED_TO";
      } else if (e.type === "OWNS") {
        color = "#f59e0b";
        const pct = e.properties && e.properties.share_pct ? `${e.properties.share_pct}%` : "";
        labelText = pct ? `OWNS (${pct})` : "OWNS";
      } else if (e.type === "SANCTIONED_UNDER") {
        color = "#dc2626";
        labelText = "SANCTIONED";
      }

      return {
        id: e.id || `edge-${idx}`,
        from: e.source,
        to: e.target,
        label: labelText,
        color: { color: color, highlight: "#38bdf8" },
        font: { color: "#94a3b8", size: 9, face: "Plus Jakarta Sans", align: "middle", background: "#0b0f19" },
        arrows: { to: { enabled: true, scaleFactor: 0.8 } },
        smooth: { type: "curvedCW", roundness: 0.15 },
        rawEdge: e
      };
    });

    visNodesDataSet = new vis.DataSet(nodesArray);
    visEdgesDataSet = new vis.DataSet(edgesArray);

    const options = {
      nodes: {
        shadow: { enabled: true, color: "rgba(0,0,0,0.5)", size: 10, x: 2, y: 2 }
      },
      edges: {
        width: 1.5,
        selectionWidth: 3,
        shadow: { enabled: false }
      },
      physics: {
        enabled: true,
        solver: "forceAtlas2Based",
        forceAtlas2Based: {
          gravitationalConstant: -70,
          centralGravity: 0.015,
          springLength: 140,
          springConstant: 0.08,
          damping: 0.4
        },
        stabilization: { iterations: 120 }
      },
      interaction: {
        hover: true,
        tooltipDelay: 100,
        navigationButtons: false,
        keyboard: true
      }
    };

    if (networkInstance) {
      networkInstance.destroy();
    }

    networkInstance = new vis.Network(container, { nodes: visNodesDataSet, edges: visEdgesDataSet }, options);

    // Node click handler
    networkInstance.on("click", (params) => {
      if (params.nodes.length > 0) {
        const selectedId = params.nodes[0];
        const nodeItem = nodesArray.find((n) => n.id === selectedId);
        if (nodeItem) {
          openDrawer(nodeItem.rawNode);
        }
      }
    });

  } catch (err) {
    console.error("Failed to render graph canvas", err);
  }
}

function applyGraphFilters() {
  const nodeType = document.getElementById("filterNodeType").value;
  const minRisk = parseFloat(document.getElementById("filterMinRisk").value || "0.0");
  loadInitialGraph(nodeType, minRisk);
}

function togglePhysics(enabled) {
  if (networkInstance) {
    networkInstance.setOptions({ physics: { enabled: enabled } });
  }
}

function focusEntityOnCanvas(entityId) {
  switchTab("explorer");
  setTimeout(() => {
    if (networkInstance) {
      networkInstance.selectNodes([entityId]);
      networkInstance.focus(entityId, {
        scale: 1.3,
        animation: { duration: 800, easingFunction: "easeInOutQuad" }
      });
      const node = rawNodes.find((n) => (n.id === entityId || n.account_number === entityId));
      if (node) openDrawer(node);
    }
  }, 100);
}

// ==========================================
// 3. TAB NAVIGATION
// ==========================================
function switchTab(tabId) {
  document.querySelectorAll(".tab-btn").forEach((btn) => btn.classList.remove("active"));
  document.querySelectorAll(".view-panel").forEach((p) => p.classList.add("hidden"));

  const targetBtn = document.getElementById(`tab-${tabId}`);
  const targetView = document.getElementById(`view-${tabId}`);

  if (targetBtn) targetBtn.classList.add("active");
  if (targetView) targetView.classList.remove("hidden");

  if (window.lucide) lucide.createIcons();
}

// ==========================================
// 4. ENTITY 360 DRAWER
// ==========================================
function openDrawer(node) {
  const drawer = document.getElementById("entityDrawer");
  const content = document.getElementById("drawerContent");
  drawer.classList.remove("hidden");

  const label = node.label || "Entity";
  const name = node.name || node.id;
  const risk = (node.risk_score || node.base_risk || 0.0);
  const riskPercent = Math.round(risk * 100);
  const nid = node.id || node.account_number;

  let riskColor = "text-emerald-400 border-emerald-500/30 bg-emerald-500/10";
  if (riskPercent >= 75) riskColor = "text-crimson-500 border-crimson-500/30 bg-crimson-500/10";
  else if (riskPercent >= 40) riskColor = "text-amber-400 border-amber-500/30 bg-amber-500/10";

  let propHtml = "";
  const props = node.properties || node;
  for (const [k, v] of Object.entries(props)) {
    if (k === "properties" || k === "rawNode" || typeof v === "object") continue;
    propHtml += `
      <div class="flex justify-between py-1.5 border-b border-dark-700/50">
        <span class="text-slate-400 capitalize font-medium">${k.replace('_', ' ')}</span>
        <span class="text-slate-200 font-mono text-right truncate max-w-[180px]">${v}</span>
      </div>
    `;
  }

  content.innerHTML = `
    <div>
      <div class="flex items-start justify-between">
        <div>
          <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider bg-dark-700 text-cyan-400 border border-dark-600">${label}</span>
          <h4 class="text-base font-bold text-white mt-1">${name}</h4>
          <p class="text-xs text-slate-400 font-mono">${nid}</p>
        </div>
        <div class="px-2.5 py-1 rounded-lg border font-bold font-mono text-xs ${riskColor}">
          Risk: ${riskPercent}%
        </div>
      </div>
    </div>

    <!-- Actions -->
    <div class="grid grid-cols-2 gap-2 pt-2">
      <button onclick="expandNeighborhood('${nid}')" class="flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg bg-dark-700 hover:bg-dark-600 border border-dark-600 text-slate-200 text-xs font-semibold transition-all">
        <i data-lucide="maximize-2" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span>2-Hop Scope</span>
      </button>
      <button onclick="traceEntitySanctions('${nid}')" class="flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg bg-crimson-600/20 hover:bg-crimson-600/30 border border-crimson-500/30 text-crimson-400 text-xs font-semibold transition-all">
        <i data-lucide="shield-alert" class="w-3.5 h-3.5"></i>
        <span>Sanctions Trace</span>
      </button>
    </div>

    <!-- Properties -->
    <div class="bg-dark-900/60 rounded-xl p-3 border border-dark-700 space-y-1">
      <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">Entity Metadata</div>
      ${propHtml}
    </div>
  `;

  if (window.lucide) lucide.createIcons();
}

function closeDrawer() {
  document.getElementById("entityDrawer").classList.add("hidden");
}

async function expandNeighborhood(entityId) {
  try {
    const res = await fetch(`/api/graph/neighborhood/${encodeURIComponent(entityId)}`);
    const data = await res.json();
    showToast(`Loaded ${data.nodes.length} nodes in 2-hop neighborhood of ${entityId}`);
    focusEntityOnCanvas(entityId);
  } catch (err) {
    showToast(`Failed to expand neighborhood: ${err}`, true);
  }
}

function traceEntitySanctions(entityId) {
  switchTab("sanctions");
  const select = document.getElementById("sanctionSelectEntity");
  // Check if option exists, otherwise add it
  let exists = false;
  for (let i = 0; i < select.options.length; i++) {
    if (select.options[i].value === entityId) {
      select.selectedIndex = i;
      exists = true;
      break;
    }
  }
  if (!exists) {
    const opt = document.createElement("option");
    opt.value = entityId;
    opt.innerText = entityId;
    select.appendChild(opt);
    select.value = entityId;
  }
  traceSanctionPath();
}

// ==========================================
// 5. SMURFING RINGS (CIRCULAR CYCLES)
// ==========================================
async function loadCircularRings() {
  const container = document.getElementById("ringsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Scanning transaction topology for closed loops...</div>`;

  let rings = DEFAULT_RINGS;
  try {
    const res = await fetch("/api/analytics/circular-rings?limit=10");
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.rings) && data.rings.length > 0) {
        rings = data.rings;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for circular rings", err);
  }

    if (rings.length === 0) {
      container.innerHTML = `<div class="p-8 text-center text-slate-400 text-xs">No circular loops detected.</div>`;
      return;
    }

    container.innerHTML = rings.map((ring, idx) => {
      const vol = (ring.total_volume || 0).toLocaleString("en-US", { style: "currency", currency: "USD" });
      const nodes = ring.ring_nodes || [];
      const edges = ring.ring_edges || [];

      const chainHtml = ring.account_chain.map((acc, i) => `
        <span class="px-2 py-1 rounded bg-dark-900 text-cyan-300 font-mono text-xs border border-dark-600">${acc}</span>
        ${i < ring.account_chain.length - 1 ? `<i data-lucide="arrow-right" class="w-3.5 h-3.5 text-amber-400"></i>` : ''}
      `).join('');

      return `
        <div class="intel-card bg-dark-800 border border-amber-500/30 rounded-xl p-5 space-y-4 shadow-xl">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-xs">#${idx + 1}</div>
              <div>
                <h4 class="font-bold text-sm text-white">Circular Smurfing Ring (${ring.loop_length} Hops)</h4>
                <p class="text-xs text-slate-400">Origin Bank: <span class="text-slate-200 font-semibold">${ring.origin_bank}</span> (${ring.origin_account})</p>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Laundered Loop Volume</div>
              <div class="text-base font-extrabold text-amber-400 font-mono">${vol}</div>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-2 py-1 bg-dark-900/60 p-3 rounded-lg border border-dark-700/60">
            ${chainHtml}
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="bg-dark-900/40 p-3 rounded-lg border border-dark-700 space-y-1.5">
              <div class="font-bold text-slate-400 uppercase text-[10px]">Involved Accounts</div>
              ${nodes.map(n => `
                <div class="flex justify-between items-center py-0.5">
                  <span class="text-slate-300">${n.bank_name || n.account_number}</span>
                  <span class="font-mono text-[11px] px-1.5 rounded bg-dark-700 text-amber-300">${n.country || 'Offshore'}</span>
                </div>
              `).join('')}
            </div>

            <div class="bg-dark-900/40 p-3 rounded-lg border border-dark-700 space-y-1.5">
              <div class="font-bold text-slate-400 uppercase text-[10px]">Transaction Hops</div>
              ${edges.map(e => `
                <div class="flex justify-between items-center py-0.5 font-mono text-[11px]">
                  <span class="text-cyan-400">${e.tx_id}</span>
                  <span class="text-emerald-400 font-bold">$${(e.amount).toLocaleString()} ${e.currency}</span>
                </div>
              `).join('')}
            </div>
          </div>

          <div class="flex justify-end pt-1">
            <button onclick="focusEntityOnCanvas('${ring.origin_account}')" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-dark-700 hover:bg-dark-600 text-cyan-400 font-semibold text-xs border border-dark-600 transition-all">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>Locate in Network Canvas</span>
            </button>
          </div>
        </div>
      `;
    }).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to load circular rings: ${err}</div>`;
  }
}

// ==========================================
// 6. UBO RESOLUTION (MULTI-TIER OWNERSHIP)
// ==========================================
async function resolveUBO() {
  const companyId = document.getElementById("uboSelectCompany").value;
  const container = document.getElementById("uboResultsContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Traversing recursive ownership graph [:OWNS*1..8]...</div>`;

  let ubos = DEFAULT_UBO[companyId] || [];
  try {
    const res = await fetch(`/api/analytics/ubo/${encodeURIComponent(companyId)}?min_share_pct=5.0`);
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.beneficial_owners)) {
        ubos = data.beneficial_owners;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for UBO resolution", err);
  }

    if (ubos.length === 0) {
      container.innerHTML = `<div class="bg-dark-800 border border-dark-700 rounded-xl p-6 text-center text-slate-400 text-xs">No beneficial owners found for this company.</div>`;
      return;
    }

    container.innerHTML = ubos.map((ubo, idx) => {
      const effPct = ubo.effective_ownership_pct;
      const isControl = effPct >= 25.0;
      const chainNodes = ubo.ownership_chain || [];
      const relChain = ubo.relationship_chain || [];

      return `
        <div class="intel-card bg-dark-800 border ${isControl ? 'border-emerald-500/40' : 'border-dark-700'} rounded-xl p-5 space-y-4 shadow-xl">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
            <div class="flex items-center space-x-3">
              <div class="w-9 h-9 rounded-lg ${ubo.is_pep ? 'bg-crimson-500/20 text-crimson-400' : 'bg-emerald-500/20 text-emerald-400'} flex items-center justify-center font-bold text-sm">
                <i data-lucide="user-check" class="w-5 h-5"></i>
              </div>
              <div>
                <div class="flex items-center space-x-2">
                  <h4 class="font-bold text-base text-white">${ubo.ubo_name}</h4>
                  ${ubo.is_pep ? `<span class="px-2 py-0.5 rounded text-[10px] font-bold bg-crimson-500/20 text-crimson-400 border border-crimson-500/30">PEP EXPOSURE</span>` : ''}
                </div>
                <p class="text-xs text-slate-400">Nationality: <span class="text-slate-200 font-semibold">${ubo.nationality}</span> | UBO Depth: <span class="text-emerald-400 font-bold">${ubo.ownership_depth} Layers</span></p>
              </div>
            </div>
            <div class="text-right">
              <div class="text-xs text-slate-400">Calculated Effective Share</div>
              <div class="text-xl font-extrabold ${isControl ? 'text-emerald-400' : 'text-slate-200'} font-mono">${effPct}%</div>
            </div>
          </div>

          <!-- Visual Ownership Pathway -->
          <div class="space-y-2">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Multi-Tier Ownership Chain</div>
            <div class="bg-dark-900/60 p-4 rounded-xl border border-dark-700/80 space-y-3">
              ${chainNodes.map((n, i) => {
                const rel = relChain[i];
                return `
                  <div class="flex items-center space-x-3">
                    <div class="w-6 h-6 rounded-full bg-dark-700 text-cyan-400 flex items-center justify-center font-bold text-[10px] shrink-0">${i + 1}</div>
                    <div class="flex-1 bg-dark-800 p-2.5 rounded-lg border border-dark-600/80 flex items-center justify-between">
                      <div>
                        <div class="font-bold text-xs text-slate-200">${n.name}</div>
                        <div class="text-[10px] text-slate-400">${n.type} • ${n.jurisdiction}</div>
                      </div>
                      <div class="text-right">
                        ${rel ? `<span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Owns ${rel.share_pct}%</span>` : `<span class="text-xs text-slate-400">Target Asset</span>`}
                      </div>
                    </div>
                  </div>
                  ${i < chainNodes.length - 1 ? `<div class="pl-3 py-0.5"><i data-lucide="arrow-down" class="w-3.5 h-3.5 text-emerald-400"></i></div>` : ''}
                `;
              }).join('')}
            </div>
          </div>

          <div class="flex justify-end pt-1">
            <button onclick="focusEntityOnCanvas('${ubo.ubo_id}')" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-dark-700 hover:bg-dark-600 text-cyan-400 font-semibold text-xs border border-dark-600 transition-all">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>Locate UBO in Canvas</span>
            </button>
          </div>
        </div>
      `;
    }).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to compute UBO: ${err}</div>`;
  }
}

// ==========================================
// 7. SANCTIONS PATH TRACER
// ==========================================
async function traceSanctionPath() {
  const entityId = document.getElementById("sanctionSelectEntity").value;
  const container = document.getElementById("sanctionPathContainer");
  container.innerHTML = `<div class="p-6 text-center text-slate-400 text-xs font-mono">Running shortest-path traversal to Sanction Watchlists...</div>`;

  let data = DEFAULT_SANCTIONS[entityId] || { found: false, message: `No sanction path found within 6 hops for ${entityId}` };
  try {
    const res = await fetch(`/api/analytics/shortest-sanction-path/${encodeURIComponent(entityId)}`);
    if (res.ok) {
      const liveData = await res.json();
      if (liveData && liveData.found !== undefined) {
        data = liveData;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for sanction path", err);
  }

    if (!data.found) {
      container.innerHTML = `
        <div class="bg-dark-800 border border-dark-700 rounded-xl p-6 text-center space-y-2">
          <i data-lucide="shield-check" class="w-8 h-8 text-emerald-400 mx-auto"></i>
          <h4 class="font-bold text-sm text-white">No Sanction Exposure Detected</h4>
          <p class="text-xs text-slate-400">${data.message || 'No connection found within 6 hops.'}</p>
        </div>
      `;
      if (window.lucide) lucide.createIcons();
      return;
    }

    const path = data.path;
    const nodes = path.path_nodes || [];
    const rels = path.path_relationships || [];

    container.innerHTML = `
      <div class="intel-card bg-dark-800 border border-crimson-500/40 rounded-xl p-5 space-y-4 shadow-xl">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-700 pb-3">
          <div class="flex items-center space-x-3">
            <div class="w-9 h-9 rounded-lg bg-crimson-500/20 text-crimson-400 flex items-center justify-center font-bold text-sm">
              <i data-lucide="alert-triangle" class="w-5 h-5"></i>
            </div>
            <div>
              <h4 class="font-bold text-base text-white">Direct / Indirect Sanctions Exposure</h4>
              <p class="text-xs text-slate-400">Target List: <span class="text-crimson-400 font-bold">${path.sanction_program}</span> (${path.sanctioning_body})</p>
            </div>
          </div>
          <div class="text-right">
            <div class="text-xs text-slate-400">Graph Distance</div>
            <div class="text-xl font-extrabold text-crimson-400 font-mono">${path.distance} Hops</div>
          </div>
        </div>

        <div class="bg-crimson-950/20 border border-crimson-500/30 rounded-lg p-3 text-xs text-slate-300">
          <span class="font-bold text-crimson-400 uppercase text-[10px] block mb-1">Sanction Justification</span>
          ${path.sanction_reason}
        </div>

        <!-- Step by Step Chain -->
        <div class="space-y-2">
          <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Tainted Capital Pathway</div>
          <div class="bg-dark-900/60 p-4 rounded-xl border border-dark-700/80 space-y-3">
            ${nodes.map((n, i) => {
              const rel = rels[i];
              return `
                <div class="flex items-center space-x-3">
                  <div class="w-6 h-6 rounded-full bg-dark-700 text-crimson-400 flex items-center justify-center font-bold text-[10px] shrink-0">${i + 1}</div>
                  <div class="flex-1 bg-dark-800 p-2.5 rounded-lg border border-dark-600/80 flex items-center justify-between">
                    <div>
                      <div class="font-bold text-xs text-slate-200">${n.name}</div>
                      <div class="text-[10px] text-slate-400">${n.label} • ${n.country}</div>
                    </div>
                    <div class="text-right">
                      ${rel ? `<span class="px-2 py-0.5 rounded bg-dark-700 text-cyan-300 font-mono text-[10px]">${rel.type}</span>` : `<span class="px-2 py-0.5 rounded bg-crimson-500/20 text-crimson-400 font-mono text-[10px] font-bold">SANCTION NODE</span>`}
                    </div>
                  </div>
                </div>
                ${i < nodes.length - 1 ? `<div class="pl-3 py-0.5"><i data-lucide="arrow-down" class="w-3.5 h-3.5 text-crimson-400"></i></div>` : ''}
              `;
            }).join('')}
          </div>
        </div>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    container.innerHTML = `<div class="p-4 text-rose-400 text-xs">Failed to trace sanctions path: ${err}</div>`;
  }
}

// ==========================================
// 8. MULE TRANSIT HUBS
// ==========================================
async function loadMuleHubs() {
  const container = document.getElementById("mulesContainer");
  let hubs = DEFAULT_MULE_HUBS;
  try {
    const res = await fetch("/api/analytics/mule-hubs?limit=6");
    if (res.ok) {
      const data = await res.json();
      if (data && Array.isArray(data.hubs) && data.hubs.length > 0) {
        hubs = data.hubs;
      }
    }
  } catch (err) {
    console.warn("Using resilient client dataset fallback for mule hubs", err);
  }

    container.innerHTML = hubs.map((h) => `
      <div class="intel-card bg-dark-800 border border-purple-500/30 rounded-xl p-4 space-y-3 shadow-xl">
        <div class="flex items-center justify-between border-b border-dark-700 pb-2">
          <div>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 font-mono">TRANSIT NEXUS</span>
            <h4 class="font-bold text-sm text-white mt-1">${h.bank_name}</h4>
            <p class="text-xs text-slate-400 font-mono">${h.account_number} (${h.country})</p>
          </div>
          <div class="text-right">
            <div class="text-[10px] text-slate-400">Centrality Index</div>
            <div class="text-base font-extrabold text-purple-400 font-mono">${h.centrality_index}</div>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-xs">
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Total Inflow</div>
            <div class="font-bold text-emerald-400 font-mono text-[11px]">$${(h.total_inflow).toLocaleString()}</div>
          </div>
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Total Outflow</div>
            <div class="font-bold text-rose-400 font-mono text-[11px]">$${(h.total_outflow).toLocaleString()}</div>
          </div>
          <div class="bg-dark-900/60 p-2 rounded-lg border border-dark-700">
            <div class="text-[10px] text-slate-400">Retained Net</div>
            <div class="font-bold text-slate-200 font-mono text-[11px]">$${(h.net_retention).toLocaleString()}</div>
          </div>
        </div>

        <div class="flex justify-end pt-1">
          <button onclick="focusEntityOnCanvas('${h.account_number}')" class="text-xs text-cyan-400 hover:underline flex items-center space-x-1">
            <span>Inspect in Canvas</span>
            <i data-lucide="chevron-right" class="w-3 h-3"></i>
          </button>
        </div>
      </div>
    `).join("");

    if (window.lucide) lucide.createIcons();
  } catch (err) {
    console.error("Failed to load mules", err);
  }
}

// ==========================================
// 9. CYPHER QUERY PLAYGROUND
// ==========================================
const CYPHER_PRESETS = {
  1: `MATCH path = (origin:BankAccount)-[txs:TRANSFERRED_TO*3..6]->(origin)
RETURN origin.account_number AS origin_acc, length(path) AS hops,
       reduce(s = 0, t IN txs | s + t.amount) AS volume
ORDER BY volume DESC LIMIT 5`,
  2: `MATCH path = (root:Person)-[owns:OWNS*1..8]->(target:Company {id: 'C-208'})
RETURN root.name AS ubo, root.nationality AS nationality,
       reduce(pct = 1.0, r IN owns | pct * (r.share_pct/100.0)) * 100.0 AS effective_pct,
       length(path) AS depth`,
  3: `MATCH (start:Company {id: 'C-208'}), (sanction:SanctionList)
MATCH p = shortestPath((start)-[*1..6]-(sanction))
RETURN length(p) AS hops, [n IN nodes(p) | coalesce(n.name, n.account_number)] AS entity_trail`,
  4: `MATCH (c:Company)-[:REGISTERED_IN]->(j:Jurisdiction {tax_haven: true})
OPTIONAL MATCH (p:Person)-[o:OWNS]->(c)
RETURN c.name AS company, j.name AS haven, p.name AS owner, o.share_pct AS share`
};

function setCypherPreset(num) {
  const query = CYPHER_PRESETS[num] || "";
  document.getElementById("cypherInput").value = query;
}

async function runCustomCypher() {
  const query = document.getElementById("cypherInput").value.trim();
  const output = document.getElementById("cypherOutput");
  const stats = document.getElementById("cypherExecStats");

  if (!query) {
    output.innerText = "Please enter a Cypher query.";
    return;
  }

  output.innerText = "Executing Cypher against CognoDB Cloud...";
  stats.innerText = "Query in flight...";

  try {
    const res = await fetch("/api/analytics/cypher-console", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query, parameters: {} })
    });
    const data = await res.json();

    if (data.success) {
      stats.innerText = `Success | ${data.row_count} records returned in ${data.execution_time_ms} ms (${data.mode})`;
      output.innerText = JSON.stringify(data.data, null, 2);
    } else {
      stats.innerText = `Query Error (${data.mode})`;
      output.innerText = data.error || "An error occurred executing query.";
    }
  } catch (err) {
    stats.innerText = "Execution failed";
    output.innerText = `Network/Server Error: ${err}`;
  }
}

// ==========================================
// 10. GLOBAL SEARCH & SEEDING UTILITIES
// ==========================================
function setupSearch() {
  const input = document.getElementById("globalSearchInput");
  const dropdown = document.getElementById("searchResultsDropdown");
  let debounceTimeout = null;

  input.addEventListener("input", () => {
    clearTimeout(debounceTimeout);
    const term = input.value.trim();
    if (term.length < 2) {
      dropdown.classList.add("hidden");
      return;
    }

    debounceTimeout = setTimeout(async () => {
      try {
        const res = await fetch(`/api/search/?q=${encodeURIComponent(term)}`);
        const data = await res.json();
        const results = data.results || [];

        if (results.length === 0) {
          dropdown.innerHTML = `<div class="p-3 text-slate-400 text-xs">No matching entities found.</div>`;
          dropdown.classList.remove("hidden");
          return;
        }

        dropdown.innerHTML = results.map((r) => `
          <div onclick="focusEntityOnCanvas('${r.id}'); document.getElementById('searchResultsDropdown').classList.add('hidden');" class="p-2.5 hover:bg-dark-700 cursor-pointer flex items-center justify-between text-xs transition-colors">
            <div>
              <div class="font-bold text-slate-200">${r.name}</div>
              <div class="text-[10px] text-slate-400">${r.label} • ${r.country || 'N/A'}</div>
            </div>
            <span class="px-2 py-0.5 rounded font-mono text-[10px] ${r.risk_score >= 0.7 ? 'bg-crimson-500/20 text-crimson-400' : 'bg-dark-600 text-slate-300'}">
              ${(r.risk_score * 100).toFixed(0)}%
            </span>
          </div>
        `).join("");

        dropdown.classList.remove("hidden");
      } catch (e) {
        console.error("Search error", e);
      }
    }, 250);
  });

  document.addEventListener("click", (e) => {
    if (!input.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.add("hidden");
    }
  });
}

async function triggerSeed() {
  if (!confirm("This will ingest the SentinelGraph syndicate dataset into your live CognoDB Cloud instance. Continue?")) {
    return;
  }
  showToast("Seeding dataset into CognoDB...");
  try {
    const res = await fetch("/api/admin/seed?clear_first=true", { method: "POST" });
    const data = await res.json();
    if (data.success) {
      showToast(`Successfully seeded ${data.nodes_inserted} nodes and ${data.relationships_inserted} relationships!`);
      loadMetrics();
      loadInitialGraph();
      loadCircularRings();
      loadMuleHubs();
    } else {
      showToast(`Seed failed: ${data.detail || 'Check database connection'}`, true);
    }
  } catch (err) {
    showToast(`Seeding request error: ${err}`, true);
  }
}

function showToast(msg, isError = false) {
  const toast = document.getElementById("toast");
  const text = document.getElementById("toastMsg");
  text.innerText = msg;
  toast.className = isError
    ? "fixed bottom-5 right-5 z-50 px-4 py-3 rounded-xl bg-dark-800 border border-crimson-500/60 text-crimson-400 text-xs shadow-2xl flex items-center space-x-2 transition-all"
    : "fixed bottom-5 right-5 z-50 px-4 py-3 rounded-xl bg-dark-800 border border-emerald-500/60 text-emerald-400 text-xs shadow-2xl flex items-center space-x-2 transition-all";
  toast.classList.remove("hidden");
  setTimeout(() => toast.classList.add("hidden"), 4000);
}

function exportGraphImage() {
  if (!networkInstance) return;
  const canvas = document.querySelector("#graphCanvas canvas");
  if (canvas) {
    const link = document.createElement("a");
    link.download = "sentinelgraph-intelligence-canvas.png";
    link.href = canvas.toDataURL("image/png");
    link.click();
    showToast("Graph canvas exported as image.");
  }
}


// ==========================================
// 8. INTERACTIVE GUIDED WALKTHROUGH
// ==========================================
let currentTourIndex = 0;
const tourSteps = [
  {
    targetId: "statsRibbon",
    title: "📊 Live Network Telemetry",
    desc: "SentinelGraph aggregates high-level telemetry across your entire graph database: 10 Persons, 11 Companies, 13 Bank Accounts, and 49 Relationships with live risk indicators.",
    action: () => switchTab("explorer")
  },
  {
    targetId: "graphCanvasContainer",
    title: "🕸️ Force-Directed Network Canvas",
    desc: "Interactive Vis.js graph physics simulation. Nodes are color-coded (Cyan=Persons, Orange=Companies, Green=Accounts, Red=Sanctions). Click any node to open its 360° Risk Profile.",
    action: () => {
      switchTab("explorer");
      focusEntityOnCanvas("C-201");
    }
  },
  {
    targetId: "globalSearchInput",
    title: "🔍 Instant Entity Search & Autocomplete",
    desc: "Debounced live search across all suspect persons, offshore holding entities, bank account numbers, and sanction watchlists with instant camera focusing.",
    action: () => switchTab("explorer")
  },
  {
    targetId: "tab-rings",
    title: "🔄 Multi-Hop Smurfing Ring Detection",
    desc: "Uncovers obfuscated circular money laundering loops (3 to 6 hops deep) where capital routes through multi-jurisdiction intermediaries and returns to the originator.",
    action: () => switchTab("rings")
  },
  {
    targetId: "tab-ubo",
    title: "🏢 Recursive Ultimate Beneficial Ownership (UBO)",
    desc: "Traverses up to 8 hops deep across complex offshore shell holding chains (BVI, Cyprus, Panama) and computes cumulative effective ownership math using Cypher reduce().",
    action: () => {
      switchTab("ubo");
      resolveUBO();
    }
  },
  {
    targetId: "tab-sanctions",
    title: "🛡️ Shortest Path to Sanction Lists",
    desc: "Calculates the shortest relationship corridor connecting any suspect entity directly to OFAC SDN and EU watchlists in milliseconds.",
    action: () => {
      switchTab("sanctions");
      traceSanctionPath();
    }
  },
  {
    targetId: "tab-mules",
    title: "⚡ Mule Transit Hub & Centrality Detection",
    desc: "Identifies transit hub accounts exhibiting high transaction velocity, multiple incoming deposits, and rapid outgoing dispersal.",
    action: () => switchTab("mules")
  },
  {
    targetId: "tab-cypher",
    title: "💻 Live openCypher Query Console",
    desc: "Interactive Cypher playground for compliance investigators. Run custom or preset openCypher queries directly against CognoDB Cloud with live execution timing.",
    action: () => switchTab("cypher")
  }
];

function startWalkthrough() {
  currentTourIndex = 0;
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.remove("hidden");
  renderTourStep();
}

function stopWalkthrough() {
  const overlay = document.getElementById("walkthroughOverlay");
  if (overlay) overlay.classList.add("hidden");
  document.querySelectorAll(".tour-highlight").forEach(el => el.classList.remove("tour-highlight"));
}

function renderTourStep() {
  document.querySelectorAll(".tour-highlight").forEach(el => el.classList.remove("tour-highlight"));

  const step = tourSteps[currentTourIndex];
  if (!step) return;

  if (step.action) step.action();

  const badge = document.getElementById("tourStepBadge");
  const title = document.getElementById("tourTitle");
  const desc = document.getElementById("tourDescription");
  const prevBtn = document.getElementById("tourPrevBtn");
  const nextBtn = document.getElementById("tourNextBtn");
  const dotsContainer = document.getElementById("tourDots");
  const card = document.getElementById("tourCard");

  // Keep card strictly pinned to bottom-right
  if (card) {
    card.style.position = "fixed";
    card.style.bottom = "24px";
    card.style.right = "24px";
    card.style.left = "auto";
    card.style.top = "auto";
    card.style.transform = "none";
  }

  if (badge) badge.innerText = `Step ${currentTourIndex + 1} of ${tourSteps.length}`;
  if (title) title.innerText = step.title;
  if (desc) desc.innerText = step.desc;

  if (prevBtn) prevBtn.style.visibility = currentTourIndex === 0 ? "hidden" : "visible";
  if (nextBtn) nextBtn.innerText = currentTourIndex === tourSteps.length - 1 ? "Finish Tour 🎉" : "Next →";

  if (dotsContainer) {
    dotsContainer.innerHTML = tourSteps.map((_, i) => `
      <span class="w-1.5 h-1.5 rounded-full transition-all ${i === currentTourIndex ? 'bg-cyan-400 w-3' : 'bg-dark-600'}"></span>
    `).join('');
  }

  const targetEl = document.getElementById(step.targetId);
  if (targetEl) {
    targetEl.classList.add("tour-highlight");
  }

  if (window.lucide) lucide.createIcons();
}

function nextTourStep() {
  if (currentTourIndex < tourSteps.length - 1) {
    currentTourIndex++;
    renderTourStep();
  } else {
    stopWalkthrough();
    showToast("Walkthrough completed! Explore the graph freely.");
  }
}

function prevTourStep() {
  if (currentTourIndex > 0) {
    currentTourIndex--;
    renderTourStep();
  }
}

"""
Built-in synthetic dataset for SentinelGraph.
Provides high-fidelity graph analytics even in standalone / fallback / demo mode.
"""

MOCK_NODES = [
    # Persons
    {"id": "P-101", "label": "Person", "name": "Viktor Sterling", "nationality": "Russian", "is_pep": True, "base_risk": 0.94, "role": "Beneficial Owner / Politically Exposed"},
    {"id": "P-102", "label": "Person", "name": "Elena Sterling", "nationality": "Cypriot", "is_pep": True, "base_risk": 0.78, "role": "Nominee Director / Spouse"},
    {"id": "P-103", "label": "Person", "name": "Marcus Vance", "nationality": "British", "is_pep": False, "base_risk": 0.65, "role": "Corporate Lawyer & Escrow Agent"},
    {"id": "P-104", "label": "Person", "name": "Chloe Dubois", "nationality": "Swiss", "is_pep": False, "base_risk": 0.35, "role": "Private Wealth Manager"},
    {"id": "P-105", "label": "Person", "name": "Tariq Al-Mansoor", "nationality": "Emirati", "is_pep": False, "base_risk": 0.52, "role": "Trade Broker & Director"},
    {"id": "P-106", "label": "Person", "name": "Sergei Volkov", "nationality": "Russian", "is_pep": True, "base_risk": 0.99, "role": "Defense Contractor / Sanctioned Entity"},
    {"id": "P-107", "label": "Person", "name": "Lin Wei", "nationality": "Singaporean", "is_pep": False, "base_risk": 0.22, "role": "Logistics Managing Director"},
    {"id": "P-108", "label": "Person", "name": "Sofia Rossi", "nationality": "Italian", "is_pep": False, "base_risk": 0.28, "role": "Maritime Assets Broker"},
    {"id": "P-109", "label": "Person", "name": "Hans Gruber", "nationality": "German", "is_pep": False, "base_risk": 0.12, "role": "CleanTech Consultant"},
    {"id": "P-110", "label": "Person", "name": "Arthur Pendelton", "nationality": "Bermudian", "is_pep": False, "base_risk": 0.72, "role": "Offshore Trust Fiduciary"},

    # Companies
    {"id": "C-201", "label": "Company", "name": "Seashell Global Holdings Ltd", "jurisdiction": "BVI", "company_type": "Offshore Shell", "risk_score": 0.91, "status": "Active"},
    {"id": "C-202", "label": "Company", "name": "Apex Meridian Trading S.A.", "jurisdiction": "Cyprus", "company_type": "Intermediary Holding", "risk_score": 0.86, "status": "Active"},
    {"id": "C-203", "label": "Company", "name": "Golden Horizon Logistics Ltd", "jurisdiction": "United Kingdom", "company_type": "Front Operational", "risk_score": 0.62, "status": "Active"},
    {"id": "C-204", "label": "Company", "name": "Sovereign Blue Maritime Corp", "jurisdiction": "Panama", "company_type": "Vessel Special Purpose Vehicle", "risk_score": 0.88, "status": "Active"},
    {"id": "C-205", "label": "Company", "name": "Vostok Precision Dynamics", "jurisdiction": "Russia", "company_type": "Dual-Use Tech Manufacturing", "risk_score": 0.99, "status": "Sanctioned"},
    {"id": "C-206", "label": "Company", "name": "Silk Route Commodities FZE", "jurisdiction": "UAE", "company_type": "Freezone Trading Broker", "risk_score": 0.68, "status": "Active"},
    {"id": "C-207", "label": "Company", "name": "Alpine Crest Advisory AG", "jurisdiction": "Switzerland", "company_type": "Asset Management", "risk_score": 0.35, "status": "Active"},
    {"id": "C-208", "label": "Company", "name": "Lumina Capital Partners LP", "jurisdiction": "United States", "company_type": "Commercial Real Estate Fund", "risk_score": 0.48, "status": "Active"},
    {"id": "C-209", "label": "Company", "name": "Nordic CleanTech Solutions AB", "jurisdiction": "Sweden", "company_type": "Renewable Tech (Decoy)", "risk_score": 0.10, "status": "Active"},
    {"id": "C-210", "label": "Company", "name": "Pacific Rim Exports Pte", "jurisdiction": "Singapore", "company_type": "Import/Export Hub", "risk_score": 0.25, "status": "Active"},
    {"id": "C-211", "label": "Company", "name": "Blue Water Real Estate GmbH", "jurisdiction": "Germany", "company_type": "Luxury Property Holding", "risk_score": 0.50, "status": "Active"},

    # Bank Accounts
    {"id": "ACC-9001", "label": "BankAccount", "name": "CH93-Zurich-Private", "account_number": "ACC-9001", "bank_name": "Credit Suisse Private Banking", "country": "Switzerland", "balance": 4500000.0, "risk_level": "LOW"},
    {"id": "ACC-9002", "label": "BankAccount", "name": "CY21-Nicosia-Commercial", "account_number": "ACC-9002", "bank_name": "Bank of Cyprus Commercial", "country": "Cyprus", "balance": 1820000.0, "risk_level": "HIGH"},
    {"id": "ACC-9003", "label": "BankAccount", "name": "VG80-RoadTown-Offshore", "account_number": "ACC-9003", "bank_name": "BVI International Trust Bank", "country": "BVI", "balance": 8900000.0, "risk_level": "CRITICAL"},
    {"id": "ACC-9004", "label": "BankAccount", "name": "GB29-London-Metro", "account_number": "ACC-9004", "bank_name": "Barclays Commercial London", "country": "United Kingdom", "balance": 640000.0, "risk_level": "MEDIUM"},
    {"id": "ACC-9005", "label": "BankAccount", "name": "AE07-Dubai-Mashreq", "account_number": "ACC-9005", "bank_name": "Emirates NBD Freezone", "country": "UAE", "balance": 3100000.0, "risk_level": "HIGH"},
    {"id": "ACC-9006", "label": "BankAccount", "name": "PA15-Panama-Pacific", "account_number": "ACC-9006", "bank_name": "Banco General Panama", "country": "Panama", "balance": 2400000.0, "risk_level": "CRITICAL"},
    {"id": "ACC-9007", "label": "BankAccount", "name": "RU40-Moscow-Sber", "account_number": "ACC-9007", "bank_name": "Gazprombank Commercial", "country": "Russia", "balance": 12500000.0, "risk_level": "CRITICAL"},
    {"id": "ACC-9008", "label": "BankAccount", "name": "SG65-DBS-Singapore", "account_number": "ACC-9008", "bank_name": "DBS Corporate Singapore", "country": "Singapore", "balance": 1100000.0, "risk_level": "LOW"},
    {"id": "ACC-9009", "label": "BankAccount", "name": "US12-JPMorgan-NYC", "account_number": "ACC-9009", "bank_name": "JPMorgan Chase NYC", "country": "United States", "balance": 5200000.0, "risk_level": "MEDIUM"},
    {"id": "ACC-9010", "label": "BankAccount", "name": "DE89-Frankfurt-DB", "account_number": "ACC-9010", "bank_name": "Deutsche Bank Frankfurt", "country": "Germany", "balance": 980000.0, "risk_level": "LOW"},
    {"id": "ACC-9011", "label": "BankAccount", "name": "SE50-Stockholm-SEB", "account_number": "ACC-9011", "bank_name": "SEB Nordic Business", "country": "Sweden", "balance": 450000.0, "risk_level": "LOW"},
    {"id": "ACC-9012", "label": "BankAccount", "name": "KY11-Cayman-Mule-Transit", "account_number": "ACC-9012", "bank_name": "Cayman Grand Trust Bank", "country": "Cayman Islands", "balance": 120000.0, "risk_level": "CRITICAL"},
    {"id": "ACC-9013", "label": "BankAccount", "name": "MH22-Majuro-Escrow", "account_number": "ACC-9013", "bank_name": "Marshall Trust Depository", "country": "Marshall Islands", "balance": 85000.0, "risk_level": "CRITICAL"},

    # Sanction Lists
    {"id": "SANCT-OFAC-SDN", "label": "SanctionList", "name": "OFAC SDN List", "authority": "US Dept of Treasury", "program": "UKRAINE-EO14024 / DEFENSE_SECTOR", "date_listed": "2022-04-15", "reason": "Dual-use technology procurement & weapons proliferation funding"},
    {"id": "SANCT-EU-CFSP", "label": "SanctionList", "name": "EU Consolidated Sanctions", "authority": "European External Action Service", "program": "REG_269_2014", "date_listed": "2022-05-10", "reason": "Destabilizing actions & illicit financial asset concealment"},

    # Jurisdictions
    {"id": "JUR-BVI", "label": "Jurisdiction", "name": "British Virgin Islands", "code": "BVI", "risk_tier": "TIER_3_HIGH", "tax_haven": True},
    {"id": "JUR-CY", "label": "Jurisdiction", "name": "Cyprus", "code": "CY", "risk_tier": "TIER_2_MEDIUM", "tax_haven": True},
    {"id": "JUR-PA", "label": "Jurisdiction", "name": "Panama", "code": "PA", "risk_tier": "TIER_3_HIGH", "tax_haven": True},
    {"id": "JUR-RU", "label": "Jurisdiction", "name": "Russia", "code": "RU", "risk_tier": "TIER_3_HIGH", "tax_haven": False},
    {"id": "JUR-AE", "label": "Jurisdiction", "name": "United Arab Emirates", "code": "AE", "risk_tier": "TIER_2_MEDIUM", "tax_haven": True},
    {"id": "JUR-CH", "label": "Jurisdiction", "name": "Switzerland", "code": "CH", "risk_tier": "TIER_1_LOW", "tax_haven": False},
    {"id": "JUR-GB", "label": "Jurisdiction", "name": "United Kingdom", "code": "GB", "risk_tier": "TIER_1_LOW", "tax_haven": False},
    {"id": "JUR-US", "label": "Jurisdiction", "name": "United States", "code": "US", "risk_tier": "TIER_1_LOW", "tax_haven": False}
]

MOCK_EDGES = [
    # Ownership (UBO Tree 1)
    {"id": "E-101", "type": "OWNS", "source": "P-101", "target": "C-201", "properties": {"share_pct": 100.0, "since": "2020-03-15", "voting_rights": 100.0}},
    {"id": "E-102", "type": "OWNS", "source": "C-201", "target": "C-202", "properties": {"share_pct": 85.0, "since": "2020-08-01", "voting_rights": 85.0}},
    {"id": "E-103", "type": "OWNS", "source": "C-202", "target": "C-203", "properties": {"share_pct": 90.0, "since": "2021-02-14", "voting_rights": 90.0}},
    {"id": "E-104", "type": "OWNS", "source": "C-203", "target": "C-208", "properties": {"share_pct": 75.0, "since": "2021-11-20", "voting_rights": 75.0}},

    # Ownership (UBO Tree 2 & Direct)
    {"id": "E-105", "type": "OWNS", "source": "P-102", "target": "C-204", "properties": {"share_pct": 100.0, "since": "2019-06-10", "voting_rights": 100.0}},
    {"id": "E-106", "type": "OWNS", "source": "C-204", "target": "C-211", "properties": {"share_pct": 100.0, "since": "2021-04-05", "voting_rights": 100.0}},
    {"id": "E-107", "type": "OWNS", "source": "P-106", "target": "C-205", "properties": {"share_pct": 100.0, "since": "2018-01-01", "voting_rights": 100.0}},
    {"id": "E-108", "type": "OWNS", "source": "P-105", "target": "C-206", "properties": {"share_pct": 100.0, "since": "2020-09-12", "voting_rights": 100.0}},
    {"id": "E-109", "type": "OWNS", "source": "P-107", "target": "C-210", "properties": {"share_pct": 100.0, "since": "2019-12-01", "voting_rights": 100.0}},
    {"id": "E-110", "type": "OWNS", "source": "P-109", "target": "C-209", "properties": {"share_pct": 100.0, "since": "2022-01-15", "voting_rights": 100.0}},

    # Directorships & Control
    {"id": "E-201", "type": "DIRECTOR_OF", "source": "P-102", "target": "C-201", "properties": {"role": "Nominee Director", "appointed": "2020-03-15"}},
    {"id": "E-202", "type": "DIRECTOR_OF", "source": "P-103", "target": "C-203", "properties": {"role": "Corporate Secretary", "appointed": "2021-02-14"}},
    {"id": "E-203", "type": "DIRECTOR_OF", "source": "P-110", "target": "C-201", "properties": {"role": "Resident Agent", "appointed": "2020-03-15"}},
    {"id": "E-204", "type": "DIRECTOR_OF", "source": "P-104", "target": "C-207", "properties": {"role": "Managing Director", "appointed": "2017-05-01"}},

    # Account Holdings
    {"id": "E-301", "type": "HOLDS_ACCOUNT", "source": "C-201", "target": "ACC-9003", "properties": {"opened": "2020-03-20"}},
    {"id": "E-302", "type": "HOLDS_ACCOUNT", "source": "C-202", "target": "ACC-9002", "properties": {"opened": "2020-08-10"}},
    {"id": "E-303", "type": "HOLDS_ACCOUNT", "source": "C-203", "target": "ACC-9004", "properties": {"opened": "2021-02-25"}},
    {"id": "E-304", "type": "HOLDS_ACCOUNT", "source": "C-204", "target": "ACC-9006", "properties": {"opened": "2019-06-20"}},
    {"id": "E-305", "type": "HOLDS_ACCOUNT", "source": "C-205", "target": "ACC-9007", "properties": {"opened": "2018-02-01"}},
    {"id": "E-306", "type": "HOLDS_ACCOUNT", "source": "C-206", "target": "ACC-9005", "properties": {"opened": "2020-09-25"}},
    {"id": "E-307", "type": "HOLDS_ACCOUNT", "source": "C-207", "target": "ACC-9001", "properties": {"opened": "2017-06-15"}},
    {"id": "E-308", "type": "HOLDS_ACCOUNT", "source": "C-208", "target": "ACC-9009", "properties": {"opened": "2021-12-01"}},
    {"id": "E-309", "type": "HOLDS_ACCOUNT", "source": "C-209", "target": "ACC-9011", "properties": {"opened": "2022-02-01"}},
    {"id": "E-310", "type": "HOLDS_ACCOUNT", "source": "C-210", "target": "ACC-9008", "properties": {"opened": "2019-12-10"}},
    {"id": "E-311", "type": "HOLDS_ACCOUNT", "source": "C-211", "target": "ACC-9010", "properties": {"opened": "2021-04-20"}},

    # Ring 1: Circular Smurfing Loop (ACC-9003 -> ACC-9002 -> ACC-9005 -> ACC-9012 -> ACC-9003)
    {"id": "E-401", "type": "TRANSFERRED_TO", "source": "ACC-9003", "target": "ACC-9002", "properties": {"amount": 850000.0, "currency": "USD", "timestamp": "2023-11-01T09:15:00Z", "tx_id": "TX-SMURF-101", "risk_flag": True}},
    {"id": "E-402", "type": "TRANSFERRED_TO", "source": "ACC-9002", "target": "ACC-9005", "properties": {"amount": 820000.0, "currency": "USD", "timestamp": "2023-11-02T11:30:00Z", "tx_id": "TX-SMURF-102", "risk_flag": True}},
    {"id": "E-403", "type": "TRANSFERRED_TO", "source": "ACC-9005", "target": "ACC-9012", "properties": {"amount": 790000.0, "currency": "USD", "timestamp": "2023-11-03T14:45:00Z", "tx_id": "TX-SMURF-103", "risk_flag": True}},
    {"id": "E-404", "type": "TRANSFERRED_TO", "source": "ACC-9012", "target": "ACC-9003", "properties": {"amount": 760000.0, "currency": "USD", "timestamp": "2023-11-04T16:20:00Z", "tx_id": "TX-SMURF-104", "risk_flag": True}},

    # Ring 2: Layering Loop (ACC-9006 -> ACC-9013 -> ACC-9004 -> ACC-9006)
    {"id": "E-405", "type": "TRANSFERRED_TO", "source": "ACC-9006", "target": "ACC-9013", "properties": {"amount": 600000.0, "currency": "USD", "timestamp": "2023-12-10T10:00:00Z", "tx_id": "TX-LAYER-201", "risk_flag": True}},
    {"id": "E-406", "type": "TRANSFERRED_TO", "source": "ACC-9013", "target": "ACC-9004", "properties": {"amount": 580000.0, "currency": "USD", "timestamp": "2023-12-11T13:10:00Z", "tx_id": "TX-LAYER-202", "risk_flag": True}},
    {"id": "E-407", "type": "TRANSFERRED_TO", "source": "ACC-9004", "target": "ACC-9006", "properties": {"amount": 550000.0, "currency": "USD", "timestamp": "2023-12-12T15:40:00Z", "tx_id": "TX-LAYER-203", "risk_flag": True}},

    # Sanctions Evasion Corridor (ACC-9007 [RU/Sanctioned] -> ACC-9005 [AE] -> ACC-9004 [UK] -> ACC-9009 [US/Real Estate])
    {"id": "E-408", "type": "TRANSFERRED_TO", "source": "ACC-9007", "target": "ACC-9005", "properties": {"amount": 1450000.0, "currency": "USD", "timestamp": "2024-01-08T08:00:00Z", "tx_id": "TX-SANCT-301", "risk_flag": True}},
    {"id": "E-409", "type": "TRANSFERRED_TO", "source": "ACC-9005", "target": "ACC-9004", "properties": {"amount": 1400000.0, "currency": "USD", "timestamp": "2024-01-10T11:20:00Z", "tx_id": "TX-SANCT-302", "risk_flag": True}},
    {"id": "E-410", "type": "TRANSFERRED_TO", "source": "ACC-9004", "target": "ACC-9009", "properties": {"amount": 1350000.0, "currency": "USD", "timestamp": "2024-01-12T16:00:00Z", "tx_id": "TX-SANCT-303", "risk_flag": True}},

    # Legitimate Inter-Company Transfers
    {"id": "E-411", "type": "TRANSFERRED_TO", "source": "ACC-9008", "target": "ACC-9011", "properties": {"amount": 180000.0, "currency": "EUR", "timestamp": "2024-02-01T10:00:00Z", "tx_id": "TX-LEGIT-401", "risk_flag": False}},
    {"id": "E-412", "type": "TRANSFERRED_TO", "source": "ACC-9011", "target": "ACC-9010", "properties": {"amount": 95000.0, "currency": "EUR", "timestamp": "2024-02-05T14:30:00Z", "tx_id": "TX-LEGIT-402", "risk_flag": False}},
    {"id": "E-413", "type": "TRANSFERRED_TO", "source": "ACC-9001", "target": "ACC-9010", "properties": {"amount": 320000.0, "currency": "EUR", "timestamp": "2024-02-15T09:45:00Z", "tx_id": "TX-LEGIT-403", "risk_flag": False}},

    # Sanctions Links
    {"id": "E-501", "type": "SANCTIONED_UNDER", "source": "P-106", "target": "SANCT-OFAC-SDN", "properties": {"listed_date": "2022-04-15", "notice": "Executive Order 14024"}},
    {"id": "E-502", "type": "SANCTIONED_UNDER", "source": "C-205", "target": "SANCT-OFAC-SDN", "properties": {"listed_date": "2022-04-15", "notice": "Specially Designated Tech Entity"}},
    {"id": "E-503", "type": "SANCTIONED_UNDER", "source": "P-101", "target": "SANCT-EU-CFSP", "properties": {"listed_date": "2022-05-10", "notice": "EU High Net-Worth Oligarch Annex I"}},

    # Jurisdictions
    {"id": "E-601", "type": "REGISTERED_IN", "source": "C-201", "target": "JUR-BVI", "properties": {}},
    {"id": "E-602", "type": "REGISTERED_IN", "source": "C-202", "target": "JUR-CY", "properties": {}},
    {"id": "E-603", "type": "REGISTERED_IN", "source": "C-204", "target": "JUR-PA", "properties": {}},
    {"id": "E-604", "type": "REGISTERED_IN", "source": "C-205", "target": "JUR-RU", "properties": {}},
    {"id": "E-605", "type": "REGISTERED_IN", "source": "C-206", "target": "JUR-AE", "properties": {}},
    {"id": "E-606", "type": "REGISTERED_IN", "source": "C-207", "target": "JUR-CH", "properties": {}},
    {"id": "E-607", "type": "REGISTERED_IN", "source": "C-203", "target": "JUR-GB", "properties": {}},
    {"id": "E-608", "type": "REGISTERED_IN", "source": "C-208", "target": "JUR-US", "properties": {}}
]

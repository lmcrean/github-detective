const ORGS = {
    "Walmart": {
      tags: ["retail", "ecommerce", "supply-chain", "payments"],
      revenue: "$648.13B",
      github: ["github.com/walmart", "github.com/walmartlabs"]
    },
    "Amazon": {
      tags: ["ecommerce", "cloud", "aws", "logistics", "advertising"],
      revenue: "$638B",
      github: ["github.com/aws", "github.com/amzn"]
    },
    "Apple": {
      tags: ["consumer-electronics", "software", "ios", "macos", "services"],
      revenue: "$391.04B",
      github: ["github.com/apple"]
    },
    "Google": {
      tags: ["search", "advertising", "cloud", "ai"],
      revenue: "$350B",
      github: ["github.com/google"]
    },
    "Microsoft": {
      tags: ["cloud", "azure", "productivity", "office365", "ai", "gaming"],
      revenue: "$245.12B",
      github: ["github.com/microsoft"]
    },
    "Samsung": {
      tags: ["electronics", "semiconductors", "smartphones", "displays", "memory"],
      revenue: "$218.9B",
      github: ["github.com/Samsung", "github.com/SamsungDS"]
    },
    "General Motors": {
      tags: ["automotive", "ev", "autonomous", "connected-cars"],
      revenue: "$187.44B",
      github: ["github.com/generalmotors"]
    },
    "JPMorgan Chase": {
      tags: ["investment-banking", "commercial-banking", "fintech", "asset-management"],
      revenue: "$177.56B",
      github: ["github.com/jpmorganchase"]
    },
    "Ford": {
      tags: ["automotive", "ev", "autonomous", "commercial-vehicles"],
      revenue: "$176B",
      github: ["github.com/ford"]
    },
    "Meta": {
      tags: ["social-media", "advertising", "vr", "ar", "metaverse"],
      revenue: "$164.50B",
      github: ["github.com/facebook", "github.com/facebookresearch"]
    },
    "ByteDance": {
      tags: ["social-media", "tiktok", "content", "ecommerce", "gaming"],
      revenue: "$155B",
      github: ["github.com/bytedance"]
    },
    "Verizon": {
      tags: ["telecom", "5g", "broadband", "iot"],
      revenue: "$134.8B",
      github: ["github.com/verizon", "github.com/verizonconnect"]
    },
    "Alibaba": {
      tags: ["ecommerce", "cloud", "fintech", "entertainment"],
      revenue: "$130.35B",
      github: ["github.com/alibaba", "github.com/aliyun"]
    },
    "Nvidia": {
      tags: ["gpu", "ai", "datacenter", "autonomous"],
      revenue: "$130.5B",
      github: ["github.com/nvidia"]
    },
    "AT&T": {
      tags: ["telecom", "5g", "fiber", "enterprise"],
      revenue: "$122.3B",
      github: ["github.com/ATT", "github.com/att-comdev"]
    },
    "Comcast": {
      tags: ["cable", "broadband", "media", "streaming"],
      revenue: "$121B",
      github: ["github.com/comcast"]
    },
    "Tesla": {
      tags: ["ev", "energy-storage", "solar", "autonomous"],
      revenue: "$97.69B",
      github: ["github.com/teslamotors"]
    },
    "Bosch": {
      tags: ["mobility", "industrial", "consumer-goods", "iot"],
      revenue: "$97.84B",
      github: ["github.com/boschresearch"]
    },
    "Tencent": {
      tags: ["social-media", "gaming", "cloud", "fintech", "ai"],
      revenue: "$91.9B",
      github: ["github.com/Tencent", "github.com/Tencent-Hunyuan"]
    },
    "Disney": {
      tags: ["entertainment", "media", "streaming", "theme-parks"],
      revenue: "$91B",
      github: ["github.com/disney", "github.com/disneystreaming"]
    },
    "Sony": {
      tags: ["electronics", "entertainment", "gaming", "imaging"],
      revenue: "$89.8B",
      github: ["github.com/sony", "github.com/SonyMobile"]
    },
    "Dell": {
      tags: ["infrastructure", "pc", "servers", "datacenter"],
      revenue: "$88.4B",
      github: ["github.com/DELL", "github.com/dellhpc"]
    },
    "Siemens": {
      tags: ["digital-industries", "infrastructure", "mobility", "healthineers"],
      revenue: "$82.37B",
      github: ["github.com/siemens"]
    },
    "Deutsche Telekom": {
      tags: ["telecom", "mobile", "cloud", "it-services"],
      revenue: "$81.7B",
      github: ["github.com/telekom", "github.com/telekom-mms"]
    },
    "IBM": {
      tags: ["it-services", "cloud", "ai", "consulting"],
      revenue: "$62.8B",
      github: ["github.com/IBM"]
    },
    "HP": {
      tags: ["pc", "laptops", "printing", "ai-pc"],
      revenue: "$53.6B",
      github: ["github.com/HPInc"]
    },
    "Cisco": {
      tags: ["networking", "security", "collaboration", "ai"],
      revenue: "$53.8B",
      github: ["github.com/cisco"]
    },
    "Goldman Sachs": {
      tags: ["investment-banking", "trading", "asset-management"],
      revenue: "$53.51B",
      github: ["github.com/goldmansachs"]
    },
    "Oracle": {
      tags: ["database", "cloud", "enterprise-apps"],
      revenue: "$53B",
      github: ["github.com/oracle"]
    },
    "Intel": {
      tags: ["cpu", "datacenter", "foundry", "ai-accelerators"],
      revenue: "$53.1B",
      github: ["github.com/intel", "github.com/IntelLabs"]
    },
    "Broadcom": {
      tags: ["semiconductors", "infrastructure-software", "networking"],
      revenue: "$51.6B",
      github: ["github.com/broadcom", "github.com/vmware"]
    },
    "Vodafone": {
      tags: ["telecom", "mobile", "iot", "enterprise"],
      revenue: "$49B",
      github: ["github.com/vodafone"]
    },
    "Uber": {
      tags: ["rideshare", "delivery", "freight", "mobility"],
      revenue: "$43.98B",
      github: ["github.com/uber"]
    },
    "Schneider Electric": {
      tags: ["energy-management", "industrial-automation"],
      revenue: "$41.29B",
      github: ["github.com/schneider-electric"]
    },
    "Netflix": {
      tags: ["streaming", "entertainment", "content", "media"],
      revenue: "$39B",
      github: ["github.com/netflix"]
    },
    "GE": {
      tags: ["aerospace", "energy", "healthcare"],
      revenue: "$38.7B",
      github: ["github.com/GENERALELECTRIC"]
    },
    "Honeywell": {
      tags: ["aerospace", "building-tech", "performance-materials"],
      revenue: "$38.5B",
      github: ["github.com/honeywell"]
    },
    "SAP": {
      tags: ["erp", "cloud", "enterprise", "ai"],
      revenue: "$37.4B",
      github: ["github.com/SAP"]
    },
    "Salesforce": {
      tags: ["crm", "cloud", "sales", "automation"],
      revenue: "$34.86B",
      github: ["github.com/salesforce"]
    },
    "Qualcomm": {
      tags: ["mobile-processors", "5g", "automotive", "iot"],
      revenue: "$33.19B",
      github: ["github.com/qualcomm", "github.com/quic"]
    },
    "ABB": {
      tags: ["electrification", "automation", "robotics"],
      revenue: "$32.85B",
      github: ["github.com/abb-iss"]
    },
    "PayPal": {
      tags: ["payments", "fintech", "venmo", "braintree"],
      revenue: "$31.8B",
      github: ["github.com/paypal"]
    },
    "ASML": {
      tags: ["lithography", "semiconductors", "euv"],
      revenue: "$30.7B",
      github: ["github.com/ASML-Labs", "github.com/asml-gh"]
    },
    "HPE": {
      tags: ["edge-cloud", "servers", "storage", "greenlake"],
      revenue: "$30.13B",
      github: ["github.com/hewlettpackard", "github.com/hpenetworking"]
    },
    "Mastercard": {
      tags: ["payments", "fintech", "card-processing"],
      revenue: "$28.2B",
      github: ["github.com/Mastercard"]
    },
    "BT Group": {
      tags: ["telecom", "broadband", "enterprise"],
      revenue: "$26B",
      github: ["github.com/BT-OpenSource"]
    },
    "AMD": {
      tags: ["cpu", "gpu", "datacenter", "ai-accelerators"],
      revenue: "$25.8B",
      github: ["github.com/amd"]
    },
    "Block": {
      tags: ["payments", "pos", "cashapp", "fintech"],
      revenue: "$24B",
      github: ["github.com/square", "github.com/block"]
    },
    "Adobe": {
      tags: ["creative", "marketing", "document-cloud"],
      revenue: "$21.5B",
      github: ["github.com/adobe"]
    },
    "Nokia": {
      tags: ["network-infrastructure", "mobile", "cloud"],
      revenue: "$20.8B",
      github: ["github.com/nokia"]
    },
    "Infineon": {
      tags: ["semiconductors", "automotive", "iot", "power"],
      revenue: "$16.2B",
      github: ["github.com/Infineon"]
    },
    "Spotify": {
      tags: ["streaming", "music", "podcasts", "audio"],
      revenue: "$14.4B",
      github: ["github.com/spotify"]
    },
    "STMicroelectronics": {
      tags: ["semiconductors", "microcontrollers", "sensors"],
      revenue: "$13.27B",
      github: ["github.com/STMicroelectronics"]
    },
    "Western Digital": {
      tags: ["storage", "hdd", "ssd", "memory"],
      revenue: "$13B",
      github: ["github.com/westerndigital"]
    },
    "Airbnb": {
      tags: ["travel", "hospitality", "marketplace", "experiences"],
      revenue: "$11B",
      github: ["github.com/airbnb"]
    },
    "ServiceNow": {
      tags: ["it-service", "workflow", "automation", "cloud"],
      revenue: "$10.98B",
      github: ["github.com/ServiceNow"]
    },
    "DoorDash": {
      tags: ["delivery", "logistics", "marketplace", "food"],
      revenue: "$10.72B",
      github: ["github.com/doordash"]
    },
    "Analog Devices": {
      tags: ["semiconductors", "analog", "signal-processing"],
      revenue: "$9.4B",
      github: ["github.com/analogdevicesinc"]
    },
    "Shopify": {
      tags: ["ecommerce", "platform", "payments", "retail"],
      revenue: "$8.88B",
      github: ["github.com/shopify"]
    },
    "Workday": {
      tags: ["hr", "finance", "cloud", "enterprise"],
      revenue: "$7.3B",
      github: ["github.com/workday"]
    },
    "NetApp": {
      tags: ["storage", "data-management", "cloud"],
      revenue: "$6.27B",
      github: ["github.com/netapp"]
    },
    "Lyft": {
      tags: ["rideshare", "mobility", "transportation"],
      revenue: "$5.7B",
      github: ["github.com/lyft"]
    },
    "Marvell": {
      tags: ["semiconductors", "datacenter", "5g", "automotive"],
      revenue: "$5.51B",
      github: ["github.com/MarvellEmbeddedProcessors"]
    },
    "Stripe": {
      tags: ["payments", "fintech", "api", "infrastructure"],
      revenue: "$5.1B",
      github: ["github.com/stripe"]
    },
    "Zoom": {
      tags: ["video", "collaboration", "communications", "remote"],
      revenue: "$4.53B",
      github: ["github.com/zoom"]
    },
    "Twilio": {
      tags: ["communications", "api", "messaging", "voice"],
      revenue: "$4.46B",
      github: ["github.com/twilio"]
    },
    "Atlassian": {
      tags: ["collaboration", "devtools", "jira", "confluence"],
      revenue: "$4.36B",
      github: ["github.com/atlassian"]
    },
    "Pinterest": {
      tags: ["social-media", "discovery", "visual", "ecommerce"],
      revenue: "$3.65B",
      github: ["github.com/pinterest"]
    },
    "CrowdStrike": {
      tags: ["security", "endpoint", "cloud", "ai"],
      revenue: "$3.06B",
      github: ["github.com/crowdstrike"]
    },
    "Palantir": {
      tags: ["data-analytics", "ai", "defense", "enterprise"],
      revenue: "$2.87B",
      github: ["github.com/palantir"]
    },
    "Datadog": {
      tags: ["monitoring", "observability", "cloud", "devops"],
      revenue: "$2.68B",
      github: ["github.com/datadog"]
    },
    "Snowflake": {
      tags: ["data-warehouse", "cloud", "analytics", "ai"],
      revenue: "$2.67B",
      github: ["github.com/snowflakedb"]
    },
    "Databricks": {
      tags: ["data", "ai", "analytics", "lakehouse"],
      revenue: "$2.4B",
      github: ["github.com/databricks"]
    },
    "HSBC": {
        tags: ["banking", "financial-services", "retail-banking", "commercial-banking", "wealth-management"],
        revenue: "$65.9B",
        github: ["github.com/hsbc"]
    },
    "London Stock Exchange Group": {
        tags: ["financial-markets", "trading", "capital-markets", "data-analytics", "clearing"],
        revenue: "$8.7B",
        github: ["github.com/LSEG"]
    },
    "Barclays": {
        tags: ["investment-banking", "retail-banking", "credit-cards", "wealth-management"],
        revenue: "$33.6B",
        github: ["github.com/Barclays"]
    },
    "Lloyds Banking Group": {
        tags: ["retail-banking", "commercial-banking", "insurance", "mortgages"],
        revenue: "$23.8B",
        github: ["github.com/lloyds-banking-group"]
    },
    "NatWest Group": {
        tags: ["retail-banking", "commercial-banking", "private-banking", "mortgages"],
        revenue: "$14.6B",
        github: ["github.com/natwest-group"]
    },
    "Standard Chartered": {
        tags: ["international-banking", "emerging-markets", "trade-finance", "transaction-banking"],
        revenue: "$16.7B",
        github: ["github.com/standard-chartered"]
    },
    "Hargreaves Lansdown": {
        tags: ["investment-platform", "wealth-management", "stockbroking", "pensions"],
        revenue: "$0.8B",
        github: ["github.com/hargreaves-lansdown"]
    },
    "AstraZeneca": {
        tags: ["pharmaceuticals", "biotechnology", "oncology", "vaccines", "r&d"],
        revenue: "$45.8B",
        github: ["github.com/AstraZeneca", "github.com/AstraZeneca-NGS"]
    },
    "GlaxoSmithKline": {
        tags: ["pharmaceuticals", "vaccines", "consumer-healthcare", "r&d"],
        revenue: "$38.3B",
        github: ["github.com/GSK"]
    },
    "The Sage Group": {
        tags: ["business-software", "accounting", "erp", "cloud", "smb"],
        revenue: "$2.3B",
        github: ["github.com/sage"]
    },
    "AVEVA": {
        tags: ["industrial-software", "engineering", "digital-transformation", "iot"],
        revenue: "$1.2B",
        github: ["github.com/AVEVA"]
    },
    "Ocado Group": {
        tags: ["ecommerce", "robotics", "automation", "logistics-tech", "retail-tech"],
        revenue: "$3.2B",
        github: ["github.com/ocadotechnology"]
    },
    "Auto Trader Group": {
        tags: ["digital-marketplace", "automotive", "classifieds", "data-analytics"],
        revenue: "$0.6B",
        github: ["github.com/autotraderuk"]
    },
    "Rightmove": {
        tags: ["property-portal", "real-estate", "marketplace", "proptech"],
        revenue: "$0.5B",
        github: ["github.com/rightmove"]
    },
    "Just Eat Takeaway.com": {
        tags: ["food-delivery", "marketplace", "logistics", "ecommerce"],
        revenue: "$5.9B",
        github: ["github.com/justeattakeaway", "github.com/justeat"]
    },
    "RELX": {
        tags: ["information-services", "analytics", "scientific-publishing", "legal-information"],
        revenue: "$11.0B",
        github: ["github.com/relx-group"]
    },
    "Experian": {
        tags: ["credit-reporting", "data-analytics", "financial-services", "identity-verification"],
        revenue: "$6.6B",
        github: ["github.com/experianplc"]
    },
    "BAE Systems": {
        tags: ["defense", "aerospace", "cybersecurity", "naval-systems"],
        revenue: "$33.0B",
        github: ["github.com/baesystemsdigital"]
    },
    "Rolls-Royce": {
        tags: ["aerospace", "defense", "power-systems", "engineering"],
        revenue: "$23.7B",
        github: ["github.com/rolls-royce", "github.com/rropen"]
    },
    "National Grid": {
        tags: ["utilities", "electricity-transmission", "gas-distribution", "energy-infrastructure"],
        revenue: "$25.4B",
        github: ["github.com/National-Grid"]
    },
    "SSE": {
        tags: ["energy", "renewables", "electricity-generation", "utilities"],
        revenue: "$12.5B",
        github: ["github.com/sse-energy"]
    },
    "Pearson": {
        tags: ["education", "publishing", "edtech", "assessment"],
        revenue: "$5.2B",
        github: ["github.com/pearsondevelopersnetwork"]
    },
    "WPP": {
        tags: ["advertising", "marketing", "communications", "digital-services"],
        revenue: "$18.9B",
        github: ["github.com/WPPOpen"]
    }
};
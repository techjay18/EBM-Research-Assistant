from test_search import search
from biomistral_api import call_llm

ONCOLOGY_KEYWORDS = [
    # General oncology terms
    "cancer", "oncology", "tumor", "tumour", "malignancy", "malignant",
    "neoplasm", "neoplasia", "carcinogenesis", "oncogenesis",
    "biopsy", "pathology", "histology", "cytology", "staging",
    "remission", "recurrence", "relapse", "progression", "prognosis",

    # Cancer types — solid tumors
    "carcinoma", "adenocarcinoma", "squamous cell", "sarcoma",
    "melanoma", "glioma", "glioblastoma", "meningioma", "astrocytoma",
    "hepatocellular", "cholangiocarcinoma", "pancreatic cancer",
    "lung cancer", "nsclc", "sclc", "small cell", "non-small cell",
    "breast cancer", "triple negative", "her2", "er-positive", "pr-positive",
    "colon cancer", "colorectal cancer", "rectal cancer", "crc",
    "prostate cancer", "ovarian cancer", "cervical cancer", "endometrial cancer",
    "uterine cancer", "bladder cancer", "renal cell", "kidney cancer",
    "thyroid cancer", "head and neck cancer", "oropharyngeal",
    "esophageal cancer", "gastric cancer", "stomach cancer",
    "skin cancer", "basal cell", "merkel cell",
    "mesothelioma", "peritoneal", "pleural",

    # Hematological malignancies
    "leukemia", "lymphoma", "myeloma", "multiple myeloma",
    "aml", "cml", "all", "cll", "acute myeloid", "chronic lymphocytic",
    "diffuse large b-cell", "dlbcl", "hodgkin", "non-hodgkin",
    "follicular lymphoma", "mantle cell", "myelodysplastic", "mds",
    "myeloproliferative", "polycythemia vera", "waldenstrom",
    "plasma cell", "bone marrow",

    # Metastasis & spread
    "metastasis", "metastatic", "metastasize", "distant spread",
    "lymph node", "brain metastasis", "liver metastasis", "bone metastasis",

    # Treatments
    "chemotherapy", "chemo", "radiotherapy", "radiation therapy",
    "immunotherapy", "targeted therapy", "hormone therapy", "endocrine therapy",
    "surgery", "resection", "mastectomy", "lumpectomy", "lobectomy",
    "stem cell transplant", "bone marrow transplant", "car-t", "car t-cell",
    "checkpoint inhibitor", "pd-1", "pd-l1", "ctla-4",
    "anti-pd1", "anti-pdl1", "pembrolizumab", "nivolumab",
    "atezolizumab", "ipilimumab", "durvalumab", "avelumab",
    "bevacizumab", "trastuzumab", "cetuximab", "rituximab",
    "osimertinib", "erlotinib", "gefitinib", "crizotinib", "alectinib",
    "imatinib", "dasatinib", "ibrutinib", "venetoclax",
    "palbociclib", "ribociclib", "abemaciclib", "olaparib", "niraparib",
    "docetaxel", "paclitaxel", "carboplatin", "cisplatin", "oxaliplatin",
    "capecitabine", "fluorouracil", "5-fu", "gemcitabine", "pemetrexed",
    "doxorubicin", "etoposide", "vincristine", "cyclophosphamide",
    "lenalidomide", "bortezomib", "daratumumab",

    # Biomarkers & genomics
    "biomarker", "mutation", "egfr", "kras", "braf", "alk", "ros1",
    "met", "ret", "ntrk", "fgfr", "pik3ca", "pten", "tp53", "brca",
    "brca1", "brca2", "msi", "mmr", "microsatellite instability",
    "tumor mutational burden", "tmb", "ctdna", "liquid biopsy",
    "gene expression", "genomic", "next-generation sequencing", "ngs",
    "whole exome", "copy number", "amplification", "fusion",

    # Clinical & trial terms
    "clinical trial", "phase 1", "phase 2", "phase 3", "randomized",
    "overall survival", "progression-free survival", "pfs", "os",
    "objective response rate", "orr", "complete response", "partial response",
    "stable disease", "hazard ratio", "confidence interval",
    "first-line", "second-line", "adjuvant", "neoadjuvant", "palliative",
    "chemoresistance", "drug resistance", "toxicity", "adverse event",
    "dose-limiting", "maximum tolerated dose",

    # Supportive & other
    "angiogenesis", "vascular", "vegf", "hypoxia", "tumor microenvironment",
    "immune evasion", "immunosuppression", "cytokine", "interleukin",
    "nausea", "fatigue", "neutropenia", "thrombocytopenia", "anemia",
    "palliative care", "hospice", "survivorship", "quality of life",
    "cancer screening", "mammogram", "psa", "colonoscopy",
    "evidence-based", "systematic review", "meta-analysis", "guideline"
]

def is_oncology_question(question):
    question = question.lower()
    return any(keyword in question for keyword in ONCOLOGY_KEYWORDS)

def ask(question):
    if not is_oncology_question(question):
        return {"context": "", "answer": "This assistant is designed only for oncology/cancer-related questions."}

    docs = search(question)

    context = ""
    for doc in docs:
        context += f"""
Title: {doc['Title']}
Summary: {doc['Summary']}
Source: {doc['Source']}
Link: {doc['Link']}
"""

    prompt = f"""
    
    You are a medical assistant specialising in oncology and evidence-based medicine.
Use only the research context below to answer the user's question.
Be concise, accurate, and cite the source titles where relevant.

Research context:
{context}

User question:
{question}

Final answer:
"""

    answer = call_llm(prompt)

    return {"context": context, "answer": answer}

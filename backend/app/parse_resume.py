from pyresparser import ResumeParser

def parse_resume(p):
    return ResumeParser(p).get_extracted_data()
